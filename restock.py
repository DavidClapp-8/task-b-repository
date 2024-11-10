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
    #Updates index 0 of the current day
    inventory_records.insert(0,current_day)

    #If statemen tto check if a restock is needed
    if current_day % 7 == 0:
        #Difference between 2000 and items left
        difference = 2000 - available_items
        if difference == 0:
            difference = 2000

        #Restocks up to 2000
        available_items = available_items + difference
        #Updates the items restocked that day
        inventory_records.insert(2, difference)
        #Updates the items available for that day
    else:
        inventory_records.insert(2, 0)


    return available_items
