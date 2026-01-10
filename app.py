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
# CARDIO / RESP / NEURO TREES (from previous code)
# ============================================================
# (Kept exactly as-is; not repeated here to keep focus. You should paste
#  your existing CARDIO_TREE, RESP_TREE, NEURO_TREE above this line.)
# ------------------------------------------------------------
# For completeness in a single file, include them here:
# ============================================================

# ---- CARDIO_TREE (shortened comment: unchanged from your previous code) ----
CARDIO_TREE = {
    "Heart": {
        "External Anatomy": [
            "Apex", "Base", "Pericardium (fibrous)",
            "Pericardium (serous - parietal layer)",
            "Pericardium (serous - visceral layer / epicardium)",
            "Pericardial cavity (pericardial fluid)",
        ],
        "Heart Chambers": ["Right atrium", "Left atrium", "Right ventricle", "Left ventricle"],
        "Septa": [
            "Interatrial septum",
            "Interventricular septum (muscular part)",
            "Interventricular septum (membranous part)",
        ],
        "Heart Valves": {
            "Atrioventricular valves": ["Tricuspid valve", "Mitral (bicuspid) valve"],
            "Semilunar valves": ["Pulmonary valve", "Aortic valve"],
        },
        "Valve Support Structures": [
            "Chordae tendineae",
            "Papillary muscles (anterior)",
            "Papillary muscles (posterior)",
            "Papillary muscles (septal - right ventricle)",
        ],
        "Myocardial Layers": ["Endocardium", "Myocardium", "Epicardium"],
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
            "Right coronary artery (RCA)": ["Marginal branch", "Posterior descending artery (PDA)"],
            "Left coronary artery (LCA)": ["Left anterior descending (LAD)", "Left circumflex (LCx)"],
        },
        "Coronary Veins": ["Great cardiac vein", "Middle cardiac vein", "Small cardiac vein", "Coronary sinus"],
    },
    "Blood Vessels": {
        "Arteries": {
            "Elastic arteries": ["Aorta (ascending)", "Aorta (arch)", "Aorta (descending thoracic)", "Aorta (abdominal)"],
            "Muscular arteries": ["Carotid arteries", "Subclavian arteries", "Femoral arteries", "Radial arteries"],
            "Arterioles": [],
        },
        "Capillaries": ["Continuous capillaries", "Fenestrated capillaries", "Sinusoidal capillaries"],
        "Veins": {
            "Venules": [],
            "Medium veins": [],
            "Large veins": ["Superior vena cava", "Inferior vena cava"],
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
            "Aortic arch branches": ["Brachiocephalic trunk", "Left common carotid artery", "Left subclavian artery"],
        },
    },
    "Blood": {
        "Cellular Components": {
            "Red blood cells (erythrocytes)": [],
            "White blood cells (leukocytes)": ["Neutrophils", "Lymphocytes", "Monocytes", "Eosinophils", "Basophils"],
            "Platelets (thrombocytes)": [],
        },
        "Plasma Components": [
            "Water", "Electrolytes", "Proteins: albumin", "Proteins: globulins", "Proteins: fibrinogen",
            "Hormones", "Nutrients", "Waste products",
        ],
    },
    "Blood Pressure Regulation Structures": {
        "Baroreceptors": ["Carotid sinus", "Aortic arch"],
        "Chemoreceptors": ["Carotid bodies", "Aortic bodies"],
    },
    "Autonomic Innervation": {
        "Sympathetic": ["Cardiac nerves", "Cervical sympathetic ganglia"],
        "Parasympathetic": ["Vagus nerve (CN X)"],
    },
    "Foetal/Paediatric-Specific Structures": [
        "Foramen ovale", "Ductus arteriosus", "Ductus venosus", "Umbilical vein", "Umbilical arteries",
    ],
}

