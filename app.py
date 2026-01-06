import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

# ----------------------------
# Data model (expand later)
# ----------------------------
SYSTEMS = [
    {"id": "cardio", "name": "Cardiovascular", "emoji": "🫀", "desc": "Cardiovascular"},
    {"id": "resp",   "name": "Respiratory",    "emoji": "🫁", "desc": "Respiratory"},
    {"id": "neuro",  "name": "Neurology",      "emoji": "🧠", "desc": "Neurology"},
    {"id": "gi",     "name": "Gastrointestinal","emoji":"🧻", "desc": "Gastrointestinal"},
    {"id": "renal",  "name": "Nephro-urology", "emoji": "🫘", "desc": "Nephro-urology"},
    {"id": "endo",   "name": "Endocrine",      "emoji": "🧪", "desc": "Endocrine"},
    {"id": "heme",   "name": "Haematology",    "emoji": "🩸", "desc": "Haematology"},
    {"id": "imm",    "name": "Immunology",     "emoji": "🦠", "desc": "Immunology"},
    {"id": "onc",    "name": "Oncology",       "emoji": "♋", "desc": "Oncology"},
    {"id": "msk",    "name": "Rheumatology",   "emoji": "🦴", "desc": "Rheumatology"},
    {"id": "derm",   "name": "Dermatology",    "emoji": "🧴", "desc": "Dermatology"},
    {"id": "ent",    "name": "ENT",            "emoji": "👂", "desc": "ENT"},
    {"id": "oph",    "name": "Ophthalmology",  "emoji": "👁️", "desc": "Ophthalmology"},
    {"id": "psych",  "name": "Psychology & Development", "emoji": "🧩", "desc": "Psychology & Development"},
]

#############################
# ADD EXTRA FUNCTIONS HERE!
def cardio_mindmap_agraph():
    nodes = [
        Node(id="CV", label="Cardiovascular", size=35),
        Node(id="A", label="A Heart", size=25),
        Node(id="B", label="B Conduction", size=25),
        Node(id="C", label="C Coronary", size=25),
        Node(id="D", label="D Vessels", size=25),
        Node(id="E", label="E Blood", size=25),
        Node(id="F", label="F Baro/Chemo", size=25),
        Node(id="G", label="G Autonomic", size=25),
        Node(id="H", label="H Foetal", size=25),
    ]
    edges = [Edge(source="CV", target=k) for k in ["A","B","C","D","E","F","G","H"]]

    config = Config(
        width=700,
        height=500,
        directed=False,
        physics=True,
        hierarchical=False,
    )

    selected = agraph(nodes=nodes, edges=edges, config=config)
    st.write("Selected:", selected)  # returns selected node info
#############################
# ----------------------------
# Page styling
# ----------------------------
def inject_css():
    st.markdown(
        """
        <style>
        .app-title { font-size: 2.0rem; font-weight: 800; margin-bottom: 0.2rem; }
        .app-sub   { color: #6b7280; margin-top: 0; margin-bottom: 1.2rem; }

        /* Scope styling ONLY to the card grid wrapper */
        .card-grid .stButton>button {
            width: 100%;
            text-align: left;
            border: 1px solid rgba(0,0,0,0.08);
            border-radius: 16px;
            padding: 14px 16px;
            background: white;
            box-shadow: 0 8px 18px rgba(0,0,0,0.04);
            white-space: pre-line;       /* allow \n to render as a new line */
            line-height: 1.25rem;
        }
        .card-grid .stButton>button:hover {
            border-color: rgba(0,0,0,0.16);
            box-shadow: 0 10px 24px rgba(0,0,0,0.07);
        }
        .card-grid .stButton>button:focus {
            outline: none;
            box-shadow: 0 10px 24px rgba(0,0,0,0.10);
        }
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
    # The button IS the card now (no extra blank button / box)
    label = f"{system['emoji']} {system['name']}"
    if st.button(label, key=f"btn_{system['id']}", use_container_width=True):
        go_system(system["id"])

# ----------------------------
# Pages
# ----------------------------
def page_home():
    st.markdown('<div class="app-title">MRCPCH Study Hub</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-sub">Select a body system to start revising.</div>', unsafe_allow_html=True)

    # Wrap the grid in a class so CSS only affects these buttons
    st.markdown('<div class="card-grid">', unsafe_allow_html=True)

    cols = st.columns(3)
    for i, system in enumerate(SYSTEMS):
        with cols[i % 3]:
            system_card(system)

    st.markdown('</div>', unsafe_allow_html=True)

def page_system_detail():
    system_id = st.session_state.selected_system_id
    system = next((s for s in SYSTEMS if s["id"] == system_id), None)

    if not system:
        st.error("System not found.")
        st.button("Back", on_click=go_home)
        return

    st.markdown(f"<div class='app-title'>{system['emoji']} {system['name']}</div>", unsafe_allow_html=True)
    #######################################
    # ADD STUFF HERE!

    if system_id == "cardio":
        cardio_mindmap_agraph()

    ######################################

    st.button("← Back to Systems", on_click=go_home)

# ----------------------------
# App entry
# ----------------------------
def main():
    st.set_page_config(page_title="MRCPCH Study Hub", layout="wide")
    inject_css()
    init_state()

    with st.sidebar:
        st.header("Navigation")
        st.button("🏠 Systems", on_click=go_home)
        st.button("📈 Stats", on_click=go_home)
        st.button("🔠 Index", on_click=go_home)

    if st.session_state.route == "home":
        page_home()
    else:
        page_system_detail()

if __name__ == "__main__":
    main()








