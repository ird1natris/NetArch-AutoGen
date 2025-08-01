import streamlit as st
import yaml
import json
import os
from datetime import datetime
from src.diagram_generator import generate_diagram_from_yaml

st.set_page_config(page_title="NetArch-AutoGen", layout="centered", page_icon="🕸️")

st.markdown(
    """
    <h1 style='text-align: center;'>🕸️ NetArch-AutoGen</h1>
    <p style='text-align: center;'>Upload your network config and instantly generate beautiful architecture diagrams!</p>
    """, unsafe_allow_html=True
)

st.divider()

with st.expander("📘 How to use this tool"):
    st.markdown("""
    - Upload a `.yaml`, `.yml`, or `.json` configuration file.
    - The file should follow the supported schema (check [sample here](https://github.com/YOUR_REPO/sample.yaml)).
    - Once processed, your diagram will appear below with a download option.
    """)

uploaded_file = st.file_uploader("📤 Upload your YAML or JSON config file", type=['yaml', 'yml', 'json'])

if uploaded_file:
    with st.spinner("🛠️ Generating diagram..."):
        try:
            content = uploaded_file.read().decode("utf-8")
            ext = os.path.splitext(uploaded_file.name)[1].lower()

            if ext == ".json":
                data = json.loads(content)
            else:
                data = yaml.safe_load(content)

            # Create a unique filename based on timestamp
            filename_base = os.path.splitext(uploaded_file.name)[0]
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            output_filename = f"outputs/{filename_base}_{timestamp}"

            output_path = generate_diagram_from_yaml(data, filename=output_filename)

            if output_path and os.path.exists(output_path):
                st.success("✅ Diagram generated successfully!")
                st.image(output_path, caption="🖼️ Your Generated Diagram", use_container_width=True)
                with open(output_path, "rb") as img_file:
                    st.download_button(
                        label="📥 Download Diagram",
                        data=img_file,
                        file_name=f"{filename_base}.png",
                        mime="image/png"
                    )
            else:
                st.warning("⚠️ Diagram file not found after generation.")

        except Exception as e:
            st.error(f"❌ Failed to generate diagram: `{e}`")

else:
    st.info("📂 Please upload a config file to begin.")
