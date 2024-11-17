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
    flag = False
    if current_day % 7 != 0:
        sold_today = random.randint(1,200)
        print("Non-restock day")
        print(f"{sold_today} were sold today")
        available_items = 2000 - sold_today
        sold_today_total = sold_today
        print(f"{available_items} are available")
        restock_units = 0

        flag = True

    else:
        sold_today = 0
        restock_units = available_items

    print(restock_units)

    my_list = []
    my_list.append(current_day)
    my_list.append(sold_today)
    my_list.append(restock_units)
    my_list.append(available_items)

    inventory_records.append(my_list)
    print(inventory_records)
    return available_items