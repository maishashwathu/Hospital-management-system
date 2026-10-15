def load_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

/* ── Reset & Base Dark Theme ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif !important;
    background-color: #0b0f17 !important;
    color: #f8fafc !important;
}

/* ── Hide Streamlit default chrome ── */
footer { visibility: hidden; }
header { background: transparent !important; }

.block-container {
    padding-top: 2rem !important;
    padding-right: 2.5rem !important;
    padding-left: 2.5rem !important;
    padding-bottom: 2rem !important;
    max-width: 100% !important;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background-color: #0f172a !important;
    border-right: 1px solid #1e293b !important;
    transition: margin-left 0.3s ease, width 0.3s ease !important;
}

/* Fixed width only when sidebar is expanded */
section[data-testid="stSidebar"][aria-expanded="true"],
section[data-testid="stSidebar"]:not([aria-expanded="false"]) {
    min-width: 250px !important;
    max-width: 250px !important;
    width: 250px !important;
}

/* Allow clean collapse without leaving blank margin */
section[data-testid="stSidebar"][aria-expanded="false"] {
    min-width: 0 !important;
    width: 0 !important;
    margin-left: -250px !important;
}

/* Sidebar toggle buttons (Open / Close chevron) */
[data-testid="stSidebarCollapsedControl"] {
    top: 1rem !important;
    left: 1rem !important;
    z-index: 99999 !important;
}

[data-testid="stSidebarCollapsedControl"] button,
[data-testid="stSidebarCollapseButton"] button {
    background-color: #0f172a !important;
    color: #f8fafc !important;
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
}

[data-testid="stSidebarCollapsedControl"] button:hover,
[data-testid="stSidebarCollapseButton"] button:hover {
    background-color: #1e293b !important;
    color: #ffffff !important;
}

section[data-testid="stSidebar"] * { color: #94a3b8 !important; }

section[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    color: #94a3b8 !important;
    border: none !important;
    text-align: left !important;
    padding: 0.6rem 0.85rem !important;
    border-radius: 8px !important;
    font-size: 0.875rem !important;
    width: 100% !important;
    font-weight: 500 !important;
    box-shadow: none !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255, 255, 255, 0.06) !important;
    color: #f1f5f9 !important;
}

/* ── Metric Cards — Dark Surface ── */
[data-testid="metric-container"] {
    background-color: #161f2e !important;
    border: 1px solid #1e293b !important;
    border-radius: 14px !important;
    padding: 1.25rem !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.25) !important;
}

[data-testid="metric-container"] label {
    color: #94a3b8 !important;
    font-size: 0.78rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
    font-weight: 600 !important;
}

[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #f8fafc !important;
    font-size: 1.8rem !important;
    font-weight: 700 !important;
}

/* ── DataFrames & Tables ── */
[data-testid="stDataFrame"] {
    border-radius: 10px !important;
    overflow: hidden !important;
    border: 1px solid #1e293b !important;
    background-color: #161f2e !important;
}

table {
    color: #f8fafc !important;
    background-color: #161f2e !important;
}

th {
    background-color: #0f172a !important;
    color: #94a3b8 !important;
    border-bottom: 1px solid #1e293b !important;
    font-weight: 600 !important;
}

td {
    border-bottom: 1px solid #1e293b !important;
    color: #f8fafc !important;
}

/* ── Form Inputs & Selectboxes ── */
.stTextInput > div > div > input,
.stSelectbox > div > div,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input,
.stDateInput > div > div > input,
.stTimeInput > div > div > input {
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.9rem !important;
    background-color: #161f2e !important;
    color: #f8fafc !important;
}

.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus,
.stNumberInput > div > div > input:focus,
.stDateInput > div > div > input:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2) !important;
    outline: none !important;
}

/* Dropdown popups & select options */
div[data-baseweb="select"] * {
    background-color: #161f2e !important;
    color: #f8fafc !important;
}

