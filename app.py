import streamlit as st
import os
import yaml
from src.diagram_generator import generate_diagram_from_yaml

st.set_page_config(page_title="NetArch-AutoGen", layout="wide")

st.title("🕸️NetArch-AutoGen")
st.markdown("Upload a YAML or JSON file describing your cloud/network setup.")

uploaded_file = st.file_uploader("Choose a YAML/JSON file", type=["yaml", "yml", "json"])

if uploaded_file:
    try:
        content = uploaded_file.read().decode("utf-8")
        if uploaded_file.name.endswith(".json"):
            import json
            data = json.loads(content)
        else:
            data = yaml.safe_load(content)

        os.makedirs("outputs", exist_ok=True)
        output_path = f"outputs/{uploaded_file.name.split('.')[0]}.png"

        generate_diagram_from_yaml(data, filename=output_path)
        st.success("Diagram generated successfully!")

        st.image(output_path, caption="Generated Diagram", use_container_width=True)

    except Exception as e:
        st.error(f"Failed to generate diagram: {str(e)}")
