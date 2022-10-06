# pylint: disable=E1101
from src.domain.models import Users as UserModel
from src.infra.config import DBConnectionHandler
from src.infra.entities import Users as UserEntity


class UserRepository:
    """Class to manage User Repository"""

    @classmethod  # especificando como método de classe
    def insert_user(cls, name: str, password: str) -> UserModel:
        """insert data in user entity
        :param - name: person name
               - password: user pasword
        :return - tuple with new user inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UserEntity(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return UserModel(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
            finally:
                db_connection.session.close()

        return None
