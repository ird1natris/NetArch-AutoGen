[![Build Status](https://github.com/ird1natris/NetArch-AutoGen/actions/workflows/diagram.yml/badge.svg)](https://github.com/ird1natris/NetArch-AutoGen/actions)
[![Python Version](https://img.shields.io/badge/python-3.10–3.11-blue.svg)](https://www.python.org/)

# NetArch‑AutoGen 🏗️

**Auto‑generate professional network architecture diagrams** from simple YAML/JSON — ideal for consultants, cloud teams, and infra architects.

---

## ⭐ Key Features

- 🛠️ **Config-driven**: Define infra in YAML/JSON and generate diagrams automatically.
- 🌐 **Multi-architecture support**: Cloud, on‑prem, multi-tier, banking, zero-trust, and beyond.
- 🤖 **GitHub Actions-ready**: `.png` outputs auto-generated and committed on config changes.
- 💻 **CLI-first design**: `src/cli.py` ensures clean, reusable invocation.
- 📁 **Artifact-friendly**: Auto-uploads PNGs for manual workflows.

---

## ⚙️ Quick Start

### 1. Clone & install dependencies
```bash
git clone https://github.com/ird1natris/NetArch-AutoGen.git
cd NetArch‑AutoGen
pip install -r requirements.txt
sudo apt-get install graphviz
```
### 2. Generate a sample diagram using CLI
```bash
python src/cli.py \
  --config configs/sample_config.yaml \
  --output outputs/sample_config.png

# View your diagram:
open outputs/sample_config.png
```
### 3. Let GitHub auto-generate diagrams
- Push changes to configs/ or src/
- CI runs automatically via diagram.yml
- PNG diagrams saved into outputs/ folder and committed back
- ✅ Check Actions tab for build status

---

## 🗂️ Project Structure
```bash
NetArch‑AutoGen/
├ configs/         # Input YAML/JSON configs
├ diagrams/        # Script definitions of various architectures
│   ├ diagram_generator.py
│   └ multi_tier_cloud_app.py
├ outputs/         # Auto-generated PNGs (via CI or CLI)
├ src/
│   ├ cli.py
│   ├ config_parser.py
│   └ diagram_generator.py
├ tests/
│   ├ test_config_parser.py
├ .github/workflows/
│   ├ diagram.yml
|   ├ github-actions-demo.yml
│   └ list_nodes.yml
├ .gitignore
├ LICENSE
├ requirements.txt
└ README.md
```
