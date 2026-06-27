menu = {
    'pizza' : 40,
    'pasta' : 50,
    'burger' : 60,
    'salad' : 70,
    'coffee' : 80 
}
print('welcome to py_restraunt')
print('menu :-')
print('pizza : RS40\npasta : rs50\nburger : rs60\nsalad : rs70\ncoffee : rs80' )
print('for exitng the menu enter :- exit')
total_order = 0
item1 = input('enter 1st item you want to order:-')
if item1 in menu:
    total_order += menu[item1]
    print(item1,'has been added to your order')
        
else:
    print(item1,'is not available yet!')


item2 = None
another_item = input('do you want something else: (yes/no)')

while True:
    if another_item == 'yes':
        item2 = input('anything else (if you want to exit menu type[exit]):-')
        if item2 in menu:
            total_order += menu[item2]
            print('item add been added ') 
        elif item2 == 'exit':
            break
    elif another_item == 'no':
        break
    
print('total amount you have to pay is:-',total_order)