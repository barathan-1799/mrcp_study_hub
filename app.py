import streamlit as st

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

# ============================================================
# CARDIOVASCULAR TREE (Complete hierarchy from earlier list)
# ============================================================
CARDIO_TREE = {
    "Heart": {
        "External Anatomy": [
            "Apex",
            "Base",
            "Pericardium (fibrous)",
            "Pericardium (serous - parietal layer)",
            "Pericardium (serous - visceral layer / epicardium)",
            "Pericardial cavity (pericardial fluid)",
        ],
        "Heart Chambers": [
            "Right atrium",
            "Left atrium",
            "Right ventricle",
            "Left ventricle",
        ],
        "Septa": [
            "Interatrial septum",
            "Interventricular septum (muscular part)",
            "Interventricular septum (membranous part)",
        ],
        "Heart Valves": {
            "Atrioventricular valves": [
                "Tricuspid valve",
                "Mitral (bicuspid) valve",
            ],
            "Semilunar valves": [
                "Pulmonary valve",
                "Aortic valve",
            ],
        },
        "Valve Support Structures": [
            "Chordae tendineae",
            "Papillary muscles (anterior)",
            "Papillary muscles (posterior)",
            "Papillary muscles (septal - right ventricle)",
        ],
        "Myocardial Layers": [
            "Endocardium",
            "Myocardium",
            "Epicardium",
        ],
    },

    "Cardiac Conduction System": [
        "Sinoatrial (SA) node",
        "Internodal pathways",
        "Atrioventricular (AV) node",
        "Bundle of His",
        "Right bundle branch",
        "Left bundle branch",
        "Left anterior fascicle",
        "Left posterior fascicle",
        "Purkinje fibres",
    ],

    "Coronary Circulation": {
        "Coronary Arteries": {
            "Right coronary artery (RCA)": [
                "Marginal branch",
                "Posterior descending artery (PDA)",
            ],
            "Left coronary artery (LCA)": [
                "Left anterior descending (LAD)",
                "Left circumflex (LCx)",
            ],
        },
        "Coronary Veins": [
            "Great cardiac vein",
            "Middle cardiac vein",
            "Small cardiac vein",
            "Coronary sinus",
        ],
    },

    "Blood Vessels": {
        "Arteries": {
            "Elastic arteries": [
                "Aorta (ascending)",
                "Aorta (arch)",
                "Aorta (descending thoracic)",
                "Aorta (abdominal)",
            ],
            "Muscular arteries": [
                "Carotid arteries",
                "Subclavian arteries",
                "Femoral arteries",
                "Radial arteries",
            ],
            "Arterioles": [],
        },
        "Capillaries": [
            "Continuous capillaries",
            "Fenestrated capillaries",
            "Sinusoidal capillaries",
        ],
        "Veins": {
            "Venules": [],
            "Medium veins": [],
            "Large veins": [
                "Superior vena cava",
                "Inferior vena cava",
            ],
        },
    },

    "Major Named Vessels": {
        "Pulmonary Circulation": [
            "Pulmonary trunk",
            "Right pulmonary artery",
            "Left pulmonary artery",
            "Pulmonary capillaries",
            "Pulmonary veins (4)",
        ],
        "Systemic Circulation": {
            "Ascending aorta": [],
            "Aortic arch branches": [
                "Brachiocephalic trunk",
                "Left common carotid artery",
                "Left subclavian artery",
            ],
        },
    },

    "Blood": {
        "Cellular Components": {
            "Red blood cells (erythrocytes)": [],
            "White blood cells (leukocytes)": [
                "Neutrophils",
                "Lymphocytes",
                "Monocytes",
                "Eosinophils",
                "Basophils",
            ],
            "Platelets (thrombocytes)": [],
        },
        "Plasma Components": [
            "Water",
            "Electrolytes",
            "Proteins: albumin",
            "Proteins: globulins",
            "Proteins: fibrinogen",
            "Hormones",
            "Nutrients",
            "Waste products",
        ],
    },

    "Blood Pressure Regulation Structures": {
        "Baroreceptors": [
            "Carotid sinus",
            "Aortic arch",
        ],
        "Chemoreceptors": [
            "Carotid bodies",
            "Aortic bodies",
        ],
    },

    "Autonomic Innervation": {
        "Sympathetic": [
            "Cardiac nerves",
            "Cervical sympathetic ganglia",
        ],
        "Parasympathetic": [
            "Vagus nerve (CN X)",
        ],
    },

    "Foetal/Paediatric-Specific Structures": [
        "Foramen ovale",
        "Ductus arteriosus",
        "Ductus venosus",
        "Umbilical vein",
        "Umbilical arteries",
    ],
}

# ----------------------------
# Helpers for hierarchical navigation
# ----------------------------
def node_children(node):
    """Return list of child names if node is dict, else empty."""
    if isinstance(node, dict):
        return list(node.keys())
    return []

def is_leaf(node):
    """Leaf = list OR empty dict OR empty list"""
    return isinstance(node, list) or (isinstance(node, dict) and len(node) == 0)

