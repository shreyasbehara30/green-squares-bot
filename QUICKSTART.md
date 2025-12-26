# ⚡ Quick Start - Green Squares Bot v2.0

## 🚀 3-Minute Setup

### Step 1: Configure Repositories
```bash
# Edit config.json and add your repos
nano config.json
```

Add your repositories:
```json
{
  "repositories": [
    "your-username/repo-1",
    "your-username/repo-2"
  ],
  "github_username": "your-username"
}
```

### Step 2: Commit Changes
```bash
git add .
git commit -m "🚀 Upgrade to v2.0"
git push origin main
```

### Step 3: Done! ✅
- Bot runs daily at 10:00 AM UTC
- Selects one random repo
- Updates README.md
- Makes 1 meaningful commit

---

## 🎯 What Happens Next?

**Day 1:** Updates repo-1  
**Day 2:** Updates repo-2  
**Day 3:** Updates repo-1 again  
...and so on, randomly!

---

## 📖 Need More Details?

- 📘 **Full Guide:** [DEPLOYMENT_V2.md](DEPLOYMENT_V2.md)
- ⚙️ **Config Help:** [CONFIG_GUIDE.md](CONFIG_GUIDE.md)
- 📊 **Examples:** [EXAMPLE_UPDATES.md](EXAMPLE_UPDATES.md)
- 📋 **Summary:** [UPGRADE_SUMMARY.md](UPGRADE_SUMMARY.md)

---

## 🔍 Quick Test

```bash
# Run bot locally (optional)
python3 commit_v2.py

# Output shows:
# ✅ Selected repo
# ✅ Updated README
# ✅ Committed changes
```

---

## ✅ Checklist

- [ ] Updated `config.json` with my repos
- [ ] Committed and pushed changes
- [ ] GitHub Actions enabled
- [ ] First run successful

**That's it! Enjoy your green squares! 🟩🟩🟩**
