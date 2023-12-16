import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    favorites = relationship("Favorites", back_populates="user")

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    average_height = Column(Integer, nullable=True)
    average_lifespan = Column(Integer, nullable=True)
    language = Column(String(250), nullable=True)
    image_url = Column(String(500), nullable=True)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship("Planet", back_populates="species")
    favorites = relationship("Favorites", back_populates="species")

    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500), nullable=True)
    population = Column(Integer, nullable=True)
    image_url = Column(String(500), nullable=True)
    characters = relationship("Characters", back_populates="homeworld")
    species = relationship("Species", back_populates="homeworld")
    favorites = relationship("Favorites", back_populates="planets")

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(500), nullable=True)
    height = Column(Integer, nullable=True)
    species_id = Column(Integer, ForeignKey('species.id'))
    image_url = Column(String(500), nullable=True)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship("Planet", back_populates="characters")
    favorites = relationship("Favorites", back_populates="characters")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))
    species_id = Column(Integer, ForeignKey('species.id'))
    user = relationship("Users", back_populates="favorites")
    planet = relationship("Planets", back_populates="favorites")
    character = relationship("Characters", back_populates="favorites")
    species = relationship("Species", back_populates="favorites")


render_er(Base, 'diagram.png')
