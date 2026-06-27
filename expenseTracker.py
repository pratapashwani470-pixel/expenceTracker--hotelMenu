expenselist = []
print ('welcome to expense tracker')

while True:
    print('====menu====')
    print('1. add expense')
    print('2. view all expense')
    print('3. view total amount')
    print('4. exit')
    
    choise=int(input('please enter your choise:--'))
    
    if(choise == 1):
        date = input('on which date you spend money:-')
        category = input('enter category (food, book , shopping , etc:-)')
        description = input('enter more detail about expense:-')
        amount = int(input('enter total amount:-'))
        
        expense = {
            'date' : date,
            'category' : category,
            'description' : description,
            'amount' : amount
        }
        expenselist.append(expense)
        print('expense has been added:-')
        
#view expense
    elif (choise == 2):
        if (len(expenselist)) == 0 :
            print('no expenses has been added yet!')
        else:
            print('here is your all expense')
            # count = 1
            # for expense in expenselist:
            #     print(f'expense no {count} {expense[date]}, {expense[category]}, {expense[description]}, {expense[amount]}') 
            #     count = count+1
            print(f'1.on date:-{date}\n2.you spend money for :-{category}\n3.more detail about your expense is :---{description}\n4.the total amount you spend :--{amount}')
                
    elif(choise == 3):
           total =0
           for expense in expenselist:
               total = total+expense['amount']
           print("total amount is :-",amount)
           
    elif(choise == 4):
        print('thankyou')
        break
    else:
       print("invalid choise, TRY AGAIN")
    
                