# 🗂️ Streamlit Portfolio

An interactive developer portfolio built with **Streamlit** and managed using **uv**.  
It showcases my **Tech Stack**, **Tools**, and personal projects in a clean, responsive web app.

---

## 🧪 Features
- Hero section with social links
- Multi‑page layout (Home, About, Projects, Contact).
- Tech Stack and Tools displayed in card‑style squares.
- Responsive design using Streamlit’s `columns` and `containers`.

---

## ⚙️ Tech Used
- **Python**
- **uv**
- **Streeamlit**
---

## 📋 Project Structure
    streamlit-profile
    ├── pyproject.toml
    ├── README.md
    ├── resources
    │   ├── images
    │   │   ├── Gemini_Avatar_Image.png
    │   │   ├── Gemini_Generated_Image_bp8gnubp8gnubp8g.png
    │   │   ├── Gemini_Generated_Image_ppinwyppinwyppin.png
    │   │   ├── Gemini_Generated_Image_xawk3dxawk3dxawk.png
    │   │   └── icons
    │   │       ├── Angular.png
    │   │       ├── AWS.png
    │   │       ├── Docker.png
    │   │       ├── Flask.png
    │   │       ├── Git.png
    │   │       ├── Linux.png
    │   │       ├── Postman.png
    │   │       ├── python.png
    │   │       └── SQLite.png
    │   └── Jadeon_Miller_CV.PDF
    ├── src
    │   ├── main.py   ->   [Project Entry Point]
    │   └── pages
    │       ├── about.py
    │       ├── contact.py
    │       ├── home.py
    │       ├── projects.py
    │       
    └── uv.lock       ->   [Required Dependencies]

## 📦 Installation

This project uses **uv** for dependency management. You will need it installed on your system

Installation options for **uv**:
```bash
# Windows install:
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux/Mac install
curl -LsSf https://astral.sh/uv/install.sh | sh

#Verify install
uv --version
```
---

## 🧩 Project Setup

```bash
# Clone the repo
git clone git@github.com:JayPycentric/streamlit-profile.git

# Install project dependencies with uv
uv sync 

#Run streamlit application
uv run streamlit run src/main.py
```

