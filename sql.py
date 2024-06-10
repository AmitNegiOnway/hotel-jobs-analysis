import mysql.connector
from mysql.connector import Error

class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='12345',
                database='thailand'
            )
            self.mycursor = self.conn.cursor()
            print('Cursor initialized successfully')  # Add this line
        except Exception as e:
            print('Error initializing cursor:', e)  # Add this line




    def fetch_resort(self):
        name=[]
        self.mycursor.execute("""
        select distinct(Resorts_name) from thailand.thai
        """)
        data=self.mycursor.fetchall()

        for item in data:
            name.append(item[0])
        return name


    def show_fetch_resort(self, resort):
        name=[]
        rating=[]
        review=[]

        self.mycursor.execute("""
        select price,Resorts_name,Rating,total_review from thailand.thai
        where Resorts_name ='{}'
        order by Resorts_name desc limit 1
        """.format(resort))
        data=self.mycursor.fetchall()
        for i in data:
            name.append(i[1])
            rating.append(i[2])
            review.append(i[3])


        result = {
            'name':name,
            'rating':rating,
            'review':review
        }
        return result

    def fetch_place(self,):
        name=[]
        self.mycursor.execute("""
        select distinct(Place) from thailand.thai
        """)
        data=self.mycursor.fetchall()
        for i in data:
            name.append(i[0])
        return name

    def show_fetch_places(self,place,a,b):
        names=[]

        rating=[]
        price=[]

        self.mycursor.execute("""
        select distinct(Resorts_name) as resort_name , Rating , price from thailand.thai
        where Place='{}' and Rating >'{}' and price <'{}'
        """.format(place,a,b))
        data=self.mycursor.fetchall()
        for item in data:
            names.append(item[0])
            rating.append(item[1])
            price.append(item[2])
        result = {
            'names':names,
            'rating':rating,
            'price':price
        }
        return result








