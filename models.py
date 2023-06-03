from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from session import engine

Base = declarative_base(engine)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    second_name = Column(String(50), nullable=False)
    nickname = Column(String(50), nullable=False)

    def __str__(self):
        return self.firt_name  + " " + self.second_name


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))


    def __str__(self):
        return {self.title}

class PostKeywords(Base):
    __tablename__ = "postkeywords"


    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(ForeignKey("post.id"))
    keyword_id = Column(ForeignKey("keyword.id"))

    def __str__(self):
        return self.post_id

class Keyword(Base):
    __tablename__ = "keyword"

    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String(50), nullable=False)