from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakeUserRepository:
    """A simple repository"""

    @classmethod
    def insert_user(cls):
        """something"""

        with DBConnectionHandler() as db_connection:
            try:
                new_user = Users(name="Programador", password="devops")
                db_connection.session.add(new_user)
                db_connection.session.commit()
            except db_connection:
                db_connection.session.rollback()
            finally:
                db_connection.session.close()