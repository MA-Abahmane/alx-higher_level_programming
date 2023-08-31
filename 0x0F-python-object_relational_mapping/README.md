## SQLAlchemy ORM Cheat Sheet
- Import Statements

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

- Database Setup


# Create a database connection
engine = create_engine('sqlite:///my_database.db', echo=True)

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()

- Define a Model
python

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

- Create Tables
python

Base.metadata.create_all(engine)

- Create and Add Objects
python

new_user = User(name='John Doe', age=30)

session = Session()
session.add(new_user)
session.commit()

# Retrieve all users
all_users = session.query(User).all()

# Retrieve a specific user by ID
user = session.query(User).get(1)

# Filter users
filtered_users = session.query(User).filter_by(age=30).all()

# Advanced filtering
from sqlalchemy import and_, or_
filtered_users = session.query(User).filter(and_(User.age >= 25, User.age <= 40)).all()

# Update
user = session.query(User).get(1)
user.age = 31
session.commit()

# Delete
user = session.query(User).get(1)
session.delete(user)
session.commit()

- -Relationships
python

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    street = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='addresses')

User.addresses = relationship('Address', order_by=Address.id, back_populates='user')

# Inner join
joined_query = session.query(User, Address).filter(User.id == Address.user_id)

# Left join
from sqlalchemy.orm import joinedload
joined_query = session.query(User).options(joinedload(User.addresses))

- Commit and Rollback
python

try:
    session.commit()
except Exception as e:
    session.rollback()
    print("Error:", e)
finally:
    session.close()
