from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :",tag)
        if len(attrs)!=0:
            for i in attrs:
                att,val=i[0],i[1]
                print("->",att,">",val)
    def handle_endtag(self, tag):
        print("End   :",tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :",tag)
        if len(attrs)!=0:
            for i in attrs:
                att,val=i[0],i[1]
                print("->",att,">",val)
parse= MyHTMLParser()
html=" "
for i in range(int(input())):
    html=html+input()
parse.feed(html)
    