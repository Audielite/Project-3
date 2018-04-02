import sqlite3
#import Invalid_Input_Error

db_merch = sqlite3.connect('Merch_Manager.db')
cur = db_merch.cursor()
cur.execute('create table if not exists Merch(id INTEGER PRIMARY KEY, City, State, Shirts_sold, Shirt_Price, Albums_sold, Album_Price)');
#cur.execute('drop table Merch')

def main():
    while True:
        try:
            choice = get_choice()
            if choice == 'q':
                break
            if choice == '1':
                add_shirts()
            if choice == '2':
                show_all()
            if choice == '3':
                edit_sales_record()
            if choice == '4':
                show_total()
            if choice == '5':
                show_qty()
            if choice == '6':
                delete_record
        except ValueError:
            print("Enter valid option!")
        #print(tracback.format_exc())

def add_shirts():
    City = (input('Enter City: '))
    State = (input('Enter State: '))
    Shirts_sold = int(input('Enter amount of T-Shirts sold: '))
    Shirt_Price = float(input('Enter cost of T-Shirts: '))
    Albums_sold = int(input('Enter amount of albums sold: '))
    Album_Price = float(input('Enter cost of albums: '))
    add_shirts_info(City, State, Shirts_sold, Shirt_Price, Albums_sold, Album_Price)

def add_shirts_info(City, State, Shirts_sold, Shirt_Price, Albums_sold, Album_Price):
    cur = db_merch.cursor()
    cur.execute('insert into Merch values(?,?,?,?,?,?,?)', (None, City, State, Shirts_sold, Shirt_Price, Albums_sold, Album_Price))
    db_merch.commit()

def show_all():
    for row in cur.execute('select * from Merch'):
        print(row)

def show_total():
    try:
        sales_total = (input("Which total would you like? \nEnter 'album' for album sales \nEnter 'shirt' for T-Shirt sales: ").lower())
        if sales_total == 'album':
            alb_total = cur.execute('''SELECT sum(Album_Price) FROM Merch''')
            albumList = list(alb_total)
            print(albumList)
            db_merch.commit()
        else:
            if sales_total == 'shirt':
                shr_total = cur.execute('''SELECT sum(Shirt_Price) FROM Merch''')
                shirtList = list(shr_total)
                print(shirtList)
                db_merch.commit()
    except NameError:
        print("Enter valid option!")

def show_qty():
    qty_total = (input("Which quantity would you like? \nEnter 'album' for quantity total \nEnter 'shirt' for quantity total: ").lower())
    if qty_total == 'album':
        alb_qty = cur.execute('''SELECT sum(Albums_sold) FROM Merch''')
        albumQty = list(alb_qty)
        print(albumQty)
        db_merch.commit()
    else:
        if qty_total == 'shirt':
            shr_qty = cur.execute('''SELECT sum(Shirts_sold) FROM Merch''')
            shirtQty = list(shr_qty)
            print(shirtQty)
            db_merch.commit()

def edit_sales_record():
    question = (input("Would you like to update? T-Shirt sales or Album sales? \nEnter 'shirt' for T-Shirt sales \nEnter 'album' for album sales: ").lower())
    if question == 'albums':
        update = int(input("What row would you like to update?: "))
        new_total = float(input("Enter new total: "))
        update_record = update
        cur.execute('''UPDATE Merch SET Albums_Price = ? WHERE id = ?''', (new_total, update_record))
        db_merch.commit()
    else:
        if question == 'shirts':
            update = int(input("What row would you like to update?: "))
            new_total = float(input("Enter new total: "))
            update_record = update
            cur.execute('''UPDATE Merch SET Shirts_Price = ? WHERE id = ?''', (new_total, update_record))
            db_merch.commit()

def edit_quantity_record():
    question = (input("What would you like to update? T-Shirt quantities or Album quantities? \nEnter 'shirt' for T-Shirt quantity \nEnter 'album' for album quantity: ").lower())
    if question == 'album':
        update = int(input("What row would you like to update?: "))
        new_total = int(input("Enter new total: "))
        update_record = update
        cur.execute('''UPDATE Merch SET Albums_sold = ? WHERE id = ?''', (new_total, update_record))
        db_merch.commit()
    else:
        if question == 'shirt':
            update = int(input("What row would you like to update?: "))
            new_total = int(input("Enter new total: "))
            update_record = update
            cur.execute('''UPDATE Merch SET Shirts_sold = ? WHERE id = ?''', (new_total, update_record))
            db_merch.commit()

def delete_record():
    erase = int(input("What row would you like to delete?: "))
    delete_row_id = erase
    cur.execute('''DELETE FROM Merch WHERE id = ?''', (delete_row_id,))
    db_merch.commit()

def get_choice():
    print('''
    Press 1 to add sales
    Press 2 to show all records
    Press 3 to edit a record
    Press 4 to get sales total
    Press 5 to get quantity total
    Press 6 to delete a record
    Press q to quit program
    ''')
    return input('Enter choice: ')

#db_cars.commit()
#db_merch.close()

if __name__ == '__main__':
    main()
