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