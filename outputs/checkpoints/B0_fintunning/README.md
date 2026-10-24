# CUB-200-2011 B-0 Teacher 학습 결과

DINOv3 ConvNeXt-Base의 LVD-1689M 사전학습 가중치에 200클래스 분류층을 추가하고, CUB-200-2011로 전체 fine-tuning한 pilot 결과입니다. Pruning은 적용하지 않았습니다.

## 체크포인트 다운로드

[B-0 Teacher 체크포인트 다운로드](https://drive.google.com/file/d/1xwR2mviCdrSYJ-n2eZuFbd14reVcXuiq/view?usp=sharing)

[DINOv3 ConvNeXt-Base의 LVD-1689M pretrained 모델](https://drive.google.com/file/d/1mU3_RtewPa2cqCcEyR6CoTzyhy98ZExv/view?usp=sharing)

- 파일명: `best.pth`
- 용도: B-0 KD와 B-30 pruning의 시작 모델
- 원본 DINOv3 사전학습 가중치가 아닌, CUB 학습을 완료한 체크포인트입니다.

## 검증 결과

| 항목          |      값 |
| ----------- | -----: |
| 학습 seed     |      0 |
| 전체 학습 epoch |     20 |
| 선택된 epoch   |     10 |
| 최고 검증 정확도   | 83.33% |
| 해당 검증 loss  | 0.7331 |

검증 정확도가 가장 높은 모델을 선택했으며, 동률이면 검증 loss가 낮은 모델을 선택했습니다. 테스트 데이터는 사용하지 않았습니다.

## 관련 파일

- `config.json`: 학습 설정과 실행 환경
- `history.json`: epoch별 학습과 검증 기록
- `notebooks/teacher_B0_finetune.ipynb`: 학습 코드

## 복원 방법

DINOv3 ConvNeXt-Base 구조에 200클래스 분류층을 구성한 뒤, `best.pth` 안의 `model_state_dict`를 불러옵니다.

이 결과는 단일 seed의 pilot 결과이며, 최종 반복 실험 결과는 아닙니다.
# CUB-200-2011 B-0 Teacher 학습 결과

DINOv3 ConvNeXt-Base의 LVD-1689M 사전학습 가중치에 200클래스 분류층을 추가하고, CUB-200-2011로 전체 fine-tuning한 pilot 결과입니다. Pruning은 적용하지 않았습니다.

## 체크포인트 다운로드

[B-0 Teacher 체크포인트 다운로드 ](여기에_Drive_공유_링크): [https://drive.google.com/file/d/1xwR2mviCdrSYJ-n2eZuFbd14reVcXuiq/view?usp=sharing](https://drive.google.com/file/d/1xwR2mviCdrSYJ-n2eZuFbd14reVcXuiq/view?usp=sharing)\


- 파일명: `best.pth`
- 용도: B-0 KD와 B-30 pruning의 시작 모델
- 원본 DINOv3 사전학습 가중치가 아닌, CUB 학습을 완료한 체크포인트입니다.

## 검증 결과

| 항목          |      값 |
| ----------- | -----: |
| 학습 seed     |      0 |
| 전체 학습 epoch |     20 |
| 선택된 epoch   |     10 |
| 최고 검증 정확도   | 83.33% |
| 해당 검증 loss  | 0.7331 |

검증 정확도가 가장 높은 모델을 선택했으며, 동률이면 검증 loss가 낮은 모델을 선택했습니다. 테스트 데이터는 사용하지 않았습니다.

## 관련 파일

- `config.json`: 학습 설정과 실행 환경
- `history.json`: epoch별 학습과 검증 기록
- `notebooks/teacher_B0_finetune.ipynb`: 학습 코드

## 복원 방법

DINOv3 ConvNeXt-Base 구조에 200클래스 분류층을 구성한 뒤, `best.pth` 안의 `model_state_dict`를 불러옵니다.

이 결과는 단일 seed의 pilot 결과이며, 최종 반복 실험 결과는 아닙니다.
