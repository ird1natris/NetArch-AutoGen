# **NetArch‑AutoGen 🏗️**  
**Infrastructure-as-Code Meets Visuals.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/) [![License](https://img.shields.io/badge/License-MIT-green)](LICENSE) [![Build Status](https://img.shields.io/github/actions/workflow/status/ird1natris/NetArch-AutoGen/diagram.yml?label=CI%20Build&logo=github)](https://github.com/ird1natris/NetArch-AutoGen/actions) [![GitHub Stars](https://img.shields.io/github/stars/ird1natris/NetArch-AutoGen?style=social)](https://github.com/ird1natris/NetArch-AutoGen/stargazers)

Automate your network architecture diagramming — transform simple YAML/JSON configs into **professional, standardized visuals**.  

Perfect for **cloud architects, network engineers, and security teams** who want to streamline documentation and communication.

---

## **🚀 Demo**
![Sample Diagram](outputs/multi_tier_cloud_app.png)  
*(Example of a multi-tier cloud architecture diagram generated with NetArch‑AutoGen.)*

---

## **🌟 Key Features**
- **🛠️ Config-Driven Diagrams** — Define infrastructure declaratively using YAML/JSON.  
- **🌐 Multi-Architecture Ready** — Cloud, on-prem, multi-tier, banking, zero-trust, and more.  
- **⚙️ GitHub Actions CI/CD** — Automatically generate, commit, and update diagrams on repo changes.  
- **💻 Clean CLI Interface** — `src/cli.py` provides reusable commands for local or automated use.  
- **📦 Artifact Management** — Upload, download, or share generated PNG diagrams.

---

## **⚡ Quick Start**

### **1. Clone & Install Dependencies**
```bash
git clone https://github.com/ird1natris/NetArch-AutoGen.git
cd NetArch‑AutoGen
pip install -r requirements.txt
sudo apt-get install graphviz
```

### 2. Generate Your First Diagram
```bash
python src/cli.py --config configs/sample_config.yaml --output outputs/sample_config.png
```
View output:
- macOS: ```open outputs/sample_config.png```
- Linux: ```xdg-open outputs/sample_config.png```

### 3. Automate Diagram Generation via GitHub Actions
- Push updates to ```configs/``` or ```src/```.
- GitHub Actions (via ```diagram.yml```) auto-generates and commits diagrams to ```outputs/```.
- Monitor progress in the Actions tab.

---

## 🗂️ Project Structure
```bash
NetArch‑AutoGen/
├─ configs/                  # YAML/JSON infrastructure definitions
├─ diagrams/                 # Diagram scripts for various architectures
│  ├─ diagram_generator.py
│  └─ multi_tier_cloud_app.py
├─ outputs/                  # Generated diagram PNG files
├─ src/                      # Core logic & CLI interface
│  ├─ cli.py
│  ├─ config_parser.py
│  └─ diagram_generator.py
├─ tests/                    # Unit tests
│  └─ test_config_parser.py
├─ .github/workflows/        # CI/CD pipelines
│  ├─ diagram.yml
│  ├─ github-actions-demo.yml
│  └─ list_nodes.yml
├─ requirements.txt
└─ README.md
```
---

## 📅 Roadmap

- ✅ CLI-driven diagram generation
- ✅ Multi-tier & config diagrams
- ✅ GitHub Actions automation
- 🔜 Streamlit / Flask UI           | Coming Soon ⏳
- 🔜 SVG/HTML export                | Coming Soon ⏳
- 🔜 Zero-Trust diagram support     | Planned 📅
- 🔜 Slack/MS Teams notifications   | Planned 📅

---

## 🎓 Use Cases

NetArch‑AutoGen is ideal for:

- ☁️ **Cloud Architects** — Visualize complex VPC and cloud setups.
- 🔌 **Network Engineers** — Document topologies with standardized diagrams.
- 🛡️ **Security Teams** — Visualize segmentation, firewall rules, and zero-trust architectures.
- 🎓 **Consultants & Academics** — Present custom network designs for clients or training.

---

## ✨ Why It Matters

- ⏳ **Saves Time** — No more manual diagramming.
- 🎯 **Consistency** — Diagrams match your config files 100%.
- 🔄 **Infrastructure-as-Code Ready** — CI/CD integrated.
- 📈 **Better Communication** — Clear visuals for all stakeholders.
- 🌍 **Scalable & Extensible** — Add new templates or architectures with ease.
