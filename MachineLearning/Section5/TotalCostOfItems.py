cart = [
    {"Item": "Apple", "quantity": 4, "price": 100},
    {"Item": "Banana", "quantity": 6, "price": 60},
    {"Item": "Orange", "quantity": 3, "price": 90},
    {"Item": "Milk", "quantity": 2, "price": 50},
    {"Item": "Bread", "quantity": 1, "price": 40}
]


ans = 0;
for i in cart:
    ans += i["quantity"]*i["price"]

print(ans);