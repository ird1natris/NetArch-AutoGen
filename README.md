# 🌐 Network Diagram Generator (Infrastructure as Code)

A GitHub Actions-powered solution for generating professional network architecture diagrams using Python and [Diagrams by Mingrammer](https://diagrams.mingrammer.com/).

---

## 🔧 Features

- Auto-generates network architecture diagrams via CI/CD
- Uses Infrastructure as Code approach
- Artifacts downloadable via GitHub Actions
- Includes public/private subnets, tiers, and hybrid on-prem setup

---

## 📌 Sample Output

![Network Diagram](assets/sample-output.png)

---

## 🚀 How It Works

1. Edit the `complex_network.py` to model your architecture.
2. Trigger the GitHub Action manually from the Actions tab.
3. Download the generated PNG from the “Artifacts” section.

---

## 🗂️ Repository Structure

| File/Folder            | Purpose                              |
|------------------------|--------------------------------------|
| `complex_network.py`   | The Python diagram definition        |
| `.github/workflows/`   | GitHub Actions automation            |
| `requirements.txt`     | Python dependencies (`diagrams`)     |
| `assets/`              | Sample output preview                |

---

## 📥 Getting Started Locally

```bash
git clone https://github.com/yourname/network-diagram-generator.git
cd network-diagram-generator
pip install -r requirements.txt
python complex_network.py
