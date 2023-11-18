from db.config import DB


class User(DB):
    def __init__(self,
                 id: int = None,
                 ):
        pass

    def insert(self):
        query = """
            insert into users(fullname, user_id, role, phone_number)
            values (%s, %s, %s, %s)
        """
        params = (self.fullname, self.user_id, self.role, self.phone_number)
        self.cur.execute(query, params)
        self.con.commit()


class Category(DB):
    def __init__(self):
        pass

    def select(self):
        super().select()
