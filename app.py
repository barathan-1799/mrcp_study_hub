%%writefile app.py
import streamlit as st

# ----------------------------
# Data model (expand later)
# ----------------------------
SYSTEMS = [
    {"id": "cardio", "name": "Cardiovascular", "emoji": "🫀", "desc": "Heart, vessels, circulation"},
    {"id": "resp",   "name": "Respiratory",    "emoji": "🫁", "desc": "Airways, lungs, gas exchange"},
    {"id": "neuro",  "name": "Neurology",      "emoji": "🧠", "desc": "CNS/PNS, development, seizures"},
    {"id": "gi",     "name": "Gastrointestinal","emoji":"🧻", "desc": "Liver, bowel, nutrition"},
    {"id": "renal",  "name": "Renal",          "emoji": "🫘", "desc": "Kidneys, fluids, electrolytes"},
    {"id": "endo",   "name": "Endocrine",      "emoji": "🧪", "desc": "Growth, diabetes, hormones"},
    {"id": "heme",   "name": "Haematology",    "emoji": "🩸", "desc": "Anaemia, bleeding, malignancy"},
    {"id": "msk",    "name": "MSK/Rheumatology","emoji":"🦴", "desc": "Joints, bone, inflammation"},
    {"id": "derm",   "name": "Dermatology",    "emoji": "🧴", "desc": "Rashes, eczema, infections"},
    {"id": "ent",    "name": "ENT",            "emoji": "👂", "desc": "Hearing, tonsils, sinus, airway"},
    {"id": "oph",    "name": "Ophthalmology",  "emoji": "👁️", "desc": "Red eye, vision, squint"},
    {"id": "psych",  "name": "Psych/Dev",      "emoji": "🧩", "desc": "Development, behaviour, ASD/ADHD"},
]

# ----------------------------
# Page styling
# ----------------------------
def inject_css():
    st.markdown(
        """
        <style>
        .app-title { font-size: 2.0rem; font-weight: 800; margin-bottom: 0.2rem; }
        .app-sub   { color: #6b7280; margin-top: 0; margin-bottom: 1.2rem; }
        div[data-testid="stVerticalBlock"] { gap: 0.7rem; }
        .card {
            border: 1px solid rgba(0,0,0,0.08);
            border-radius: 16px;
            padding: 14px 16px;
            background: white;
            box-shadow: 0 8px 18px rgba(0,0,0,0.04);
        }
        .card:hover {
            border-color: rgba(0,0,0,0.16);
            box-shadow: 0 10px 24px rgba(0,0,0,0.07);
        }
        .card-title { font-size: 1.05rem; font-weight: 750; }
        .card-desc  { color: #6b7280; font-size: 0.92rem; margin-top: 4px; }
        /* Make buttons look like invisible overlays */
        .stButton>button {
            width: 100%;
            border-radius: 14px;
            padding: 0;
            border: none;
            background: transparent;
        }
        .stButton>button:hover { background: transparent; }
        .stButton>button:focus { box-shadow: none; outline: none; }
        </style>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# Simple router using session_state
# ----------------------------
def init_state():
    st.session_state.setdefault("route", "home")
    st.session_state.setdefault("selected_system_id", None)

def go_home():
    st.session_state.route = "home"
    st.session_state.selected_system_id = None

def go_system(system_id: str):
    st.session_state.route = "system"
    st.session_state.selected_system_id = system_id

# ----------------------------
# UI components
# ----------------------------
def system_card(system):
    # We use a button to capture click, but we render the card ourselves
    clicked = st.button("",
                        key=f"btn_{system['id']}",
                        help=f"Open {system['name']}")
    st.markdown(
        f"""
        <div class="card">
          <div class="card-title">{system['emoji']} {system['name']}</div>
          <div class="card-desc">{system['desc']}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    if clicked:
        go_system(system["id"])

# ----------------------------
# Pages
# ----------------------------
def page_home():
    st.markdown('<div class="app-title">MRCPCH Study Hub</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-sub">Select a body system to start revising.</div>', unsafe_allow_html=True)

    # Grid layout
    cols = st.columns(3)
    for i, system in enumerate(SYSTEMS):
        with cols[i % 3]:
            system_card(system)

def page_system_detail():
    system_id = st.session_state.selected_system_id
    system = next((s for s in SYSTEMS if s["id"] == system_id), None)

    if not system:
        st.error("System not found.")
        st.button("Back", on_click=go_home)
        return

    st.markdown(f"<div class='app-title'>{system['emoji']} {system['name']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='app-sub'>{system['desc']}</div>", unsafe_allow_html=True)

    # Placeholder sections you can expand into real MRCPCH features
    st.subheader("Quick Actions")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.button("📚 Notes (coming soon)")
    with c2:
        st.button("📝 Question Bank (coming soon)")
    with c3:
        st.button("🧠 Flashcards (coming soon)")

    st.divider()
    st.subheader("Content Placeholder")
    st.info(
        "Add your MRCPCH content here: guidelines summaries, red flags, management algorithms, "
        "and system-based question sets."
    )

    st.button("← Back to Systems", on_click=go_home)

# ----------------------------
# App entry
# ----------------------------
def main():
    st.set_page_config(page_title="MRCPCH Study Hub", layout="wide")
    inject_css()
    init_state()

    # Sidebar nav (optional)
    with st.sidebar:
        st.header("Navigation")
        st.button("🏠 Systems", on_click=go_home)
        st.caption("Framework: add auth, progress tracking, Qbank, spaced repetition, etc.")

    if st.session_state.route == "home":
        page_home()
    else:
        page_system_detail()

if __name__ == "__main__":
    main()
