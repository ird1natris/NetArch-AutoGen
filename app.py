import streamlit as st
import yaml
import json
import os
from io import StringIO
from pathlib import Path
from src.diagram_generator import generate_diagram_from_yaml

# Set page config
st.set_page_config(page_title="NetArch-AutoGen", page_icon="🛠️", layout="centered")

# Sidebar: Theme toggle + Sample file download
st.sidebar.title("⚙️ Settings")
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=True)
st.sidebar.markdown("### 🧪 Sample Config")

    # Sample file download
    sample_path = Path(__file__).parent / "configs" / "sample.yaml"
    if sample_path.exists():
        st.sidebar.download_button(
            label="📄 Download Sample File (YAML)",
            data=sample_path.read_bytes(),
            file_name="sample.yaml",
            mime="application/x-yaml"
        )
    else:
        st.warning("⚠️ Sample file not found in /configs.")

# --- Main UI ---
st.markdown("<h1 style='text-align: center;'>NetArch-AutoGen 🛠️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload your network config and auto-generate diagrams!</p>", unsafe_allow_html=True)

# Drag-and-drop uploader
uploaded_file = st.file_uploader("📂 Upload File", type=['yaml', 'yml', 'json'])

if uploaded_file:
    try:
        content = uploaded_file.read().decode("utf-8")

        # Detect file type
        if uploaded_file.name.endswith(".json"):
            data = json.loads(content)
        else:
            data = yaml.safe_load(content)

        # Output path
        filename_wo_ext = Path(uploaded_file.name).stem
        output_path = generate_diagram_from_yaml(data, filename=f"outputs/{filename_wo_ext}")

        # Show diagram
        st.success("✅ Diagram generated successfully!")
        st.image(output_path, caption="🖼️ Generated Diagram", use_container_width=True)

    except Exception as e:
        st.error(f"❌ Failed to generate diagram: {e}")

# Footer
st.markdown("---")
st.markdown(
    "<small>Made with ❤️ by ird1natris • NetArch-AutoGen • Secure your network visually</small>",
    unsafe_allow_html=True
)
