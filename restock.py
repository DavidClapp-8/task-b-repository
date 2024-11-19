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

    #If statement to check if a restock is needed
    if current_day % 7 == 0:
        #restock_amount between 2000 and items left
        restock_amount = 2000 - available_items
        #If the difference is zero then it means the stock is empty so sohlud refill fully by 2000
        if restock_amount == 0:
            restock_amount = 2000
    #If not restock day then restock is 0
    else:
        restock_amount = 0
    #Set available_items as a list to be used in sales function to append restock and available_items in correct order in the list
    available_items = [available_items, restock_amount]
    return available_items
