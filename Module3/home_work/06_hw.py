# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
brands = ""
price = 0
brands_max = 0
brands_max_print = ""
key_brand = ""
price_max = 0
brand_print = ""

for key_items in items:
    key_brand = key_items.get("brand")
    if brands.find(key_brand) == -1:
        brands = brands + " " + key_brand
print("Товары на складе представлены брэндами: ", brands)

brands = ""
for key_items in items:
    key_brand = key_items.get("brand")
    brands = brands + " " + key_brand + " "
for key_items in items:
    key_brand = key_items.get("brand") + " "
    if brands.count(key_brand) >= brands_max:
        brands_max = brands.count(key_brand)
    if brands.count(key_brand) >= brands_max and brands_max_print.find(key_brand) == -1:
        brands_max_print = brands_max_print + " " + key_brand
print("На складе больше всего товаров брэнда(ов): ", brands_max_print)

for key_items in items:
    key_brand = key_items.get("brand")
    price_max = key_items.get("price")
    if price_max > price:
        brand_print = key_brand
        price = price_max
print("На складе самый дорогой товар брэнда(ов): ", brand_print)

