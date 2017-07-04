from html.parser import HTMLParser  
class MyHTMLParser(HTMLParser):
  def handle_starttag(self,tag,attrs):
    print("Karşılaşılan başlangıç tagi : ", tag)
    
  def handle_endtag(self,tag):
    print("Karşılaşılan bitiş tagi : " , tag)
  
  def handle_data(self,data):
    print("Karşılaşılan veri : " , data)
    
parser = MyHTMLParser()
parser.feed("<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>")
