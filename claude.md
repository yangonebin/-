# 프로젝트 구조 정보

## 디렉토리 구조
```
-/
├── app.py                  # Flask 웹 애플리케이션 메인 파일
├── database.py             # SQLite DB 관리 모듈
├── resume_manager.py       # 이력서 데이터 관리 및 분석 로직
├── resume_data.json        # 이력서 원본 데이터 (JSON)
├── templates/
│   └── index.html         # 웹 인터페이스 템플릿
├── static/                # 정적 파일 (CSS, JS, 이미지)
└── *.pdf, *.jpg, *.xlsx   # 증빙 서류들
```

## 주요 파일 설명

### app.py
- Flask 기반 웹 서버
- API 엔드포인트 제공
- 포트: 5000

### database.py
- SQLite 기반 DB 관리
- 테이블: grades, certifications, awards, activities, projects, career
- CRUD 메서드 제공

### resume_data.json
- 개인정보, 학력, 교육, 경력, 자격증, 스킬, 활동, 수상, 프로젝트 정보
- **현재 문제**: 자격증 날짜가 "YYYY-MM" 형식 (일까지 필요)

## 현재 작업 상황
1. DB 구축 중단 상태
2. 자격증 날짜 형식 수정 필요 (월 → 일까지)
3. 서버 배포 준비 필요

## 스크린샷
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
