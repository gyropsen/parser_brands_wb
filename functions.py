import csv


def add_product(product_list, filename):
    """
    Добавляем список данных о товаре в файл
    """
    with open(f"{filename}.csv", "a", newline="") as file:
        writer = csv.writer(file)
        for product in product_list:
            writer.writerow(product)


def create_csv(filename):
    """
    Создаем файл
    """
    with open(f"{filename}.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "price", "brand", "sell", "rating", "volume"])


def get_products_list(page):
    """
    Берем из словаря нудные данный и записываем их в список
    """
    total = len(page["data"]["products"])
    product_list = [
        [
            page["data"]["products"][i]["id"],
            page["data"]["products"][i]["name"],
            page["data"]["products"][i]["salePriceU"],
            page["data"]["products"][i]["brand"],
            page["data"]["products"][i]["sale"],
            page["data"]["products"][i]["reviewRating"],
            page["data"]["products"][i]["volume"]
        ]
        for i in range(total)]
    return product_list, total
