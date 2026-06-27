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
            for i,expense in enumerate (expenselist,start=1):
                print(f"\nExpense {i}:")
                print(f"1. Date: {expense['date']}")
                print(f"2. Category: {expense['category']}")
                print(f"3. Description: {expense['description']}")
                print(f"4. Amount: {expense['amount']}")
                
                
    elif(choise == 3):
           total =0
           for expense in expenselist:
               total += expense['amount']
           print("total amount is :-",total)
           
    elif(choise == 4):
        print('thankyou')
        break
    else:
       print("invalid choise, TRY AGAIN")
    
                