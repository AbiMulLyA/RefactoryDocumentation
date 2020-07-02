# mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
# PyMySql
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)

engine = create_engine("mysql+pymysql://root:@localhost/demo", echo = False)
Session = sessionmaker(bind=engine)
session = Session()
# tambah data user
# user = User(name="ami")
# user.id = 1
# user.name = "budi"
# session.add(user)
# session.commit()

# update data table
# user = User()
# user_update = session.query(User).filter_by(id=2).first()
# user_update.name = "ini ganti ga"

# select data table
user_show = session.query(User).first()
# for a in user_show:
#     print(a.name)
# print(user_show.name)
# print(user_show)
test = session.query(User).get(2)
print(test.name)
session.delete(test)

session.commit()
session.close()