import streamlit as st
st.set_page_config(layout="wide")

# Updated CSS without fixed width for the metric cards and added flexible spacing
st.markdown("""
    <style>
        /* Expand the main content area */
        .main {
            max-width: 100%;
            padding: 1rem;
        }
        /* Section header styling */
        .section-header {
            font-size: 20px;
            font-weight: bold;
            color: #A3A8C3;
            margin: 10px 0;
            padding: 5px 0;
            border-bottom: 2px solid #5A5E6B;
        }
        /* Card styling for each metric */
        .metric-card {
            background-color: #1C1E28;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
            margin: 10px; /* This margin will ensure space between boxes */
            text-align: center;
            color: #EAEAEA;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .metric-value {
            font-size: 24px;
            font-weight: bold;
            color: #4CE0D2;
        }
        .metric-delta {
            font-size: 16px;
            color: #FF4B4B;
        }
    </style>
""", unsafe_allow_html=True)

# Function to create metric cards without a fixed width
def metric_card(title, value, delta):
    st.markdown(f"""
        <div class="metric-card">
            <p>{title}</p>
            <div class="metric-value">{value}</div>
            <div class="metric-delta">{delta}</div>
        </div>
    """, unsafe_allow_html=True)

# Downloaders section with dynamic column width
with st.container():
    st.markdown("<div class='section-header'>Downloaders</div>", unsafe_allow_html=True)
    cols = st.columns([1, 1, 1, 1, 1, 1])  # Six evenly spaced columns
    for col in cols:
        with col:
            metric_card("Downloader A", "3.5 TB", "-12 GB")

# Media Management section
with st.container():
    st.markdown("<div class='section-header'>Media Management</div>", unsafe_allow_html=True)
    media_cols = st.columns([1, 1, 1])  # Three columns, evenly spaced
    for col in media_cols:
        with col:
            metric_card("Library A", "120 Movies", "+5")

# Media & Hosting section
with st.container():
    st.markdown("<div class='section-header'>Media & Hosting</div>", unsafe_allow_html=True)
    hosting_cols = st.columns([1, 1, 1, 1, 1, 1])  # Six columns, evenly spaced
    for col in hosting_cols:
        with col:
            metric_card("Service A", "300 GB Used", "-10 GB")
