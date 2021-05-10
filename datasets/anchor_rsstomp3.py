import feedparser
import json
import html2text

fout = open("anchor-mp3.jsonl", "a+")
for url in open("anchor-rss.txt"):
    try:
        feed = feedparser.parse(url.strip())
        entries = feed.entries
        if feed.feed["language"] != "in":  # Indonesian = in
            continue
        data = {
            "title": feed.feed["title"],
            "description": feed.feed["description"],
            "episodes": [],
        }
        for entry in entries:
            data["episodes"].append(
                (
                    {
                        "title": entry["title"],
                        "description": html2text.html2text(entry["description"]),
                        "link": entry["link"],
                        "audio_url": entry["links"][1]["href"],
                    }
                )
            )
        fout.write(json.dumps(data) + "\n")
        print(url.strip())
    except:
        pass
