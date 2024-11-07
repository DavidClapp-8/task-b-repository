def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
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


The function will also update the inventory_records (For restocking) for a  given current day. It will also return "available_items".
    '''
    #(len(inventory_records) == 0)

    #If statemen tto check if a restock is needed
    if current_day % 7 == 0 or current_day == 0:
        #inventory_records.append() * available_items
        print(f"{inventory_records} + {current_day}")
        difference = 2000 - available_items
        available_items = available_items + difference

    return available_items
