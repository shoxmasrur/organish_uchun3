import pymysql 



# class Mysql:
#     def __init__(self):
#        self.connection()
#        self.CreateDB()
#        self.CreateTB()



#     def connection(self):
#         self.db=pymysql.connect(
#            host="localhost",
#            user="root",
#            password="1234"
#         )
#         self.c=self.db.cursor()
#     def CreateDB(self):
#        self.c.execute("create database if not exists uy_ish")
#        self.c.execute("Use uy_ish")


#     def CreateTB(self):
#         self.c.execute("""Create table if not exists company( name varchar(50), location varchar(50), capital varchar(50), employees_count int,
#                            establishedAt int, monthly_expenses int)""")
        


#     def insertTB(self):
#          self.c.execute("""insert into company values("Apple", "USA", "New_York", 100000, 2006, 5000000)""")
#          self.c.execute("""insert into company values("Samsung", "Korea", "Seul", 80000 , 2004, 300000)""")
#          self.c.execute("""insert into company values("Nike", "Canada", "Taronta", 70000 , 2010, 3000000)""")
#          self.c.execute("""insert into company values("sofia", "uzbekiston", "Toshkent", 5000 , 2020, 10000)""")
#          self.c.execute("""insert into company values("karzinka", "Rassia", "Mascov", 90000 , 2015, 1000000)""")
#          self.db.commit()

#     def firstQuery(self):
        
#        self.c.execute("""select * from company order by name""")
#        return self.c.fetchall()
#     def secendQuery(self):
#         self.c.execute("""select * from company order by monthly_expenses desc""")
#         return self.c.fetchall() 
#     def thirdQuery(self):
#         self.c.execute("""select * from company order by employees_count """)
#         return self.c.fetchone()
#     def fourthQuery(self):
#        self.c.execute("""select * from company where capital='Toshkent'""")
#        return  self.c.fetchall()
#     def fifthQuery(self):
#         self.c.execute("""select name, count(*) from company group by name""")
#         return self.c.fetchall()
#     def sixth(self):
#         self.c.execute("""select name, (2026-establishedAt)*monthly_expenses from company""")
#         return self.c.fetchall()
      

mysql=Mysql()
# 
# mysql.insertTB()

# 1-shart
# natija=mysql.firstQuery()
# for i in natija:
#    print(i)

# # 2-SHART
# natija=mysql.secendQuery()
# for i in natija:
#     print(i)

   #  3-shart
# natija=mysql.thirdQuery()
# print(natija)

# # 4-shart
# natija=mysql.fourthQuery()
# print(natija)

# 5- shart    Har bir manzilda nechtadan company joylashgani haqida ma'lumotlarni ekranga chiqaring.

# natija=mysql.fifthQuery()
# for i in natija:
#     print(i)

# 6-shart Kompaniya tashkil topgan yilidan shu  yilga qadar qancha harajat qilgani haqida ma'lumotni ekranga chiqaring.

# natija=mysql.sixth()
# for i in natija:
#     print(i)


# ---------------------------------------------------------------------------------------------------------------------------------




        

    


   









        












