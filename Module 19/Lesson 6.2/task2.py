incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
total_income = sum(incomes.values())
print('\nОбщий доход за год составил', total_income)
lowest_income = min(incomes.values())
for fruit in incomes:
    if incomes[fruit] == lowest_income:
        print('Самый маленький доход у {0}. Он составляет {1} рублей'.format(fruit, lowest_income))
        incomes.pop(fruit)
        break
print('Итоговый словарь:', incomes)
