
class Trie:
    data=set()
    @staticmethod
    def load():
        #loading all the cities to a static variable called data
        f=open('cities.txt','r',encoding='UTF-8')
        
        for i in f.read().split('\n'):
            try:
                Trie().data.add(i.split()[1])
            except:
                print(i)
        return Trie().data
    @staticmethod
    def insert(new):
        #inserting new city to the existing data
        Trie().data.add(new)
        return Trie().data
    @staticmethod
    def delete(city):
        #delete a city to the existing data
        if city in Trie().data:
            Trie().data.remove(city)
        return Trie().data
