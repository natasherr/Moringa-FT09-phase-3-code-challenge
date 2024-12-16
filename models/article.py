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
        
    def author(self):
        from models.author import Author
        conn = get_db_connection()
        CURSOR = conn.cursor()
        
        sql = """
            SELECT a.*
            FROM authors a
            INNER JOIN articles ar ON ar.author = a.id
            WHERE ar.id = ?
        """
        CURSOR.execute(sql, (self.id))
        author_data = CURSOR.fetchone()

        if author_data:
            return Author(*author_data)
        else:
            return None

    def magazine(self):
        from models.magazine import Magazine
        conn = get_db_connection()
        CURSOR = conn.cursor()
       
        sql = """
            SELECT m.*
            FROM magazines m
            INNER JOIN articles ar ON ar.magazine = m.id
            WHERE ar.id = ?
        """
        CURSOR.execute(sql, (self.id))
        magazine_data = CURSOR.fetchone()

        if magazine_data:
            return Magazine(*magazine_data)
        else:
            return None

        