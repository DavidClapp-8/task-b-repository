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
        #print("Non-restock day")
        #print(f"{sold_today} were sold today")
        available_items_2 = available_items[0] - sold_today
        #items_left = available_items - sold_today
        #print(f"{available_items} are available")
        restock_amount = available_items[1]
    else:
        #Non-sale day so sold is 0
        sold_today = 0
        #Set restock variable
        restock_amount = available_items[1]
        #If statement to stop available_units being 4000 for first day
        if current_day != 0:
            available_items_2 = available_items[0] + restock_amount
        else:
            available_items_2 = 2000
    #Creation of list for each day
    my_list = []
    #Add each data item into list in correct order
    my_list.append(current_day)
    my_list.append(sold_today)
    my_list.append(restock_amount)
    my_list.append(available_items_2)
    #Add day list into whole inventory_records list
    inventory_records.append(my_list)
    #Set available_items back to a variable for start of next day
    available_items = available_items_2
    return available_items