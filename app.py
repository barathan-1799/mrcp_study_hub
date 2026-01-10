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

# ============================================================
# NEPHRO-UROLOGY TREE (Comprehensive hierarchy)
# ============================================================
RENAL_TREE = {
    "Kidneys": {
        "Gross anatomy": [
            "Right kidney",
            "Left kidney",
            "Renal capsule",
            "Cortex",
            "Medulla",
            "Renal pyramids",
            "Renal columns",
            "Renal papillae",
            "Hilum",
            "Renal sinus",
        ],
        "Collecting system (within kidney)": [
            "Minor calyces",
            "Major calyces",
            "Renal pelvis",
        ],
        "Nephron (functional unit)": {
            "Renal corpuscle": [
                "Glomerulus",
                "Bowman's capsule",
                "Filtration barrier (endothelium, GBM, podocytes) (overview)",
                "Mesangial cells (overview)",
            ],
            "Tubules": [
                "Proximal convoluted tubule (PCT)",
                "Loop of Henle (descending limb)",
                "Loop of Henle (ascending limb)",
                "Distal convoluted tubule (DCT)",
                "Connecting tubule (overview)",
                "Collecting duct",
            ],
            "Juxtaglomerular apparatus (JGA)": [
                "Macula densa",
                "Juxtaglomerular (granular) cells",
                "Extraglomerular mesangial cells (lacis cells) (overview)",
            ],
            "Nephron types (overview)": [
                "Cortical nephrons",
                "Juxtamedullary nephrons",
            ],
        },
        "Renal blood supply": {
            "Arteries": [
                "Renal artery",
                "Segmental arteries",
                "Interlobar arteries",
                "Arcuate arteries",
                "Interlobular (cortical radiate) arteries",
                "Afferent arterioles",
            ],
            "Microcirculation": [
                "Glomerular capillaries",
                "Efferent arterioles",
                "Peritubular capillaries",
                "Vasa recta (juxtamedullary nephrons)",
            ],
            "Veins": [
                "Interlobular (cortical radiate) veins",
                "Arcuate veins",
                "Interlobar veins",
                "Renal vein",
            ],
        },
        "Renal innervation (overview)": [
            "Sympathetic fibres (renal plexus)",
            "Pain pathways (loin to groin pattern, clinical overview)",
        ],
    },

    "Ureters": {
        "Segments": [
            "Abdominal ureter",
            "Pelvic ureter",
            "Intramural (bladder wall) segment",
        ],
        "Physiological narrowings (clinical)": [
            "Ureteropelvic junction (UPJ)",
            "Crossing iliac vessels (pelvic brim)",
            "Ureterovesical junction (UVJ)",
        ],
        "Wall layers (overview)": [
            "Mucosa (urothelium)",
            "Muscularis",
            "Adventitia",
        ],
    },

    "Urinary Bladder": {
        "Regions": [
            "Apex",
            "Body",
            "Fundus (base)",
            "Neck",
        ],
        "Trigone": [
            "Interureteric ridge (overview)",
            "Ureteric orifices",
            "Internal urethral orifice",
        ],
        "Wall / musculature": [
            "Detrusor muscle",
            "Bladder mucosa (urothelium)",
        ],
        "Sphincters": [
            "Internal urethral sphincter (smooth muscle, mainly male prominent)",
            "External urethral sphincter (skeletal muscle)",
        ],
        "Innervation (overview)": [
            "Parasympathetic (pelvic splanchnic nerves S2–S4)",
            "Sympathetic (hypogastric nerves, overview)",
            "Somatic (pudendal nerve to external sphincter)",
        ],
    },

    "Urethra": {
        "Female urethra": [
            "Short urethra (overview)",
            "External urethral meatus",
        ],
        "Male urethra": [
            "Prostatic urethra",
            "Membranous urethra",
            "Spongy (penile) urethra",
            "External urethral meatus",
        ],
        "Continence structures (overview)": [
            "Internal sphincter contribution",
            "External sphincter contribution",
            "Pelvic floor support",
        ],
    },

    "Male Reproductive (Urology-linked)": {
        "Testes & epididymis": [
            "Testis",
            "Epididymis (head, body, tail)",
        ],
        "Spermatic cord contents (overview)": [
            "Vas deferens",
            "Testicular artery",
            "Pampiniform plexus",
        ],
        "Vas deferens": [],
        "Seminal vesicles": [],
        "Prostate gland": [
            "Prostate (zones overview: peripheral, transitional, central)",
            "Prostatic urethra (link)",
        ],
        "Penis": [
            "Corpora cavernosa",
            "Corpus spongiosum",
            "Glans",
        ],
    },

    "Female Pelvic / Urogyne (Urology-linked)": {
        "Pelvic floor (continence support)": [
            "Levator ani (overview)",
            "Fascial supports (overview)",
        ],
        "Proximity structures (overview)": [
            "Anterior vaginal wall (relation to urethra)",
        ],
    },

    "Renal Physiology (functional modules)": {
        "Filtration": [
            "Glomerular filtration rate (GFR) (overview)",
            "Filtration barrier function (overview)",
        ],
        "Reabsorption & Secretion": {
            "Proximal tubule": [
                "Glucose reabsorption (overview)",
                "Amino acids reabsorption (overview)",
                "Bicarbonate handling (overview)",
            ],
            "Loop of Henle": [
                "Countercurrent multiplier (overview)",
                "Concentrating gradient (overview)",
            ],
            "Distal tubule & collecting duct": [
                "Sodium handling (overview)",
                "Potassium handling (overview)",
                "Acid-base handling (overview)",
                "Water reabsorption (ADH effect, overview)",
            ],
        },
        "Concentration/Dilution of urine": [
            "Countercurrent mechanisms (overview)",
            "Vasa recta (overview)",
        ],
        "Hormonal regulation": [
            "Renin-angiotensin-aldosterone system (RAAS)",
            "Antidiuretic hormone (ADH)",
            "Atrial natriuretic peptide (ANP)",
            "Parathyroid hormone (PTH) effects on phosphate/calcium (overview)",
        ],
        "Acid-base regulation": [
            "Bicarbonate reabsorption",
            "Hydrogen ion secretion",
            "Ammoniagenesis (overview)",
        ],
    },

    "Paediatric / Developmental Nephro-urology": {
        "Embryology (overview)": [
            "Pronephros (rudimentary)",
            "Mesonephros",
            "Metanephros (definitive kidney)",
            "Ureteric bud",
            "Metanephric mesenchyme (blastema)",
        ],
        "Foetal urine & amniotic fluid": [
            "Foetal urine contribution to amniotic fluid",
            "Oligohydramnios relevance (overview)",
        ],
        "Common congenital anomalies (overview)": [
            "Hydronephrosis",
            "Vesicoureteral reflux (VUR)",
            "Posterior urethral valves (PUV)",
            "Hypospadias",
            "Polycystic kidney disease (overview)",
        ],
    },
}

# ============================================================
# ENDOCRINE TREE (Comprehensive hierarchy)
# ============================================================
ENDO_TREE = {
    "Hypothalamic–Pituitary Axis": {
        "Hypothalamus": {
            "Hypothalamic nuclei (overview)": [
                "Arcuate nucleus",
                "Paraventricular nucleus",
                "Supraoptic nucleus",
                "Ventromedial nucleus",
                "Lateral hypothalamic area",
            ],
            "Releasing / inhibiting hormones": [
                "CRH (corticotropin-releasing hormone)",
                "TRH (thyrotropin-releasing hormone)",
                "GnRH (gonadotropin-releasing hormone)",
                "GHRH (growth hormone–releasing hormone)",
                "Somatostatin",
                "Dopamine (prolactin inhibition)",
            ],
        },

        "Pituitary Gland": {
            "Anterior pituitary (adenohypophysis)": {
                "Hormones": [
                    "ACTH",
                    "TSH",
                    "GH",
                    "Prolactin",
                    "FSH",
                    "LH",
                ],
                "Cell types (overview)": [
                    "Corticotrophs",
                    "Thyrotrophs",
                    "Somatotrophs",
                    "Lactotrophs",
                    "Gonadotrophs",
                ],
            },
            "Posterior pituitary (neurohypophysis)": {
                "Hormones": [
                    "ADH (vasopressin)",
                    "Oxytocin",
                ],
                "Hypothalamic origin (overview)": [
                    "Supraoptic nucleus",
                    "Paraventricular nucleus",
                ],
            },
        },
    },

    "Thyroid Gland": {
        "Gross anatomy": [
            "Right lobe",
            "Left lobe",
            "Isthmus",
            "Pyramidal lobe (variant)",
        ],
        "Microscopic structure": [
            "Thyroid follicles",
            "Colloid",
            "Follicular cells",
            "Parafollicular (C) cells",
        ],
        "Hormones": [
            "Thyroxine (T4)",
            "Triiodothyronine (T3)",
            "Calcitonin",
        ],
        "Regulation": [
            "TSH",
            "Negative feedback (T3/T4)",
        ],
    },

    "Parathyroid Glands": {
        "Number & location": [
            "Superior parathyroids",
            "Inferior parathyroids",
        ],
        "Cells": [
            "Chief cells",
            "Oxyphil cells (overview)",
        ],
        "Hormone": [
            "Parathyroid hormone (PTH)",
        ],
        "Physiological actions": [
            "Bone resorption",
            "Renal calcium reabsorption",
            "Vitamin D activation",
        ],
    },

    "Adrenal (Suprarenal) Glands": {
        "Adrenal cortex": {
            "Zones": [
                "Zona glomerulosa",
                "Zona fasciculata",
                "Zona reticularis",
            ],
            "Hormones": {
                "Zona glomerulosa": ["Aldosterone"],
                "Zona fasciculata": ["Cortisol"],
                "Zona reticularis": ["Androgens (DHEA)"],
            },
        },
        "Adrenal medulla": {
            "Cells": [
                "Chromaffin cells",
            ],
            "Hormones": [
                "Adrenaline (epinephrine)",
                "Noradrenaline (norepinephrine)",
            ],
        },
    },

    "Pancreatic Endocrine System": {
        "Islets of Langerhans": {
            "Cell types": [
                "Alpha cells (glucagon)",
                "Beta cells (insulin)",
                "Delta cells (somatostatin)",
                "PP cells (pancreatic polypeptide)",
            ],
        },
        "Hormonal regulation of glucose": [
            "Insulin",
            "Glucagon",
            "Counter-regulatory hormones (overview)",
        ],
    },

    "Gonadal Endocrine System": {
        "Testes": {
            "Cells": [
                "Leydig cells",
                "Sertoli cells",
            ],
            "Hormones": [
                "Testosterone",
                "Inhibin B",
                "Anti-Müllerian hormone (foetal)",
            ],
        },
        "Ovaries": {
            "Structures": [
                "Follicles",
                "Corpus luteum",
            ],
            "Hormones": [
                "Oestrogen",
                "Progesterone",
                "Inhibin",
            ],
        },
    },

    "Other Endocrine Organs & Tissues": {
        "Pineal gland": [
            "Melatonin",
            "Circadian rhythm regulation",
        ],
        "Thymus": [
            "Thymosin",
            "T-cell maturation (immuno-endocrine link)",
        ],
        "Placenta (pregnancy)": [
            "hCG",
            "Progesterone",
            "Oestrogen",
            "Human placental lactogen",
        ],
        "Kidney (endocrine roles)": [
            "Renin",
            "Erythropoietin",
            "Vitamin D activation",
        ],
        "Heart (endocrine role)": [
            "Atrial natriuretic peptide (ANP)",
        ],
        "Adipose tissue": [
            "Leptin",
            "Adiponectin (overview)",
        ],
    },

    "Endocrine Axes (Functional Pathways)": {
        "HPA axis": [
            "CRH → ACTH → Cortisol",
        ],
        "HPT axis": [
            "TRH → TSH → T3/T4",
        ],
        "HPG axis": [
            "GnRH → LH/FSH → Sex steroids",
        ],
        "GH–IGF axis": [
            "GHRH → GH → IGF-1",
        ],
    },

    "Paediatric / Developmental Endocrinology": {
        "Growth & puberty": [
            "Growth hormone",
            "IGF-1",
            "Pubertal staging (Tanner stages, overview)",
        ],
        "Congenital endocrine disorders (overview)": [
            "Congenital hypothyroidism",
            "Congenital adrenal hyperplasia (CAH)",
            "Hypopituitarism",
        ],
        "Neonatal endocrine adaptations": [
            "Post-natal glucose regulation",
            "Calcium homeostasis",
        ],
    },
}

