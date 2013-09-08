import feedparser


d = feedparser.parser("feed://feeds.huffingtionpost.com/HP/MostPopular")

print d['feed]['title']

