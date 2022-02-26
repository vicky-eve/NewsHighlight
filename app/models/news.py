class Source:
        """
        Articles class to define articles object
        """
def __init__(self, id, name, author, title, description, url):
        self.id =id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url

class Articles:
        """
        Articles class to define articles object
        """
def __init__(self, id, name, author, title, description, url, urlToImage, publishedAt, content):
        self.id = id
        self.name = name
        self.author = author
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content