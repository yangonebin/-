# -*- coding: utf-8 -*-
"""
양한빈 이력서 관리 웹 애플리케이션
Flask 기반 웹 인터페이스
"""

from flask import Flask, render_template, request, jsonify, send_file
from resume_manager import ResumeManager, CoverLetterRecommender
from database import ResumeDatabase
import os
import sys
import io

# Windows 콘솔 인코딩 문제 해결
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# 전역 인스턴스
rm = ResumeManager()
clr = CoverLetterRecommender(rm)
db = ResumeDatabase()


@app.route('/')
def index():
    """메인 페이지"""
    return render_template('index.html')


@app.route('/api/summary')
def get_summary():
    """이력서 요약 정보 API"""
    summary = rm.get_summary()
    return jsonify(summary)


@app.route('/api/personal-info')
def get_personal_info():
    """개인 정보 API"""
    return jsonify(rm.personal_info)


@app.route('/api/education')
def get_education():
    """학력 정보 API"""
    return jsonify(rm.education)


@app.route('/api/training')
def get_training():
    """교육 정보 API"""
    return jsonify(rm.training)


@app.route('/api/career')
def get_career():
    """경력 정보 API (DB에서 조회)"""
    career = db.get_all_career()
    return jsonify(career)


@app.route('/api/career/<int:career_id>', methods=['DELETE'])
def delete_career(career_id):
    """경력 삭제 API"""
    db.delete_career(career_id)
    return jsonify({'success': True, 'message': '경력이 삭제되었습니다.'})


@app.route('/api/certifications')
def get_certifications():
    """자격증 정보 API (DB에서 조회)"""
    certifications = db.get_all_certifications()
    return jsonify(certifications)


@app.route('/api/certifications/<int:cert_id>', methods=['PUT'])
def update_certification(cert_id):
    """자격증 수정 API"""
    data = request.get_json()
    db.update_certification(cert_id, data)
    return jsonify({'success': True, 'message': '자격증이 수정되었습니다.'})


@app.route('/api/certifications/<int:cert_id>', methods=['DELETE'])
def delete_certification(cert_id):
    """자격증 삭제 API"""
    db.delete_certification(cert_id)
    return jsonify({'success': True, 'message': '자격증이 삭제되었습니다.'})


@app.route('/api/skills')
def get_skills():
    """스킬 정보 API"""
    category = request.args.get('category')
    if category:
        return jsonify(rm.get_skills_by_category(category))
    return jsonify(rm.skills)


@app.route('/api/activities')
def get_activities():
    """활동 정보 API (DB에서 조회)"""
    activities = db.get_all_activities()
    keyword = request.args.get('keyword')
    if keyword:
        # 키워드 필터링
        filtered = [a for a in activities if keyword.lower() in a['name'].lower() or keyword.lower() in a.get('description', '').lower()]
        return jsonify(filtered)
    return jsonify(activities)


@app.route('/api/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    """활동 삭제 API"""
    db.delete_activity(activity_id)
    return jsonify({'success': True, 'message': '활동이 삭제되었습니다.'})


@app.route('/api/awards')
def get_awards():
    """수상 내역 API (DB에서 조회)"""
    awards = db.get_all_awards()
    limit = request.args.get('limit', type=int)
    if limit:
        return jsonify(awards[:limit])
    return jsonify(awards)


@app.route('/api/awards/<int:award_id>', methods=['DELETE'])
def delete_award(award_id):
    """수상 삭제 API"""
    db.delete_award(award_id)
    return jsonify({'success': True, 'message': '수상이 삭제되었습니다.'})


@app.route('/api/projects')
def get_projects():
    """프로젝트 정보 API (DB에서 조회)"""
    projects = db.get_all_projects()
    return jsonify(projects)


@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """프로젝트 삭제 API"""
    db.delete_project(project_id)
    return jsonify({'success': True, 'message': '프로젝트가 삭제되었습니다.'})


@app.route('/api/analyze-job', methods=['POST'])
def analyze_job():
    """직무 적합도 분석 API"""
    data = request.get_json()
    job_description = data.get('job_description', '')

    if not job_description:
        return jsonify({'error': '직무 설명을 입력해주세요.'}), 400

    analysis = clr.analyze_job_fit(job_description)
    return jsonify(analysis)


@app.route('/api/recommend-topics', methods=['POST'])
def recommend_topics():
    """자기소개서 주제 추천 API"""
    data = request.get_json()
    job_type = data.get('job_type', '데이터분석')

    topics = clr.recommend_cover_letter_topics(job_type)
    return jsonify({'topics': topics})


@app.route('/api/writing-tips', methods=['POST'])
def get_writing_tips():
    """자기소개서 작성 팁 API"""
    data = request.get_json()
    job_type = data.get('job_type', 'MLOps')
    company = data.get('company', '기업명')

    tips = clr.generate_customized_tips(job_type, company)
    return jsonify(tips)


@app.route('/api/export-json')
def export_json():
    """JSON 파일 다운로드"""
    filename = rm.export_to_json()
    return send_file(filename, as_attachment=True, download_name='resume_data.json')


@app.route('/api/cover-letter-template/<template_type>')
def get_cover_letter_template(template_type):
    """자기소개서 템플릿 조회"""
    template = clr.cover_letter_templates.get(template_type)
    if template:
        return jsonify({'template': template})
    return jsonify({'error': '템플릿을 찾을 수 없습니다.'}), 404


# ==================== 추가 CRUD API ====================
@app.route('/api/certifications', methods=['POST'])
def add_certification():
    """자격증 추가 API"""
    data = request.get_json()
    cert_id = db.add_certification(data)
    return jsonify({'success': True, 'id': cert_id, 'message': '자격증이 추가되었습니다.'})


@app.route('/api/awards', methods=['POST'])
def add_award():
    """수상 추가 API"""
    data = request.get_json()
    award_id = db.add_award(data)
    return jsonify({'success': True, 'id': award_id, 'message': '수상이 추가되었습니다.'})


@app.route('/api/activities', methods=['POST'])
def add_activity():
    """활동 추가 API"""
    data = request.get_json()
    activity_id = db.add_activity(data)
    return jsonify({'success': True, 'id': activity_id, 'message': '활동이 추가되었습니다.'})


@app.route('/api/projects', methods=['POST'])
def add_project():
    """프로젝트 추가 API"""
    data = request.get_json()
    project_id = db.add_project(data)
    return jsonify({'success': True, 'id': project_id, 'message': '프로젝트가 추가되었습니다.'})


@app.route('/api/career', methods=['POST'])
def add_career():
    """경력 추가 API"""
    data = request.get_json()
    career_id = db.add_career(data)
    return jsonify({'success': True, 'id': career_id, 'message': '경력이 추가되었습니다.'})


if __name__ == '__main__':
    # templates 폴더 생성
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # static 폴더 생성
    if not os.path.exists('static'):
        os.makedirs('static')

    print("=" * 80)
    print("양한빈 이력서 관리 시스템 웹 서버 시작")
    print("=" * 80)
    print()
    print("서버 주소: http://localhost:5000")
    print("모바일에서 접속: http://[내PC의IP]:5000")
    print()
    print("Ctrl+C를 눌러 서버를 종료할 수 있습니다.")
    print("=" * 80)
    print()

    app.run(debug=True, host='0.0.0.0', port=5000)
