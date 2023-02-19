import time
import os
import sqlite3


connection = sqlite3.connect('manager.db')
c = connection.cursor()

try:
    query = 'CREATE TABLE manager(username VARCHAR(15), password VARCHAR(20), website VARCHAR(10))'
    c.execute(query)
except:
    pass



def new_pass():
    query = 'INSERT INTO manager(username, password, website) values(\'' + input('Username : ') + '\', \'' + input('Password : ') + '\', \'' + input('website : ') + '\'' + ')'
    c.execute(query)
    connection.commit()
    print('\n\n\n')
    if input('Another?[y/n] : ') == 'y':
        new_pass()

def get_pass():
    request_status = False
    what = input('website: ')
    c.execute('SELECT * FROM manager')
    # use 50 space for each column
    for i in c.fetchall():
        if what in i[2]:
            request_status = True
            print(' '*21 + 'Username' + ' '*22 + ' '*22 + 'Password' + ' '*21 + ' '*23 + 'Website' + ' '*21)
            print('\n\n')
            print(' '*(25-len(i[0])//2) + i[0] + ' '*(25-len(i[0])//2) + ' '*(25-len(i[1])//2)  + i[1] + ' '*(25-len(i[1])//2) + ' '*(25-len(i[2])//2) + i[2] + ' '*(25-len(i[2])//2))
            print('\n\n\n')
    if request_status == False:
        print('no accout found\n\n\n')

def view_all_pass():
    c.execute('SELECT * FROM manager')
    print(' '*21 + 'Username' + ' '*22 + ' '*22 + 'Password' + ' '*21 + ' '*23 + 'Website' + ' '*21)
    print('_'*(155))
    for i in c.fetchall():
        print('\n')
        print(' '*(25-len(i[0])//2) + i[0] + ' '*(25-len(i[0])//2) + ' '*(25-len(i[1])//2)  + i[1] + ' '*(25-len(i[1])//2) + ' '*(25-len(i[2])//2) + i[2] + ' '*(25-len(i[2])//2))
    print('\n\n\n')

def update():
    account = input('change password for which website? ')
    password = input('Enter the new password : ')
    q = "UPDATE manager SET password=\'" + password + "\' where website=\'" + account + "\'"
    print(q)
    c.execute(q)

count = 0
while True:
    if count == 0:
        pass
    else:
        time.sleep(1)
    t = input('Welcome to password Manager\n\t1. Get your password\n\t2. New Account\n\t3. View all passwords\n\t4. update password\n\t5. Quit\n>>>')
    if t == '1':
        get_pass()
    elif t == '2':
        new_pass()
    elif t == '3':
        view_all_pass()
    elif t == '4':
        update()
    elif t == '5':
        break
    else:
        print('Error')
    count += 1








