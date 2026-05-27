import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards
import time

# ── 페이지 기본 설정 ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="자기소개 | Jihoo",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── 글로벌 CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ══════════════════════════════════════════════════
       Earth & Neon Palette
       BG       #0B1914  (deep forest dark green)
       Card     #1A3029  (dark khaki green)
       Accent   #CCFF00  (neon lime)
       Accent2  #00FF88  (neon mint — secondary glow)
       TextHi   #E8F5E2  (pale green-white)
       TextMid  #7DAF8A  (muted green)
       TextLow  #4A7060  (dim green-grey)
    ══════════════════════════════════════════════════ */

    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', 'Inter', sans-serif;
    }

    /* ── 전체 배경 ── */
    .stApp {
        background-color: #0B1914;
        background-image:
            radial-gradient(ellipse 80% 50% at 10% 0%, rgba(204,255,0,0.06) 0%, transparent 60%),
            radial-gradient(ellipse 60% 40% at 90% 100%, rgba(0,255,136,0.05) 0%, transparent 55%);
        color: #E8F5E2;
    }

    /* ── 숨기기 ── */
    #MainMenu, footer, header { visibility: hidden; }

    /* ── 히어로 섹션 ── */
    .hero-container {
        background: linear-gradient(135deg, rgba(26,48,41,0.95) 0%, rgba(11,25,20,0.98) 100%);
        border: 1px solid rgba(204,255,0,0.18);
        border-radius: 24px;
        padding: 3rem 2rem;
        text-align: center;
        backdrop-filter: blur(12px);
        margin-bottom: 2rem;
        box-shadow: 0 0 60px rgba(204,255,0,0.05), inset 0 1px 0 rgba(204,255,0,0.1);
    }
    .hero-avatar {
        width: 140px;
        height: 140px;
        border-radius: 50%;
        background: linear-gradient(135deg, #1A3029 0%, #0B1914 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1.5rem auto;
        font-size: 4rem;
        box-shadow:
            0 0 0 3px rgba(204,255,0,0.35),
            0 0 30px rgba(204,255,0,0.25),
            0 8px 32px rgba(0,0,0,0.5);
        border: 2px solid rgba(204,255,0,0.5);
    }
    .hero-name {
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #CCFF00 0%, #00FF88 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.3rem;
        letter-spacing: -0.02em;
        filter: drop-shadow(0 0 20px rgba(204,255,0,0.4));
    }
    .hero-title {
        font-size: 1.1rem;
        color: #7DAF8A;
        font-weight: 400;
        margin-bottom: 1rem;
        letter-spacing: 0.02em;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(204,255,0,0.08);
        border: 1px solid rgba(204,255,0,0.28);
        color: #CCFF00;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.82rem;
        margin: 0.2rem;
        font-weight: 500;
        letter-spacing: 0.01em;
        transition: background 0.2s, box-shadow 0.2s;
    }
    .hero-badge:hover {
        background: rgba(204,255,0,0.15);
        box-shadow: 0 0 12px rgba(204,255,0,0.2);
    }

    /* ── 섹션 카드 ── */
    .section-card {
        background: #1A3029;
        border: 1px solid rgba(204,255,0,0.1);
        border-radius: 16px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }
    .section-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 16px 48px rgba(0,0,0,0.4), 0 0 20px rgba(204,255,0,0.08);
        border-color: rgba(204,255,0,0.22);
    }
    .section-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #CCFF00;
        margin-bottom: 1.2rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        letter-spacing: 0.01em;
    }

    /* ── 스킬 바 ── */
    .skill-item { margin-bottom: 0.85rem; }
    .skill-label {
        display: flex;
        justify-content: space-between;
        margin-bottom: 0.3rem;
        font-size: 0.88rem;
        color: #E8F5E2;
        font-weight: 500;
    }
    .skill-pct { color: #CCFF00; font-weight: 600; }
    .skill-bar-bg {
        background: rgba(255,255,255,0.06);
        border-radius: 10px;
        height: 7px;
        overflow: hidden;
    }
    .skill-bar-fill {
        height: 100%;
        border-radius: 10px;
        background: linear-gradient(90deg, #CCFF00 0%, #00FF88 100%);
        box-shadow: 0 0 8px rgba(204,255,0,0.5);
    }

    /* ── 타임라인 ── */
    .timeline-item {
        position: relative;
        padding-left: 1.5rem;
        padding-bottom: 1.5rem;
        border-left: 2px solid rgba(204,255,0,0.2);
    }
    .timeline-item:last-child { border-left: 2px solid transparent; }
    .timeline-dot {
        position: absolute;
        left: -6px;
        top: 4px;
        width: 10px;
        height: 10px;
        border-radius: 50%;
        background: #CCFF00;
        box-shadow: 0 0 10px rgba(204,255,0,0.8), 0 0 20px rgba(204,255,0,0.3);
    }
    .timeline-period {
        font-size: 0.75rem;
        color: #CCFF00;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }
    .timeline-company {
        font-size: 1rem;
        font-weight: 700;
        color: #E8F5E2;
        margin-top: 0.2rem;
    }
    .timeline-role {
        font-size: 0.85rem;
        color: #7DAF8A;
        margin-top: 0.1rem;
    }
    .timeline-desc {
        font-size: 0.83rem;
        color: #4A7060;
        margin-top: 0.4rem;
        line-height: 1.6;
    }

    /* ── 프로젝트 카드 ── */
    .project-card {
        background: rgba(11,25,20,0.7);
        border: 1px solid rgba(204,255,0,0.1);
        border-radius: 12px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .project-card:hover {
        border-color: rgba(204,255,0,0.45);
        box-shadow: 0 0 20px rgba(204,255,0,0.08);
    }
    .project-title {
        font-weight: 700;
        color: #E8F5E2;
        font-size: 0.97rem;
        margin-bottom: 0.35rem;
    }
    .project-desc {
        color: #4A7060;
        font-size: 0.83rem;
        line-height: 1.6;
        margin-bottom: 0.6rem;
    }
    .tech-tag {
        display: inline-block;
        background: rgba(204,255,0,0.08);
        border: 1px solid rgba(204,255,0,0.22);
        color: #CCFF00;
        padding: 0.15rem 0.6rem;
        border-radius: 6px;
        font-size: 0.73rem;
        margin: 0.1rem;
        font-weight: 600;
        letter-spacing: 0.02em;
    }

    /* ── 연락처 ── */
    .contact-item {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        padding: 0.8rem 1rem;
        background: rgba(11,25,20,0.6);
        border-radius: 10px;
        margin-bottom: 0.6rem;
        color: #7DAF8A;
        font-size: 0.88rem;
        border: 1px solid rgba(204,255,0,0.08);
        transition: border-color 0.2s, color 0.2s;
    }
    .contact-item:hover {
        border-color: rgba(204,255,0,0.3);
        color: #E8F5E2;
    }
    .contact-icon { font-size: 1.15rem; }

    /* ── 버튼 오버라이드 ── */
    div[data-testid="stButton"] > button {
        background: #CCFF00 !important;
        color: #0B1914 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        letter-spacing: 0.02em !important;
        transition: box-shadow 0.2s, transform 0.15s !important;
        box-shadow: 0 0 20px rgba(204,255,0,0.25) !important;
    }
    div[data-testid="stButton"] > button:hover {
        box-shadow: 0 0 35px rgba(204,255,0,0.55) !important;
        transform: translateY(-2px) !important;
    }
    div[data-testid="stButton"] > button:active {
        transform: translateY(0) !important;
    }

    /* ── 텍스트 인풋 오버라이드 ── */
    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea {
        background: rgba(11,25,20,0.8) !important;
        border: 1px solid rgba(204,255,0,0.2) !important;
        border-radius: 8px !important;
        color: #E8F5E2 !important;
    }
    div[data-testid="stTextInput"] input:focus,
    div[data-testid="stTextArea"] textarea:focus {
        border-color: rgba(204,255,0,0.55) !important;
        box-shadow: 0 0 0 2px rgba(204,255,0,0.12) !important;
    }

    /* ── Streamlit Metric 카드 ── */
    div[data-testid="stMetric"] {
        background: #1A3029 !important;
        border: 1px solid rgba(204,255,0,0.12) !important;
        border-radius: 12px !important;
        padding: 1rem !important;
    }
    div[data-testid="stMetric"] label {
        color: #7DAF8A !important;
        font-size: 0.8rem !important;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        color: #CCFF00 !important;
        font-size: 1.55rem !important;
        font-weight: 700 !important;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricDelta"] {
        color: #4A7060 !important;
        font-size: 0.78rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════
# 1. 히어로 섹션
# ═══════════════════════════════════════════════════════
st.markdown(
    """
    <div class="hero-container">
        <div class="hero-avatar">👨‍💻</div>
        <div class="hero-name">Jihoo</div>
        <div class="hero-title">IT Engineer / Data Developer @ KDN</div>
        <div style="margin-top:0.8rem;">
            <span class="hero-badge">🏢 한전KDN</span>
            <span class="hero-badge">💡 데이터 엔지니어링</span>
            <span class="hero-badge">🐍 Python / Streamlit</span>
            <span class="hero-badge">☁️ Cloud & DevOps</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════
# 2. 핵심 지표 (Stats)
# ═══════════════════════════════════════════════════════
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric("💼 경력", "5+ 년", "IT 인프라·개발")
with c2:
    st.metric("🚀 프로젝트", "20+", "완료 프로젝트")
with c3:
    st.metric("🛠️ 기술 스택", "15+", "보유 기술")
with c4:
    st.metric("📜 자격증", "3", "보유 자격")

st.markdown("<br>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# 3. 메인 컨텐츠 (2열 레이아웃)
# ═══════════════════════════════════════════════════════
left_col, right_col = st.columns([1.1, 1], gap="large")

# ────────── 왼쪽 컬럼 ──────────
with left_col:

    # 3-1. About Me
    st.markdown(
        """
        <div class="section-card">
            <div class="section-title">👤 About Me</div>
            <p style="color:#7DAF8A; line-height:1.9; font-size:0.93rem;">
                안녕하세요! <strong style="color:#CCFF00;">한전KDN</strong>에서 근무하고 있는 IT 개발자 <strong style="color:#E8F5E2;">지후</strong>입니다.<br><br>
                전력 IT 인프라와 데이터 플랫폼 개발을 전문으로 하며,
                <strong style="color:#CCFF00;">Python</strong>과 <strong style="color:#CCFF00;">Streamlit</strong>을 활용한
                데이터 시각화·대시보드 개발에 열정을 갖고 있습니다.<br><br>
                복잡한 에너지 데이터를 누구나 쉽게 이해할 수 있는 인터페이스로 만드는 것을 목표로,
                오늘도 코드 한 줄 한 줄에 의미를 담아 개발하고 있습니다. 🔋
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 3-2. 기술 스킬
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🛠️ 기술 스택</div>', unsafe_allow_html=True)

    skills = [
        ("Python", 90),
        ("Streamlit / Dash", 85),
        ("SQL / PostgreSQL", 80),
        ("Docker / Kubernetes", 70),
        ("Spark / Hadoop", 65),
        ("React / JavaScript", 60),
        ("Linux / Shell Script", 75),
        ("Git / CI·CD", 80),
    ]

    for skill, pct in skills:
        st.markdown(
            f"""
            <div class="skill-item">
                <div class="skill-label"><span>{skill}</span><span class="skill-pct">{pct}%</span></div>
                <div class="skill-bar-bg">
                    <div class="skill-bar-fill" style="width:{pct}%;"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # 3-3. 자격증 & 교육
    st.markdown(
        """
        <div class="section-card">
            <div class="section-title">📜 자격증 · 교육</div>
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-period">2023</div>
                <div class="timeline-company">정보처리기사</div>
                <div class="timeline-role">한국산업인력공단</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-period">2022</div>
                <div class="timeline-company">AWS Solutions Architect – Associate</div>
                <div class="timeline-role">Amazon Web Services</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-period">2021</div>
                <div class="timeline-company">ADsP (데이터분석 준전문가)</div>
                <div class="timeline-role">한국데이터산업진흥원</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-period">2018</div>
                <div class="timeline-company">컴퓨터공학 학사 졸업</div>
                <div class="timeline-role">전자공학부 · 국내 4년제 대학</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ────────── 오른쪽 컬럼 ──────────
with right_col:

    # 3-4. 경력 사항
    st.markdown(
        """
        <div class="section-card">
            <div class="section-title">💼 경력 사항</div>
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-period">2021.03 – 현재</div>
                <div class="timeline-company">한전KDN (KDN)</div>
                <div class="timeline-role">IT 개발팀 · 주임연구원</div>
                <div class="timeline-desc">
                    전력 IT 시스템 운영 및 데이터 플랫폼 개발.<br>
                    Streamlit 기반 내부 대시보드 다수 구축.<br>
                    클라우드 전환 프로젝트(AWS) 참여.
                </div>
            </div>
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-period">2019.01 – 2021.02</div>
                <div class="timeline-company">IT 솔루션 기업 (전 직장)</div>
                <div class="timeline-role">백엔드 개발자</div>
                <div class="timeline-desc">
                    Python / Django 기반 REST API 개발.<br>
                    PostgreSQL DB 설계 및 쿼리 최적화.<br>
                    CI/CD 파이프라인 구성 (Jenkins, Docker).
                </div>
            </div>
            <div class="timeline-item">
                <div class="timeline-dot"></div>
                <div class="timeline-period">2018.07 – 2018.12</div>
                <div class="timeline-company">스타트업 인턴십</div>
                <div class="timeline-role">데이터 분석 인턴</div>
                <div class="timeline-desc">
                    Python pandas/matplotlib 활용 데이터 분석.<br>
                    Jupyter 기반 리포트 자동화.
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 3-5. 주요 프로젝트
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🚀 주요 프로젝트</div>', unsafe_allow_html=True)

    projects = [
        {
            "title": "⚡ 전력 데이터 모니터링 대시보드",
            "desc": "실시간 전력 사용량·이상 탐지 대시보드. Streamlit + WebSocket 기반으로 1,000+ 사용자 내부 운영.",
            "tags": ["Streamlit", "Python", "PostgreSQL", "Redis", "Docker"],
        },
        {
            "title": "☁️ 클라우드 인프라 비용 분석 시스템",
            "desc": "AWS 비용 데이터를 자동 수집·분석하여 절감 포인트를 시각화하는 내부 도구 개발.",
            "tags": ["Python", "AWS Boto3", "Pandas", "Plotly", "Airflow"],
        },
        {
            "title": "🔍 이상 탐지 ML 파이프라인",
            "desc": "설비 센서 데이터 기반 이상 탐지 모델 운영 파이프라인 구축. 검출 정확도 94%.",
            "tags": ["Python", "Scikit-learn", "Spark", "Kafka", "MLflow"],
        },
        {
            "title": "📊 자동화 KPI 리포트 시스템",
            "desc": "사업부별 KPI 지표 자동 집계 및 주간 리포트 메일 발송 시스템 구축·운영.",
            "tags": ["Python", "SQL", "Pandas", "Jinja2", "Cron"],
        },
    ]

    for p in projects:
        tags_html = "".join(f'<span class="tech-tag">{t}</span>' for t in p["tags"])
        st.markdown(
            f"""
            <div class="project-card">
                <div class="project-title">{p["title"]}</div>
                <div class="project-desc">{p["desc"]}</div>
                <div>{tags_html}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# 4. 연락처 & 인터랙티브 섹션
# ═══════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
cont_col, msg_col = st.columns([1, 1.5], gap="large")

with cont_col:
    st.markdown(
        """
        <div class="section-card">
            <div class="section-title">📬 연락처</div>
            <div class="contact-item">
                <span class="contact-icon">📧</span>
                <span>joon7.jihoo@kdn.com</span>
            </div>
            <div class="contact-item">
                <span class="contact-icon">🐙</span>
                <span>github.com/joon7jihoo-ctrl</span>
            </div>
            <div class="contact-item">
                <span class="contact-icon">🏢</span>
                <span>한전KDN · IT 개발팀</span>
            </div>
            <div class="contact-item">
                <span class="contact-icon">📍</span>
                <span>전라남도 나주시</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with msg_col:
    st.markdown(
        '<div class="section-card"><div class="section-title">✉️ 메시지 남기기</div>',
        unsafe_allow_html=True,
    )
    sender = st.text_input("이름", placeholder="홍길동", key="sender")
    message = st.text_area("메시지", placeholder="안녕하세요! ...", height=100, key="msg")

    if st.button("📨 보내기", use_container_width=True):
        if sender.strip() and message.strip():
            with st.spinner("전송 중..."):
                time.sleep(0.8)
            st.success(f"✅ {sender}님, 메시지가 전달되었습니다. 빠르게 회신드리겠습니다!")
            st.balloons()
        else:
            st.warning("이름과 메시지를 모두 입력해주세요.")
    st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════
# 5. 푸터
# ═══════════════════════════════════════════════════════
st.markdown(
    """
    <div style="text-align:center; margin-top:3rem; padding:1.5rem;
                border-top:1px solid rgba(204,255,0,0.1); color:#4A7060; font-size:0.82rem; letter-spacing:0.03em;">
        © 2026 Jihoo · Built with ❤️ using
        <strong style="color:#CCFF00; text-shadow:0 0 10px rgba(204,255,0,0.5);">Streamlit</strong>
    </div>
    """,
    unsafe_allow_html=True,
)
