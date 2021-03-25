import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    rotationPeriod = Column(Integer) 
    orbitalPeriod = Column(Integer) 
    diameter = Column(Integer) 
    gravity = Column(String(250))
    population = Column(Integer) 
    

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    height = Column(Integer) 
    mass = Column(Integer)
    hairColor = Column(Integer) 
    skinColor = Column(Integer)
    birthYear = Column(String(250))
    

class FavoritesPlanets(Base):
    __tablename__ = 'favoritesplanets'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey("user.id"))
    planetId = Column(Integer, ForeignKey("planets.id"))
    planets = relationship(Planets)
    user = relationship(User)
    
class FavoritesCharacter(Base):
    __tablename__ = 'favoritescharacter'
    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey("user.id"))
    characterId = Column(Integer, ForeignKey("characters.id"))
    characters = relationship(Characters)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')