# ============================
# ADD THIS: HAEMATOLOGY TREE
# ============================
HEME_TREE = {
    "Blood": {
        "Plasma": {
            "Water": [],
            "Electrolytes": ["Sodium", "Potassium", "Chloride", "Bicarbonate", "Calcium", "Magnesium", "Phosphate"],
            "Proteins": ["Albumin", "Globulins", "Fibrinogen", "Complement proteins (overview)"],
            "Other solutes (overview)": ["Glucose", "Lipids", "Hormones", "Waste products (urea, creatinine, bilirubin)"],
        },
        "Cellular components": {
            "Red blood cells (Erythrocytes)": {
                "Structure": ["Biconcave disc", "Cell membrane & cytoskeleton (spectrin, ankyrin) (overview)"],
                "Haemoglobin (Hb)": ["Haem", "Globin chains", "Oxygen dissociation (overview)"],
                "RBC lifespan & removal": ["Reticuloendothelial system (spleen/liver) (overview)"],
            },
            "White blood cells (Leukocytes)": {
                "Neutrophils": ["Primary granules (azurophilic) (overview)", "Secondary granules (overview)", "NETs (overview)"],
                "Lymphocytes": {
                    "B cells": ["Plasma cells (differentiation) (overview)", "Antibody production (overview)"],
                    "T cells": ["CD4+ helper T cells (overview)", "CD8+ cytotoxic T cells (overview)", "T-regulatory cells (overview)"],
                    "NK cells": [],
                },
                "Monocytes / Macrophages": ["Phagocytosis (overview)", "Antigen presentation (overview)"],
                "Eosinophils": ["Parasitic defence (overview)", "Allergy/asthma role (overview)"],
                "Basophils / Mast cells (linked)": ["Histamine release (overview)", "IgE-mediated reactions (overview)"],
            },
            "Platelets (Thrombocytes)": {
                "Origin": ["Megakaryocytes (bone marrow)"],
                "Granules": ["Alpha granules (vWF, fibrinogen, factor V) (overview)", "Dense granules (ADP, Ca2+) (overview)"],
                "Primary haemostasis role": ["Adhesion", "Activation", "Aggregation"],
            },
        },
    },

    "Haematopoiesis": {
        "Sites (by age)": [
            "Yolk sac (early embryo)",
            "Liver (foetus)",
            "Spleen (foetus)",
            "Bone marrow (late foetus → childhood/adult)",
        ],
        "Bone marrow": {
            "Red marrow": [],
            "Yellow marrow (fatty)": [],
            "Stem cell niches (overview)": ["Haematopoietic stem cell (HSC) niche", "Stromal support (overview)"],
        },
        "Haematopoietic hierarchy": {
            "Haematopoietic stem cell (HSC)": [],
            "Common myeloid progenitor (CMP)": [
                "Erythroid lineage (overview)",
                "Megakaryocyte lineage (overview)",
                "Granulocyte/monocyte lineages (overview)",
            ],
            "Common lymphoid progenitor (CLP)": ["B lineage", "T lineage", "NK lineage"],
        },
        "Key growth factors (overview)": [
            "Erythropoietin (EPO)",
            "Thrombopoietin (TPO)",
            "G-CSF",
            "GM-CSF",
            "IL-3",
            "IL-7 (lymphoid development)",
        ],
    },

    "Red Cell System": {
        "Erythropoiesis": [
            "Proerythroblast",
            "Basophilic erythroblast",
            "Polychromatic erythroblast",
            "Orthochromatic erythroblast",
            "Reticulocyte",
            "Mature erythrocyte",
        ],
        "Haemoglobin types": [
            "HbA (α2β2)",
            "HbA2 (α2δ2)",
            "HbF (α2γ2)",
        ],
        "Iron metabolism": {
            "Absorption": ["Duodenum (primary site)", "DMT1 (overview)", "Heme iron vs non-heme iron (overview)"],
            "Transport": ["Transferrin"],
            "Storage": ["Ferritin", "Haemosiderin (overview)"],
            "Regulation": ["Hepcidin", "Ferroportin (overview)"],
        },
        "Vitamin support": ["Folate", "Vitamin B12"],
        "Haemolysis (overview)": {
            "Extravascular haemolysis": ["Splenic macrophages"],
            "Intravascular haemolysis": ["Free Hb", "Haptoglobin consumption (overview)"],
        },
        "Blood groups": {
            "ABO system": ["A antigen", "B antigen", "O (no A/B antigens)"],
            "Rhesus system": ["Rh(D) antigen (overview)"],
            "Compatibility concepts (overview)": ["Crossmatch", "Antibodies (IgM vs IgG)"],
        },
    },

    "White Cell / Immune Haematology": {
        "Innate immunity (haematology link)": [
            "Neutrophil response",
            "Monocyte/macrophage response",
            "Complement (overview)",
        ],
        "Adaptive immunity (haematology link)": [
            "B-cell antibody response",
            "T-cell mediated response",
        ],
        "Lymphoid organs (functional)": {
            "Primary lymphoid organs": ["Bone marrow", "Thymus"],
            "Secondary lymphoid organs": ["Lymph nodes", "Spleen", "MALT (overview)"],
        },
    },

    "Haemostasis & Coagulation": {
        "Vessel wall / Endothelium (overview)": ["vWF release", "Anticoagulant surface properties (overview)"],
        "Primary haemostasis (platelet plug)": [
            "Adhesion (vWF–GpIb)",
            "Activation (shape change, granule release)",
            "Aggregation (GpIIb/IIIa–fibrinogen bridges)",
        ],
        "Secondary haemostasis (coagulation cascade)": {
            "Intrinsic pathway": ["Factor XII", "Factor XI", "Factor IX", "Factor VIII"],
            "Extrinsic pathway": ["Factor VII", "Tissue factor"],
            "Common pathway": ["Factor X", "Factor V", "Prothrombin (Factor II)", "Fibrinogen (Factor I)", "Factor XIII"],
        },
        "Vitamin K–dependent factors": ["II", "VII", "IX", "X", "Protein C", "Protein S"],
        "Natural anticoagulants": ["Antithrombin", "Protein C", "Protein S", "TFPI (overview)"],
        "Fibrinolysis": ["Plasminogen", "Plasmin", "tPA (overview)", "D-dimer (fibrin breakdown product, overview)"],
        "Laboratory tests (overview)": [
            "FBC / CBC",
            "Peripheral blood film",
            "Reticulocyte count",
            "PT/INR",
            "aPTT",
            "Fibrinogen",
            "D-dimer",
        ],
    },

    "Haemoglobinopathies & RBC Disorders (overview modules)": {
        "Sickle cell disease": [
            "HbS mutation (β chain) (overview)",
            "Vaso-occlusion (overview)",
            "Haemolysis (overview)",
        ],
        "Thalassaemias": [
            "Alpha thalassaemia (overview)",
            "Beta thalassaemia (overview)",
        ],
        "Membrane disorders": [
            "Hereditary spherocytosis (overview)",
            "Hereditary elliptocytosis (overview)",
        ],
        "Enzyme disorders": [
            "G6PD deficiency (overview)",
            "Pyruvate kinase deficiency (overview)",
        ],
    },

    "Bleeding & Clotting Disorders (overview modules)": {
        "Platelet disorders": [
            "Quantitative (thrombocytopenia) (overview)",
            "Qualitative platelet dysfunction (overview)",
        ],
        "Coagulation factor deficiencies": [
            "Haemophilia A (Factor VIII) (overview)",
            "Haemophilia B (Factor IX) (overview)",
            "von Willebrand disease (vWF) (overview)",
        ],
        "Consumptive coagulopathy": ["DIC (overview)"],
        "Thrombosis (overview)": [
            "Virchow triad",
            "Inherited thrombophilias (overview)",
        ],
    },

    "Transfusion Medicine (overview)": {
        "Components": [
            "Packed red cells",
            "Platelets",
            "Fresh frozen plasma (FFP)",
            "Cryoprecipitate",
        ],
        "Reactions (overview)": [
            "Acute haemolytic reaction",
            "Febrile non-haemolytic reaction",
            "Allergic reaction",
            "TRALI (overview)",
            "TACO (overview)",
        ],
    },

    "Paediatric Haematology (MRCPCH-relevant)": {
        "Normal paediatric variations (overview)": [
            "Physiologic anaemia of infancy",
            "Age-related WBC differentials (overview)",
        ],
        "Neonatal issues (overview)": [
            "Haemolytic disease of the newborn (ABO/Rh) (overview)",
            "Vitamin K deficiency bleeding (overview)",
        ],
        "Malignancy link (overview)": [
            "Leukaemia basics (overview)",
            "Lymphoma basics (overview)",
        ],
    },
}

