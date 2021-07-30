menue_snake_cafe = {"Appetizers":["Cookies","Spring Rolls","Wings"],
"Entrees":["Steak","Salmon","A Literal Garden","Meat Tornado"],
"Drinks":["Tea","Unicorn Tears","Coffee"],
"Desserts":["Cake","Pie","Ice Cream"],
}

def welcoming_Massage():
    print('**************************************')
    print('**    Welcome to the Snakes Cafe!   **')
    print('**    Please see our menu below.    **')
    print('**')
    print('** To quit at any time, type "quit" **')
    print('**************************************\n')
    print('')
    orders = menue_snake_cafe.items()
    print(orders)
    for item, category in orders:
      print(item)
      print('-'*len(item))
      print(category)
      for order in category:
        print(order)
      print('\n')


def choose_snake():
    counter=0
    counter_orders=0
    print('***********************************')
    print('** What would you like to order? **')
    print('***********************************\n')
    order_dish = input('> ')
    print('\n')
    snake_category = order_dish
    while order_dish:
      if order_dish == 'quit':
        exit_game()
      else:
        if snake_category == order_dish:
            counter+=1
            print(f'** {counter} order of {order_dish} have been added to your meal **\n')
        else:
            counter_orders+=1
            print(f'** {counter_orders} order of {order_dish} have been added to your meal **\n')
        order_dish=''
        order_dish= input('> ')
        print('\n')
          
          
def exit_game():
    exit_menue=input('Would you like to exit the program?quit(y/n) \n> ')
    if exit_menue=='y':
        exit()
    else:
        choose_snake()


welcoming_Massage()
choose_snake()
