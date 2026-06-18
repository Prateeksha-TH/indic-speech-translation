# 📚 How to Add Your App to GitHub

## Prerequisites

1. **GitHub Account** - Create one at https://github.com (free)
2. **Git Installed** - Download from https://git-scm.com/

Verify Git is installed by running in terminal:
```bash
git --version
```

---

## Step 1: Create a GitHub Repository

1. Go to https://github.com/new
2. Fill in:
   - **Repository name**: `indic-speech-translation` (or your preferred name)
   - **Description**: "Real-Time Indic Speech Translation with Whisper, NLLB-200, and TTS"
   - **Visibility**: Choose "Public" (anyone can see) or "Private" (only you)
3. **CHECK**: "Add a README file"
4. Click **"Create repository"**

✅ Your repository is now created!

---

## Step 2: Set Up Git Locally

Open terminal/command prompt in your project folder:

```bash
# Navigate to your project folder
cd path/to/your/indic-speech-translation
```

### Initialize Git

```bash
git init
git add .
git commit -m "Initial commit: Add Indic Speech Translation app"
```

---

## Step 3: Connect to GitHub

Copy the repository URL from GitHub (looks like: `https://github.com/YOUR_USERNAME/indic-speech-translation.git`)

Then run:

```bash
git remote add origin https://github.com/YOUR_USERNAME/indic-speech-translation.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

✅ Your code is now on GitHub!

---

## Step 4: Create a .gitignore File

Create a file named `.gitignore` in your project folder with this content:

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Models (they're large, don't commit them)
models/
*.pt
*.pth
*.bin

# Streamlit cache
.streamlit/

# Temporary files
*.tmp
*.temp
temp/
tmp/
*.log

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Audio files (if you don't want to commit them)
*.mp3
*.wav
*.ogg
*.flac
*.m4a
```

Add and commit it:

```bash
git add .gitignore
git commit -m "Add .gitignore file"
git push
```

---

## Step 5: Update Your README (Optional)

Replace the auto-generated README with the one we created. On GitHub:

1. Click the `README.md` file
2. Click the pencil icon to edit
3. Paste the content from our README.md
4. Commit changes

Or do it locally and push:

```bash
git add README.md
git commit -m "Update README with setup instructions"
git push
```

---

## Step 6: Add Additional Files (Optional)

Create a `.github/workflows/` folder for automated testing (advanced):

```bash
mkdir -p .github/workflows
```

---

## Common Git Commands

### Make Changes and Push

```bash
# See what changed
git status

# Add specific files
git add filename.py

# Or add everything
git add .

# Commit with message
git commit -m "Your message describing changes"

# Push to GitHub
git push
```

### Create a New Branch (for features)

```bash
git checkout -b feature/my-feature
# Make changes...
git add .
git commit -m "Add my feature"
git push -u origin feature/my-feature
```

### View Commit History

```bash
git log --oneline
```

---

## Enable GitHub Pages (Optional - for documentation)

1. Go to Settings → Pages
2. Select main branch
3. Choose a theme
4. Your README becomes a website!

---

## Deploy to Streamlit Cloud (Bonus!)

Once on GitHub:

1. Go to https://streamlit.io/cloud
2. Click "New app"
3. Connect your GitHub account
4. Select the repository
5. Set main file to: `indic_speech_translation.py`
6. Click Deploy

✅ Your app is now live on the web!

---

## Quick Reference Sheet

| Command | What it does |
|---------|------------|
| `git init` | Initialize Git in folder |
| `git add .` | Stage all files for commit |
| `git commit -m "msg"` | Create a commit with message |
| `git push` | Upload to GitHub |
| `git pull` | Download latest from GitHub |
| `git status` | See what changed |
| `git log` | View commit history |
| `git clone <url>` | Download a repository |

---

## Troubleshooting

### Error: "fatal: not a git repository"
```bash
git init
```

### Error: "Permission denied (publickey)"
Follow GitHub's SSH setup: https://docs.github.com/en/authentication/connecting-to-github-with-ssh

### Error: "rejected... the current branch is behind"
```bash
git pull origin main
```

### Want to change remote URL?
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/new-repo.git
```

---

## Folder Structure on GitHub

After pushing, your repository should look like:

```
indic-speech-translation/
├── README.md                      ← Project documentation
├── requirements.txt               ← Python dependencies
├── indic_speech_translation.py    ← Main app
├── .gitignore                     ← Ignored files
└── .git/                          ← Git folder (hidden)
```

---

## Next Steps

1. ✅ Push code to GitHub
2. 📝 Add a proper README
3. 🏷️ Add GitHub topics (tags): `indic-languages`, `speech-translation`, `ai`
4. ⭐ Get stars! Share your repo
5. 🚀 Deploy to Streamlit Cloud
6. 📦 Consider publishing on PyPI (advanced)

---

Happy coding! 🚀
