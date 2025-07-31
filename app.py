# app.py

import streamlit as st
from diagram_generator import generate_diagram
import os
from PIL import Image

st.set_page_config(page_title="NetArch-AutoGen", layout="centered")
st.title("📡 Auto-Generate Network Diagram from YAML")

uploaded_file = st.file_uploader("Upload your YAML file", type=["yaml", "yml"])

if uploaded_file:
    st.success("YAML file uploaded!")
    
    # Read and generate
    yaml_content = uploaded_file.read().decode("utf-8")
    output_path = "outputs/generated_diagram"
    os.makedirs("outputs", exist_ok=True)
    generate_diagram(yaml_content, filename=output_path)
    
    st.image(f"{output_path}.png", caption="Generated Architecture Diagram", use_container_width=True)

# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ by [ird1natris](https://github.com/ird1natris)")
