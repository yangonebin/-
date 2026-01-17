"""
데이터베이스 관리 모듈
SQLite를 사용한 이력서 데이터 관리
"""

import sqlite3
import json
from datetime import datetime

class ResumeDatabase:
    def __init__(self, db_path='resume.db'):
        self.db_path = db_path
        self.init_db()

    def get_connection(self):
        """DB 연결"""
        return sqlite3.connect(self.db_path)

    def init_db(self):
        """데이터베이스 초기화"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # 성적 테이블
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS grades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                year TEXT NOT NULL,
                semester TEXT NOT NULL,
                type TEXT NOT NULL,
                category TEXT NOT NULL,
                subject TEXT NOT NULL,
                credit TEXT NOT NULL,
                grade TEXT NOT NULL,
                note TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # 자격증 테이블
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS certifications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade TEXT,
                issuer TEXT NOT NULL,
                date TEXT NOT NULL,
                number TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # 수상 테이블
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS awards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                organization TEXT NOT NULL,
                date TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # 활동 테이블
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                organization TEXT NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # 프로젝트 테이블
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date TEXT NOT NULL,
                team_size TEXT,
                role TEXT,
                tech_stack TEXT,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # 경력 테이블
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS career (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT NOT NULL,
                position TEXT NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        conn.close()

    # ==================== 성적 관리 ====================
    def add_grade(self, data):
        """성적 추가"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO grades (year, semester, type, category, subject, credit, grade, note)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (data['year'], data['semester'], data['type'], data['category'],
              data['subject'], data['credit'], data['grade'], data.get('note', '')))
        conn.commit()
        grade_id = cursor.lastrowid
        conn.close()
        return grade_id

    def get_all_grades(self):
        """모든 성적 조회"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM grades ORDER BY year DESC, semester')
        rows = cursor.fetchall()
        conn.close()

        grades = []
        for row in rows:
            grades.append({
                'id': row[0],
                'year': row[1],
                'semester': row[2],
                'type': row[3],
                'category': row[4],
                'subject': row[5],
                'credit': row[6],
                'grade': row[7],
                'note': row[8]
            })
        return grades

    def update_grade(self, grade_id, data):
        """성적 수정"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE grades
            SET year=?, semester=?, type=?, category=?, subject=?, credit=?, grade=?, note=?
            WHERE id=?
        ''', (data['year'], data['semester'], data['type'], data['category'],
              data['subject'], data['credit'], data['grade'], data.get('note', ''), grade_id))
        conn.commit()
        conn.close()

    def delete_grade(self, grade_id):
        """성적 삭제"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM grades WHERE id=?', (grade_id,))
        conn.commit()
        conn.close()

    # ==================== 자격증 관리 ====================
    def add_certification(self, data):
        """자격증 추가"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO certifications (name, grade, issuer, date, number)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['name'], data.get('grade', '-'), data['issuer'],
              data['date'], data.get('number', '')))
        conn.commit()
        cert_id = cursor.lastrowid
        conn.close()
        return cert_id

    def get_all_certifications(self):
        """모든 자격증 조회"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM certifications ORDER BY date DESC')
        rows = cursor.fetchall()
        conn.close()

        certs = []
        for row in rows:
            certs.append({
                'id': row[0],
                'name': row[1],
                'grade': row[2],
                'issuer': row[3],
                'date': row[4],
                'number': row[5]
            })
        return certs

    def update_certification(self, cert_id, data):
        """자격증 수정"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE certifications
            SET name=?, grade=?, issuer=?, date=?, number=?
            WHERE id=?
        ''', (data['name'], data.get('grade', '-'), data['issuer'],
              data['date'], data.get('number', ''), cert_id))
        conn.commit()
        conn.close()

    def delete_certification(self, cert_id):
        """자격증 삭제"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM certifications WHERE id=?', (cert_id,))
        conn.commit()
        conn.close()

    # ==================== 수상 관리 ====================
    def add_award(self, data):
        """수상 추가"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO awards (name, organization, date)
            VALUES (?, ?, ?)
        ''', (data['name'], data['organization'], data['date']))
        conn.commit()
        award_id = cursor.lastrowid
        conn.close()
        return award_id

    def get_all_awards(self):
        """모든 수상 조회"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM awards ORDER BY date DESC')
        rows = cursor.fetchall()
        conn.close()

        awards = []
        for row in rows:
            awards.append({
                'id': row[0],
                'name': row[1],
                'organization': row[2],
                'date': row[3]
            })
        return awards

    def delete_award(self, award_id):
        """수상 삭제"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM awards WHERE id=?', (award_id,))
        conn.commit()
        conn.close()

    # ==================== 활동 관리 ====================
    def add_activity(self, data):
        """활동 추가"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO activities (name, organization, start_date, end_date, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['name'], data['organization'], data['start_date'],
              data['end_date'], data.get('description', '')))
        conn.commit()
        activity_id = cursor.lastrowid
        conn.close()
        return activity_id

    def get_all_activities(self):
        """모든 활동 조회"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM activities ORDER BY start_date DESC')
        rows = cursor.fetchall()
        conn.close()

        activities = []
        for row in rows:
            activities.append({
                'id': row[0],
                'name': row[1],
                'organization': row[2],
                'start_date': row[3],
                'end_date': row[4],
                'description': row[5]
            })
        return activities

    def delete_activity(self, activity_id):
        """활동 삭제"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM activities WHERE id=?', (activity_id,))
        conn.commit()
        conn.close()

    # ==================== 프로젝트 관리 ====================
    def add_project(self, data):
        """프로젝트 추가"""
        conn = self.get_connection()
        cursor = conn.cursor()
        tech_stack = json.dumps(data.get('tech_stack', []))
        cursor.execute('''
            INSERT INTO projects (name, date, team_size, role, tech_stack, description)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (data['name'], data['date'], data.get('team_size', ''),
              data.get('role', ''), tech_stack, data.get('description', '')))
        conn.commit()
        project_id = cursor.lastrowid
        conn.close()
        return project_id

    def get_all_projects(self):
        """모든 프로젝트 조회"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM projects ORDER BY date DESC')
        rows = cursor.fetchall()
        conn.close()

        projects = []
        for row in rows:
            projects.append({
                'id': row[0],
                'name': row[1],
                'date': row[2],
                'team_size': row[3],
                'role': row[4],
                'tech_stack': json.loads(row[5]) if row[5] else [],
                'description': row[6]
            })
        return projects

    def delete_project(self, project_id):
        """프로젝트 삭제"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM projects WHERE id=?', (project_id,))
        conn.commit()
        conn.close()

    # ==================== 경력 관리 ====================
    def add_career(self, data):
        """경력 추가"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO career (company, position, start_date, end_date, description)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['company'], data['position'], data['start_date'],
              data['end_date'], data.get('description', '')))
        conn.commit()
        career_id = cursor.lastrowid
        conn.close()
        return career_id

    def get_all_career(self):
        """모든 경력 조회"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM career ORDER BY start_date DESC')
        rows = cursor.fetchall()
        conn.close()

        careers = []
        for row in rows:
            careers.append({
                'id': row[0],
                'company': row[1],
                'position': row[2],
                'start_date': row[3],
                'end_date': row[4],
                'description': row[5]
            })
        return careers

    def delete_career(self, career_id):
        """경력 삭제"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM career WHERE id=?', (career_id,))
        conn.commit()
        conn.close()
