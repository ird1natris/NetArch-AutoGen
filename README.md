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