div[data-baseweb="popover"], div[data-baseweb="menu"] {
    background-color: #161f2e !important;
    border: 1px solid #334155 !important;
    border-radius: 8px !important;
}

ul[role="listbox"] {
    background-color: #161f2e !important;
}

li[role="option"] {
    color: #f8fafc !important;
    background-color: #161f2e !important;
}

li[role="option"]:hover, li[role="option"][aria-selected="true"] {
    background-color: #1e293b !important;
    color: #60a5fa !important;
}

/* ── Buttons ── */
.stButton > button,
.stFormSubmitButton > button,
.stDownloadButton > button {
    border-radius: 8px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    transition: all 0.2s ease !important;
    background-color: #3b82f6 !important;
    color: #ffffff !important;
    border: 1px solid #3b82f6 !important;
    box-shadow: 0 2px 6px rgba(59, 130, 246, 0.25) !important;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover,
.stDownloadButton > button:hover {
    background-color: #2563eb !important;
    border-color: #2563eb !important;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35) !important;
}

.stButton > button:focus,
.stFormSubmitButton > button:focus,
.stDownloadButton > button:focus {
    box-shadow: none !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background-color: #161f2e !important;
    border-bottom: 1px solid #1e293b !important;
    gap: 0.25rem !important;
    padding: 0.25rem 0.5rem 0 0.5rem !important;
    border-radius: 10px 10px 0 0 !important;
}

.stTabs [data-baseweb="tab"] {
    background-color: transparent !important;
    color: #94a3b8 !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    padding: 0.65rem 1.25rem !important;
    border-radius: 6px 6px 0 0 !important;
    border-bottom: 2px solid transparent !important;
}

.stTabs [aria-selected="true"] {
    background-color: transparent !important;
    color: #60a5fa !important;
    border-bottom: 2px solid #3b82f6 !important;
    font-weight: 600 !important;
}

/* ── Alerts & Toasts ── */
.stSuccess, .stError, .stWarning, .stInfo {
    background-color: #161f2e !important;
    border-radius: 8px !important;
    border: 1px solid #1e293b !important;
}

.stSuccess > div { border-left: 4px solid #10b981 !important; color: #34d399 !important; }
.stError > div   { border-left: 4px solid #ef4444 !important; color: #f87171 !important; }
.stWarning > div { border-left: 4px solid #f59e0b !important; color: #fbbf24 !important; }
.stInfo > div    { border-left: 4px solid #3b82f6 !important; color: #60a5fa !important; }

/* ── Section header ── */
.section-header {
    font-size: 1.1rem;
    font-weight: 700;
    color: #f8fafc;
    margin: 1.5rem 0 0.75rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #1e293b;
}

/* ── Page Title ── */
.page-title {
    font-size: 1.875rem !important;
    font-weight: 800 !important;
    color: #f8fafc !important;
    margin: 0 0 1.25rem 0 !important;
    padding: 0 !important;
    line-height: 1.2 !important;
    letter-spacing: -0.5px !important;
    text-align: left !important;
}

.page-subtitle {
    font-size: 0.95rem;
    color: #94a3b8;
    margin-bottom: 1.5rem;
}

/* ── Card ── */
.info-card {
    background: #161f2e;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 1.25rem;
    margin-bottom: 1rem;
    color: #f8fafc;
}

/* ── Badges ── */
.badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 600;
}
.badge-green  { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.3); }
.badge-red    { background: rgba(239, 68, 68, 0.15);  color: #f87171; border: 1px solid rgba(248, 113, 113, 0.3); }
.badge-amber  { background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.3); }
.badge-blue   { background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(96, 165, 250, 0.3); }
.badge-gray   { background: rgba(148, 163, 184, 0.15); color: #94a3b8; border: 1px solid rgba(148, 163, 184, 0.3); }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #0b0f17; }
::-webkit-scrollbar-thumb { background: #334155; border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: #475569; }
</style>
"""