import streamlit as st
import yaml
import json
from src.diagram_generator import generate_diagram_from_yaml

st.title("NetArch-AutoGen Diagram Generator")

uploaded_file = st.file_uploader("Upload your YAML or JSON config file", type=['yaml', 'yml', 'json'])

if uploaded_file:
    try:
        content = uploaded_file.read().decode()
        if uploaded_file.type in ['application/json']:
            data = json.loads(content)
        else:
            data = yaml.safe_load(content)

        # Use your improved function here
        output_path = generate_diagram_from_yaml(data, filename=f"outputs/{uploaded_file.name.rsplit('.',1)[0]}")

        st.success("✅ Diagram generated successfully!")
        st.image(output_path, caption="Generated Diagram", use_container_width=True)

    except Exception as e:
        st.error(f"❌ Failed to generate diagram: {e}")

