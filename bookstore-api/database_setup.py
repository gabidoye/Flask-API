import sys
import psycopg2
from flask_sqlalchemy import SQLAlchemy
# initialize our db
db = SQLAlchemy()

# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

# for configuration
from sqlalchemy import create_engine

# create declarative_base instance
Base = declarative_base()


# We will add classes here
class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))

    @property
    def serialize(self):
        return {
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'id': self.id,
        }


# creates a create_engine instance at the bottom of the file
engine = create_engine('postgresql://postgres:Oracle987@localhost:5432/bookstore')
Base.metadata.create_all(engine)
print("Table created")