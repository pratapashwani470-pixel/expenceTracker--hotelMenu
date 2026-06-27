menu = {
    'pizza' : 40,
    'pasta' : 50,
    'burger' : 60,
    'salad' : 70,
    'coffee' : 80 
}
# print('welcome')
# print("pizza : rs40 \npasta : rs50\nburger : rs60\nsalad : rs70\ncoffe : rs80")
# order_total = 0
# item1 = input('enter your first item you want to order')
# if item1 in menu:
#     order_total += menu[item1]
#     print('your item has been added to your order ')
# else:
#     print("ordered item", item1 ,end =" " )
#     print('is not available yet!')

# another_item = input('do you want another item,(yes/no)')
# if another_item == 'yes':
#     item2 = input('enter 2nd item you want to order:')
#     if item2 in menu:
#         order_total += menu[item2]
#         print(item2, ' has been added to you order')
# else:
#     print('ordered item is not available yet')
# print('the total amount of item to pay is',order_total)        
    
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
        item2 = input('enter what you want:-')
        if item2 in menu:
            total_order += menu[item2]
            print('item add been added ') 
        elif item2 == 'exit':
            break
    elif another_item == 'no':
        break
# if another_item == exit :
#     break
    
    # else:
    #     print(f'{item2} is not availabe yet!')
    #     break
        
  # else :
    #     print('thank you')
    #     break
    #     # else:
        #      print('ordered item is not available yet!')
             
         
# order(input('enter order'))
# if order in menu:
#     total_order += menu[order]

# a = input('any thing else(yes/no):-')
# if a == 'yes':
#    item3 = input('enter item:-')
# else:
#     print('')
# if item3 in menu:
#     print('item has been added')
#     total_order += menu[item3]
# else:
#     print('is not available yet!')
    
            
# else:
#     print('thank you')
    
print('total amount you have to pay is:-',total_order)