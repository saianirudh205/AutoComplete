
class Trie:
    data=set()
    @staticmethod
    def load():
        f=open('cities.txt','r',encoding='UTF-8')
        
        for i in f.read().split('\n'):
            try:
                Trie().data.add(i.split()[1])
            except:
                print(i)
        return Trie().data
    @staticmethod
    def insert(new):
        Trie().data.add(new)
        return Trie().data
    @staticmethod
    def delete(city):
        if city in Trie().data:
            Trie().data.remove(city)
        return Trie().data
