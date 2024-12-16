
from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        if isinstance(id, int):
            self._id = id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
         # If the input is not a string, it should raise an error
        if isinstance(new_name, str):
        # using ValueError instead of print since it stops the execution of the program if there is an error in that input.
        # If the input's length isn't between 2 and 16 chars, raise an error
            if len(new_name) >= 2 and len(new_name) <= 16:
                 self._name = new_name
            else:
                raise ValueError("name MUST be btn 2 and 16 characters")
        else:
            TypeError("name MUST be a string")
    
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        # If the input is not a string, it should raise an error
        if isinstance(new_category, str):
            # If the input is empty(less than one character) it should raise an error
            if len(new_category) > 0:
                 self._category = new_category
            else:
                raise ValueError("Please input a category")
        # using ValueError instead of print since it stops the execution of the program if there is an error in that input.
        else:
            TypeError("Category MUST be a string!!")

    def articles(self):
        from models.article import Article
        CONN = get_db_connection()
        CURSOR = CONN.cursor()

        sql = """
            SELECT ar.*
            FROM articles ar
            INNER JOIN magazines m ON ar.magazine = m.id
            WHERE m.id = ?
        """

        CURSOR.execute(sql, (self.id,))
        article_data = CURSOR.fetchall()

        articles = []
        for row in article_data:
            articles.append(Article(*row))

        return articles
    
    def contributors(self):
        from models.author import Author
        conn = get_db_connection()
        CURSOR = conn.cursor()

        sql = """
            SELECT DISTINCT a.*
            FROM authors a
            INNER JOIN articles ar ON ar.author = a.id
            INNER JOIN magazines m on ar.magazine = m.id
            WHERE m.id = ?
        """

        CURSOR.execute(sql, (self.id,))
        author_data = CURSOR.fetchall()

        authors = []
        for row in author_data:
            authors.append(Author(*row))
        return authors
    
    def article_titles(self):
        conn = get_db_connection()
        CURSOR = conn.cursor()
        
        sql = """
            SELECT ar.title
            FROM articles ar
            INNER JOIN magazines m ON ar.magazine = m.id
            WHERE m.id = ?
        """

        CURSOR.execute(sql, (self.id,))
        article_data = CURSOR.fetchall()

        if not article_data:
            return None

        titles = [row[0] for row in article_data]
        return titles

    def contributing_authors(self):
        from models.author import Author
        conn = get_db_connection()
        CURSOR = conn.cursor()
        
        sql = """
            SELECT DISTINCT a.*
            FROM authors a
            INNER JOIN articles ar ON ar.author = a.id
            INNER JOIN magazines m on ar.magazine = m.id
            WHERE m.id = ?
            GROUP BY a.id
            HAVING COUNT(ar.id) > 2
        """

        CURSOR.execute(sql, (self.id,))
        author_data = CURSOR.fetchall()

        if not author_data:
            return None

        authors = []
        for row in author_data:
            authors.append(Author(*row)) 

        return authors
    
    @classmethod
    def find_by_id(cls, id):
        conn = get_db_connection()
        CURSOR = conn.cursor()
        sql = """
            SELECT * FROM magazines
            WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        if row:
            return Magazine(*row)
        return None
    

    def save(self):
        conn = get_db_connection()
        CURSOR = conn.cursor()
        sql = """
            INSERT INTO magazines (name, category)
            VALUES (?,?)
        """
        CURSOR.execute(sql, (self.name, self.category))
        conn.commit()
        
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    