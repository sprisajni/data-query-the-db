# pylint:disable=C0111,C0103



def query_orders(db):
    
    query = """SELECT * FROM orders ORDER BY orderID ASC"""
    results = db.execute(query)
    results = results.fetchall()
    return results
    
    # return a list of orders displaying each column

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    query = f"""SELECT * FROM ORDERS WHERE ORDERDATE > '{date_from}'and ORDERDATE <= '{date_to}' ORDER BY ORDERDATE ASC"""
    results = db.execute(query)
    results = results.fetchall()
    return results
    

def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    results = db.execute(f"select *, julianday(ShippedDate) - JULIANDAY(OrderDate) as TimeDelta from Orders order by TimeDelta ASC")
    results = results.fetchall()
    return results
    
    
    
    
