import streamlit as st
import yaml
import json
import os
from io import StringIO
from src.diagram_generator import generate_diagram_from_yaml

# Set page config
st.set_page_config(page_title="NetArch-AutoGen", page_icon="assets/deep-learning.png", layout="centered")

# --- Sidebar (Dark mode + Sample download) ---
st.sidebar.title("⚙️ Settings")
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=True)
st.sidebar.markdown("### 🧪 Sample Config")

# Apply dark theme (via Streamlit themes)
if dark_mode:
    st.markdown(
        """
        <style>
            body { color: white; background-color: #0e1117; }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Title and Intro ---
st.markdown("<h1 style='text-align: center;'>NetArch-AutoGen 🖼️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload your network config and auto-generate diagrams!</p>", unsafe_allow_html=True)

# --- File Uploader ---
st.markdown("### 📤 Upload your YAML or JSON config file")
uploaded_file = st.file_uploader(
    label="Drag & drop or browse",
    type=['yaml', 'yml', 'json'],
    label_visibility="collapsed"
)

# --- Diagram Generator ---
if uploaded_file:
    try:
        content = uploaded_file.read().decode("utf-8")
        file_ext = os.path.splitext(uploaded_file.name)[1].lower()

        # Parse content
        data = json.loads(content) if file_ext == ".json" else yaml.safe_load(content)

        # Generate diagram
        filename_base = os.path.splitext(uploaded_file.name)[0]
        output_path = generate_diagram_from_yaml(data, filename=f"outputs/{filename_base}")

        st.success("✅ Diagram generated successfully!")
        st.image(output_path, caption="🖼️ Generated Diagram", use_container_width=True)

    except Exception as e:
        st.error(f"❌ Failed to generate diagram:\n`{e}`")

else:
    st.info("Upload a `.yaml`, `.yml`, or `.json` file to get started.")

# Footer
st.markdown("---")
st.markdown(
    "<small>Made with ❤️ by ird1natris • NetArch-AutoGen • Secure your network visually</small>",
    unsafe_allow_html=True
)
