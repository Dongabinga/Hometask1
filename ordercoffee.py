def order(*drinks):
    ord = list(drinks)
    for i in range(len(ord)):
        if ord[i] == 'Эспрессо':
            if in_stock['coffee'] < 1:
                print('К сожалению, не можем предложить Вам напиток')
                break
            else:
                print('Эспрессо')
                in_stock['coffee']=-1
        if ord[i] == 'Капучино':
            if in_stock['coffee'] < 1 or in_stock['milk']<3:
                print('К сожалению, не можем предложить Вам напиток')
                break
            else:
                print('Капучино')
                in_stock['coffee']=-1
                in_stock['milk']=-3
        if ord[i] == 'Макиато':
            if in_stock['coffee'] < 2 or in_stock['milk']<1:
                print('К сожалению, не можем предложить Вам напиток')
                break
            else:
                print('Макиато')
                in_stock['coffee']=-2
                in_stock['milk']=-1
        if ord[i] == 'Кофе по-венски':
            if in_stock['coffee'] < 1 or in_stock['cream'] < 2:
                print('К сожалению, не можем предложить Вам напиток')
                break
            else:
                print('Кофе по-венски')
                in_stock['coffee']=-1
                in_stock['cream']=-2
        if ord[i] == 'Латте Макиато':
            if in_stock['coffee'] < 1 or in_stock['cream'] < 1 or in_stock['milk'] < 2:
                print('К сожалению, не можем предложить Вам напиток')
                break
            else:
                print('Латте Макиато')
                in_stock['coffee']=-1
                in_stock['cream']=-1
                in_stock['milk']=-2
        if ord[i] == 'Кон Панна':
            if in_stock['coffee'] < 1 or in_stock['cream'] < 1:
                print('К сожалению, не можем предложить Вам напиток')
                break
            else:
                print('Кон Панна')
                in_stock['coffee']=-1
                in_stock['cream']=-1
in_stock = {"coffee": 1, "milk": 2, "cream": 3}
print(order("Эспрессо", "Капучино", "Макиато", "Кофе по-венски", "Латте Макиато", "Кон Панна"))