# ============================
# ADD THIS: IMMUNOLOGY TREE
# ============================
IMM_TREE = {
    "Immune System Overview": {
        "Innate immunity": [
            "Physical barriers (skin, mucosa)",
            "Chemical barriers (pH, lysozyme, defensins)",
            "Cellular responses (phagocytes, NK cells)",
            "Complement system (overview)",
            "Inflammation (overview)",
            "Fever (overview)",
        ],
        "Adaptive immunity": [
            "Humoral immunity (B cells, antibodies)",
            "Cell-mediated immunity (T cells)",
            "Immunological memory",
            "Tolerance (self vs non-self, overview)",
        ],
    },

    "Primary Lymphoid Organs": {
        "Bone marrow": {
            "Haematopoietic stem cells (HSCs)": [],
            "B cell development": [
                "Pro-B cell",
                "Pre-B cell",
                "Immature B cell",
                "Mature naive B cell",
            ],
            "Central tolerance (B cells)": [
                "Clonal deletion (overview)",
                "Receptor editing (overview)",
                "Anergy (overview)",
            ],
        },
        "Thymus": {
            "Anatomy": [
                "Cortex",
                "Medulla",
                "Hassall corpuscles (overview)",
            ],
            "T cell development": [
                "Double negative (CD4-/CD8-) stage (overview)",
                "Double positive (CD4+/CD8+) stage (overview)",
                "Single positive (CD4+ or CD8+) stage (overview)",
            ],
            "Selection": [
                "Positive selection (MHC restriction, overview)",
                "Negative selection (central tolerance, overview)",
            ],
        },
    },

    "Secondary Lymphoid Organs": {
        "Lymph nodes": {
            "Anatomy": [
                "Capsule",
                "Cortex (B cell follicles)",
                "Paracortex (T cell zone)",
                "Medulla (cords & sinuses)",
            ],
            "Lymph flow": [
                "Afferent lymphatics",
                "Subcapsular sinus",
                "Medullary sinuses",
                "Efferent lymphatics",
            ],
            "Germinal centre reaction (overview)": [
                "Somatic hypermutation",
                "Class-switch recombination",
                "Affinity maturation",
                "Plasma cell formation",
                "Memory B cell formation",
            ],
        },
        "Spleen": {
            "White pulp": [
                "PALS (periarteriolar lymphoid sheath, T cells)",
                "Follicles (B cells)",
                "Marginal zone (overview)",
            ],
            "Red pulp": [
                "Splenic cords",
                "Sinusoids",
                "RBC clearance (RES function, overview)",
            ],
        },
        "MALT (mucosa-associated lymphoid tissue)": {
            "GALT": [
                "Peyer patches",
                "Appendix lymphoid tissue (overview)",
            ],
            "Tonsils/adenoids": [
                "Palatine tonsils",
                "Pharyngeal tonsil (adenoids)",
                "Lingual tonsils",
            ],
            "BALT (overview)": [],
        },
    },

    "Innate Immune Cells": {
        "Neutrophils": [
            "Chemotaxis",
            "Phagocytosis",
            "Respiratory burst (overview)",
            "Degranulation (overview)",
            "NET formation (overview)",
        ],
        "Monocytes / Macrophages": [
            "Phagocytosis",
            "Antigen presentation (MHC II)",
            "Cytokine production (overview)",
        ],
        "Dendritic cells": [
            "Antigen capture",
            "Migration to lymph nodes",
            "T cell priming (overview)",
        ],
        "Natural killer (NK) cells": [
            "Recognition of low MHC I (overview)",
            "Cytotoxicity (perforin/granzyme, overview)",
            "ADCC (antibody-dependent cellular cytotoxicity, overview)",
        ],
        "Eosinophils": [
            "Helminth defence (overview)",
            "Allergic inflammation (overview)",
        ],
        "Basophils / Mast cells": [
            "IgE receptor (FcεRI, overview)",
            "Degranulation (histamine, leukotrienes) (overview)",
        ],
    },

    "Adaptive Immune Cells": {
        "B cells": {
            "Maturation states (overview)": [
                "Naive B cell",
                "Activated B cell",
                "Plasma cell",
                "Memory B cell",
            ],
            "Functions": [
                "Antibody production",
                "Antigen presentation (MHC II)",
                "Cytokine production (overview)",
            ],
        },
        "T cells": {
            "CD4+ helper T cells": {
                "Th1": ["IFN-γ (overview)", "Intracellular pathogen response (overview)"],
                "Th2": ["IL-4/IL-5/IL-13 (overview)", "Helminths/allergy (overview)"],
                "Th17": ["IL-17 (overview)", "Neutrophil recruitment (overview)"],
                "Tfh": ["Germinal centre help (overview)"],
            },
            "CD8+ cytotoxic T cells": [
                "Perforin/granzyme killing (overview)",
                "Fas–FasL apoptosis (overview)",
            ],
            "Regulatory T cells (Treg)": [
                "Immune tolerance (overview)",
                "IL-10/TGF-β (overview)",
            ],
        },
    },

    "Antigen Presentation & MHC": {
        "Antigen-presenting cells (APCs)": [
            "Dendritic cells",
            "Macrophages",
            "B cells",
        ],
        "MHC Class I": [
            "All nucleated cells",
            "Presents endogenous antigens to CD8+ T cells",
        ],
        "MHC Class II": [
            "Professional APCs",
            "Presents exogenous antigens to CD4+ T cells",
        ],
        "Co-stimulation (overview)": [
            "CD80/86 (B7) – CD28",
            "CD40 – CD40L",
        ],
    },

    "Antibodies (Immunoglobulins)": {
        "Structure": [
            "Heavy chain",
            "Light chain",
            "Fab region",
            "Fc region",
        ],
        "Isotypes": {
            "IgG": ["Most abundant", "Placental transfer (neonatal immunity)", "Opsonisation (overview)"],
            "IgA": ["Mucosal immunity", "Secretory IgA (breast milk)"],
            "IgM": ["Primary response", "Strong complement activator (overview)"],
            "IgE": ["Allergy", "Parasite defence (overview)"],
            "IgD": ["B cell receptor role (overview)"],
        },
        "Functions": [
            "Neutralisation",
            "Opsonisation",
            "Complement activation",
            "ADCC (overview)",
        ],
    },

    "Complement System": {
        "Pathways": {
            "Classical pathway": ["Triggered by IgG/IgM immune complexes (overview)"],
            "Lectin pathway": ["MBL (mannose-binding lectin) (overview)"],
            "Alternative pathway": ["Spontaneous activation on microbial surfaces (overview)"],
        },
        "Key components (overview)": [
            "C3 (central component)",
            "C5 convertase (overview)",
            "MAC (C5b-9)",
        ],
        "Main outcomes": [
            "Opsonisation (C3b)",
            "Inflammation (C3a, C5a)",
            "Cell lysis (MAC)",
        ],
        "Regulation (overview)": [
            "Factor H/I",
            "DAF (CD55)",
            "CD59",
        ],
    },

    "Cytokines & Signalling (overview)": {
        "Pro-inflammatory cytokines": ["IL-1", "IL-6", "TNF-α"],
        "Antiviral cytokines": ["Type I interferons (IFN-α/β)"],
        "T cell-related cytokines (overview)": ["IL-2", "IFN-γ", "IL-4", "IL-5", "IL-17"],
        "Chemokines (overview)": ["IL-8 (CXCL8) and others"],
    },

    "Hypersensitivity Reactions": {
        "Type I (IgE-mediated)": [
            "Allergic rhinitis (overview)",
            "Asthma (overview)",
            "Anaphylaxis (overview)",
        ],
        "Type II (antibody-mediated)": [
            "Autoimmune haemolytic anaemia (overview)",
            "Goodpasture syndrome (overview)",
        ],
        "Type III (immune complex)": [
            "Serum sickness (overview)",
            "Post-streptococcal glomerulonephritis (overview)",
        ],
        "Type IV (delayed-type, T cell-mediated)": [
            "Contact dermatitis (overview)",
            "TB skin test reaction (overview)",
        ],
    },

    "Autoimmunity & Tolerance (overview)": {
        "Central tolerance": ["Thymic negative selection", "Bone marrow B cell editing (overview)"],
        "Peripheral tolerance": ["Anergy", "Treg suppression", "Immune privilege (overview)"],
        "Autoimmune disease concepts (overview)": [
            "Genetic predisposition",
            "Environmental triggers",
            "Molecular mimicry (overview)",
        ],
    },

    "Immunodeficiency": {
        "Primary (congenital) immunodeficiencies (overview)": {
            "B cell defects": [
                "X-linked agammaglobulinaemia (overview)",
                "Common variable immunodeficiency (overview)",
            ],
            "T cell defects": [
                "DiGeorge syndrome (overview)",
            ],
            "Combined immunodeficiency": [
                "SCID (overview)",
            ],
            "Phagocyte defects": [
                "Chronic granulomatous disease (overview)",
                "Leukocyte adhesion deficiency (overview)",
            ],
            "Complement deficiencies (overview)": [
                "C3 deficiency (overview)",
                "C5-9 deficiency (Neisseria risk, overview)",
            ],
        },
        "Secondary (acquired) immunodeficiencies (overview)": [
            "HIV (overview)",
            "Malnutrition (overview)",
            "Immunosuppressive medications (steroids/chemo, overview)",
            "Asplenia/splenectomy (infection risk, overview)",
        ],
    },

    "Vaccinology & Paediatric Immunology": {
        "Vaccine types": [
            "Live attenuated vaccines (overview)",
            "Inactivated vaccines (overview)",
            "Subunit/conjugate vaccines (overview)",
            "Toxoid vaccines (overview)",
            "mRNA/viral vector concepts (overview)",
        ],
        "Immune response to vaccination": [
            "Primary response",
            "Booster (secondary response)",
            "Memory cell formation",
        ],
        "Passive immunity": [
            "Placental IgG transfer",
            "Breast milk secretory IgA",
        ],
        "Paediatric red flags (overview)": [
            "Recurrent severe infections",
            "Poor growth / chronic diarrhoea (immunodeficiency clue)",
        ],
    },
}