# ---- RESP_TREE (unchanged from your previous code) ----
RESP_TREE = {
    "Upper Respiratory Tract": {
        "Nose & Nasal Cavity": [
            "External nose", "Nasal vestibule", "Nasal septum",
            "Nasal conchae (turbinates): superior, middle, inferior",
            "Meatuses: superior, middle, inferior",
            "Olfactory region", "Respiratory mucosa",
        ],
        "Paranasal Sinuses": ["Frontal sinus", "Maxillary sinus", "Ethmoid air cells", "Sphenoid sinus"],
        "Pharynx": ["Nasopharynx", "Oropharynx", "Laryngopharynx (hypopharynx)"],
        "Larynx": {
            "Cartilages": [
                "Thyroid cartilage", "Cricoid cartilage", "Epiglottis",
                "Arytenoid cartilages", "Corniculate cartilages", "Cuneiform cartilages",
            ],
            "Glottic structures": ["Vocal folds (true vocal cords)", "Vestibular folds (false vocal cords)", "Glottis"],
            "Regions": ["Supraglottis", "Glottis", "Subglottis"],
        },
    },
    "Lower Respiratory Tract": {
        "Trachea": ["Tracheal rings (C-shaped cartilage)", "Trachealis muscle", "Carina"],
        "Bronchi": {
            "Main (primary) bronchi": ["Right main bronchus", "Left main bronchus"],
            "Lobar (secondary) bronchi": [
                "Right: superior, middle, inferior lobar bronchi",
                "Left: superior, inferior lobar bronchi",
            ],
            "Segmental (tertiary) bronchi": ["Bronchopulmonary segment bronchi"],
        },
        "Bronchioles": ["Bronchioles (conducting)", "Terminal bronchioles", "Respiratory bronchioles"],
        "Alveolar Region": [
            "Alveolar ducts", "Alveolar sacs", "Alveoli", "Alveolar-capillary (respiratory) membrane",
            "Type I pneumocytes", "Type II pneumocytes (surfactant-producing)", "Alveolar macrophages",
        ],
    },
    "Lungs": {
        "Lobes": {
            "Right lung": ["Superior lobe", "Middle lobe", "Inferior lobe"],
            "Left lung": ["Superior lobe", "Inferior lobe", "Lingula (part of superior lobe)"],
        },
        "Surfaces & Landmarks": ["Apex", "Base (diaphragmatic surface)", "Costal surface", "Mediastinal surface", "Hilum", "Root of lung"],
        "Bronchopulmonary Segments": ["Segmental anatomy (bronchopulmonary segments)"],
    },
    "Pleura": {
        "Visceral pleura": [],
        "Parietal pleura": ["Costal pleura", "Mediastinal pleura", "Diaphragmatic pleura", "Cervical pleura (cupula)"],
        "Pleural cavity (fluid)": [],
        "Pleural recesses": ["Costodiaphragmatic recess", "Costomediastinal recess"],
    },
    "Respiratory Muscles & Mechanics": {
        "Primary muscles": ["Diaphragm", "External intercostals"],
        "Accessory muscles (increased work of breathing)": ["Sternocleidomastoid", "Scalenes", "Pectoralis major/minor (fixed shoulder girdle)"],
        "Expiration (active)": ["Internal intercostals", "Abdominal muscles (rectus abdominis, obliques, transversus abdominis)"],
        "Chest wall & mechanics": ["Rib cage", "Pleural pressure", "Alveolar pressure", "Compliance (lung & chest wall)", "Airway resistance"],
    },
    "Pulmonary Circulation (Resp-specific)": {
        "Pulmonary arteries": ["Pulmonary trunk", "Right pulmonary artery", "Left pulmonary artery", "Arterioles"],
        "Pulmonary capillaries": [],
        "Pulmonary veins": ["Pulmonary veins (4)"],
    },
    "Neural Control of Breathing": {
        "Central control": ["Medulla (respiratory rhythm generators)", "Pons (modulation of breathing pattern)"],
        "Peripheral receptors": [
            "Central chemoreceptors (CO₂/pH sensing)",
            "Peripheral chemoreceptors (carotid bodies, aortic bodies)",
            "Pulmonary stretch receptors",
            "Irritant receptors",
            "J (juxtacapillary) receptors",
        ],
        "Motor pathways": ["Phrenic nerve (C3–C5)", "Intercostal nerves"],
    },
    "Airway Defence & Clearance": {
        "Mucociliary escalator": ["Ciliated epithelium", "Goblet cells", "Mucus layer"],
        "Cough & sneeze reflex": [],
        "Local immune defence": ["Alveolar macrophages", "Secretory IgA (upper airways)", "Bronchus-associated lymphoid tissue (BALT)"],
    },
    "Foetal/Paediatric Respiratory Structures": {
        "Foetal lung development stages": ["Embryonic stage", "Pseudoglandular stage", "Canalicular stage", "Saccular stage", "Alveolar stage"],
        "Surfactant": ["Produced by Type II pneumocytes", "Increases late gestation (clinical relevance for prematurity)"],
        "Neonatal/paeds anatomy considerations": ["Narrower airways (higher resistance)", "More compliant chest wall", "Higher oxygen consumption", "Obligate nasal breathing (especially infants)"],
    },
}

