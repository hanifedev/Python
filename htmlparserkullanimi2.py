from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_starttag(self,tag,attrs):
    print("Start tag : " , tag)
    for attr in attrs:
      print("attr : " , attr)
      
  def handle_endtag(self,tag):
    print("end tag : ", tag)
    
  def handle_data(self,data):
    print("data : " , data)
    
  def handle_comment(self, data):
    print("Comment : " , data)
    
parser = MyHTMLParser()
parser.feed('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
            '"http://www.w3.org/TR/html4/strict.dtd">')
print("*"*30)
parser.feed('<img src="python-logo.png" alt="The Python logo">')
print("*"*30)
parser.feed('<h1>Python</h1>')
print("*"*30)
parser.feed('<style type="text/css">#python { color: green }</style>')
print("*"*30)
parser.feed('<script type="text/javascript">'
             'alert("<strong>hello!</strong>");</script>')
print("*"*30)
parser.feed('<!-- a comment -->'
             '<!--[if IE 9]>IE-specific content<![endif]-->')
print("*"*30)
parser.feed('<p><a class=link href=#main>tag soup</p ></a>')
