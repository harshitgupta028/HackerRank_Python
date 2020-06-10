from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if len(attrs)!=0:
            for i in attrs:
                print("->",i[0],">",i[1])
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if len(attrs)!=0:
            for i in attrs:
                print("->",i[0],">",i[1])
parse= MyHTMLParser()
html=" "

for i in range(int(input())):
    html=html+input()
parse.feed(html)
    