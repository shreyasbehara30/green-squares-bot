# 🚀 Green Squares Bot v2.0 - Deployment Guide

## ✨ What's New in v2.0

### Major Features
- **✅ Multi-Repository Support** - Manage multiple repos from a single bot
- **✅ Smart Random Selection** - One repo per run, never the same repo twice in a day
- **✅ Anti-Spam Guards** - Max 1 commit per repo per day
- **✅ Random Delays** - 5-40 minute delays before commits (disabled in CI)
- **✅ Meaningful README Updates** - No more dummy file spam
- **✅ Commit Message Rotation** - Professional, varied commit messages
- **✅ Ownership Verification** - Never touches repos you don't own
- **✅ Transparency Note** - Auto-adds bot disclosure to README

---

## 📦 Files Overview

| File | Purpose |
|------|---------|
| `commit_v2.py` | New bot engine with multi-repo support |
| `config.json` | Repository list and settings |
| `.github/workflows/activity.yml` | Updated workflow (runs once daily) |
| `CONFIG_GUIDE.md` | How to add more repos |
| `.repo_tracker.json` | Auto-generated tracking file (git-ignored) |

---

## 🔧 Step-by-Step Deployment

### 1️⃣ Update Configuration

Edit `config.json` to add your repositories:

```json
{
  "repositories": [
    "shreyasbehara30/green-squares-bot",
    "shreyasbehara30/my-other-repo"
  ],
  "github_username": "shreyasbehara30",
  ...
}
```

**Important:** Only add repos you own!

### 2️⃣ Update .gitignore

Add tracking file to `.gitignore`:

```bash
echo ".repo_tracker.json" >> .gitignore
```

### 3️⃣ Test Locally (Optional)

```bash
python3 commit_v2.py
```

This will:
- Select a random repo
- Wait 5-40 minutes (skipped in CI)
- Update README.md
- Commit and track the change

### 4️⃣ Commit and Push

```bash
git add .
git commit -m "🚀 Upgrade to v2.0 - Multi-repo support"
git push origin main
```

### 5️⃣ Verify GitHub Actions

- Go to **Actions** tab in your repo
- Wait for the daily scheduled run (10:00 AM UTC)
- Or trigger manually with "Run workflow"

---

## 🎯 How It Works

### Execution Flow

```
1. Load config.json
2. Select random repository (skip if already committed today)
3. Verify repository ownership
4. Apply random delay (5-40 min, disabled in CI)
5. Add transparency note (one-time)
6. Update README.md with dated entry
7. Commit with professional message
8. Track commit in .repo_tracker.json
9. Exit gracefully
```

### Anti-Spam Protection

- ✅ Max 1 commit per repository per day
- ✅ Skip if README already contains today's date
- ✅ Never commits to the same repo twice in one day
- ✅ Graceful exit when no action needed

### Safety Features

- ✅ Repository ownership verification
- ✅ Only commits to configured repos
- ✅ Never touches forks or other users' repos
- ✅ Meaningful, non-duplicate content
- ✅ Full transparency with bot disclosure

---

## 📊 Example README Diff

### Before:
```markdown
# My Project

Documentation here...
```

### After:
```markdown
# My Project

Documentation here...

## Daily Activity Log

- [2025-12-26] Documentation reviewed and updated

---

🤖 This repository is maintained with the help of an automated documentation bot.
```

---

## 💡 Example Commit Messages

The bot rotates through professional messages:

- `📝 docs: update documentation`
- `📚 chore: daily maintenance`
- `✨ docs: enhance README content`
- `🔧 chore: routine documentation update`
- `📖 docs: add activity notes`
- `🧹 chore: clean up documentation`
- `📄 docs: improve project documentation`
- `🌿 chore: keep repository fresh`

---

## 🔄 Adding More Repositories

1. Edit `config.json`
2. Add repo in format: `"username/repo-name"`
3. Ensure repo has a README.md
4. Commit and push changes
5. Bot will automatically include it in rotation

**Example:**
```json
{
  "repositories": [
    "shreyasbehara30/green-squares-bot",
    "shreyasbehara30/portfolio",
    "shreyasbehara30/learning-journal",
    "shreyasbehara30/side-project"
  ],
  ...
}
```

---

## 🛡️ GitHub ToS Compliance

✅ **Compliant Features:**
- Meaningful, readable commits
- Human-like activity patterns
- Transparent bot disclosure
- Respects rate limits
- No spam or abuse
- No fake contributions
- Only touches owned repositories

❌ **Forbidden (Not Implemented):**
- Mass commits
- Empty/no-op commits
- Committing to others' repos
- Auto-forking
- Contribution graph manipulation
- Violating GitHub ToS

---

## 🐛 Troubleshooting

### Bot not committing?

1. Check `.repo_tracker.json` - may already be committed today
2. Verify `config.json` has correct repo names
3. Ensure README.md exists in target repos
4. Check GitHub Actions logs

### README not updating?

- Ensure README doesn't already have today's date
- Check file permissions
- Verify git config is correct

### Multiple commits in one day?

- This shouldn't happen - check `.repo_tracker.json`
- If it does, the guard logic needs review

---

## 📝 Migration from v1

### What Changed?

| v1 | v2 |
|----|-----|
| Multiple commits to dummy files | One commit to README.md |
| 3 runs per day | 1 run per day |
| Single repo only | Multi-repo support |
| Random quotes to txt files | Meaningful README updates |
| No tracking | Persistent tracking |

### Keep v1 Running?

Both can coexist:
- `commit.py` - Old bot (optional, can be disabled)
- `commit_v2.py` - New bot (recommended)

**Recommendation:** Disable v1 workflow and use v2 exclusively.

---

## 🎉 Success Checklist

- [ ] `config.json` configured with your repos
- [ ] `.repo_tracker.json` added to `.gitignore`
- [ ] GitHub Actions workflow updated
- [ ] Tested locally (optional)
- [ ] Committed and pushed to GitHub
- [ ] GitHub Actions enabled
- [ ] First successful run verified

---

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Terms of Service](https://docs.github.com/en/site-policy/github-terms/github-terms-of-service)
- [Git Automation Best Practices](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)

---

## 🤝 Support

Questions? Issues? Improvements?

1. Check the logs in GitHub Actions
2. Review `CONFIG_GUIDE.md`
3. Verify your `config.json` syntax
4. Open an issue if needed

---

**Version:** 2.0  
**Last Updated:** December 26, 2025  
**Maintained by:** Green Squares Bot Team 🌿
