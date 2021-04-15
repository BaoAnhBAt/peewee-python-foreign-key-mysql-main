from peewee import *

host='localhost'
db_name = 'test'
db_user='root'
db_pass=''

db = MySQLDatabase(db_name,host=host, user=db_user, passwd=db_pass)

class Role(Model):
    name = CharField()
    class Meta:
        database=db

class User(Model):
    name = CharField()
    age = IntegerField()
    role = ForeignKeyField(Role,backref='users') #=> auto create role_id
    #role.users se ra tat ca users
    class Meta:
        database=db



if __name__ =="__main__":
    Role.create_table()
    User.create_table()
    #B1 la tao
    # #create role
    # instance = Role(name = "admin")
    # instance.save()
    # role_id = Role.select().where(Role.name == 'admin')[0]

    # # #create admin
    # instance = User(name ="hung", age=20, role_id = role_id)
    # instance.save()

    # instance = User(name ="kiet", age=20, role_id = role_id)
    # instance.save()

    #B1 la select
    #select theo foreign key
    
    #lay tat ca user la admin
    role_admin = Role.select().where(Role.name == 'admin')[0]
    role_admin.users

    #lay role cua 1 user
    user_nghia = User.select().where(User.name == "nghia")[0]
    user_nghia.role
