from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model



# def this -> ProductScrapeEvent.objects().filter(asin="AMZNIDNUMBER")

# not this -> Product.objects().filter(title="Mark 1")


data = {
    "author" : "mochi vani",
    "title"  : "Elon Musk offers to buy Twitter",
    "description" : "Elon Musk has stepped up the strangest back and forth in tech by offering to buy Twitter outright. As revealed by a new SEC filing, the Tesla and SpaceX chief is willing to pay $54.20 per share for the social network, which would to a $43.4 billion bid to inc…",
    "content" : "Elon Musk has stepped up the strangest back and forth in tech by offering to buy Twitter outright.\r\nAs revealed by a new SEC filing, the Tesla and SpaceX chief is willing to pay $54.20"
}



class News(Model):
    __keyspace__ = "NewsApi"
    uuid = columns.UUID(primary_key=True) 
    source = columns.txt()


class News_Articles(Model):
    __keyspace__ = "NewsApi" 
    author = columns.txt()
    title  = columns.txt()
    description = columns.txt()
    url = columns.txt()
    urlImage = columns.txt()
    published = columns.txt()
    content = columns.Txt()






