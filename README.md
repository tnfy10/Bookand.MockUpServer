# Book& 더미 REST API

## 1. 기술 스택
#### 언어: Python 3.10 이상
#### 프레임워크: FastAPI

## 2. 설치해야 할 라이브러리
```shell
pip install fastapi
pip install "uvicorn[standard]"
pip install Faker
pip install pydantic
```

## 3. 실행 방법
```shell
uvicorn app.main:app --reload
```

### 기타 옵션
- 포트 번호 설정
```
--port=80
```

- 외부 접속 허용
```
--host=0.0.0.0
```

## 4. API 문서 주소

- Swagger UI - http://127.0.0.1:8000/docs
- ReDoc - http://127.0.0.1:8000/redoc
