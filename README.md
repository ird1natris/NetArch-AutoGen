# 🌐 NetArch-AutoGen – CI/CD-Based Network Diagram Generator

**NetArch-AutoGen** is a GitHub Actions–powered tool that auto-generates professional **network architecture diagrams** using Python and [Diagrams by Mingrammer](https://diagrams.mingrammer.com/). Designed with Infrastructure-as-Code principles, it enables seamless, repeatable diagram generation as part of your CI/CD pipeline.

---

## 🔧 Features

- 🔁 **CI/CD Integration** – Automatically generates diagrams via GitHub Actions on demand or push
- 📐 **Infrastructure as Code** – Define your architecture logically using Python
- 📤 **Downloadable Artifacts** – Output diagrams saved as PNGs and attached to each CI run
- 🌐 **Supports Hybrid Topologies** – Visualize public/private subnets, multiple tiers, and on-prem components

---

## 📌 Sample Output

![Network Diagram](assets/sample-output.png)

---

## 🚀 How It Works

1. Modify the architecture in `complex_network.py` to match your system.
2. Trigger the GitHub Action manually or on a push event.
3. Download the generated diagram (PNG) from the “Artifacts” section of the workflow run.

---

## 🗂️ Repository Structure

| Path                     | Description                                 |
|--------------------------|---------------------------------------------|
| `complex_network.py`     | Defines the network architecture diagram     |
| `.github/workflows/`     | GitHub Actions workflow for automation       |
| `requirements.txt`       | Python dependencies (`diagrams`, etc.)       |
| `assets/`                | Contains sample output previews              |

---

## 📥 Getting Started Locally

```bash
git clone https://github.com/yourname/NetArch-AutoGen.git
cd NetArch-AutoGen
pip install -r requirements.txt
python complex_network.py
