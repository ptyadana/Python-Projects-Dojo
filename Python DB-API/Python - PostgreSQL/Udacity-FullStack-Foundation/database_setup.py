#1) Configuration File
import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()


#2) Class - Restaurant
class Restaurant(Base):
    
    #3)Table
    __tablename__ = 'restaurant'

    #4)Mapper
    id = Column(Integer,primary_key=True)
    name = Column(String(80),nullable=False)


#2) Class - MenuItem
class MenuItem(Base):

    #3)Table
    __tablename__ = 'menu_item'

    #4)Mapper
    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))

    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)


    #We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
       
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'price'         : self.price,
           'course'         : self.course,
       }

#1) End of Configuration File
##### insert at the end of file #####
engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)