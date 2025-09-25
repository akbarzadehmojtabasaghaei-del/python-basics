# ⚙️ Chapter 1: Setting Up The Development Environment

Welcome to the first real step! A clean and correctly configured environment is the foundation for an efficient and error-free programming journey.

This guide details the essential tools and configuration steps required to work with the code in this repository.

---

## Step 1: Installing Python 🐍

All code in this repository is written in **Python 3**. It is crucial to have a recent version installed.

- **Action:**
  1. Visit the [official Python website](https://www.python.org/downloads/).
  2. Download the latest stable version for your operating system (Windows, macOS, or Linux).

- **⭐ Critical Tip for Windows Users:**
  During installation, make sure to check the box that says **"Add Python to PATH"**. This is a very important step that allows you to run Python from anywhere in your terminal.

- **Verification:**
  Open your terminal and run the following command. You should see a version number like `Python 3.10.x` or higher.
  ```bash
  python --version
---
## Step 2: Installing The Code Editor: VS Code 📝
We need a place to write our code. We'll use Visual Studio Code (VS Code), a powerful and popular free editor.

- **Action:**
  1. Download and install VS Code from the [official website](https://code.visualstudio.com/).

- **Essential Extensions:**
  To turn VS Code into a Python powerhouse, we need to install the official Microsoft extension.
  1. Open VS Code.
  2. Go to the Extensions view (the icon with four squares on the left sidebar, or press `Ctrl+Shift+X`).
  3. Search for **"Python Extension Pack"** published by Microsoft and click **Install**.
---
## Step 3: Setting Up Version Control with Git
This project is managed using Git. This is the standard for almost all modern software development.

- **Action:**
  1. Install Git on your system by following the guide on the [official Git website](https://git-scm.com/downloads).

- **Getting The Project Files:**
  To get a local copy of this project on your machine, you'll use the `git clone` command in your terminal.
  ```bash
  git clone https://github.com/akbarzadehmojtabasaghaei-del/python-basics.git
  ```

- **Opening in VS Code:**
  After cloning, open the project folder in VS Code with these commands:
  ```bash
  cd python-basics
  code .
  ```