# ============================
# ADD THIS: ONCOLOGY TREE
# ============================
ONC_TREE = {
    "Fundamentals of Cancer Biology": {
        "Definition & hallmarks of cancer": [
            "Uncontrolled cell proliferation",
            "Evasion of apoptosis",
            "Sustained angiogenesis",
            "Invasion and metastasis",
            "Immune evasion (overview)",
            "Genomic instability",
        ],
        "Cell cycle & regulation": {
            "Cell cycle phases": [
                "G0",
                "G1",
                "S",
                "G2",
                "M",
            ],
            "Key regulators": [
                "Cyclins",
                "Cyclin-dependent kinases (CDKs)",
                "Checkpoint proteins (p53, Rb)",
            ],
        },
        "Genetic basis of cancer": {
            "Oncogenes": [
                "Proto-oncogenes",
                "Gain-of-function mutations",
                "Examples (overview): RAS, MYC",
            ],
            "Tumour suppressor genes": [
                "Loss-of-function mutations",
                "Examples (overview): TP53, RB1, APC",
            ],
            "DNA repair genes": [
                "Mismatch repair genes (overview)",
                "BRCA1/BRCA2 (overview)",
            ],
        },
    },

    "Tumour Classification": {
        "By tissue of origin": {
            "Carcinomas": [
                "Epithelial origin",
                "Examples: adenocarcinoma, squamous cell carcinoma",
            ],
            "Sarcomas": [
                "Mesenchymal origin",
                "Examples: osteosarcoma, rhabdomyosarcoma",
            ],
            "Haematological malignancies": [
                "Leukaemias",
                "Lymphomas",
                "Plasma cell dyscrasias (overview)",
            ],
            "Neuroectodermal tumours": [
                "Neuroblastoma",
                "Medulloblastoma",
            ],
        },
        "Benign vs malignant": [
            "Growth rate",
            "Invasion",
            "Metastatic potential",
            "Degree of differentiation",
        ],
    },

    "Paediatric Oncology (Core MRCPCH)": {
        "Leukaemias": {
            "Acute lymphoblastic leukaemia (ALL)": [
                "Most common childhood cancer",
                "B-cell ALL",
                "T-cell ALL",
            ],
            "Acute myeloid leukaemia (AML)": [],
            "Chronic leukaemias (rare in children)": [],
        },
        "Lymphomas": {
            "Hodgkin lymphoma": [
                "Reed–Sternberg cells",
                "B symptoms (overview)",
            ],
            "Non-Hodgkin lymphoma": [
                "Burkitt lymphoma",
                "Lymphoblastic lymphoma",
                "Diffuse large B-cell lymphoma (overview)",
            ],
        },
        "Solid tumours": {
            "Neuroblastoma": [
                "Adrenal origin",
                "N-myc amplification (overview)",
            ],
            "Wilms tumour (nephroblastoma)": [
                "WT1 gene (overview)",
                "Aniridia association (overview)",
            ],
            "Retinoblastoma": [
                "RB1 gene",
                "Leukocoria",
            ],
            "Brain tumours": [
                "Medulloblastoma",
                "Astrocytoma (overview)",
                "Ependymoma (overview)",
            ],
            "Bone & soft tissue tumours": [
                "Osteosarcoma",
                "Ewing sarcoma",
                "Rhabdomyosarcoma",
            ],
        },
    },

    "Tumour Growth & Spread": {
        "Local invasion": [
            "Basement membrane breach",
            "Matrix metalloproteinases (overview)",
        ],
        "Metastasis": {
            "Routes": [
                "Lymphatic spread",
                "Haematogenous spread",
                "Transcoelomic spread (overview)",
            ],
            "Steps": [
                "Detachment",
                "Invasion",
                "Intravasation",
                "Extravasation",
                "Colonisation",
            ],
        },
        "Angiogenesis": [
            "VEGF",
            "Tumour neovascularisation (overview)",
        ],
    },

    "Cancer Staging & Grading": {
        "Staging systems": {
            "TNM staging": [
                "Tumour size (T)",
                "Nodal involvement (N)",
                "Metastasis (M)",
            ],
            "Paediatric staging systems (overview)": [
                "INSS (neuroblastoma)",
                "Ann Arbor (lymphoma)",
            ],
        },
        "Grading": [
            "Degree of differentiation",
            "Mitotic activity",
            "Histological appearance",
        ],
    },

    "Cancer Diagnosis": {
        "Clinical features": [
            "Weight loss",
            "Fatigue",
            "Unexplained fever",
            "Night sweats",
            "Persistent pain or mass",
        ],
        "Laboratory investigations": [
            "Full blood count",
            "Peripheral blood film",
            "Tumour markers (overview)",
        ],
        "Imaging": [
            "Ultrasound",
            "CT",
            "MRI",
            "PET scan (overview)",
        ],
        "Tissue diagnosis": [
            "Biopsy",
            "Histopathology",
            "Immunohistochemistry (overview)",
            "Cytogenetics / molecular testing (overview)",
        ],
    },

    "Cancer Treatment Modalities": {
        "Surgery": [
            "Curative resection",
            "Debulking surgery",
            "Biopsy procedures",
        ],
        "Chemotherapy": {
            "Principles": [
                "Cell cycle–specific drugs",
                "Combination therapy",
            ],
            "Drug classes (overview)": [
                "Alkylating agents",
                "Antimetabolites",
                "Anthracyclines",
                "Vinca alkaloids",
                "Platinum agents",
            ],
            "Common side effects": [
                "Myelosuppression",
                "Nausea/vomiting",
                "Mucositis",
                "Alopecia",
            ],
        },
        "Radiotherapy": [
            "External beam radiotherapy",
            "Targeted fields",
            "Late effects in children (overview)",
        ],
        "Targeted & biological therapies": [
            "Monoclonal antibodies",
            "Tyrosine kinase inhibitors",
            "Immune checkpoint inhibitors (overview)",
        ],
        "Haematopoietic stem cell transplant (overview)": [
            "Autologous transplant",
            "Allogeneic transplant",
        ],
    },

    "Oncological Emergencies": {
        "Tumour lysis syndrome": [
            "Hyperkalaemia",
            "Hyperphosphataemia",
            "Hypocalcaemia",
            "Hyperuricaemia",
        ],
        "Spinal cord compression": [
            "Back pain",
            "Neurological deficits",
        ],
        "Superior vena cava (SVC) syndrome": [
            "Facial swelling",
            "Venous congestion",
        ],
        "Febrile neutropenia": [
            "Neutropenia",
            "Sepsis risk",
        ],
    },

    "Late Effects & Survivorship": {
        "Growth & development issues": [
            "Growth hormone deficiency",
            "Delayed puberty",
        ],
        "Organ toxicity": [
            "Cardiotoxicity (anthracyclines)",
            "Nephrotoxicity",
            "Neurotoxicity",
        ],
        "Second malignancies": [
            "Therapy-related cancers (overview)",
        ],
        "Psychosocial aspects": [
            "School reintegration",
            "Mental health support",
        ],
    },

    "Paediatric Red Flags (Exam-Oriented)": {
        "Unexplained symptoms": [
            "Persistent lymphadenopathy",
            "Unexplained bruising",
            "Bone pain/night pain",
        ],
        "Failure to thrive": [],
        "Recurrent infections (malignancy vs immunodeficiency)": [],
    },
}

# ============================
# ADD THIS: RHEUMATOLOGY TREE
# ============================
MSK_TREE = {
    "Musculoskeletal System (Core Structures)": {
        "Bones": {
            "Bone types": ["Long bones", "Short bones", "Flat bones", "Irregular bones", "Sesamoid bones"],
            "Bone structure": [
                "Periosteum",
                "Cortical (compact) bone",
                "Trabecular (spongy) bone",
                "Bone marrow (red/yellow) (overview)",
            ],
            "Cells": ["Osteoblasts", "Osteoclasts", "Osteocytes"],
            "Remodelling (overview)": ["RANK/RANKL/OPG axis (overview)", "Wolff's law (overview)"],
        },

        "Joints": {
            "Joint types": {
                "Fibrous joints": ["Sutures", "Syndesmoses", "Gomphoses (overview)"],
                "Cartilaginous joints": ["Synchondroses", "Symphyses"],
                "Synovial joints": [
                    "Hinge",
                    "Ball-and-socket",
                    "Pivot",
                    "Condyloid",
                    "Saddle",
                    "Plane/gliding",
                ],
            },
            "Synovial joint anatomy": {
                "Articular cartilage": ["Hyaline cartilage (most joints)", "Fibrocartilage (some joints) (overview)"],
                "Synovial membrane": [],
                "Synovial fluid": [],
                "Joint capsule": ["Fibrous capsule", "Synovial lining"],
                "Ligaments": ["Capsular ligaments", "Extracapsular ligaments", "Intracapsular ligaments"],
                "Menisci / labrum (where present)": ["Menisci (knee)", "Labrum (hip/shoulder)"],
                "Bursae": ["Prepatellar bursa (example)", "Olecranon bursa (example)"],
            },
        },

        "Muscles & Tendons": {
            "Skeletal muscle": [
                "Muscle fibres (overview)",
                "Neuromuscular junction (overview)",
                "Motor unit concept (overview)",
            ],
            "Tendons": ["Tendon insertion", "Enthesis (attachment site)"],
            "Entheses (rheum relevance)": ["Enthesitis (overview)", "Spondyloarthropathies association (overview)"],
        },

        "Connective Tissue": {
            "Collagen": ["Type I", "Type II", "Type III", "Type IV (basement membrane, overview)"],
            "Elastin (overview)": [],
            "Proteoglycans / GAGs (overview)": ["Hyaluronic acid", "Chondroitin sulfate", "Keratan sulfate (overview)"],
        },
    },

    "Immune-Mediated Rheumatologic Mechanisms": {
        "Inflammation in joints": [
            "Synovitis",
            "Pannus formation (overview)",
            "Cartilage degradation (overview)",
            "Bone erosions (overview)",
        ],
        "Autoantibodies (overview)": [
            "ANA",
            "RF",
            "Anti-CCP",
            "ANCA (vasculitis link, overview)",
        ],
        "Cytokines (overview)": [
            "TNF-α",
            "IL-1",
            "IL-6",
            "IL-17",
        ],
        "Complement & immune complexes (overview)": [
            "Immune complex deposition",
            "Complement activation",
        ],
    },

    "Paediatric Rheumatology (Core MRCPCH)": {
        "Juvenile Idiopathic Arthritis (JIA)": {
            "Subtypes": [
                "Oligoarticular JIA",
                "Polyarticular RF-negative JIA",
                "Polyarticular RF-positive JIA",
                "Systemic JIA (Still disease)",
                "Enthesitis-related arthritis (ERA)",
                "Psoriatic JIA",
                "Undifferentiated JIA",
            ],
            "Key features": [
                "Morning stiffness",
                "Joint swelling",
                "Reduced range of motion",
                "Pain may be absent in young children",
            ],
            "Complications": [
                "Uveitis (esp. oligoarticular)",
                "Growth disturbance (overview)",
                "Macrophage activation syndrome (MAS) (systemic JIA)",
            ],
        },

        "Vasculitis": {
            "IgA vasculitis (Henoch–Schönlein purpura)": [
                "Palpable purpura",
                "Arthralgia/arthritis",
                "Abdominal pain",
                "Renal involvement",
            ],
            "Kawasaki disease": [
                "Prolonged fever",
                "Mucocutaneous inflammation",
                "Coronary artery aneurysm risk (overview)",
            ],
            "Polyarteritis nodosa (PAN) (overview)": [],
            "ANCA-associated vasculitis (overview)": ["GPA", "MPA", "EGPA (overview)"],
        },

        "Connective Tissue / Multisystem Autoimmune": {
            "Systemic Lupus Erythematosus (SLE)": [
                "Malar rash (overview)",
                "Photosensitivity (overview)",
                "Arthritis",
                "Renal disease (overview)",
                "Cytopenias (overview)",
            ],
            "Juvenile dermatomyositis": [
                "Proximal muscle weakness",
                "Gottron papules (overview)",
                "Heliotrope rash (overview)",
            ],
            "Scleroderma (juvenile) (overview)": [
                "Localised scleroderma (morphea) (overview)",
                "Systemic sclerosis (rare) (overview)",
            ],
            "Mixed connective tissue disease (overview)": [],
        },

        "Autoinflammatory Syndromes (overview)": {
            "Periodic fever syndromes": [
                "PFAPA",
                "Familial Mediterranean fever (FMF)",
                "TRAPS (overview)",
                "Hyper-IgD syndrome / mevalonate kinase deficiency (overview)",
            ],
        },
    },

    "Bones & Metabolic/MSK Conditions (Rheum-adjacent in paeds)": {
        "Rickets / Osteomalacia (overview)": [
            "Vitamin D deficiency rickets",
            "Calcium deficiency rickets (overview)",
            "Phosphate-related rickets (overview)",
        ],
        "Osteomyelitis vs inflammatory arthritis (overview)": [
            "Septic arthritis (overview)",
            "Osteomyelitis (overview)",
        ],
        "Non-accidental injury considerations (overview)": [],
    },

    "Pain & Regional Syndromes": {
        "Mechanical vs inflammatory pain": [
            "Inflammatory pain: morning stiffness, improves with movement",
            "Mechanical pain: worse with activity, improves with rest",
        ],
        "Hypermobility spectrum": [
            "Benign joint hypermobility",
            "Ehlers–Danlos spectrum (overview)",
        ],
        "Chronic pain syndromes (overview)": [
            "Amplified musculoskeletal pain syndrome",
            "Juvenile fibromyalgia (overview)",
        ],
    },

    "Investigations in Rheumatology (overview)": {
        "Blood tests": [
            "ESR",
            "CRP",
            "FBC",
            "ANA",
            "RF",
            "Anti-CCP",
            "Complement levels (C3/C4)",
            "HLA-B27 (ERA/spondyloarthropathy link)",
        ],
        "Imaging": [
            "X-ray",
            "Ultrasound (effusion/synovitis)",
            "MRI (bone marrow oedema/early arthritis)",
        ],
        "Joint aspiration (overview)": [
            "Synovial fluid cell count",
            "Gram stain & culture",
            "Crystals (rare in children, overview)",
        ],
    },

    "Treatment Modalities (overview)": {
        "Non-pharmacological": [
            "Physiotherapy",
            "Occupational therapy",
            "Exercise / activity modification",
            "Psychological support (chronic disease)",
        ],
        "NSAIDs": ["Ibuprofen (overview)", "Naproxen (overview)"],
        "Steroids": ["Oral prednisolone (overview)", "Intra-articular steroid injections (overview)"],
        "DMARDs": [
            "Methotrexate",
            "Sulfasalazine (overview)",
            "Hydroxychloroquine (overview)",
        ],
        "Biologics (overview)": [
            "Anti-TNF agents (etanercept, adalimumab) (overview)",
            "IL-1 inhibitors (anakinra) (systemic JIA, overview)",
            "IL-6 inhibitors (tocilizumab) (overview)",
        ],
        "Immunosuppression (selected conditions, overview)": [
            "Cyclophosphamide (severe vasculitis/SLE, overview)",
            "Mycophenolate mofetil (SLE, overview)",
        ],
    },
}

