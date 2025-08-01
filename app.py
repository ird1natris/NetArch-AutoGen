import streamlit as st
import os
import yaml
from src.diagram_generator import generate_diagram_from_yaml

st.set_page_config(page_title="NetArch-AutoGen", layout="centered")
st.title("📊 NetArch-AutoGen")
st.write("Upload a YAML or JSON config to generate your network architecture diagram.")

uploaded_file = st.file_uploader("Upload a config file", type=["yaml", "yml", "json"])

if uploaded_file is not None:
    file_contents = uploaded_file.read().decode("utf-8")
    filename = os.path.splitext(uploaded_file.name)[0]
    output_path = f"outputs/{filename}.png"

    os.makedirs("outputs", exist_ok=True)

    try:
        config_data = yaml.safe_load(file_contents)
        generate_diagram_from_yaml(config_data, filename=output_path)
        st.success("✅ Diagram generated successfully!")

        if os.path.exists(output_path):
            st.image(output_path, caption="Generated Network Diagram", use_container_width=True)
        else:
            st.error("❌ Failed to generate diagram: Output file not found.")

    except Exception as e:
        st.error(f"❌ Failed to generate diagram: {e}")
