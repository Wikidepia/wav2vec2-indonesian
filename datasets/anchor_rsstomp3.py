import feedparser

o = open("mp3.txt", "a+")
for e in open("rss.txt"):
    try:
        feed = feedparser.parse(e.strip())
        entries = feed.entries

        for entry in entries:
            o.write(entry["links"][1]["href"])
        print(e.strip())
    except:
        pass
