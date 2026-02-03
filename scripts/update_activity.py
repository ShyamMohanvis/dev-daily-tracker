from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("activity_log.md", "a", encoding="utf-8") as f:
    f.write(f"\n- Activity updated on {now}")
