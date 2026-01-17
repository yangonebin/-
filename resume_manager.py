"""
양한빈 이력서 관리 시스템
- 이력서 정보 통합 관리
- 자기소개서 AI 추천 시스템
"""

import json
from datetime import datetime
from typing import Dict, List, Optional

class ResumeManager:
    """이력서 정보를 관리하는 클래스"""

    def __init__(self):
        self.personal_info = {
            "name": "양한빈",
            "birth_date": "2000-02-05",
            "phone": "010-3861-4897",
            "email": "footballcf0205@gmail.com",
            "address": "부산광역시 수영구 남천동로 41번길",
            "portfolio": "https://yangonebin.github.io/yangonebin/",
            "github": "https://github.com/yangonebin"
        }

        self.education = [
            {
                "institution": "부산대학교",
                "major": "경영학과",
                "degree": "학사",
                "start_date": "2019-03",
                "end_date": "2025-08",
                "gpa": "3.48/4.5",
                "status": "졸업"
            },
            {
                "institution": "부산대학교",
                "major": "예술문화영상학과",
                "degree": "부전공",
                "start_date": "2023-03",
                "end_date": "2025-12",
                "status": "수료"
            }
        ]

        self.training = [
            {
                "name": "SSAFY (삼성 청년 SW 아카데미)",
                "institution": "멀티캠퍼스",
                "start_date": "2025-07",
                "end_date": "2026-06",
                "description": "Python 기반 웹 풀스택 개발 및 생성형 AI 활용",
                "skills": ["Python", "Django", "Vue.js", "AI/ML", "Prompt Engineering"]
            },
            {
                "name": "CJ 리모트 인턴십",
                "institution": "CJ 올리브네트웍스",
                "start_date": "2023-09",
                "end_date": "2023-12",
                "description": "데이터 기획/분석 역량 강화 (CDS 양성)",
                "skills": ["데이터 분석", "엑셀", "데이터 사이언스"]
            }
        ]

        self.career = [
            {
                "company": "(주)이루티",
                "position": "PM Assistant / All-rounder",
                "start_date": "2023-05",
                "end_date": "2025-05",
                "description": "스타트업 초기 멤버로 비즈니스 스케일업 주도",
                "achievements": [
                    "매출 320만원 → 5억원 성장 견인",
                    "창사 이래 최초 영업이익 흑자 전환 기여",
                    "블록체인/3D 기술 시각화 및 콘텐츠 마케팅",
                    "프로젝트 매니징 및 외주사업 관리"
                ]
            }
        ]

        self.certifications = [
            {"name": "빅데이터분석기사", "issuer": "한국데이터산업진흥원", "date": "2025-12"},
            {"name": "정보처리기사", "issuer": "과기부", "date": "2025-09"},
            {"name": "사회조사분석사 2급", "issuer": "통계청", "date": "2025-06"},
            {"name": "SQLD", "issuer": "한국데이터산업진흥원", "date": "2024-12"},
            {"name": "ADsP", "issuer": "한국데이터산업진흥원", "date": "2024-09"},
            {"name": "컴활 1급", "issuer": "대한상공회의소", "date": "2024-04"},
            {"name": "GTQi 일러스트 1급", "issuer": "한국생산성본부", "date": "2024-03"},
            {"name": "GTQ 포토샵 1급", "issuer": "한국생산성본부", "date": "2024-02"}
        ]

        self.skills = {
            "programming": {
                "Python": "상급",
                "SQL": "중급",
                "Django": "중급",
                "Vue.js": "중급"
            },
            "data_analysis": {
                "Pandas": "상급",
                "NumPy": "상급",
                "SPSS": "중급",
                "Power BI": "중급"
            },
            "ai_ml": {
                "TensorFlow": "중급",
                "PyTorch": "중급",
                "MLflow": "중급",
                "FastAPI": "중급"
            },
            "creative": {
                "Adobe Photoshop": "상급",
                "Adobe Illustrator": "상급",
                "Final Cut Pro": "상급",
                "Adobe Animate": "상급"
            },
            "infrastructure": {
                "Docker": "중급",
                "Git": "중급"
            }
        }

        self.activities = [
            {
                "name": "남앞지 (유튜브 채널)",
                "organization": "유튜브",
                "start_date": "2024-12",
                "end_date": "2025-06",
                "description": "데이터 분석 및 통계학 교육 콘텐츠 제작",
                "achievements": ["구독자 3,000명 달성", "조회수 2만회 영상 보유"]
            },
            {
                "name": "A.B.S (AI 논문 스터디)",
                "organization": "부산대학교",
                "start_date": "2025-10",
                "end_date": "2026-01",
                "description": "AI 핵심 논문 심층 리뷰 (CNN, LSTM, Transformer 등)"
            },
            {
                "name": "KB 캠퍼스 스타",
                "organization": "KB 국민은행",
                "start_date": "2023-02",
                "end_date": "2023-07",
                "description": "KB 국민은행 홍보대사, 영상 콘텐츠 제작"
            },
            {
                "name": "청소년 SW 멘토링",
                "organization": "한국과학창의재단",
                "start_date": "2024-08",
                "end_date": "2024-11",
                "description": "중·고등학생 SW 해커톤 멘토"
            },
            {
                "name": "K-pop 콘텐츠 마케팅",
                "organization": "한국진로교육원",
                "start_date": "2022-12",
                "end_date": "2023-04",
                "description": "K-POP 아이돌 마케팅 실무 과정"
            },
            {
                "name": "M.A.D (축구 동아리)",
                "organization": "부산대학교",
                "start_date": "2019-03",
                "end_date": "2025-08",
                "description": "부산대학교 축구 동아리 활동"
            }
        ]

        self.awards = [
            {"name": "문화기획 포럼 장려상", "organization": "부산대학교", "date": "2024-12"},
            {"name": "SW 동행 프로젝트 이사장상", "organization": "한국과학창의재단", "date": "2024-12"},
            {"name": "대한민국 대학생 광고대회 챌린저상", "organization": "한국광고총연합회", "date": "2024-11"},
            {"name": "전공소개 콘텐츠 개발 장려상", "organization": "부산대학교", "date": "2024-01"},
            {"name": "ESG 지원사업 고용노동부 장관상", "organization": "고용노동부", "date": "2023-12"},
            {"name": "세가더 영상 공모전 최우수상", "organization": "포스코홀딩스", "date": "2023-12"},
            {"name": "연구 아이디어 공모전 최우수상", "organization": "부산대학교", "date": "2023-11"},
            {"name": "KB 캠퍼스 스타 종합 3등", "organization": "KB국민은행", "date": "2023-07"},
            {"name": "마케팅 콘텐츠 기획 최우수상", "organization": "한국진로교육원", "date": "2023-04"}
        ]

        self.projects = [
            {
                "name": "FinMatch - AI 주식가격 예측 서비스 (TFT-R)",
                "date": "2025",
                "duration": "팀 프로젝트",
                "team_size": "2명",
                "role": "Machine Learning Engineer (AI 모델링 및 API 서버 구축 전담)",
                "tech_stack": ["PyTorch", "TensorFlow", "LSTM", "Transformer (TFT)", "MLflow", "FastAPI", "Docker", "yfinance", "SQL"],
                "description": "전통적 기술 분석(일목균형표)과 딥러닝을 결합한 주가 예측 AI 시스템",
                "achievements": [
                    "LSTM → TFT(Temporal Fusion Transformer) 모델 진화를 통한 성능 개선",
                    "MLflow를 활용한 500회 이상 실험 추적 및 관리",
                    "평균 ROI 103.68%, 최고 ROI 292.45% 달성",
                    "FastAPI 기반 실시간 추론 API 서버 구축",
                    "회귀 vs 분류 모델 A/B 테스트를 통한 통계적 검증",
                    "일목균형표 지표를 수치화하여 피처 엔지니어링 수행",
                    "Docker 기반 배포 파이프라인 구축"
                ],
                "challenges": [
                    "금융권의 설명의무 규제로 인한 딥러닝 도입 어려움 인식",
                    "복잡한 피처(14개)가 오히려 노이즈로 작용하는 발견",
                    "순수 OHLCV 5개 피처로 단순화하여 성능 대폭 향상"
                ],
                "link": "https://github.com/yangonebin"
            },
            {
                "name": "MNIST 성능 개선 및 MLOps 구축",
                "date": "2025-12",
                "duration": "2일",
                "team_size": "1명",
                "tech_stack": ["PyTorch", "Hugging Face", "FastAPI", "Docker", "MLflow"],
                "description": "Vision Transformer(ViT) 모델 Fine-tuning 및 MLOps 파이프라인 구축",
                "achievements": [
                    "ViT 모델로 99.22% 정확도 달성",
                    "통계적 가설검증(T-test)으로 성능 우위 입증",
                    "FastAPI 기반 추론 서버 구축",
                    "Docker 컨테이너화 완료"
                ],
                "link": "https://winter-azimuth-dd0.notion.site/Project-Report-MNIST-MLOps-Pipeline-2bd1a506dcad80818476e00e25042394"
            }
        ]

    def get_summary(self) -> Dict:
        """이력서 요약 정보 반환"""
        return {
            "personal_info": self.personal_info,
            "education_count": len(self.education),
            "training_count": len(self.training),
            "career_years": self._calculate_career_years(),
            "certifications_count": len(self.certifications),
            "awards_count": len(self.awards),
            "skills_categories": len(self.skills)
        }

    def _calculate_career_years(self) -> float:
        """경력 연수 계산"""
        total_months = 0
        for career in self.career:
            start = datetime.strptime(career["start_date"], "%Y-%m")
            end = datetime.strptime(career["end_date"], "%Y-%m")
            months = (end.year - start.year) * 12 + (end.month - start.month)
            total_months += months
        return round(total_months / 12, 1)

    def get_skills_by_category(self, category: str) -> Dict:
        """카테고리별 스킬 조회"""
        return self.skills.get(category, {})

    def search_activities(self, keyword: str) -> List[Dict]:
        """키워드로 활동 검색"""
        results = []
        for activity in self.activities:
            if keyword.lower() in activity["name"].lower() or \
               keyword.lower() in activity["description"].lower():
                results.append(activity)
        return results

    def get_recent_achievements(self, limit: int = 5) -> List[Dict]:
        """최근 수상 내역 조회"""
        sorted_awards = sorted(self.awards,
                              key=lambda x: datetime.strptime(x["date"], "%Y-%m"),
                              reverse=True)
        return sorted_awards[:limit]

    def export_to_json(self, filename: str = "resume_data.json"):
        """이력서 데이터를 JSON으로 저장"""
        data = {
            "personal_info": self.personal_info,
            "education": self.education,
            "training": self.training,
            "career": self.career,
            "certifications": self.certifications,
            "skills": self.skills,
            "activities": self.activities,
            "awards": self.awards,
            "projects": self.projects,
            "last_updated": datetime.now().isoformat()
        }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return filename


