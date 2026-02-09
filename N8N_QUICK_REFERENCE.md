# 📋 n8n Quick Reference

Quick commands and tips for running the dev-daily-tracker n8n workflow.

---

## 🚀 Quick Start Commands

### Import Workflow
```bash
# 1. Open n8n at http://localhost:5678
# 2. Click "Import from File"
# 3. Select: n8n_workflow.json
```

### Set Repository Path
```javascript
// In "Set Repository Path" node:
c:\Users\SHYAM MOHAN\Desktop\sdxfcgvhj\dev-daily-tracker
```

### Test Execution
```
Click "Execute Workflow" button → Watch nodes turn green ✅
```

### Activate Schedule
```
Toggle "Active" switch → Workflow runs daily at 9:00 AM UTC
```

---

## 📊 Workflow Flow

```
Schedule (9:00 AM UTC)
    ↓
Set Repo Path
    ↓
Git Pull
    ↓
Update Activity Script
    ↓
Update Learning Script
    ↓
Is Sunday? ─── Yes ──→ Weekly Summary ─┐
    │                                    │
    No ─────────────────────────────────┘
    ↓
Merge Paths
    ↓
Check Git Status
    ↓
Has Changes? ─── Yes ──→ Git Add → Commit & Push → Success ✅
    │
    No ──→ Success (No Changes) ✅
```

---

## 🔧 Common Modifications

### Change Schedule Time
```javascript
// Current: 0 9 * * * (9:00 AM UTC)
// 8:00 AM UTC: 0 8 * * *
// Twice daily: 0 9,18 * * *
// Weekdays only: 0 9 * * 1-5
```

### Modify Repository Path
```javascript
// Windows:
c:\Users\SHYAM MOHAN\Desktop\sdxfcgvhj\dev-daily-tracker

// Linux/Mac:
/home/username/projects/dev-daily-tracker
```

### Add Python Virtual Environment
```bash
# In Execute Command nodes:
cd {{ $json.repoPath }} && source venv/bin/activate && python scripts/update_learning.py
```

---

## ⚡ Troubleshooting Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| Python not found | Use full path: `C:\Python311\python.exe` |
| Git auth failed | Set up SSH keys or use Personal Access Token |
| Workflow not scheduling | Check "Active" toggle is ON |
| No changes to commit | Expected - scripts already ran today |
| Scripts fail | Check `repoPath` is set correctly |

---

## 📁 Files Created

| File | Purpose |
|------|---------|
| `n8n_workflow.json` | Import into n8n |
| `N8N_SETUP.md` | Detailed setup guide |
| `N8N_QUICK_REFERENCE.md` | This file |

---

## 🎯 Checklist

- [ ] Install n8n (Desktop App or Docker)
- [ ] Import `n8n_workflow.json`
- [ ] Update repository path in workflow
- [ ] Click "Execute Workflow" to test
- [ ] Verify all nodes turn green ✅
- [ ] Check Git commit was created
- [ ] Toggle "Active" switch ON
- [ ] Verify schedule shows in Executions tab

---

## 🔗 Quick Links

- n8n Web UI: http://localhost:5678
- Executions: http://localhost:5678/executions
- Workflows: http://localhost:5678/workflows
- [Cron Generator](https://crontab.guru/)
- [n8n Docs](https://docs.n8n.io/)

---

**Ready? Import → Configure → Execute → Activate! 🚀**