# ============================
# ADD THIS: DERMATOLOGY TREE
# ============================
DERM_TREE = {
    "Skin (Integumentary System)": {
        "Layers of the skin": {
            "Epidermis": {
                "Strata": [
                    "Stratum basale",
                    "Stratum spinosum",
                    "Stratum granulosum",
                    "Stratum lucidum (palms/soles)",
                    "Stratum corneum",
                ],
                "Cell types": [
                    "Keratinocytes",
                    "Melanocytes",
                    "Langerhans cells",
                    "Merkel cells",
                ],
                "Key functions": [
                    "Barrier function",
                    "Keratinisation",
                    "Pigmentation (melanin)",
                    "Immune surveillance (overview)",
                ],
            },
            "Dermis": {
                "Layers": [
                    "Papillary dermis",
                    "Reticular dermis",
                ],
                "Contents": [
                    "Collagen (Type I/III)",
                    "Elastin fibres",
                    "Fibroblasts",
                    "Blood vessels",
                    "Lymphatics",
                    "Nerves",
                ],
            },
            "Subcutaneous tissue (Hypodermis)": [
                "Adipose tissue",
                "Connective tissue septae",
                "Larger blood vessels",
                "Larger nerves",
            ],
        },

        "Skin appendages": {
            "Hair": {
                "Hair follicle": [
                    "Infundibulum",
                    "Isthmus",
                    "Bulb",
                    "Dermal papilla",
                ],
                "Hair shaft": ["Cuticle", "Cortex", "Medulla (overview)"],
                "Hair cycle": ["Anagen", "Catagen", "Telogen"],
            },
            "Nails": [
                "Nail plate",
                "Nail bed",
                "Nail matrix",
                "Lunula",
                "Cuticle (eponychium)",
                "Hyponychium",
            ],
            "Sweat glands": {
                "Eccrine glands": [
                    "Thermoregulation",
                    "Distributed widely (overview)",
                ],
                "Apocrine glands": [
                    "Axilla/groin distribution (overview)",
                    "Pubertal activation (overview)",
                ],
            },
            "Sebaceous glands": [
                "Sebum production",
                "Associated with hair follicles (overview)",
            ],
        },

        "Skin vasculature & innervation (overview)": {
            "Blood supply": [
                "Superficial vascular plexus",
                "Deep vascular plexus",
            ],
            "Lymphatics": ["Superficial lymphatic network (overview)"],
            "Nerve endings": [
                "Free nerve endings (pain/temp)",
                "Meissner corpuscles (light touch)",
                "Pacinian corpuscles (pressure/vibration)",
            ],
        },

        "Skin function": [
            "Barrier protection",
            "Thermoregulation",
            "Sensation",
            "Immune defence (overview)",
            "Vitamin D synthesis",
        ],
    },

    "Dermatological Lesions (Morphology)": {
        "Primary lesions": [
            "Macule",
            "Patch",
            "Papule",
            "Plaque",
            "Nodule",
            "Vesicle",
            "Bulla",
            "Pustule",
            "Wheal (urticarial lesion)",
        ],
        "Secondary lesions": [
            "Scale",
            "Crust",
            "Erosion",
            "Ulcer",
            "Excoriation",
            "Fissure",
            "Lichenification",
            "Atrophy",
            "Scar",
        ],
        "Distribution patterns (overview)": [
            "Flexural",
            "Extensor",
            "Dermatomal",
            "Photodistributed",
            "Generalised vs localised",
        ],
    },

    "Inflammatory Dermatoses (Paeds Core)": {
        "Eczema / Dermatitis": {
            "Atopic dermatitis": [
                "Flexural eczema (typical older child)",
                "Cheeks/extensors (infant pattern, overview)",
                "Pruritus",
                "Secondary infection risk",
            ],
            "Contact dermatitis": [
                "Irritant contact dermatitis",
                "Allergic contact dermatitis (Type IV hypersensitivity, overview)",
            ],
            "Seborrhoeic dermatitis": [
                "Cradle cap (infants)",
                "Scalp/face involvement (overview)",
            ],
            "Nappy (diaper) dermatitis": [
                "Irritant dermatitis",
                "Candida-associated dermatitis (overview)",
            ],
        },

        "Psoriasis": {
            "Plaque psoriasis": [],
            "Guttate psoriasis": ["Post-streptococcal association (overview)"],
            "Nail psoriasis (overview)": ["Pitting", "Onycholysis"],
        },

        "Urticaria & Angioedema": {
            "Acute urticaria": ["Often infection-related (overview)"],
            "Chronic urticaria (overview)": [],
            "Angioedema (overview)": ["Histaminergic", "Bradykinin-mediated (rare paeds, overview)"],
        },
    },

    "Infectious Skin Disorders": {
        "Bacterial": {
            "Impetigo": ["Bullous", "Non-bullous"],
            "Cellulitis / Erysipelas": [],
            "Folliculitis": [],
            "Staphylococcal scalded skin syndrome (SSSS) (overview)": [],
        },
        "Viral": {
            "Warts (HPV)": [],
            "Molluscum contagiosum": [],
            "Herpes simplex": ["Gingivostomatitis (overview)", "Eczema herpeticum (overview)"],
            "Varicella (chickenpox) (overview)": [],
            "Hand-foot-and-mouth disease (enteroviruses) (overview)": [],
        },
        "Fungal": {
            "Tinea corporis": [],
            "Tinea capitis": [],
            "Tinea pedis (older children) (overview)": [],
            "Candidiasis": ["Oral thrush", "Intertrigo (overview)", "Nappy rash (Candida)"],
        },
        "Parasitic": {
            "Scabies": ["Burrows", "Nocturnal itch", "Household spread (overview)"],
            "Pediculosis (lice) (overview)": ["Head lice", "Body lice (rare)", "Pubic lice (rare)"],
        },
    },

    "Pigmentary Disorders": {
        "Hypopigmentation": [
            "Vitiligo (autoimmune, overview)",
            "Pityriasis alba (often eczema-related, overview)",
            "Albinism (overview)",
        ],
        "Hyperpigmentation": [
            "Post-inflammatory hyperpigmentation",
            "Café-au-lait macules (overview)",
            "Acanthosis nigricans (endocrine link, overview)",
        ],
        "Birthmarks / naevi (overview)": {
            "Melanocytic naevi": ["Congenital melanocytic naevus (overview)", "Acquired naevus"],
            "Vascular lesions": ["Infantile haemangioma", "Port-wine stain (capillary malformation)"],
        },
    },

    "Blistering & Severe Reactions (overview)": {
        "Erythema multiforme": [],
        "Stevens–Johnson syndrome / TEN (overview)": [],
        "Autoimmune blistering (rare paeds, overview)": [
            "Bullous pemphigoid (overview)",
            "Pemphigus vulgaris (very rare in children, overview)",
        ],
    },

    "Acne & Follicular Disorders": {
        "Acne vulgaris": [
            "Comedones (open/closed)",
            "Papules/pustules",
            "Nodulocystic acne (overview)",
        ],
        "Hidradenitis suppurativa (overview)": ["Axillary/groin nodules", "Sinus tracts (overview)"],
        "Keratosis pilaris": [],
    },

    "Hair & Nail Disorders": {
        "Alopecia": {
            "Alopecia areata": ["Autoimmune", "Exclamation mark hairs (overview)"],
            "Tinea capitis (infective alopecia link)": [],
            "Traction alopecia (overview)": [],
        },
        "Nail disorders": [
            "Onychomycosis (overview)",
            "Paronychia (overview)",
            "Nail pitting (psoriasis link)",
            "Clubbing (systemic disease link, overview)",
        ],
    },

    "Paediatric Dermatology Special Topics": {
        "Neonatal rashes (overview)": [
            "Erythema toxicum neonatorum",
            "Milia",
            "Neonatal acne (overview)",
        ],
        "Genetic skin disorders (overview)": {
            "Ichthyosis (overview)": [],
            "Epidermolysis bullosa (overview)": [],
            "Neurocutaneous syndromes (overview)": [
                "Neurofibromatosis (café-au-lait, neurofibromas, overview)",
                "Tuberous sclerosis (ash-leaf macules, overview)",
            ],
        },
        "Child protection dermatology (overview)": [
            "Bruising patterns (overview)",
            "Burns/scalds distribution (overview)",
        ],
    },

    "Dermatology Investigations (overview)": {
        "Clinical": [
            "Full skin exam",
            "Dermatoscopy (overview)",
        ],
        "Laboratory": [
            "Skin swab culture (infective lesions)",
            "Fungal microscopy/culture (tinea)",
        ],
        "Procedures": [
            "Skin scraping (scabies)",
            "Biopsy (selected cases, overview)",
            "Patch testing (allergic contact dermatitis, overview)",
        ],
    },

    "Dermatology Treatments (overview)": {
        "Topical therapies": [
            "Emollients",
            "Topical corticosteroids (potency ladder, overview)",
            "Topical calcineurin inhibitors (tacrolimus/pimecrolimus, overview)",
            "Topical antibiotics (selected cases, overview)",
            "Antifungals (topical)",
        ],
        "Systemic therapies": [
            "Oral antibiotics (acne/infection, overview)",
            "Antihistamines (urticaria itch, overview)",
            "Systemic steroids (selected severe inflammation, overview)",
            "Immunosuppressants/biologics (severe eczema/psoriasis, overview)",
        ],
        "Supportive care": [
            "Trigger avoidance",
            "Infection control",
            "Education & skin care routines",
        ],
    },
}