# ---- NEURO_TREE (unchanged from your previous code; not expanded here) ----
# To keep this file readable, paste your full NEURO_TREE from the previous message.
# If you want a single complete file, just replace this placeholder with your NEURO_TREE.
NEURO_TREE = {
    "Central Nervous System (CNS)": {
        "Brain": {
            "Cerebrum": {
                "Cerebral hemispheres": ["Left hemisphere", "Right hemisphere"],
                "Lobes": ["Frontal lobe", "Parietal lobe", "Temporal lobe", "Occipital lobe", "Insula"],
            }
        }
    }
}

# ============================================================
# GASTROINTESTINAL TREE (Comprehensive hierarchy)
# ============================================================
GI_TREE = {
    "Oral Cavity & Salivary Apparatus": {
        "Oral cavity": [
            "Lips",
            "Teeth",
            "Tongue",
            "Hard palate",
            "Soft palate",
            "Gingivae",
            "Buccal mucosa",
            "Floor of mouth",
        ],
        "Salivary glands": {
            "Major salivary glands": [
                "Parotid gland",
                "Submandibular gland",
                "Sublingual gland",
            ],
            "Minor salivary glands (overview)": [],
            "Salivary ducts": [
                "Stensen duct (parotid)",
                "Wharton duct (submandibular)",
                "Rivinus ducts (sublingual, overview)",
            ],
        },
        "Pharynx (shared region)": [
            "Oropharynx (swallowing pathway)",
            "Laryngopharynx (hypopharynx, swallowing pathway)",
        ],
        "Swallowing (deglutition, overview)": [
            "Oral phase",
            "Pharyngeal phase",
            "Oesophageal phase",
        ],
    },

    "Oesophagus": {
        "Segments": [
            "Cervical oesophagus",
            "Thoracic oesophagus",
            "Abdominal oesophagus",
        ],
        "Sphincters": [
            "Upper oesophageal sphincter (UES)",
            "Lower oesophageal sphincter (LES)",
        ],
        "Layers (overview)": [
            "Mucosa",
            "Submucosa",
            "Muscularis propria",
            "Adventitia",
        ],
    },

    "Stomach": {
        "Regions": [
            "Cardia",
            "Fundus",
            "Body",
            "Antrum",
            "Pylorus",
        ],
        "Sphincter": ["Pyloric sphincter"],
        "Curvatures": ["Greater curvature", "Lesser curvature"],
        "Cell types (overview)": [
            "Parietal cells (acid, intrinsic factor)",
            "Chief cells (pepsinogen)",
            "Mucous cells",
            "G cells (gastrin)",
            "ECL cells (histamine, overview)",
        ],
        "Layers (overview)": [
            "Mucosa",
            "Submucosa",
            "Muscularis (incl. oblique layer)",
            "Serosa",
        ],
    },

    "Small Intestine": {
        "Segments": [
            "Duodenum",
            "Jejunum",
            "Ileum",
        ],
        "Mucosal structures": [
            "Plicae circulares",
            "Villi",
            "Microvilli (brush border)",
            "Crypts of Lieberkühn",
        ],
        "Specialised cells (overview)": [
            "Enterocytes",
            "Goblet cells",
            "Paneth cells",
            "Enteroendocrine cells",
            "M cells (Peyer patches-associated)",
        ],
        "Lymphoid tissue": [
            "Peyer patches (ileum)",
            "GALT (gut-associated lymphoid tissue, overview)",
        ],
        "Sphincters/valves (overview)": [
            "Ileocecal valve",
        ],
    },

    "Large Intestine": {
        "Segments": [
            "Caecum",
            "Appendix",
            "Ascending colon",
            "Transverse colon",
            "Descending colon",
            "Sigmoid colon",
            "Rectum",
            "Anal canal",
        ],
        "Anal sphincters": [
            "Internal anal sphincter",
            "External anal sphincter",
        ],
        "Features (overview)": [
            "Haustra",
            "Taeniae coli",
            "Appendices epiploicae",
        ],
        "Mucosa (overview)": [
            "No villi (compared with small intestine)",
            "Crypts (glands) in colon",
        ],
    },

    "Liver": {
        "Gross anatomy": [
            "Right lobe",
            "Left lobe",
            "Caudate lobe (overview)",
            "Quadrate lobe (overview)",
        ],
        "Microscopic/functional units": [
            "Hepatic lobule (overview)",
            "Portal triad (hepatic artery, portal vein, bile duct)",
            "Hepatocytes",
            "Kupffer cells",
            "Sinusoids",
            "Central vein",
        ],
        "Blood supply (overview)": [
            "Hepatic artery",
            "Portal vein",
            "Hepatic veins",
        ],
    },

    "Gallbladder & Biliary Tree": {
        "Gallbladder": ["Fundus", "Body", "Neck"],
        "Bile ducts": [
            "Right hepatic duct",
            "Left hepatic duct",
            "Common hepatic duct",
            "Cystic duct",
            "Common bile duct (CBD)",
        ],
        "Ampulla & sphincter": [
            "Ampulla of Vater (hepatopancreatic ampulla)",
            "Sphincter of Oddi",
        ],
    },

    "Pancreas": {
        "Regions": ["Head", "Uncinate process (overview)", "Neck (overview)", "Body", "Tail"],
        "Exocrine pancreas": [
            "Acinar cells",
            "Ductal cells",
        ],
        "Endocrine pancreas": [
            "Islets of Langerhans (overview)",
            "Alpha cells (glucagon)",
            "Beta cells (insulin)",
            "Delta cells (somatostatin)",
            "PP cells (pancreatic polypeptide, overview)",
        ],
        "Pancreatic ducts": [
            "Main pancreatic duct (Wirsung)",
            "Accessory pancreatic duct (Santorini, overview)",
        ],
    },

    "Peritoneum & Mesenteries": {
        "Peritoneum": ["Parietal peritoneum", "Visceral peritoneum"],
        "Peritoneal cavity (overview)": [],
        "Mesenteries/omentum": [
            "Mesentery of small intestine",
            "Transverse mesocolon",
            "Sigmoid mesocolon",
            "Greater omentum",
            "Lesser omentum",
        ],
    },

    "GI Vasculature (overview)": {
        "Arterial supply": [
            "Celiac trunk",
            "Superior mesenteric artery (SMA)",
            "Inferior mesenteric artery (IMA)",
        ],
        "Portal venous system": [
            "Portal vein",
            "Splenic vein",
            "Superior mesenteric vein (SMV)",
            "Inferior mesenteric vein (IMV, overview)",
        ],
        "Lymphatics (overview)": [
            "Mesenteric lymph nodes",
            "Lacteals (intestinal lymphatics, overview)",
        ],
    },

    "GI Innervation (overview)": {
        "Enteric nervous system": [
            "Myenteric (Auerbach) plexus",
            "Submucosal (Meissner) plexus",
        ],
        "Parasympathetic": [
            "Vagus nerve (foregut & midgut)",
            "Pelvic splanchnic nerves (hindgut)",
        ],
        "Sympathetic (overview)": [
            "Splanchnic nerves",
            "Prevertebral ganglia (celiac, superior mesenteric, inferior mesenteric)",
        ],
    },

    "Foetal/Paediatric GI Structures": {
        "Embryologic gut divisions": [
            "Foregut",
            "Midgut",
            "Hindgut",
        ],
        "Key paeds structures/topics": [
            "Meckel diverticulum (vitelline duct remnant)",
            "Malrotation/volvulus (overview)",
            "Hirschsprung disease (aganglionosis, overview)",
        ],
        "Liver/bile in neonates (overview)": [
            "Physiologic jaundice context",
            "Biliary atresia (overview)",
        ],
    },
}

