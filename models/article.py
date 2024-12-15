from database.connection import get_db_connection
class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, 'title'):
            raise AttributeError("Title can't be changed after it has been instantiated!")
        # Must be a string and characters must be btn 5 and 50 characters
        if isinstance(title, str) and (len(title) >= 5 and len(title) <= 50):
            self._title = title
        else:
            raise ValueError(
                "Please input some data"
            )
        
    def contributing_authors(self):
        authors = {}
        list_of_authors = []
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1  
        for author in authors:
            if authors[author] >= 2:
                list_of_authors.append(author)   
        if (list_of_authors):
            return list_of_authors
        else:
            return None
        