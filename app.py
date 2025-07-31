import streamlit as st
from pathlib import Path

# --- App Config ---
st.set_page_config(
    page_title="NetArch-AutoGen",
    page_icon="🕸️",
    layout="wide",
)

# --- Title ---
st.title("🕸️ NetArch-AutoGen")
st.markdown("Auto-generate network architecture diagrams from Python scripts, powered by the [Diagrams](https://diagrams.mingrammer.com/) library.")

# --- Sample Output Preview ---
st.header("📌 Sample Output")
sample_path = Path("outputs/multi_tier_cloud_app.png")  # Replace with your generated image path
if sample_path.exists():
    st.image(str(sample_path), caption="Generated Architecture Diagram", use_column_width=True)
else:
    st.warning("No output image found. Make sure your diagram file exists in the 'outputs/' folder.")

# --- Features Section ---
st.header("✨ Key Features")
st.markdown("""
- 🛠️ Automatically generate diagrams via GitHub Actions  
- ☁️ Visualize cloud/hybrid/on-prem infrastructures  
- 📁 Organized output saved in `/outputs` folder  
- ⚡ No terminal needed — just push code to GitHub  
""")

# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ by [ird1natris](https://github.com/ird1natris)")
