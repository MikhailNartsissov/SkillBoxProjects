incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00
}
order = {
    'apple': 2,
    'banana': 3,
    'pear': 1,
    'watermelon': 10,
    'chocolate': 5
}
prices = [0 if incomes.get(fruit) is None
          else incomes.get(fruit) * order[fruit]
          for fruit in order
          ]
total_income = sum(prices)
print('\nИтоговая выручка компании по имеющимся товарам составляет {0} рублей.'.format(total_income))