# ============================
# ADD THIS: ENT TREE
# ============================
ENT_TREE = {
    "Ear": {
        "External ear": {
            "Auricle (pinna)": [
                "Helix",
                "Antihelix",
                "Tragus",
                "Antitragus",
                "Concha",
                "Lobule",
            ],
            "External auditory canal": [
                "Cartilaginous portion",
                "Bony portion",
                "Cerumen glands (overview)",
            ],
        },

        "Middle ear": {
            "Tympanic membrane (eardrum)": [
                "Pars tensa",
                "Pars flaccida",
            ],
            "Ossicles": [
                "Malleus",
                "Incus",
                "Stapes",
            ],
            "Middle ear cavity spaces (overview)": [
                "Epitympanum (attic)",
                "Mesotympanum",
                "Hypotympanum",
            ],
            "Muscles": [
                "Tensor tympani",
                "Stapedius",
            ],
            "Eustachian tube (pharyngotympanic tube)": [
                "Opening into nasopharynx",
                "Ventilation of middle ear",
                "Paediatric: shorter/more horizontal (otitis media risk, overview)",
            ],
            "Mastoid system": [
                "Mastoid antrum",
                "Mastoid air cells",
            ],
        },

        "Inner ear": {
            "Bony labyrinth": [
                "Cochlea",
                "Vestibule",
                "Semicircular canals",
            ],
            "Membranous labyrinth": [
                "Cochlear duct",
                "Utricle",
                "Saccule",
                "Semicircular ducts",
                "Endolymph",
                "Perilymph (overview)",
            ],
            "Hearing apparatus": {
                "Organ of Corti": [
                    "Inner hair cells",
                    "Outer hair cells",
                    "Tectorial membrane (overview)",
                ],
                "Auditory pathway (overview)": [
                    "Cochlear nerve",
                    "Cochlear nucleus (brainstem, overview)",
                    "Inferior colliculus (overview)",
                    "Medial geniculate body (overview)",
                    "Auditory cortex (overview)",
                ],
            },
            "Vestibular apparatus": {
                "Semicircular canals": ["Angular acceleration"],
                "Utricle": ["Linear acceleration (horizontal)"],
                "Saccule": ["Linear acceleration (vertical)"],
                "Vestibular nerve": [],
            },
        },
    },

    "Nose & Nasal Cavity": {
        "External nose": [
            "Nasal bones",
            "Septal cartilage (overview)",
            "Alar cartilages (overview)",
        ],
        "Nasal cavity": {
            "Nasal septum": ["Cartilaginous septum", "Bony septum (vomer/ethmoid, overview)"],
            "Turbinates (conchae)": ["Superior", "Middle", "Inferior"],
            "Meatuses": ["Superior meatus", "Middle meatus", "Inferior meatus"],
            "Olfactory region": ["Olfactory epithelium (overview)"],
            "Respiratory mucosa": ["Mucociliary clearance (overview)"],
        },
        "Nasal airflow & function": [
            "Humidification",
            "Warming",
            "Filtration",
            "Olfaction",
        ],
    },

    "Paranasal Sinuses": {
        "Frontal sinuses": [],
        "Maxillary sinuses": [],
        "Ethmoid air cells": [],
        "Sphenoid sinuses": [],
        "Drainage pathways (overview)": [
            "Ostiomeatal complex (middle meatus, overview)",
        ],
        "Paediatric development (overview)": [
            "Sinuses develop with age (clinical relevance for sinusitis patterns)",
        ],
    },

    "Pharynx": {
        "Nasopharynx": [
            "Eustachian tube openings",
            "Adenoids (pharyngeal tonsil)",
        ],
        "Oropharynx": [
            "Palatine tonsils",
            "Tongue base (overview)",
        ],
        "Laryngopharynx (hypopharynx)": [
            "Piriform fossae (overview)",
        ],
    },

    "Larynx": {
        "Regions": [
            "Supraglottis",
            "Glottis",
            "Subglottis",
        ],
        "Cartilages": [
            "Thyroid cartilage",
            "Cricoid cartilage",
            "Epiglottis",
            "Arytenoid cartilages",
            "Corniculate cartilages (overview)",
            "Cuneiform cartilages (overview)",
        ],
        "Vocal structures": [
            "True vocal cords (vocal folds)",
            "False vocal cords (vestibular folds)",
            "Glottis",
        ],
        "Laryngeal muscles (overview)": [
            "Posterior cricoarytenoid (abduction)",
            "Lateral cricoarytenoid (adduction)",
            "Cricothyroid (tension)",
        ],
        "Innervation (overview)": [
            "Recurrent laryngeal nerve (motor to most muscles)",
            "Superior laryngeal nerve (cricothyroid + sensation, overview)",
        ],
    },

    "Oral Cavity (ENT interface)": {
        "Tongue": ["Taste (overview)", "Speech/swallowing roles (overview)"],
        "Tonsils": [
            "Palatine tonsils",
            "Lingual tonsils (overview)",
        ],
        "Salivary glands (overview)": [
            "Parotid",
            "Submandibular",
            "Sublingual",
        ],
    },

    "Neck (ENT-relevant Anatomy)": {
        "Lymph nodes (overview)": [
            "Anterior cervical nodes",
            "Posterior cervical nodes",
            "Submandibular nodes",
            "Supraclavicular nodes",
        ],
        "Thyroid (ENT overlap)": [
            "Thyroid gland enlargement (goitre, overview)",
            "Thyroglossal duct remnant/cyst (overview)",
        ],
        "Congenital neck masses (overview)": [
            "Branchial cleft cyst",
            "Thyroglossal duct cyst",
            "Cystic hygroma (lymphatic malformation, overview)",
        ],
    },

    "ENT Physiology & Defence": {
        "Hearing (overview)": [
            "Sound conduction: external → middle → inner ear",
            "Cochlear transduction (hair cells)",
        ],
        "Balance (overview)": [
            "Vestibular input",
            "Cerebellar integration (overview)",
            "Oculomotor reflexes (VOR, overview)",
        ],
        "Mucociliary clearance": [
            "Nasal mucosa cilia",
            "Sinus drainage (overview)",
        ],
        "Local immune defence": [
            "Waldeyer ring (tonsils/adenoids)",
            "Secretory IgA (overview)",
        ],
    },

    "Paediatric ENT (High-yield)": {
        "Paediatric anatomy considerations": [
            "Eustachian tube shorter/more horizontal → otitis media risk",
            "Smaller subglottic airway → croup severity risk (overview)",
            "Adenoid hypertrophy relevance (overview)",
        ],
        "Common paediatric ENT conditions (overview)": [
            "Otitis media",
            "Otitis externa",
            "Glue ear (OME)",
            "Tonsillitis",
            "Adenoid hypertrophy",
            "Croup",
            "Epiglottitis (rare with vaccination, overview)",
            "Foreign body (nose/ear)",
        ],
        "Hearing screening / development (overview)": [
            "Newborn hearing screen",
            "Speech delay linkage (overview)",
        ],
    },

    "ENT Investigations (overview)": {
        "Ear tests": [
            "Otoscopy",
            "Tympanometry (overview)",
            "Pure tone audiometry (older child)",
            "Otoacoustic emissions (newborn, overview)",
        ],
        "Nose/sinus": [
            "Anterior rhinoscopy",
            "Nasal endoscopy (overview)",
        ],
        "Throat/larynx": [
            "Throat exam",
            "Flexible nasendoscopy (overview)",
            "Laryngoscopy (overview)",
        ],
        "Imaging (overview)": [
            "X-ray/CT sinuses (selected cases, overview)",
            "CT temporal bone (selected cases, overview)",
        ],
    },

    "ENT Treatments (overview)": {
        "Medical": [
            "Antibiotics (selected infections, overview)",
            "Intranasal steroids (rhinitis/adenoids, overview)",
            "Analgesia",
            "Antihistamines (selected cases, overview)",
        ],
        "Surgical / procedures (overview)": [
            "Grommets (ventilation tubes)",
            "Adenoidectomy",
            "Tonsillectomy",
            "Myringotomy",
            "Foreign body removal",
        ],
    },
}

# ============================
# ADD THIS: OPHTHALMOLOGY TREE
# ============================
OPH_TREE = {
    "Eye (Globe) Anatomy": {
        "Layers (Tunics) of the eye": {
            "Fibrous coat": [
                "Sclera",
                "Cornea",
            ],
            "Vascular coat (Uvea)": [
                "Iris",
                "Ciliary body",
                "Choroid",
            ],
            "Neural coat": [
                "Retina",
            ],
        },

        "Cornea": {
            "Layers": [
                "Epithelium",
                "Bowman's layer (overview)",
                "Stroma",
                "Descemet membrane (overview)",
                "Endothelium",
            ],
            "Functions": [
                "Refraction",
                "Barrier protection",
            ],
        },

        "Sclera": [
            "Scleral structure (overview)",
            "Extraocular muscle insertion points (overview)",
        ],

        "Anterior chamber & aqueous humour": {
            "Chambers": [
                "Anterior chamber",
                "Posterior chamber",
            ],
            "Aqueous humour production": [
                "Ciliary processes",
            ],
            "Aqueous drainage": [
                "Trabecular meshwork",
                "Canal of Schlemm",
                "Episcleral veins (overview)",
                "Uveoscleral outflow (overview)",
            ],
        },

        "Iris & pupil": {
            "Iris muscles": [
                "Sphincter pupillae (parasympathetic)",
                "Dilator pupillae (sympathetic)",
            ],
            "Pupil": [
                "Pupillary light reflex (overview)",
                "Accommodation response (overview)",
            ],
        },

        "Ciliary body": {
            "Ciliary muscle": [
                "Accommodation",
            ],
            "Ciliary processes": [
                "Aqueous humour secretion",
            ],
            "Zonules (suspensory ligaments)": [
                "Lens suspension",
            ],
        },

        "Lens": {
            "Structure": [
                "Lens capsule",
                "Lens fibres (overview)",
            ],
            "Functions": [
                "Refraction",
                "Accommodation",
            ],
        },

        "Vitreous body": [
            "Vitreous humour",
            "Vitreoretinal interface (overview)",
        ],

        "Retina": {
            "Key regions": [
                "Macula",
                "Fovea",
                "Optic disc",
                "Peripheral retina",
            ],
            "Photoreceptors": [
                "Rods",
                "Cones",
            ],
            "Retinal layers (overview)": [
                "Retinal pigment epithelium (RPE)",
                "Photoreceptor layer",
                "Bipolar cell layer (overview)",
                "Ganglion cell layer",
            ],
            "Retinal blood supply": [
                "Central retinal artery",
                "Choroidal circulation (outer retina) (overview)",
            ],
        },

        "Optic nerve": {
            "Optic nerve head": [
                "Optic disc",
                "Cup (optic cup, overview)",
            ],
            "Visual pathway (overview)": [
                "Optic nerve",
                "Optic chiasm",
                "Optic tract",
                "Lateral geniculate nucleus",
                "Optic radiations",
                "Visual cortex (occipital lobe)",
            ],
        },
    },

    "Adnexa (Supporting Structures)": {
        "Eyelids": {
            "Anatomy": [
                "Skin",
                "Orbicularis oculi",
                "Tarsal plate",
                "Levator palpebrae superioris (upper lid)",
                "Müller muscle (sympathetic, overview)",
            ],
            "Glands": [
                "Meibomian glands (tarsal glands)",
                "Glands of Zeis (overview)",
                "Glands of Moll (overview)",
            ],
            "Eyelashes": [],
        },

        "Conjunctiva": {
            "Parts": [
                "Palpebral conjunctiva",
                "Bulbar conjunctiva",
                "Fornices",
            ],
            "Functions": [
                "Lubrication",
                "Barrier defence (overview)",
            ],
        },

        "Lacrimal system": {
            "Tear production": [
                "Lacrimal gland",
                "Accessory lacrimal glands (overview)",
            ],
            "Tear film": [
                "Lipid layer (Meibomian)",
                "Aqueous layer (lacrimal gland)",
                "Mucin layer (goblet cells)",
            ],
            "Tear drainage": [
                "Puncta",
                "Canaliculi",
                "Lacrimal sac",
                "Nasolacrimal duct",
                "Drainage into inferior meatus (overview)",
            ],
        },

        "Orbit": {
            "Bony orbit (overview)": [
                "Frontal bone",
                "Zygomatic bone",
                "Maxilla",
                "Ethmoid",
                "Sphenoid",
                "Lacrimal bone",
                "Palatine bone (overview)",
            ],
            "Orbital contents": [
                "Globe",
                "Extraocular muscles",
                "Optic nerve",
                "Orbital fat",
                "Lacrimal gland",
            ],
        },
    },

    "Extraocular Muscles & Eye Movements": {
        "Extraocular muscles": {
            "Recti": [
                "Medial rectus",
                "Lateral rectus",
                "Superior rectus",
                "Inferior rectus",
            ],
            "Obliques": [
                "Superior oblique",
                "Inferior oblique",
            ],
            "Levator palpebrae superioris": [],
        },
        "Cranial nerve innervation": [
            "CN III (oculomotor): most muscles + pupil constriction (parasymp)",
            "CN IV (trochlear): superior oblique",
            "CN VI (abducens): lateral rectus",
        ],
        "Gaze physiology (overview)": [
            "Saccades",
            "Smooth pursuit",
            "Vestibulo-ocular reflex (VOR)",
        ],
    },

    "Physiology of Vision": {
        "Refraction": [
            "Cornea (major refractive surface)",
            "Lens (fine focus/accommodation)",
        ],
        "Accommodation": [
            "Ciliary muscle contraction",
            "Lens thickening",
        ],
        "Phototransduction (overview)": [
            "Rods (dim light)",
            "Cones (colour/acuity)",
        ],
        "Pupillary reflexes (overview)": [
            "Afferent: CN II",
            "Efferent: CN III",
        ],
        "Visual fields (overview)": [
            "Nasal vs temporal retina mapping",
            "Optic chiasm crossing (nasal fibres)",
        ],
    },

    "Common Paediatric Ophthalmology (MRCPCH Core)": {
        "Red eye": {
            "Conjunctivitis": [
                "Viral conjunctivitis",
                "Bacterial conjunctivitis",
                "Allergic conjunctivitis",
            ],
            "Blepharitis (overview)": [],
            "Keratitis (overview)": [],
        },

        "Visual development": {
            "Amblyopia": [
                "Strabismic amblyopia",
                "Refractive amblyopia",
                "Deprivation amblyopia",
            ],
            "Strabismus": [
                "Esotropia",
                "Exotropia",
                "Hypertropia (overview)",
            ],
        },

        "Refractive errors": [
            "Myopia",
            "Hyperopia",
            "Astigmatism",
        ],

        "Paediatric emergencies (overview)": {
            "Leukocoria": [
                "Congenital cataract",
                "Retinoblastoma",
                "Persistent fetal vasculature (overview)",
                "Retinopathy of prematurity (overview)",
            ],
            "Acute painful red eye (rare paeds, overview)": [
                "Acute glaucoma (rare)",
                "Uveitis (overview)",
            ],
            "Orbital cellulitis": [
                "Sinus-related spread (overview)",
                "Proptosis / painful eye movements (overview)",
            ],
            "Chemical injury (overview)": [],
        },

        "Neonatal eye conditions": [
            "Nasolacrimal duct obstruction",
            "Ophthalmia neonatorum (overview)",
        ],
    },

    "Investigations (overview)": {
        "Visual acuity assessment": [
            "Age-appropriate charts (overview)",
            "Fix-and-follow (infant, overview)",
        ],
        "Pupil exam": [
            "Direct/consensual light reflex",
            "RAPD (relative afferent pupillary defect, overview)",
        ],
        "Eye alignment": [
            "Hirschberg test (overview)",
            "Cover–uncover test (overview)",
        ],
        "Fundoscopy (overview)": [
            "Optic disc",
            "Vessels",
            "Macula",
        ],
        "Intraocular pressure (overview)": [
            "Tonometry",
        ],
        "Imaging (overview)": [
            "Ocular ultrasound (selected cases)",
            "OCT (retina/optic nerve, overview)",
        ],
    },

    "Treatments (overview)": {
        "Topical": [
            "Lubricants",
            "Topical antibiotics (selected cases, overview)",
            "Topical antihistamines (allergic conjunctivitis, overview)",
            "Topical steroids (specialist use, overview)",
        ],
        "Vision correction": [
            "Glasses",
            "Contact lenses (selected cases, overview)",
        ],
        "Amblyopia therapy": [
            "Patching",
            "Atropine penalisation (overview)",
        ],
        "Surgical (overview)": [
            "Strabismus surgery",
            "Cataract surgery (congenital cataract)",
            "Nasolacrimal probing (persistent obstruction)",
        ],
    },
}

