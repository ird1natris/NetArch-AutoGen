import streamlit as st
from pathlib import Path
from diagram_generator import generate_diagram  # Adjust this import if needed
import tempfile
import os

# --- App Config ---
st.set_page_config(
    page_title="NetArch-AutoGen",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 NetArch-AutoGen")
st.markdown(
    """
    Upload your **YAML** or **JSON** file and get your auto-generated network architecture diagram.  
    Built for Cloud | Hybrid | On-Prem | Edge ☁️🧩🏢
    """
)

# File uploader
uploaded_file = st.file_uploader("📂 Upload your network config file", type=["yaml", "yml", "json"])

if uploaded_file:
    with st.spinner("Processing your file and generating diagram... ⏳"):
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = Path(tmp.name)

        # Output path
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / f"{uploaded_file.name}_diagram.png"

        # Generate diagram
        try:
            generate_diagram(tmp_path, output_path)
            st.success("✅ Diagram generated successfully!")
            st.image(str(output_path), caption="📊 Generated Architecture Diagram", use_container_width=True)

            # Optional: Download button
            with open(output_path, "rb") as f:
                st.download_button(
                    label="⬇️ Download Diagram",
                    data=f,
                    file_name=output_path.name,
                    mime="image/png"
                )
        except Exception as e:
            st.error(f"⚠️ Diagram generation failed: {e}")

        # Cleanup temp file
        os.remove(tmp_path)

# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ by [ird1natris](https://github.com/ird1natris)")
