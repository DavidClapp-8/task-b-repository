import random

def daily_sales(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the sales for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.

The function will also update the inventory_records (For restocking) for a  given current day. 

    '''
    if current_day % 7 != 0:
        sold_today = random.randint(1,200)
        print("Non-restock day")
        print(f"{sold_today} were sold today")
        available_items = available_items - sold_today
        print(f"{available_items} are available")




        inventory_records.insert(1, sold_today)
        
        inventory_records.insert(3, available_items)

    else:
        inventory_records.insert(1, 0)



    print(inventory_records, "The list")
    return available_items