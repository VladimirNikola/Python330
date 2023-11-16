from dz26 import sales, working, adminEmployee

s = [
    adminEmployee.AdminEmp("Валерий Задорожный"),
    working.Working("Илья Кромин", 60),
    sales.Sales("Николай Хорольский", 50)
]
rz = 0
print("Расчет заработной платы")
print("=" * 50)

for i in s:
    rz += 1
    print(f"Заработная плата: {rz} - {i.print_name()}\n- Проверить сумму: {i.zp_all()}")