class CoverLetterRecommender:
    """자기소개서 추천 시스템"""

    def __init__(self, resume_manager: ResumeManager):
        self.rm = resume_manager

        # 직무별 키워드 매핑
        self.job_keywords = {
            "데이터분석": ["데이터", "분석", "통계", "AI", "ML", "Python", "빅데이터"],
            "백엔드개발": ["백엔드", "서버", "API", "Django", "FastAPI", "데이터베이스"],
            "프론트엔드개발": ["프론트엔드", "Vue.js", "JavaScript", "UI/UX"],
            "MLOps": ["ML", "AI", "MLOps", "Docker", "FastAPI", "모델링"],
            "마케팅": ["마케팅", "콘텐츠", "기획", "영상", "홍보"],
            "기획": ["기획", "PM", "프로젝트", "매니징", "전략"]
        }

        # 자기소개서 템플릿 (실제 이력서의 자소서 내용 기반)
        self.cover_letter_templates = {
            "지원동기": self._get_motivation_template(),
            "목표달성경험": self._get_achievement_template(),
            "협업경험": self._get_collaboration_template(),
            "직무강점": self._get_strength_template()
        }

    def _get_motivation_template(self) -> str:
        return """[지원 동기 및 입사 후 계획]

{company_specific_intro}

저는 '{key_experience}'을(를) 통해 {field} 분야에 대한 깊은 관심을 갖게 되었습니다.
특히 {specific_skill}을(를) 활용하여 {achievement}을(를) 달성한 경험이 있습니다.

{company}에 입사하면:
1. {strength_1}을(를) 활용하여 {contribution_1}
2. {strength_2}와(과) {strength_3}을(를)결합하여 {contribution_2}
3. 지속적인 학습과 성장을 통해 {long_term_goal}

저의 {unique_background}과(와) {technical_skill}을(를)바탕으로
{company}의 {business_area}에 기여하는 인재가 되겠습니다."""

    def _get_achievement_template(self) -> str:
        return """[높은 목표 설정 및 달성 경험]

[{project_name}]

{challenge_description}

저는 "{goal}"라는 목표를 설정하고, 다음과 같이 달성했습니다:

1. 문제 정의: {problem}
2. 해결 전략: {strategy}
3. 실행 과정: {execution}
4. 성과: {achievement}

이 경험을 통해 {learning}을(를) 배웠으며,
입사 후에는 {application}에 적용하여 {contribution}하겠습니다."""

    def _get_collaboration_template(self) -> str:
        return """[협업을 통한 목표 달성 경험]

[{project_name}]

{situation_description}

협업 과정에서의 역할:
- {role_1}
- {role_2}
- {role_3}

{challenge_situation}

이를 해결하기 위해:
1. {solution_1}
2. {solution_2}
3. {result}

이 경험을 통해 {learning}을(를) 깨달았으며,
입사 후에는 {application}하는 팀원이 되겠습니다."""

    def _get_strength_template(self) -> str:
        return """[직무 강점 및 관련 경험]

[{strength_title}]

저의 가장 큰 강점은 '{core_strength}'입니다.

주요 경험:
1. {experience_1}
   - 기술: {tech_1}
   - 성과: {achievement_1}

2. {experience_2}
   - 기술: {tech_2}
   - 성과: {achievement_2}

3. {experience_3}
   - 기술: {tech_3}
   - 성과: {achievement_3}

이러한 역량을 바탕으로 {application}하여
{contribution}하는 전문가로 성장하겠습니다."""

    def analyze_job_fit(self, job_description: str) -> Dict:
        """직무 설명서 분석 및 적합도 평가"""
        job_desc_lower = job_description.lower()

        # 직무 카테고리별 매칭 점수
        matching_scores = {}
        for job_type, keywords in self.job_keywords.items():
            score = sum(1 for keyword in keywords if keyword.lower() in job_desc_lower)
            matching_scores[job_type] = score

        # 가장 적합한 직무 유형
        best_match = max(matching_scores.items(), key=lambda x: x[1])

        # 관련 스킬 추출
        relevant_skills = []
        for category, skills in self.rm.skills.items():
            for skill in skills.keys():
                if skill.lower() in job_desc_lower:
                    relevant_skills.append(skill)

        # 관련 경험 추출
        relevant_experiences = []
        for career in self.rm.career:
            if any(keyword.lower() in career["description"].lower()
                   for keyword in self.job_keywords[best_match[0]]):
                relevant_experiences.append(career)

        for activity in self.rm.activities:
            if any(keyword.lower() in activity["description"].lower()
                   for keyword in self.job_keywords[best_match[0]]):
                relevant_experiences.append(activity)

        return {
            "best_job_type": best_match[0],
            "match_score": best_match[1],
            "all_scores": matching_scores,
            "relevant_skills": relevant_skills,
            "relevant_experiences": relevant_experiences[:5]
        }

    def recommend_cover_letter_topics(self, job_type: str) -> List[str]:
        """직무 유형별 자기소개서 추천 주제"""
        recommendations = {
            "데이터분석": [
                "빅데이터분석기사 자격증 취득 과정과 데이터 분석 역량",
                "CJ 리모트 인턴십에서의 데이터 기획/분석 경험",
                "유튜브 채널 운영을 통한 데이터 시각화 및 스토리텔링",
                "SPSS, Power BI 등 분석 도구 활용 경험"
            ],
            "MLOps": [
                "MNIST MLOps 파이프라인 구축 프로젝트",
                "PyTorch, TensorFlow 활용 딥러닝 모델 구현",
                "Docker 기반 모델 서빙 및 배포 경험",
                "A.B.S 논문 스터디를 통한 AI 이론 깊이"
            ],
            "백엔드개발": [
                "Django, FastAPI 기반 백엔드 개발 경험",
                "SSAFY에서의 웹 풀스택 개발 교육",
                "데이터베이스 설계 및 SQL 활용 능력",
                "RESTful API 설계 및 구현"
            ],
            "마케팅": [
                "KB 캠퍼스 스타 홍보대사 활동",
                "K-pop 아이돌 마케팅 실무 경험",
                "유튜브 채널 '남앞지' 운영 (구독자 3K)",
                "Adobe Creative Suite 활용 콘텐츠 제작"
            ],
            "기획": [
                "(주)이루티에서 PM Assistant 역할 수행",
                "스타트업 비즈니스 스케일업 주도 (매출 320만원→5억원)",
                "프로젝트 매니징 및 외주사업 관리",
                "다양한 이해관계자와의 커뮤니케이션 경험"
            ]
        }

        return recommendations.get(job_type, [
            "다양한 활동을 통한 문제해결 능력",
            "팀 프로젝트 협업 경험",
            "자격증 취득을 통한 전문성 강화",
            "지속적인 자기계발 의지"
        ])

    def generate_customized_tips(self, job_type: str, company: str) -> Dict:
        """맞춤형 자기소개서 작성 팁"""
        tips = {
            "강조할_강점": [],
            "활용할_경험": [],
            "키워드": [],
            "작성_주의사항": []
        }

        if job_type == "MLOps":
            tips["강조할_강점"] = [
                "PyTorch, TensorFlow 활용 모델링 능력",
                "Docker, FastAPI 기반 인프라 구축 경험",
                "MLflow를 통한 실험 관리 능력",
                "통계적 가설검증 능력"
            ]
            tips["활용할_경험"] = [
                "MNIST MLOps 프로젝트",
                "A.B.S AI 논문 스터디",
                "SSAFY ML/DL 교육"
            ]
            tips["키워드"] = [
                "모델 서빙", "실험 관리", "파이프라인",
                "자동화", "모니터링", "성능 최적화"
            ]

        elif job_type == "데이터분석":
            tips["강조할_강점"] = [
                "빅데이터분석기사 자격증",
                "Python 기반 데이터 분석",
                "통계적 분석 능력",
                "데이터 시각화 및 스토리텔링"
            ]
            tips["활용할_경험"] = [
                "CJ 리모트 인턴십",
                "유튜브 채널 운영",
                "SPSS, Power BI 활용"
            ]
            tips["키워드"] = [
                "인사이트 도출", "데이터 기반 의사결정",
                "비즈니스 가치 창출", "데이터 리터러시"
            ]

        elif job_type == "기획":
            tips["강조할_강점"] = [
                "PM Assistant 실무 경험",
                "비즈니스 스케일업 주도",
                "프로젝트 매니징",
                "All-rounder 역량"
            ]
            tips["활용할_경험"] = [
                "(주)이루티 경력",
                "다양한 프로젝트 리더십",
                "외주사업 관리"
            ]
            tips["키워드"] = [
                "프로젝트 관리", "리스크 관리",
                "이해관계자 조율", "비즈니스 성과"
            ]

        tips["작성_주의사항"] = [
            f"{company}의 비전과 본인의 목표를 연결하여 작성",
            "구체적인 수치와 성과를 포함",
            "STAR 기법 활용 (Situation, Task, Action, Result)",
            "직무 키워드를 자연스럽게 녹여내기",
            "나열식이 아닌 스토리텔링 형식으로 작성"
        ]

        return tips


