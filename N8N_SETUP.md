# 🔧 n8n Setup Guide for Dev Daily Tracker

This guide will help you set up and run the dev-daily-tracker automation using n8n instead of GitHub Actions.

---

## 📋 Prerequisites

### Required Software

1. **n8n** (choose one option):
   - [n8n Desktop App](https://n8n.io/download/) (recommended for beginners)
   - Self-hosted via Docker: `docker run -it --rm --name n8n -p 5678:5678 n8nio/n8n`
   - npm installation: `npm install n8n -g`

2. **Python 3.9+**
   - Verify: `python --version`
   - Must be accessible from command line

3. **Git**
   - Verify: `git --version`
   - GitHub repository with write access

---

## 🚀 Quick Start

### Step 1: Install n8n

**Option A: Desktop App (Easiest)**
```bash
# Download from https://n8n.io/download/
# Install and launch the application
```

**Option B: Docker**
```bash
docker run -it --rm --name n8n -p 5678:5678 -v ~/.n8n:/home/node/.n8n n8nio/n8n
```

**Option C: npm**
```bash
npm install n8n -g
n8n start
```

Access n8n at: `http://localhost:5678`

---

### Step 2: Import the Workflow

1. Open n8n in your browser
2. Click **"Workflows"** in the sidebar
3. Click **"Import from File"** or **"+"** → **"Import"**
4. Select `n8n_workflow.json` from your repository
5. The workflow "Dev Daily Tracker Automation" will appear

---

### Step 3: Configure Repository Path

**Update the workflow variable:**

1. Open the imported workflow
2. Find the **"Set Repository Path"** node (first node after trigger)
3. Click on it to edit
4. Update the `repoPath` value to your local repository path:

   **Windows:**
   ```
   c:\Users\SHYAM MOHAN\Desktop\sdxfcgvhj\dev-daily-tracker
   ```

   **Linux/Mac:**
   ```
   /home/username/projects/dev-daily-tracker
   ```

**Alternative: Use Environment Variable**

Set `DEV_TRACKER_REPO_PATH` in your system or n8n settings:

```bash
# Windows (PowerShell)
$env:DEV_TRACKER_REPO_PATH = "c:\Users\SHYAM MOHAN\Desktop\sdxfcgvhj\dev-daily-tracker"

# Linux/Mac
export DEV_TRACKER_REPO_PATH="/home/username/projects/dev-daily-tracker"
```

---

### Step 4: Test the Workflow

1. Click **"Execute Workflow"** button in the top right
2. Watch the nodes execute in real-time
3. Green checkmarks ✅ = success
4. Red error indicators ❌ = check the error message

**Expected Result:**
- All nodes turn green
- Repository files are updated
- New commit appears in Git history
- Success message displayed

---

### Step 5: Activate Scheduled Execution

1. Toggle the **"Active"** switch at the top of the workflow (turn it ON)
2. The workflow will now run automatically every day at 9:00 AM UTC
3. Check the **"Executions"** tab to view past runs

---

## 🔐 Git Authentication (If Needed)

If your repository requires authentication for pushing:

### Option 1: SSH Keys (Recommended)

1. Generate SSH key (if not already done):
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. Add public key to GitHub:
   - Go to GitHub → Settings → SSH and GPG keys
   - Add new SSH key
   - Paste contents of `~/.ssh/id_ed25519.pub`

3. Update repository remote to use SSH:
   ```bash
   cd /path/to/dev-daily-tracker
   git remote set-url origin git@github.com:ShyamMohanvis/dev-daily-tracker.git
   ```

### Option 2: Personal Access Token

1. Create GitHub token:
   - Go to GitHub → Settings → Developer settings → Personal access tokens
   - Generate new token (classic)
   - Select scopes: `repo` (full control)

2. Update Git credentials:
   ```bash
   git config credential.helper store
   git pull  # Will prompt for username and token
   ```

---

## ⚙️ Workflow Configuration Options

### Change Schedule

Edit the **"Daily Schedule"** node:

```javascript
// Current: Daily at 9:00 AM UTC
0 9 * * *

// Examples:
0 */12 * * *     // Every 12 hours
0 9 * * 1-5      // Weekdays only at 9 AM
30 8 * * *       // Daily at 8:30 AM
```

### Adjust Working Directory

If scripts fail to find files, ensure `repoPath` is set correctly in the **"Set Repository Path"** node.

### Modify Script Execution

Each Execute Command node can be customized:

```javascript
// Current format:
cd {{ $json.repoPath }} && python scripts/update_learning.py

// With virtual environment:
cd {{ $json.repoPath }} && source venv/bin/activate && python scripts/update_learning.py

// With specific Python version:
cd {{ $json.repoPath }} && python3.11 scripts/update_learning.py
```

---

## 🐛 Troubleshooting

### Issue: "Python not found"

**Solution:**
- Verify Python is in PATH: `python --version`
- Update node to use absolute path: `C:\Python311\python.exe scripts/update_learning.py`

---

### Issue: "Git command failed"

**Solution:**
- Check if Git is installed: `git --version`
- Verify you're in a Git repository: `git status`
- Ensure remote is configured: `git remote -v`

---

### Issue: "Permission denied (publickey)"

**Solution:**
- Set up SSH keys (see Git Authentication section above)
- Or use HTTPS with Personal Access Token

---

### Issue: "No changes to commit"

**Solution:**
- This is expected behavior if scripts don't modify files
- Check if entry for today already exists (idempotency check)
- Scripts skip execution if data already exists for the date

---

### Issue: "Workflow not running on schedule"

**Solution:**
- Ensure workflow is **ACTIVE** (toggle switch is ON)
- Check execution history for errors
- Verify cron expression is correct
- Ensure n8n is running (desktop app or server)

---

## 📊 Monitoring

### View Execution History

1. Click **"Executions"** in the sidebar
2. Select the workflow
3. See all past executions with timestamps
4. Click any execution to view detailed logs

### Enable Notifications

Add a notification node to alert on failures:

1. Add **"Send Email"** or **"Discord"** node after error
2. Connect from error outputs of Execute Command nodes
3. Configure with your notification credentials

---

## 🔄 Workflow Nodes Explained

| Node Name | Purpose | Command |
|-----------|---------|---------|
| **Daily Schedule** | Triggers workflow at 9:00 AM UTC daily | Cron trigger |
| **Set Repository Path** | Sets working directory variable | Sets `repoPath` |
| **Git Pull Latest** | Syncs with remote repository | `git pull origin main` |
| **Run Activity Tracker** | Logs daily activity timestamp | `python scripts/update_activity.py` |
| **Run Learning Update** | Generates daily learning entry | `python scripts/update_learning.py` |
| **Is Sunday?** | Checks if today is Sunday | Day check condition |
| **Run Weekly Summary** | Generates weekly summary (Sunday only) | `python scripts/weekly_summary.py` |
| **Merge Paths** | Combines Sunday/non-Sunday branches | Merge node |
| **Check Git Status** | Checks if files were modified | `git status --porcelain` |
| **Has Changes?** | Determines if commit is needed | String not empty check |
| **Git Add All** | Stages all changes | `git add .` |
| **Git Commit & Push** | Commits and pushes to GitHub | `git commit && git push` |
| **Success Nodes** | Log completion status | Returns success message |

---

## 🎯 Best Practices

1. **Test First**: Always test manually before activating schedule
2. **Check Logs**: Review execution logs regularly for errors
3. **Backup Data**: Keep backups of your learning logs
4. **Monitor Resources**: Ensure n8n has enough system resources
5. **Update Scripts**: Keep Python scripts in sync with workflow

---

## 🔗 Resources

- [n8n Documentation](https://docs.n8n.io/)
- [n8n Community Forum](https://community.n8n.io/)
- [Cron Expression Generator](https://crontab.guru/)
- [GitHub: dev-daily-tracker](https://github.com/ShyamMohanvis/dev-daily-tracker)

---

## 💡 Tips

- **Use n8n Desktop App** for easiest setup (no server management)
- **Set environment variables** for easier path management
- **Enable error notifications** to catch failures quickly
- **Test schedule changes** before deploying
- **Keep n8n updated** for latest features and fixes

---

## 🆘 Need Help?

If you encounter issues:

1. Check the **Executions** tab for error details
2. Review this troubleshooting guide
3. Consult [n8n documentation](https://docs.n8n.io/)
4. Ask in [n8n community forum](https://community.n8n.io/)

---

**Ready to automate? Import the workflow and click Execute! 🚀**
