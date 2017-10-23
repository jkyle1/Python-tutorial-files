import urllib, htmllib, formatter

#use python 2
website = urllib.urlopen("http://www.bbc.co.uk")
data = website.read()
website.close()

format = formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
print(ptext.anchorlist)
