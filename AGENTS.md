# 프로젝트 작업 원칙

## 학습 방식

- 이 프로젝트는 수업 팀 프로젝트이자 사용자의 PyTorch 실습이다.
- 사용자가 코드를 직접 타이핑한다. 구현을 요청하기 전에는 실행 코드, 완성된 노트북, 학습 스크립트를 작성하지 않는다.
- AI 도움은 개념 설명, 작은 단계의 힌트, 사용자가 작성한 코드 검토와 오류 원인 설명을 우선한다. 코드 예시는 요청한 범위에서 짧게 제공한다.
- 코드를 제공할 때는 전체 목적과 흐름, 사용하는 라이브러리가 무엇이며 왜 필요한지, 각 줄의 문법과 역할을 친절하게 풀어서 설명한다. 필요한 사전 개념과 실행 후 확인할 출력과 관찰 사항도 함께 안내한다. 한 번에 작은 단위로 진행하며 사용자가 직접 실행하고 이해할 시간을 둔다.
- DeepLearning.AI의 PyTorch for Deep Learning에서 배운 흐름을 따른다. 프로젝트 적용 순서는 `docs/학습실습계획.md`를 참고한다.
- 데이터셋은 CUB-200-2011과 앞으로 선정할 두 개다. 후보를 확정된 선택처럼 기록하지 않는다.
- 원본 연구 자료와 사용자가 작성한 코드를 존중하고, 실험 결과를 추정값으로 채우지 않는다.
- 원본 데이터와 가중치는 Git에 넣지 않는다. 실험 조건, 분할, seed, 결과는 재현할 수 있게 기록한다.

## 문서와 주석 작성

- 응답, 코드 주석, 프로젝트 문서에 중간점을 사용하지 않는다. 나열은 쉼표나 접속사로 표현한다.
- 코드 주석은 해당 코드의 역할과 필요한 근거를 간결하게 설명하고, 문장은 "한다." 형태로 작성한다.
- 대화 내용, 수정 이력, 작업 지시를 주석에 남기지 않는다. "한 번만 정의한다" 같은 편집 과정 설명을 넣지 않는다.

## 커밋 작성

- Conventional Commits 형식인 `type(scope): 설명`을 사용한다. scope는 필요한 경우에만 넣는다.
- 설명은 변경 목적이 드러나도록 간단하고 직관적인 한국어로 작성한다.
- 독립적인 작업은 목적별로 나누어 커밋한다.
- 원격 push는 사용자가 직접 진행한다.

<!-- CODEGRAPH_START -->
## CodeGraph

In repositories indexed by CodeGraph (a `.codegraph/` directory exists at the repo root), reach for it BEFORE grep/find or reading files when you need to understand or locate code:

- **MCP tool** (when available): `codegraph_explore` answers most code questions in one call — the relevant symbols' verbatim source plus the call paths between them, including dynamic-dispatch hops grep can't follow. Name a file or symbol in the query to read its current line-numbered source. If it's listed but deferred, load it by name via tool search.
- **Shell** (always works): `codegraph explore "<symbol names or question>"` prints the same output.

If there is no `.codegraph/` directory, skip CodeGraph entirely — indexing is the user's decision.
<!-- CODEGRAPH_END -->
