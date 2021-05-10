import feedparser

o = open("anchor-mp3.txt", "a+")
for e in open("anchor-rss.txt"):
    try:
        feed = feedparser.parse(e.strip())
        entries = feed.entries
        if feed.feed["language"] != "in": # Indonesian = in
            continue
        for entry in entries:
            o.write(entry["links"][1]["href"] + '\n')
        print(e.strip())
    except:
        pass
