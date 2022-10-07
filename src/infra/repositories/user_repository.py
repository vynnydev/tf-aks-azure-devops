# pylint: disable=E1101
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.domain.models import Users as UsersModel
from src.infra.config import DBConnectionHandler
from src.data.interfaces.repositories import UserRepositoryInterface
from src.infra.entities import Users as UsersEntity


class UserRepository(UserRepositoryInterface):
    """Class to manage User Repository"""

    @classmethod  # especificando como método de classe
    def insert_user(cls, name: str, password: str) -> UsersModel:
        """insert data in user entity
        :param - name: person name
               - password: user pasword
        :return - tuple with new user inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersEntity(name=name, password=password)
                db_connection.session.add(new_user)
                db_connection.session.commit()

                return UsersModel(
                    id=new_user.id, name=new_user.name, password=new_user.password
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[UsersModel]:
        """
        Select data in user entity by id and/or name
        :param - user_id: Id of the registry
               - name: User name
        :return - List with Users selected
        """

        try:
            query_data = None

            if user_id and not name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersEntity)
                        .filter_by(id=user_id)
                        .one()
                    )
                    query_data = [data]

            elif not user_id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersEntity)
                        .filter_by(name=name)
                        .one()
                    )
                    query_data = [data]

            elif user_id and name:

                with DBConnectionHandler() as db_connection:
                    data = (
                        db_connection.session.query(UsersEntity)
                        .filter_by(id=user_id, name=name)
                        .one()
                    )
                    query_data = [data]

            return query_data

        except NoResultFound:
            return []
        except:
            db_connection.session.rollback()
        finally:
            db_connection.session.close()

        return None
