# jev

Python 학습 및 실습을 위한 독립 프로젝트 공간입니다. Python 3.12와 uv를 사용하며, 다른 루트 프로젝트 없이 실행할 수 있습니다.

## 구성 원칙

- 이 폴더에서 작업할 때 루트의 다른 프로젝트 폴더에 접근하지 않습니다.
- Docker 빌드 컨텍스트와 소스 마운트는 이 폴더로 제한합니다.
- 다른 프로젝트의 컨테이너를 재사용하더라도 독립 실행이 가능하도록 구성합니다.

## 기본 구성

- `main.py`: 기본 실행 예제
- `pyproject.toml`, `uv.lock`: Python 버전과 의존성 관리
- `Dockerfile`, `compose.yaml`: 독립 개발 컨테이너
- `.env.example`: 선택적으로 사용하는 환경 변수 템플릿
- `.gitignore`, `.dockerignore`: 로컬 환경과 비밀 파일 제외

아래 명령은 모두 `jev` 폴더에서 실행합니다.

## Docker로 실행

Docker Desktop의 Linux 컨테이너 엔진을 실행한 뒤:

```sh
docker compose up -d --build
docker compose exec dev uv run --locked main.py
```

개발 컨테이너는 작업을 위해 대기 상태로 유지됩니다. 호스트에서 수정한 파일은 바로 반영되며, 가상 환경은 컨테이너 전용 볼륨에 저장합니다. 기본 구성에서는 외부 포트를 열지 않습니다.

```sh
# 컨테이너 셸
docker compose exec dev sh

# 의존성 추가 (pyproject.toml과 uv.lock에 반영)
docker compose exec dev uv add 패키지이름

# 상태 확인 및 종료
docker compose ps
docker compose down
```

## 로컬에서 실행

uv가 설치되어 있으면:

```sh
uv sync --locked
uv run --locked main.py
```

## 환경 변수

필요하면 `.env.example`을 `.env`로 복사하고 값을 수정합니다. PowerShell에서는:

```powershell
Copy-Item .env.example .env
```

Compose는 `.env`의 `JEV_GREETING`을 컨테이너에 전달합니다. 로컬 실행 시에는 다음 명령으로 읽습니다.

```sh
uv run --locked --env-file .env main.py
```

`.env`는 Git과 Docker 이미지에서 제외됩니다. 의존성을 변경한 뒤에는 `uv.lock`도 함께 커밋합니다.
