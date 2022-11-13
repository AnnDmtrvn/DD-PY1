money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

#month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение

def count_month(spend, salary, money_capital, increase):
    curent_spend = spend
    curent_capital = money_capital
    month = 0    
    while curent_capital > current_spend - salary:
        curent_capital = current_capital - current_spend + salary
        current_spend = current_spend * (1 + increase)
        month = month + 1
    return month
    

print(count_month(spend, salary, money_capital, increase))
