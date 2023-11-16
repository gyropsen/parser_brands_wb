from wb_page import ParceWB
from functions import *

# счетчик
count = 1

# Запрашиваем у пользователя url и создаем экземлпяр класса
wb_page = ParceWB(str(input("URL должен быть подобен данному: https://www.wildberries.ru/brands/ostin\n"
                            "Введите url сайта: ")))
filename = input("Введите файл сохранения парсера (без расширения): ")

# Получаем параматеры брэнда
brand_params = wb_page.get_brand()

print(f"Получен брэнд: {brand_params[0]}, его id: {brand_params[1]}")

# создаем файл csv
create_csv(filename)

# Цикл, в котором полчаем данные с сайта, переносим их в список и добавляем в файл
while True:
    page = wb_page.get_data(brand_params[1][0].lower(), count)
    if page:
        count += 1
        product_list = get_products_list(page.json())
        add_product(product_list[0], filename)
    else:
        break

# Конец
print("Успешно")
