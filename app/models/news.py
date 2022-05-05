class Articles:
    '''
    News class to define News Objects
    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        
        self.author= author
        self.tilte = title
        self.description= description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
class source:
    def __init__(self,name,url):
        self.name= name
        self.url=url
        