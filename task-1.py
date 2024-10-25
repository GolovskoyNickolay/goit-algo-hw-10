from pulp import LpMaximize, LpProblem, LpVariable, value

# Створюємо модель задачі лінійного програмування
model = LpProblem(name="maximize-drinks-production", sense=LpMaximize)

# Змінні: кількість виробленого "Лимонаду" і "Фруктового соку"
lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Цільова функція: максимізувати загальну кількість напоїв
model += lemonade + fruit_juice, "Total_Production"

# Обмеження на ресурси
model += (2 * lemonade + 1 * fruit_juice <= 100), "Water_Constraint"
model += (1 * lemonade <= 50), "Sugar_Constraint"
model += (1 * lemonade <= 30), "Lemon_Juice_Constraint"
model += (2 * fruit_juice <= 40), "Fruit_Puree_Constraint"

# Розв'язуємо задачу
model.solve()

# Отримуємо результати
lemonade_qty = value(lemonade)
fruit_juice_qty = value(fruit_juice)
total_production = value(model.objective)

print(f"Кількість лимонаду: {lemonade_qty}")
print(f"Кількість фруктового соку: {fruit_juice_qty}")
print(f"Загальна кількість напоїв: {total_production}")