def get_node_by_path(tree, path):
    """
    path: list[str]
    Returns the node at that path.
    """
    node = tree
    for p in path:
        if isinstance(node, dict) and p in node:
            node = node[p]
        else:
            return None
    return node

def set_path(new_path):
    st.session_state.cardio_path = new_path

def push_path(item):
    st.session_state.cardio_path.append(item)

def pop_path():
    if st.session_state.cardio_path:
        st.session_state.cardio_path.pop()

def reset_cardio_nav():
    st.session_state.cardio_path = []

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
            white-space: pre-line;
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

        /* Breadcrumb */
        .crumb { color: #6b7280; font-size: 0.95rem; }
        </style>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# Simple router using session_state
# ----------------------------
def init_state():
    st.session_state.setdefault("route", "home")  # home | system | cardio_tree
    st.session_state.setdefault("selected_system_id", None)
    st.session_state.setdefault("cardio_path", [])  # hierarchical path within cardio tree

def go_home():
    st.session_state.route = "home"
    st.session_state.selected_system_id = None
    reset_cardio_nav()

def go_system(system_id: str):
    st.session_state.route = "system"
    st.session_state.selected_system_id = system_id
    reset_cardio_nav()

def go_cardio_tree():
    st.session_state.route = "cardio_tree"
    st.session_state.selected_system_id = "cardio"
    reset_cardio_nav()

# ----------------------------
# UI components
# ----------------------------
def system_card(system):
    label = f"{system['emoji']} {system['name']}"
    if st.button(label, key=f"btn_{system['id']}", use_container_width=True):
        # Cardiovascular goes to the dedicated cardio tree page
        if system["id"] == "cardio":
            go_cardio_tree()
        else:
            go_system(system["id"])

def item_card(label, key):
    """Reusable clickable card button."""
    if st.button(label, key=key, use_container_width=True):
        return True
    return False

# ----------------------------
# Pages
# ----------------------------
def page_home():
    st.markdown('<div class="app-title">MRCPCH Study Hub</div>', unsafe_allow_html=True)
    st.markdown('<div class="app-sub">Select a body system to start revising.</div>', unsafe_allow_html=True)

    st.markdown('<div class="card-grid">', unsafe_allow_html=True)

    cols = st.columns(3)
    for i, system in enumerate(SYSTEMS):
        with cols[i % 3]:
            system_card(system)

    st.markdown('</div>', unsafe_allow_html=True)

def page_system_detail():
    # Generic placeholder for non-cardio systems
    system_id = st.session_state.selected_system_id
    system = next((s for s in SYSTEMS if s["id"] == system_id), None)

    if not system:
        st.error("System not found.")
        st.button("Back", on_click=go_home)
        return

    st.markdown(f"<div class='app-title'>{system['emoji']} {system['name']}</div>", unsafe_allow_html=True)
    st.info("This system page is a placeholder. Cardiovascular has a full component tree demo.")
    st.button("← Back to Systems", on_click=go_home)

def page_cardio_tree():
    st.markdown("<div class='app-title'>🫀 Cardiovascular</div>", unsafe_allow_html=True)

    path = st.session_state.cardio_path
    node = get_node_by_path(CARDIO_TREE, path)

    if node is None:
        st.error("Navigation error: path not found.")
        reset_cardio_nav()
        node = CARDIO_TREE

    # Breadcrumb
    crumb = " > ".join(["Cardiovascular"] + path) if path else "Cardiovascular"
    st.markdown(f"<div class='crumb'>{crumb}</div>", unsafe_allow_html=True)
    st.write("")

    # Controls
    c1, c2, c3 = st.columns([1, 1, 2])
    with c1:
        if st.button("⬅️ Back"):
            pop_path()
            st.rerun()
    with c2:
        if st.button("⟲ Reset"):
            reset_cardio_nav()
            st.rerun()
    with c3:
        st.button("← Back to Systems", on_click=go_home)

    st.write("")
    st.markdown('<div class="card-grid">', unsafe_allow_html=True)

    # If dict: show children as clickable cards
    if isinstance(node, dict):
        children = list(node.keys())
        if not children:
            st.info("No further sub-components.")
        else:
            cols = st.columns(2)
            for i, child in enumerate(children):
                with cols[i % 2]:
                    if item_card(child, key=f"cardio_{'_'.join(path)}_{child}"):
                        push_path(child)
                        st.rerun()

    # If list: show leaf items (not clickable)
    elif isinstance(node, list):
        if len(node) == 0:
            st.info("No further sub-components.")
        else:
            st.markdown("### Components")
            for item in node:
                st.write(f"- {item}")
    else:
        st.info("No further sub-components.")

    st.markdown("</div>", unsafe_allow_html=True)

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

        st.divider()
        st.caption("Cardio navigation state:")
        st.code(" > ".join(st.session_state.cardio_path) if st.session_state.cardio_path else "(root)")

    if st.session_state.route == "home":
        page_home()
    elif st.session_state.route == "system":
        page_system_detail()
    else:
        page_cardio_tree()

if __name__ == "__main__":
    main()
