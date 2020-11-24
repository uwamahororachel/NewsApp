class Sources:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,name,description,url,category,country,language):
        self.id =id
        self.name = name
       
        self.description = description
        self.language = language
        self.coutry=country
        self.url=url
        self.category=category

class Articles:
    '''
    Movie class to arcticles Objects
    '''

    def __init__(self,id,author,title,description,url,content,urlToImage,publishedAt):
        self.id =id
        self.author= author
        self.description = description
        self.title = title
        self.content=content
        self.url=url
        self.publishedAt=publishedAt
        self.urlToImage=urlToImage
               