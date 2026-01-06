import streamlit as st
import plotly.graph_objects as go
from streamlit_plotly_events import plotly_events

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

CARDIO_RADIAL = [
    ("A", "Heart (chambers, valves, layers, pericardium)"),
    ("B", "Conduction system (SA node → Purkinje fibres)"),
    ("C", "Coronary circulation (RCA/LCA, LAD/LCx, coronary veins)"),
    ("D", "Blood vessels (arteries, arterioles, capillaries, veins)"),
    ("E", "Blood (RBC/WBC/platelets + plasma)"),
    ("F", "Pressure/chemo regulation (baroreceptors, chemoreceptors)"),
    ("G", "Autonomic control (sympathetic + vagus)"),
    ("H", "Foetal/paeds structures (ductus arteriosus, foramen ovale, etc.)"),
]

CARDIO_DETAILS = {
    "A": [
        "Pericardium: fibrous, serous (parietal/visceral), pericardial cavity",
        "Chambers: RA, LA, RV, LV",
        "Septa: interatrial, interventricular (muscular/membranous)",
        "Valves: tricuspid, mitral, pulmonary, aortic",
        "Support: chordae tendineae, papillary muscles",
        "Layers: endocardium, myocardium, epicardium",
    ],
    "B": [
        "SA node", "Internodal pathways", "AV node",
        "Bundle of His", "Right bundle branch",
        "Left bundle branch (anterior/posterior fascicles)",
        "Purkinje fibres",
    ],
    "C": [
        "RCA → marginal branch, posterior descending (PDA)",
        "LCA → LAD, LCx",
        "Coronary sinus",
        "Great, middle, small cardiac veins",
    ],
    "D": [
        "Aorta (ascending, arch, descending, abdominal)",
        "Elastic arteries; muscular arteries; arterioles",
        "Capillaries (continuous/fenestrated/sinusoidal)",
        "Venules; medium veins; SVC; IVC",
        "Pulmonary trunk/arteries; pulmonary veins",
    ],
    "E": [
        "Cells: RBCs; WBCs (neutrophils, lymphocytes, monocytes, eosinophils, basophils); platelets",
        "Plasma: water, electrolytes, proteins (albumin, globulins, fibrinogen), nutrients, hormones, wastes",
    ],
    "F": [
        "Baroreceptors: carotid sinus, aortic arch",
        "Chemoreceptors: carotid bodies, aortic bodies",
    ],
    "G": [
        "Sympathetic cardiac nerves (incl. cervical ganglia pathways)",
        "Parasympathetic: vagus nerve (CN X)",
    ],
    "H": [
        "Foetal shunts: foramen ovale, ductus arteriosus, ductus venosus",
        "Umbilical circulation: umbilical vein, umbilical arteries",
        "Postnatal remnants (e.g., ligamentum arteriosum) (overview)",
    ],
}

def radial_plot(nodes, center_label="Cardiovascular"):
    """
    nodes: list of (letter, label)
    Returns a Plotly figure arranged in a radial layout.
    """
    n = len(nodes)
    R = 1.0

    # Center node
    x = [0.0]
    y = [0.0]
    text = [f"<b>{center_label}</b>"]

    # Outer nodes on a circle
    for i, (letter, label) in enumerate(nodes):
        theta = 2 * math.pi * i / n
        x.append(R * math.cos(theta))
        y.append(R * math.sin(theta))
        text.append(f"<b>{letter}</b><br>{label}")

    # Lines from center to each outer node
    line_x = []
    line_y = []
    for i in range(1, n + 1):
        line_x += [0.0, x[i], None]
        line_y += [0.0, y[i], None]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=line_x, y=line_y,
        mode="lines",
        hoverinfo="skip"
    ))

    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode="markers+text",
        text=[""] * (n + 1),
        hovertext=text,
        hoverinfo="text",
        marker=dict(size=[42] + [34] * n),
        customdata=["CENTER"] + [letter for (letter, _) in nodes],  # for click detection
    ))

    fig.update_layout(
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        margin=dict(l=10, r=10, t=10, b=10),
        height=500,
    )
    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    return fig


def cardio_radial_ui():
    st.subheader("Cardiovascular Radial Map")

    fig = radial_plot(CARDIO_RADIAL, center_label="Cardiovascular")

    # Capture clicks from plotly
    clicked = plotly_events(fig, click_event=True, hover_event=False, select_event=False, override_height=520)

    # Store selection in session state
    st.session_state.setdefault("cardio_selected_letter", None)

    if clicked:
        point = clicked[0]
        # point["customdata"] corresponds to our letter (or CENTER)
        key = point.get("customdata")
        if key and key != "CENTER":
            st.session_state.cardio_selected_letter = key

    # Render details
    letter = st.session_state.cardio_selected_letter
    if letter:
        title = next((lbl for (L, lbl) in CARDIO_RADIAL if L == letter), "")
        st.markdown(f"### {letter} — {title}")
        for item in CARDIO_DETAILS.get(letter, []):
            st.write(f"- {item}")
    else:
        st.info("Click a lettered node (A–H) to view the parts in that category.")

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
    # ADD STUFF HERE!

    if system_id == "cardio":
        cardio_radial_ui()

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





