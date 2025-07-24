import streamlit as st
from src.config_parser import parse_config
from src.diagram_generator import generate_diagram
import tempfile
import os

st.title("NetArch-AutoGen Demo")

uploaded_file = st.file_uploader("Upload YAML/JSON config file", type=["yaml", "yml", "json"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    output_path = tmp_path + ".png"

    try:
        config = parse_config(tmp_path)
        generate_diagram(config, output_path)
        st.image(output_path, caption="Generated Diagram")
    except Exception as e:
        st.error(f"Error: {e}")

    os.unlink(tmp_path)
