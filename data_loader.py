"""CUB 데이터 읽기, 분할, 전처리와 DataLoader 생성을 제공한다."""

import random
from pathlib import Path

from PIL import Image, ImageOps
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms


def read_cub_metadata(data_dir):
    """이미지 목록, 0부터 시작하는 레이블과 클래스 이름을 읽는다."""
    data_dir = Path(data_dir)
    image_list = (data_dir / "images.txt").read_text().splitlines()
    label_rows = (data_dir / "image_class_labels.txt").read_text().splitlines()
    image_labels = {}
    for row in label_rows:
        image_id, class_id = row.split()
        image_labels[image_id] = int(class_id) - 1

    class_rows = (data_dir / "classes.txt").read_text().splitlines()
    class_names = {}
    for row in class_rows:
        class_id, class_name = row.split()
        class_names[int(class_id) - 1] = class_name

    return image_list, image_labels, class_names


def split_cub_images(data_dir, image_list, image_labels):
    """공식 학습 집합에서 seed 42로 클래스별 검증 이미지를 분리한다."""
    data_dir = Path(data_dir)
    split_rows = (data_dir / "train_test_split.txt").read_text().splitlines()
    train_ids = set()
    for row in split_rows:
        image_id, is_train = row.split()
        if is_train == "1":
            train_ids.add(image_id)

    official_train_image_list = []
    test_image_list = []
    for row in image_list:
        image_id, relative_path = row.split()
        if image_id in train_ids:
            official_train_image_list.append(row)
        else:
            test_image_list.append(row)

    image_lists_by_class = {}
    for row in official_train_image_list:
        image_id, relative_path = row.split()
        label = image_labels[image_id]
        if label not in image_lists_by_class:
            image_lists_by_class[label] = []
        image_lists_by_class[label].append(row)

    rng = random.Random(42)
    train_image_list = []
    val_image_list = []
    for class_image_list in image_lists_by_class.values():
        rng.shuffle(class_image_list)
        val_count = round(len(class_image_list) * 0.2)
        val_image_list.extend(class_image_list[:val_count])
        train_image_list.extend(class_image_list[val_count:])

    return train_image_list, val_image_list, test_image_list


def pad_image(image):
    """종횡비를 유지하고 회색 여백으로 224×224 크기를 맞춘다."""
    return ImageOps.pad(
        image,
        (224, 224),
        method=Image.Resampling.BILINEAR,
        color=(128, 128, 128),
        centering=(0.5, 0.5),
    )


def build_transforms():
    """학습용 어그멘테이션과 공통 padding, 텐서 변환, 정규화를 구성한다."""
    flip_transform = transforms.RandomHorizontalFlip(p=0.5)
    brightness_transform = transforms.ColorJitter(brightness=0.1)
    to_tensor = transforms.ToTensor()
    normalize = transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225],
    )
    train_transform = transforms.Compose([
        flip_transform,
        brightness_transform,
        pad_image,
        to_tensor,
        normalize,
    ])
    eval_transform = transforms.Compose([
        pad_image,
        to_tensor,
        normalize,
    ])
    return train_transform, eval_transform


class BirdDataset(Dataset):
    """목록의 이미지 경로를 읽어 변환한 텐서와 정수 레이블을 반환한다."""

    def __init__(self, image_list, data_dir, image_labels, transform):
        self.image_list = image_list
        self.data_dir = data_dir
        self.image_labels = image_labels
        self.transform = transform

    def __len__(self):
        return len(self.image_list)

    def __getitem__(self, index):
        image_id, relative_path = self.image_list[index].split()
        image_path = self.data_dir / "images" / relative_path
        with Image.open(image_path) as image:
            image = image.convert("RGB")
        image_tensor = self.transform(image)
        label = self.image_labels[image_id]
        return image_tensor, label


def build_dataloaders(
    data_dir,
    image_labels,
    train_image_list,
    val_image_list,
    test_image_list,
    train_transform,
    eval_transform,
    batch_size=32,
    num_workers=0,
):
    """분할별 Dataset을 만들고 학습 목록만 섞는 DataLoader를 반환한다."""
    train_dataset = BirdDataset(
        image_list=train_image_list,
        data_dir=data_dir,
        image_labels=image_labels,
        transform=train_transform,
    )
    val_dataset = BirdDataset(
        image_list=val_image_list,
        data_dir=data_dir,
        image_labels=image_labels,
        transform=eval_transform,
    )
    test_dataset = BirdDataset(
        image_list=test_image_list,
        data_dir=data_dir,
        image_labels=image_labels,
        transform=eval_transform,
    )
    train_loader = DataLoader(
        dataset=train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
    )
    val_loader = DataLoader(
        dataset=val_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
    )
    test_loader = DataLoader(
        dataset=test_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
    )
    return train_loader, val_loader, test_loader
