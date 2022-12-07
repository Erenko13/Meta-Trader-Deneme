import mysql.connector
from flask import Flask, render_template, request, redirect, url_for, session
from mysql.connector import errorcode
import matplotlib.pyplot as plt
import numpy as np
try:
    cnx = mysql.connector.connect(user='root',
                                  password='1234',
                                  host='127.0.0.1')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

cursor = cnx.cursor()
DB_NAME = 'projtest'
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)


cursor.execute('SELECT * FROM record')
data = cursor.fetchall()
x = []
y = []
a = 20
date = '.06.2021'
for i in data:
    a += 1
    x.append(str(a)+date)
    y.append(int(i[2]))
plt.rcParams['xtick.major.pad'] = '0.2'
plt.rcParams['figure.figsize'] = (10, 8)
plt.plot(x, y, color='green')
plt.xticks(rotation=70, horizontalalignment='center')
plt.ylabel('Pieces')
plt.xlabel('Dates')
plt.subplots_adjust(bottom=0.15)
plt.title('Price of Products')
plt.savefig('./static/Tlot.png')
plt.plot()
plt.clf()

