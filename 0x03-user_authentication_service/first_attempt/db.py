#!/bin/bash/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> str:
        """
        Adds a new user to the database

        Args:
        email (str): The email of the user.
        hashed_password (str): The hased password of the user

        Returns:
        User: The created User Object
        """
        try:
            if  not email or not hashed_password:
                return
            # Create a new User object
            new_user = User(email=email, hashed_password=hashed_password)
            # Add the user to the session
            self._session.add(new_user)
            # Commit the session to persist the user in the databse
            self._session.commit()
            # Return the new user object
            return new_user
        except Exception as e:
            self._session.rollback()
            raise e
