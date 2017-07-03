class Sorgu():
    def __init__(self, deger = None, sira = None):
        self.liste = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                      ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                      ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]
        
        if not deger and not sira:
          l = self.liste 
        else:
          l = [li for li in self.liste if deger == li[sira]]
          
        for i in l: 
          print(*i, sep=", ")
          
    @classmethod
    def isbn(cls, isbn):
      cls(isbn,0)
      
    @classmethod
    def yazar(cls,yazar):
      cls(yazar,1)
    
    @classmethod
    def eser(cls,eser):
      cls(eser,2)
    
    @classmethod
    def yayınevi(cls,yayınevi):
      cls(yayınevi,3)
      
print(Sorgu.yazar("Greenberg"))
    
