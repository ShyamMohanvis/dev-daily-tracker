import random
from datetime import datetime

today = datetime.now()
day_name = today.strftime("%A")
date_str = today.strftime("%Y-%m-%d")
is_weekend = day_name in ["Saturday", "Sunday"]

domains = {
    "AI": [{
        "topic": "Retrieval-Augmented Generation (RAG)",
        "difficulty": "Intermediate",
        "short": "RAG improves LLM accuracy by retrieving documents before generation.",
        "deep": "RAG combines retrieval systems with language models to ground responses in external knowledge and reduce hallucinations.",
        "link": "https://www.pinecone.io/learn/retrieval-augmented-generation/"
    }],
    "DSA": [{
        "topic": "Binary Search on Answer",
        "difficulty": "Intermediate",
        "short": "Binary Search on Answer applies binary search on the solution space.",
        "deep": "This technique is used in optimization problems where feasibility is monotonic.",
        "link": "https://leetcode.com/problems/koko-eating-bananas/"
    }],
    "System Design": [{
        "topic": "Load Balancing",
        "difficulty": "Beginner",
        "short": "Load balancing distributes traffic across servers.",
        "deep": "It improves availability and scalability by preventing server overload.",
        "link": "https://www.geeksforgeeks.org/load-balancing-in-system-design/"
    }]
}

domain = random.choice(list(domains.keys()))
selected = random.choice(domains[domain])
explanation = selected["deep"] if is_weekend else selected["short"]

with open("learning_log.md", "a", encoding="utf-8") as f:
    f.write(f"\n## {date_str} — [{domain}] {selected['topic']}\n")
    f.write(f"**Difficulty:** {selected['difficulty']}\n\n")
    f.write(explanation + "\n")
    f.write(f"🔗 Reference: {selected['link']}\n")

linkedin_post = f"""
🚀 Daily Learning Update

Today I explored **{selected['topic']}** ({domain}).

{explanation}

#LearningInPublic #AI #DSA #SystemDesign
"""

open("linkedin_post.md", "w", encoding="utf-8").write(linkedin_post.strip())

image_prompt = f"""
Create a clean LinkedIn post image.
Topic: {selected['topic']}
Domain: {domain}
Style: Minimal, professional, flat illustration.
"""

open("linkedin_image_prompt.txt", "w", encoding="utf-8").write(image_prompt.strip())

if day_name == "Sunday":
    with open("weekly_summary.md", "a", encoding="utf-8") as f:
        f.write(f"\n## Week of {date_str}\n")
        f.write("- [ ] Review learning log for this week\n")
        f.write("- [ ] Identify key takeaways\n")
        f.write("- [ ] Plan next week's focus\n")
