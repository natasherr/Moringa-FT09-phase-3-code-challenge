#Import the database
from database.connection import get_db_connection

class Author:
    all = {}

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'
    
    # getter
    @property
    def id(self):
        return self._id
    
    # setter
    @id.setter
    def id(self, id):
        # The id must be of integer type
        if isinstance(id, int):
            self._id = id


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if hasattr(self, 'name'):
            raise AttributeError("Name cannot be changed after it has been instantiated!")
        else:
            if isinstance(new_name, str):
                # Name must be longer than 0 characters
                if len(new_name) > 0:
                    self._name = new_name

    def articles(self):
        from models.article import Article
        conn = get_db_connection()
        CURSOR = conn.cursor()
        
        sql = """
            SELECT ar.*
            FROM articles ar
            INNER JOIN authors a ON ar.author = a.id
            WHERE a.id = ?
        """

        CURSOR.execute(sql, (self.id,))
        article_data = CURSOR.fetchall()

        articles = []
        for row in article_data:
            articles.append(Article(*row))
        return articles
    
    
    

    def magazines(self):
        from models.magazine import Magazine
        conn = get_db_connection()
        CURSOR = conn.cursor()
        
        sql = """
            SELECT DISTINCT m.*
            FROM magazines m
            INNER JOIN articles ar ON ar.magazine = m.id
            INNER JOIN authors a ON ar.author = a.id
            WHERE a.id = ?
        """

        CURSOR.execute(sql, (self.id,))
        magazine_data = CURSOR.fetchall()

        magazines = []
        for row in magazine_data:
            magazines.append(Magazine(*row))
        return magazines
    
