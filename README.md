# 양한빈 이력서 관리 시스템

Flask 기반 이력서 데이터 관리 웹 애플리케이션

## 기능

- 자격증, 수상, 활동, 프로젝트, 경력 데이터 관리 (CRUD)
- SQLite 데이터베이스
- 자소서 문항 관리 (LocalStorage)
- 엑셀 다운로드 기능

## 로컬 실행

```bash
# 의존성 설치
pip install -r requirements.txt

# DB 초기화
python init_db.py

# 서버 실행
python app.py
```

http://localhost:5000 접속

## 서버 배포 (Render.com)

1. GitHub 저장소 연결
2. Build Command: `pip install -r requirements.txt && python init_db.py`
3. Start Command: `gunicorn app:app`

## 기술 스택

- Backend: Flask, SQLite
- Frontend: Vanilla JavaScript, HTML/CSS
- Deployment: Gunicorn