def main():
    """메인 실행 함수"""
    # 이력서 관리자 초기화
    rm = ResumeManager()

    # 자기소개서 추천 시스템 초기화
    clr = CoverLetterRecommender(rm)

    print("=" * 80)
    print("양한빈 이력서 관리 시스템")
    print("=" * 80)
    print()

    # 이력서 요약
    summary = rm.get_summary()
    print("📋 이력서 요약")
    print(f"  - 이름: {summary['personal_info']['name']}")
    print(f"  - 이메일: {summary['personal_info']['email']}")
    print(f"  - 학력: {summary['education_count']}개")
    print(f"  - 교육: {summary['training_count']}개")
    print(f"  - 경력: {summary['career_years']}년")
    print(f"  - 자격증: {summary['certifications_count']}개")
    print(f"  - 수상: {summary['awards_count']}개")
    print()

    # 최근 수상 내역
    print("🏆 최근 수상 내역 (Top 5)")
    for award in rm.get_recent_achievements(5):
        print(f"  - {award['name']} ({award['organization']}, {award['date']})")
    print()

    # 스킬 요약
    print("💻 보유 스킬")
    for category, skills in rm.skills.items():
        print(f"  [{category}]")
        for skill, level in list(skills.items())[:3]:
            print(f"    - {skill}: {level}")
    print()

    # 자기소개서 추천 예시
    print("=" * 80)
    print("자기소개서 추천 시스템")
    print("=" * 80)
    print()

    # MLOps 직무 분석 예시
    job_description = """
    MLOps 엔지니어를 모집합니다.
    - 머신러닝 모델 개발 및 배포 파이프라인 구축
    - PyTorch, TensorFlow 활용 경험
    - Docker, Kubernetes 기반 인프라 관리
    - FastAPI를 통한 모델 서빙
    - 모델 성능 모니터링 및 최적화
    """

    print("�� 직무 적합도 분석 (MLOps 직무 기준)")
    fit_analysis = clr.analyze_job_fit(job_description)
    print(f"  - 가장 적합한 직무: {fit_analysis['best_job_type']}")
    print(f"  - 매칭 점수: {fit_analysis['match_score']}")
    print(f"  - 관련 스킬: {', '.join(fit_analysis['relevant_skills'][:5])}")
    print()

    # 추천 주제
    print("✍️ 추천 자기소개서 주제")
    topics = clr.recommend_cover_letter_topics("MLOps")
    for i, topic in enumerate(topics, 1):
        print(f"  {i}. {topic}")
    print()

    # 작성 팁
    print("💡 맞춤형 작성 팁")
    tips = clr.generate_customized_tips("MLOps", "툰스퀘어")

    print("  [강조할 강점]")
    for strength in tips["강조할_강점"]:
        print(f"    - {strength}")

    print("\n  [활용할 경험]")
    for exp in tips["활용할_경험"]:
        print(f"    - {exp}")

    print("\n  [핵심 키워드]")
    print(f"    {', '.join(tips['키워드'])}")

    print("\n  [작성 주의사항]")
    for i, note in enumerate(tips["작성_주의사항"], 1):
        print(f"    {i}. {note}")
    print()

    # JSON 내보내기
    print("=" * 80)
    filename = rm.export_to_json()
    print(f"✅ 이력서 데이터를 {filename}에 저장했습니다.")
    print("=" * 80)


if __name__ == "__main__":
    main()