# ----------------------------
# Helpers for hierarchical navigation (generalised)
# ----------------------------
def get_node_by_path(tree, path):
    node = tree
    for p in path:
        if isinstance(node, dict) and p in node:
            node = node[p]
        else:
            return None
    return node

def push_path(state_key, item):
    st.session_state[state_key].append(item)

def pop_path(state_key):
    if st.session_state[state_key]:
        st.session_state[state_key].pop()

def reset_nav(state_key):
    st.session_state[state_key] = []

# ----------------------------
# Page styling
# ----------------------------
def inject_css():
    st.markdown(
        """
        <style>
        .app-title { font-size: 2.0rem; font-weight: 800; margin-bottom: 0.2rem; }
        .app-sub   { color: #6b7280; margin-top: 0; margin-bottom: 1.2rem; }

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

        .crumb { color: #6b7280; font-size: 0.95rem; }
        </style>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# Simple router using session_state
# ----------------------------
def init_state():
    st.session_state.setdefault("route", "home")  # home | system | cardio_tree | resp_tree | neuro_tree | gi_tree
    st.session_state.setdefault("selected_system_id", None)

    st.session_state.setdefault("cardio_path", [])
    st.session_state.setdefault("resp_path", [])
    st.session_state.setdefault("neuro_path", [])
    st.session_state.setdefault("gi_path", [])

def go_home():
    st.session_state.route = "home"
    st.session_state.selected_system_id = None
    reset_nav("cardio_path")
    reset_nav("resp_path")
    reset_nav("neuro_path")
    reset_nav("gi_path")

def go_system(system_id: str):
    st.session_state.route = "system"
    st.session_state.selected_system_id = system_id
    reset_nav("cardio_path")
    reset_nav("resp_path")
    reset_nav("neuro_path")
    reset_nav("gi_path")

def go_cardio_tree():
    st.session_state.route = "cardio_tree"
    st.session_state.selected_system_id = "cardio"
    reset_nav("cardio_path"); reset_nav("resp_path"); reset_nav("neuro_path"); reset_nav("gi_path")

def go_resp_tree():
    st.session_state.route = "resp_tree"
    st.session_state.selected_system_id = "resp"
    reset_nav("resp_path"); reset_nav("cardio_path"); reset_nav("neuro_path"); reset_nav("gi_path")

def go_neuro_tree():
    st.session_state.route = "neuro_tree"
    st.session_state.selected_system_id = "neuro"
    reset_nav("neuro_path"); reset_nav("cardio_path"); reset_nav("resp_path"); reset_nav("gi_path")

def go_gi_tree():
    st.session_state.route = "gi_tree"
    st.session_state.selected_system_id = "gi"
    reset_nav("gi_path"); reset_nav("cardio_path"); reset_nav("resp_path"); reset_nav("neuro_path")

# ----------------------------
# UI components
# ----------------------------
def system_card(system):
    label = f"{system['emoji']} {system['name']}"
    if st.button(label, key=f"btn_{system['id']}", use_container_width=True):
        if system["id"] == "cardio":
            go_cardio_tree()
        elif system["id"] == "resp":
            go_resp_tree()
        elif system["id"] == "neuro":
            go_neuro_tree()
        elif system["id"] == "gi":
            go_gi_tree()
        else:
            go_system(system["id"])

def item_card(label, key):
    if st.button(label, key=key, use_container_width=True):
        return True
    return False

def tree_page(title, tree, path_key, root_label):
    st.markdown(f"<div class='app-title'>{title}</div>", unsafe_allow_html=True)

    path = st.session_state[path_key]
    node = get_node_by_path(tree, path)

    if node is None:
        st.error("Navigation error: path not found.")
        reset_nav(path_key)
        node = tree

    crumb = " > ".join([root_label] + path) if path else root_label
    st.markdown(f"<div class='crumb'>{crumb}</div>", unsafe_allow_html=True)
    st.write("")

    c1, c2, c3 = st.columns([1, 1, 2])
    with c1:
        if st.button("⬅️ Back", key=f"back_{path_key}"):
            pop_path(path_key)
            st.rerun()
    with c2:
        if st.button("⟲ Reset", key=f"reset_{path_key}"):
            reset_nav(path_key)
            st.rerun()
    with c3:
        st.button("← Back to Systems", on_click=go_home, key=f"systems_{path_key}")

    st.write("")
    st.markdown('<div class="card-grid">', unsafe_allow_html=True)

    if isinstance(node, dict):
        children = list(node.keys())
        if not children:
            st.info("No further sub-components.")
        else:
            cols = st.columns(2)
            for i, child in enumerate(children):
                with cols[i % 2]:
                    if item_card(child, key=f"{path_key}_{'_'.join(path)}_{child}"):
                        push_path(path_key, child)
                        st.rerun()
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
    system_id = st.session_state.selected_system_id
    system = next((s for s in SYSTEMS if s["id"] == system_id), None)

    if not system:
        st.error("System not found.")
        st.button("Back", on_click=go_home)
        return

    st.markdown(f"<div class='app-title'>{system['emoji']} {system['name']}</div>", unsafe_allow_html=True)
    st.info("This system page is a placeholder. Cardio + Resp + Neuro + GI have full component trees.")
    st.button("← Back to Systems", on_click=go_home)

def page_cardio_tree():
    tree_page("🫀 Cardiovascular", CARDIO_TREE, "cardio_path", "Cardiovascular")

def page_resp_tree():
    tree_page("🫁 Respiratory", RESP_TREE, "resp_path", "Respiratory")

def page_neuro_tree():
    tree_page("🧠 Neurology", NEURO_TREE, "neuro_path", "Neurology")

def page_gi_tree():
    tree_page("🧻 Gastrointestinal", GI_TREE, "gi_path", "Gastrointestinal")

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
        st.caption("Cardio path:")
        st.code(" > ".join(st.session_state.cardio_path) if st.session_state.cardio_path else "(root)")
        st.caption("Resp path:")
        st.code(" > ".join(st.session_state.resp_path) if st.session_state.resp_path else "(root)")
        st.caption("Neuro path:")
        st.code(" > ".join(st.session_state.neuro_path) if st.session_state.neuro_path else "(root)")
        st.caption("GI path:")
        st.code(" > ".join(st.session_state.gi_path) if st.session_state.gi_path else "(root)")

    if st.session_state.route == "home":
        page_home()
    elif st.session_state.route == "system":
        page_system_detail()
    elif st.session_state.route == "cardio_tree":
        page_cardio_tree()
    elif st.session_state.route == "resp_tree":
        page_resp_tree()
    elif st.session_state.route == "neuro_tree":
        page_neuro_tree()
    else:
        page_gi_tree()

if __name__ == "__main__":
    main()