# ============================
# ADD THIS: PSYCHOLOGY & DEVELOPMENT TREE (MRCPCH-oriented)
# ============================
PSYCH_TREE = {
    "Child Development (Core Domains)": {
        "Gross motor": {
            "Posture & tone (overview)": [
                "Head control",
                "Truncal stability",
                "Balance and gait (overview)",
            ],
            "Milestones (overview)": [
                "Rolling",
                "Sitting",
                "Crawling",
                "Standing",
                "Walking",
                "Running/jumping",
            ],
            "Coordination (overview)": [
                "Climbing stairs",
                "Hopping",
                "Skipping",
            ],
        },

        "Fine motor & vision": {
            "Hand skills (overview)": [
                "Reaching",
                "Grasp patterns (palmar → pincer) (overview)",
                "Manipulation (stacking, scribbling) (overview)",
            ],
            "Pre-writing skills (overview)": [
                "Scribble",
                "Copy shapes",
                "Draw person (overview)",
            ],
            "Visual-motor integration (overview)": [
                "Tracking",
                "Hand–eye coordination",
            ],
        },

        "Speech, language & communication": {
            "Language components": {
                "Receptive language": [
                    "Understanding commands",
                    "Understanding vocabulary",
                ],
                "Expressive language": [
                    "Babbling",
                    "First words",
                    "Two-word phrases",
                    "Sentences (overview)",
                ],
                "Pragmatics (social use of language)": [
                    "Turn-taking",
                    "Eye contact (overview)",
                    "Gestures (pointing, waving)",
                ],
            },
            "Speech sound production (overview)": [
                "Articulation",
                "Phonology",
            ],
            "Non-verbal communication": [
                "Gestures",
                "Facial expression",
                "Joint attention",
            ],
        },

        "Social, emotional & behavioural development": {
            "Attachment": [
                "Secure attachment",
                "Insecure attachment (overview)",
                "Separation anxiety (overview)",
            ],
            "Emotional regulation (overview)": [
                "Self-soothing",
                "Tantrums and limits (overview)",
            ],
            "Play": {
                "Stages of play (overview)": [
                    "Solitary play",
                    "Parallel play",
                    "Associative play",
                    "Cooperative play",
                ],
                "Imaginative play (overview)": [],
            },
            "Peer relationships (overview)": [
                "Friendship skills",
                "Bullying and social stressors (overview)",
            ],
        },

        "Cognition & learning": {
            "Executive functions (overview)": [
                "Attention",
                "Working memory",
                "Planning",
                "Inhibitory control",
            ],
            "Problem-solving (overview)": [],
            "School readiness (overview)": [
                "Pre-literacy skills",
                "Pre-numeracy skills",
            ],
        },
    },

    "Neurodevelopmental Disorders": {
        "Autism spectrum disorder (ASD)": {
            "Core features": [
                "Social communication differences",
                "Restricted/repetitive behaviours",
                "Sensory differences (overview)",
            ],
            "Associated features (overview)": [
                "Language delay",
                "Intellectual disability (some)",
                "Anxiety (common, overview)",
                "Sleep difficulties (overview)",
            ],
            "Red flags (overview)": [
                "No babbling/gestures by ~12 months (overview)",
                "No single words by ~16 months (overview)",
                "No 2-word phrases by ~24 months (overview)",
                "Loss of skills (regression)",
                "Poor joint attention (overview)",
            ],
        },

        "ADHD": {
            "Domains": [
                "Inattention",
                "Hyperactivity",
                "Impulsivity",
            ],
            "Presentations (overview)": [
                "Predominantly inattentive",
                "Predominantly hyperactive-impulsive",
                "Combined",
            ],
            "Functional impacts (overview)": [
                "School performance",
                "Peer relationships",
                "Injury risk (overview)",
            ],
        },

        "Specific learning disorders (overview)": {
            "Dyslexia (reading)": [],
            "Dyscalculia (maths)": [],
            "Written expression difficulties": [],
        },

        "Developmental coordination disorder (DCD)": [
            "Clumsiness / poor motor coordination",
            "Impact on daily living and school (overview)",
        ],

        "Intellectual disability (overview)": {
            "Definition (overview)": [
                "Limitations in intellectual functioning",
                "Limitations in adaptive functioning",
            ],
            "Adaptive domains (overview)": [
                "Conceptual",
                "Social",
                "Practical",
            ],
        },

        "Speech & language disorders": {
            "Developmental language disorder (DLD)": [],
            "Speech sound disorder (overview)": [],
            "Stuttering (overview)": [],
        },
    },

    "Mental Health in Children & Adolescents": {
        "Anxiety disorders (overview)": [
            "Separation anxiety disorder",
            "Generalised anxiety disorder",
            "Social anxiety disorder",
            "Specific phobias",
            "Panic disorder (overview)",
        ],
        "Depressive disorders (overview)": [
            "Major depressive disorder",
            "Persistent depressive disorder (dysthymia) (overview)",
        ],
        "Obsessive-compulsive disorder (OCD) (overview)": [
            "Obsessions",
            "Compulsions",
        ],
        "Trauma & stressor-related disorders (overview)": [
            "PTSD (overview)",
            "Adjustment disorder (overview)",
        ],
        "Eating disorders (informational, overview)": [
            "Anorexia nervosa (overview)",
            "Avoidant/restrictive food intake disorder (ARFID) (overview)",
        ],
        "Tic disorders (overview)": [
            "Transient tic disorder",
            "Chronic motor/vocal tic disorder",
            "Tourette syndrome (overview)",
        ],
        "Psychosis (rare in paeds, overview)": [
            "Hallucinations/delusions (overview)",
            "Early-onset psychosis (overview)",
        ],
    },

    "Behavioural & Emotional Presentations (Common in Paeds)": {
        "Sleep problems": {
            "Sleep hygiene (overview)": [],
            "Behavioural insomnia of childhood (overview)": [],
            "Night terrors (overview)": [],
            "Nightmares (overview)": [],
            "Sleepwalking (overview)": [],
            "OSA symptoms (ENT link, overview)": ["Snoring", "Daytime sleepiness/behavioural issues (overview)"],
        },
        "Enuresis & encopresis (overview)": [
            "Nocturnal enuresis",
            "Daytime wetting (overview)",
            "Encopresis/soiling (overview)",
        ],
        "Temper tantrums & oppositional behaviour (overview)": [
            "Normal toddler tantrums vs atypical patterns (overview)",
            "Oppositional defiant disorder (overview)",
        ],
        "School refusal (overview)": [
            "Anxiety-related school refusal",
            "Bullying-related (overview)",
        ],
        "Substance use (adolescents, overview)": [
            "Screening and risk factors (overview)",
        ],
    },

    "Developmental Assessment & Screening": {
        "History": [
            "Pregnancy/birth history",
            "Medical history",
            "Family history",
            "Social history",
            "Developmental history (all domains)",
        ],
        "Examination (overview)": [
            "Growth parameters",
            "Dysmorphic features (overview)",
            "Neurological exam (tone, reflexes, coordination)",
            "Vision/hearing screen (overview)",
        ],
        "Screening tools (overview)": [
            "Developmental surveillance",
            "Parent questionnaires (overview)",
            "ASD screening tools (overview)",
            "ADHD rating scales (overview)",
        ],
        "Hearing assessment": [
            "Newborn hearing screen",
            "Audiology referral (overview)",
        ],
        "Vision assessment (overview)": [
            "Visual acuity",
            "Strabismus screening (overview)",
        ],
    },

    "Safeguarding, Adverse Childhood Experiences & Social Factors": {
        "Safeguarding principles (overview)": [
            "Recognising abuse/neglect",
            "Documenting findings (overview)",
            "Multi-agency working (overview)",
        ],
        "Types of maltreatment (overview)": [
            "Physical abuse",
            "Emotional abuse",
            "Sexual abuse (overview)",
            "Neglect",
        ],
        "ACE and toxic stress (overview)": [
            "Impact on development",
            "Mental health and behaviour effects (overview)",
        ],
        "Family & social context (overview)": [
            "Parental mental health",
            "Domestic violence exposure (overview)",
            "Poverty/housing instability (overview)",
        ],
    },

    "Child & Adolescent Psychiatry Interface (Care Pathways)": {
        "Initial management (overview)": [
            "Psychoeducation",
            "Parenting support",
            "School liaison (overview)",
            "Lifestyle/sleep interventions (overview)",
        ],
        "Therapies (overview)": [
            "CBT",
            "Family therapy",
            "Behavioural interventions",
            "Speech and language therapy (SALT)",
            "Occupational therapy (OT)",
            "Physiotherapy (PT)",
        ],
        "Medication (overview)": [
            "ADHD medications (stimulant/non-stimulant, overview)",
            "SSRIs for anxiety/depression (specialist use, overview)",
            "Melatonin for sleep (selected cases, overview)",
        ],
        "Referral & MDT": [
            "CAMHS",
            "Educational psychology (overview)",
            "SEN support / school services (overview)",
            "Community paediatrics",
        ],
    },

    "Paediatric-Specific Developmental Topics": {
        "Prematurity & development (overview)": [
            "Corrected age",
            "Neurodevelopmental follow-up (overview)",
        ],
        "Global developmental delay": [
            "Definition (overview)",
            "Key causes (overview)",
            "Red flags (loss of skills, severe delay)",
        ],
        "Developmental regression": [
            "Loss of previously acquired skills",
            "Urgent evaluation triggers (overview)",
        ],
        "Language bilingualism (overview)": [
            "Normal bilingual language patterns (overview)",
            "When to worry (overview)",
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
    st.session_state.setdefault("route", "home")  # home | system | cardio_tree | resp_tree | neuro_tree | gi_tree | renal_tree
    st.session_state.setdefault("selected_system_id", None)

    st.session_state.setdefault("cardio_path", [])
    st.session_state.setdefault("resp_path", [])
    st.session_state.setdefault("neuro_path", [])
    st.session_state.setdefault("gi_path", [])
    st.session_state.setdefault("renal_path", [])
    st.session_state.setdefault("endo_path", [])
    st.session_state.setdefault("heme_path", [])
    st.session_state.setdefault("imm_path", [])
    st.session_state.setdefault("onc_path", [])
    st.session_state.setdefault("msk_path", [])
    st.session_state.setdefault("derm_path", [])
    st.session_state.setdefault("ent_path", [])
    st.session_state.setdefault("oph_path", [])
    st.session_state.setdefault("psych_path", [])

path_list = ["cardio_path",
             "resp_path",
             "neuro_path",
             "gi_path",
             "renal_path",
             "endo_path",
             "heme_path",
             "imm_path",
             "onc_path",
             "msk_path",
             "derm_path", 
             "ent_path",
             "oph_path",
             "psych_path"]

def go_home():
    st.session_state.route = "home"
    st.session_state.selected_system_id = None
    for k in path_list:
        reset_nav(k)

def go_system(system_id: str):
    st.session_state.route = "system"
    st.session_state.selected_system_id = system_id
    for k in path_list:
        reset_nav(k)

def go_cardio_tree():
    st.session_state.route = "cardio_tree"
    st.session_state.selected_system_id = "cardio"
    for k in path_list:
        reset_nav(k)

def go_resp_tree():
    st.session_state.route = "resp_tree"
    st.session_state.selected_system_id = "resp"
    for k in path_list:
        reset_nav(k)

def go_neuro_tree():
    st.session_state.route = "neuro_tree"
    st.session_state.selected_system_id = "neuro"
    for k in path_list:
        reset_nav(k)

def go_gi_tree():
    st.session_state.route = "gi_tree"
    st.session_state.selected_system_id = "gi"
    for k in path_list:
        reset_nav(k)

def go_renal_tree():
    st.session_state.route = "renal_tree"
    st.session_state.selected_system_id = "renal"
    for k in path_list:
        reset_nav(k)

def go_endo_tree():
    st.session_state.route = "endo_tree"
    st.session_state.selected_system_id = "endo"
    for k in path_list:
        reset_nav(k)

def go_heme_tree():
    st.session_state.route = "heme_tree"
    st.session_state.selected_system_id = "heme"
    for k in path_list:
        reset_nav(k)

def go_imm_tree():
    st.session_state.route = "imm_tree"
    st.session_state.selected_system_id = "imm"
    for k in path_list:
        reset_nav(k)
        
def go_onc_tree():
    st.session_state.route = "onc_tree"
    st.session_state.selected_system_id = "onc"
    for k in path_list:
        reset_nav(k)

def go_msk_tree():
    st.session_state.route = "msk_tree"
    st.session_state.selected_system_id = "msk"
    for k in path_list:
        reset_nav(k)

def go_derm_tree():
    st.session_state.route = "derm_tree"
    st.session_state.selected_system_id = "derm"
    for k in path_list:
        reset_nav(k)

def go_ent_tree():
    st.session_state.route = "ent_tree"
    st.session_state.selected_system_id = "ent"
    for k in path_list:
        reset_nav(k)
        
def go_oph_tree():
    st.session_state.route = "oph_tree"
    st.session_state.selected_system_id = "oph"
    for k in path_list:
        reset_nav(k)

def go_psych_tree():
    st.session_state.route = "psych_tree"
    st.session_state.selected_system_id = "psych"
    for k in path_list:
        reset_nav(k)
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
        elif system["id"] == "renal":
            go_renal_tree()
        elif system["id"] == "endo":
            go_endo_tree()
        elif system["id"] == "heme":
            go_heme_tree()
        elif system["id"] == "imm":
            go_imm_tree()
        elif system["id"] == "onc":
            go_onc_tree()
        elif system["id"] == "msk":
            go_msk_tree()
        elif system["id"] == "derm":
            go_derm_tree()
        elif system["id"] == "ent":
            go_ent_tree()
        elif system["id"] == "oph":
            go_oph_tree()
        elif system["id"] == "psych":
            go_psych_tree()

def item_card(label, key):
    return st.button(label, key=key, use_container_width=True)

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
    st.info("Placeholder page. Cardio/Resp/Neuro/GI/Renal have full component trees.")
    st.button("← Back to Systems", on_click=go_home)

def page_cardio_tree():
    tree_page("🫀 Cardiovascular", CARDIO_TREE, "cardio_path", "Cardiovascular")

def page_resp_tree():
    tree_page("🫁 Respiratory", RESP_TREE, "resp_path", "Respiratory")

def page_neuro_tree():
    tree_page("🧠 Neurology", NEURO_TREE, "neuro_path", "Neurology")

def page_gi_tree():
    tree_page("🧻 Gastrointestinal", GI_TREE, "gi_path", "Gastrointestinal")

def page_renal_tree():
    tree_page("🫘 Nephro-urology", RENAL_TREE, "renal_path", "Nephro-urology")

def page_endo_tree():
    tree_page("🧪 Endocrine", ENDO_TREE, "endo_path", "Endocrine")

def page_heme_tree():
    tree_page("🩸 Haematology", HEME_TREE, "heme_path", "Haematology")
    
def page_imm_tree():
    tree_page("🦠 Immunology", IMM_TREE, "imm_path", "Immunology")

def page_onc_tree():
    tree_page("♋ Oncology", ONC_TREE, "onc_path", "Oncology")

def page_msk_tree():
    tree_page("🦴 Rheumatology", MSK_TREE, "msk_path", "Rheumatology")

def page_derm_tree():
    tree_page("🧴 Dermatology", DERM_TREE, "derm_path", "Dermatology")

def page_ent_tree():
    tree_page("👂 ENT", ENT_TREE, "ent_path", "ENT")

def page_oph_tree():
    tree_page("👁️ Ophthalmology", OPH_TREE, "oph_path", "Ophthalmology")

def page_psych_tree():
    tree_page("🧩 Psychology & Development", PSYCH_TREE, "psych_path", "Psychology & Development")

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

        #st.divider()
        #st.caption("Cardio path:")
        #st.code(" > ".join(st.session_state.cardio_path) if st.session_state.cardio_path else "(root)")
        #st.caption("Resp path:")
        #st.code(" > ".join(st.session_state.resp_path) if st.session_state.resp_path else "(root)")
        #st.caption("Neuro path:")
        #st.code(" > ".join(st.session_state.neuro_path) if st.session_state.neuro_path else "(root)")
        #st.caption("GI path:")
        #st.code(" > ".join(st.session_state.gi_path) if st.session_state.gi_path else "(root)")
        #st.caption("Renal path:")
        #st.code(" > ".join(st.session_state.renal_path) if st.session_state.renal_path else "(root)")
        #st.caption("Endo path:")
        #st.code(" > ".join(st.session_state.endo_path) if st.session_state.endo_path else "(root)")
        #st.caption("Heme path:")
        #st.code(" > ".join(st.session_state.heme_path) if st.session_state.heme_path else "(root)")
        #st.caption("Imm path:")
        #st.code(" > ".join(st.session_state.imm_path) if st.session_state.imm_path else "(root)")
        #st.caption("Onc path:")
        #st.code(" > ".join(st.session_state.onc_path) if st.session_state.onc_path else "(root)")
        #st.caption("MSK path:")
        #st.code(" > ".join(st.session_state.msk_path) if st.session_state.msk_path else "(root)")
        #st.caption("Derm path:")
        #st.code(" > ".join(st.session_state.derm_path) if st.session_state.derm_path else "(root)")
        #st.caption("ENT path:")
        #st.code(" > ".join(st.session_state.ent_path) if st.session_state.ent_path else "(root)")
        #st.caption("Oph path:")
        #st.code(" > ".join(st.session_state.oph_path) if st.session_state.oph_path else "(root)")
        #st.caption("Psych path:")
        #st.code(" > ".join(st.session_state.psych_path) if st.session_state.psych_path else "(root)")

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
    elif st.session_state.route == "gi_tree":
        page_gi_tree()
    elif st.session_state.route == "renal_tree":
        page_renal_tree()
    elif st.session_state.route == "endo_tree":
        page_endo_tree()
    elif st.session_state.route == "heme_tree":
        page_heme_tree()
    elif st.session_state.route == "imm_tree":
        page_imm_tree()
    elif st.session_state.route == "onc_tree":
        page_onc_tree()
    elif st.session_state.route == "msk_tree":
        page_msk_tree()
    elif st.session_state.route == "derm_tree":
        page_derm_tree()
    elif st.session_state.route == "ent_tree":
        page_ent_tree()
    elif st.session_state.route == "oph_tree":
        page_oph_tree()
    elif st.session_state.route == "psych_tree":
        page_psych_tree()

if __name__ == "__main__":
    main()




