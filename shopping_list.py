shopping_list = []
fruits = []
grocery = []
vegetable = []


def show_help():
    print('''
   # Enter 'DONE' to exit the app.
   # Enter 'SHOW' to see your items.
   # Enter 'HELP' to see help.
   # Enter 'DEL' to remove item.
   # Enter 'CLEAR' to clear your list.
   # Enter 'CAT' to add in specific category
   # Add 'Multiple' items using comma.
    ''')
    
show_help()

def show_list():
    print('Here is your Misc shopping list')
    print("--------------------------")
    
    for index, item in enumerate(shopping_list):
        index += 1
        remove_white_space = str(item).replace(' ', '')
        print("{}. {} ".format(index, remove_white_space.title()))
    
    if len(shopping_list) < 1:
         print("You haven't add anyting yet in your shopping list")
    elif len(shopping_list) == 1:
          print("You have only {} item in your shopping list".format(len(shopping_list)))
    else:
        print("You have {} items in your shopping list".format(len(shopping_list)))
        
    print("________________________________________________")
    
    print("FRUITS LIST: ")
    for index, item in enumerate(fruits):
        index += 1
        remove_white_space = str(item).replace(' ', '')
        print("{}. {} ".format(index, remove_white_space.title()))
    print("________________________________________________") 
    
    print("GROCERY LIST: ")
    for index, item in enumerate(grocery):
        index += 1
        remove_white_space = str(item).replace(' ', '')
        print("{}. {} ".format(index, remove_white_space.title()))
    print("________________________________________________")   
        
        

        
def show_category():
    print("FRUITS, VEGETABLE, GROCERY")
    print("Enter 'DONE' to finish adding")
    category = input("Enter your category >> ")
    
    if category.upper() == "FRUITS":
        while True:
            new_item = input("Add fruits >> ")
            if new_item.upper() == 'DONE':
                print(fruits)
                break
            fruits.append(new_item)
        
            
    elif category.upper() == "GROCERY":
         while True:
            new_item = input("Add grocery >> ")
            if new_item.upper() == 'DONE':
                print(grocery)
                break
            grocery.append(new_item)
            

    
def delete_list():
    confirm = input("Are you sure you want to clear your list\n Y / N ")
    if confirm.upper() == 'Y':
        shopping_list.clear()
        print('You just cleared your shopping list\nStart adding')
    else:
        show_help()
    

def add_item(item):
    if item in shopping_list:
        print("=" * len(item))
        print(item, "!! already in the list.")
        print("=" * len(item))
        print('''
  ^ ^     
( o.o )
>> V <<

        ''')
    elif ',' in item:
        seperated = item.split(',')
        
        # try to remove space while adding to list
        shopping_list.extend(seperated)
    else:
        shopping_list.append(item)
    
    
def remove_item():
    while True:
        try:
            item_to_remove = input('What item you want to remove >> ')
            if item_to_remove.upper() == 'DONE':
                show_list()
                break
            shopping_list.remove(item_to_remove)
            print(item_to_remove, " 'REMOVED' from your list")
            print("Enter 'DONE' to exit!")
                
        except ValueError:
            print(item_to_remove, " is not available in your list")
            print("Enter 'DONE' to exit!")
    
                  
while True:
    new_item = input("Add item >> ")
    
    if new_item.upper() == 'DONE':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    
    elif new_item.upper() == 'DEL':
        show_list()
        remove_item()
        continue
    elif new_item.upper() == 'CAT':
        show_category()
        continue
    elif new_item.upper() == 'CLEAR':
        delete_list()
        continue
    add_item(new_item)
    
    
show_list()
