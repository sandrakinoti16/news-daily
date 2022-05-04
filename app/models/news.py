class Articles:
    '''
    News class to define News Objects
    '''

    def __init__(self,author,title,description,url,urltoImage,publishedAt,content):
        
        self.author= author
        self.tilte = title
        self.description= description
        self.url = url
        self.urlToImage = urltoImage
        self.publishedAt = publishedAt
        self.content = content
        