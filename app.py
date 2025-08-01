import streamlit as st
import yaml
import json
from pathlib import Path
from src.diagram_generator import generate_diagram_from_yaml

# --- Theme toggle ---
st.set_page_config(page_title="NetArch-AutoGen", layout="centered")

# Sidebar: Theme toggle + Sample file download
with st.sidebar:
    st.markdown("## ⚙️ Settings")

    # Dark mode toggle
    theme = st.radio("Choose Theme", ["🌞 Light Mode", "🌙 Dark Mode"])
    if theme == "🌙 Dark Mode":
        st.markdown(
            """
            <style>
            body { background-color: #0e1117; color: white; }
            .stApp { background-color: #0e1117; }
            </style>
            """,
            unsafe_allow_html=True
        )

    # Sample file download
    sample_path = Path(__file__).parent / "configs" / "sample.yaml"
    if sample_path.exists():
        st.download_button(
            label="📥 Download Sample File (YAML)",
            data=sample_path.read_bytes(),
            file_name="sample.yaml",
            mime="application/x-yaml"
        )
    else:
        st.warning("⚠️ Sample file not found in /configs.")

# --- Main UI ---
st.title("🧠 NetArch-AutoGen Diagram Generator")
st.markdown("Upload your **YAML or JSON** network architecture config to generate a diagram.")

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
        st.image(output_path, caption="Generated Diagram", use_container_width=True)

    except Exception as e:
        st.error(f"❌ Failed to generate diagram: {e}")

# Footer
st.markdown("---")
st.markdown(
    "<small>Made with ❤️ by ird1natris • NetArch-AutoGen • Secure your network visually</small>",
    unsafe_allow_html=True
)
