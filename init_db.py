# -*- coding: utf-8 -*-
"""
데이터베이스 초기화 및 데이터 삽입 스크립트
resume_data.json의 데이터를 SQLite DB에 삽입
"""

import json
import sys
import io
from database import ResumeDatabase

# Windows 콘솔 인코딩 문제 해결
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def init_database():
    """DB 초기화 및 데이터 삽입"""

    # DB 인스턴스 생성
    db = ResumeDatabase()
    print("OK 데이터베이스 초기화 완료")

    # JSON 데이터 로드
    with open('resume_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    print("OK resume_data.json 로드 완료")

    # 자격증 데이터 삽입
    print("\n[자격증 데이터 삽입]")
    for cert in data['certifications']:
        cert_id = db.add_certification(cert)
        print(f"  - {cert['name']} (취득일: {cert['date']}) [ID: {cert_id}]")

    # 수상 데이터 삽입
    print("\n[수상 데이터 삽입]")
    for award in data['awards']:
        award_id = db.add_award(award)
        print(f"  - {award['name']} ({award['date']}) [ID: {award_id}]")

    # 활동 데이터 삽입
    print("\n[활동 데이터 삽입]")
    for activity in data['activities']:
        activity_id = db.add_activity(activity)
        print(f"  - {activity['name']} ({activity['start_date']} ~ {activity['end_date']}) [ID: {activity_id}]")

    # 프로젝트 데이터 삽입
    print("\n[프로젝트 데이터 삽입]")
    for project in data['projects']:
        project_id = db.add_project(project)
        print(f"  - {project['name']} ({project['date']}) [ID: {project_id}]")

    # 경력 데이터 삽입
    print("\n[경력 데이터 삽입]")
    for career in data['career']:
        career_id = db.add_career(career)
        print(f"  - {career['company']} - {career['position']} ({career['start_date']} ~ {career['end_date']}) [ID: {career_id}]")

    print("\n" + "="*80)
    print("OK 모든 데이터 삽입 완료!")
    print("="*80)

    # 데이터 확인
    print("\n[삽입된 데이터 확인]")
    print(f"  - 자격증: {len(db.get_all_certifications())}개")
    print(f"  - 수상: {len(db.get_all_awards())}개")
    print(f"  - 활동: {len(db.get_all_activities())}개")
    print(f"  - 프로젝트: {len(db.get_all_projects())}개")
    print(f"  - 경력: {len(db.get_all_career())}개")

if __name__ == '__main__':
    print("="*80)
    print("데이터베이스 초기화 시작")
    print("="*80)
    init_database()
