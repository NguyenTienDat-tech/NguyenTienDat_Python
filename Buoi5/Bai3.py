def create_item(name, qty, price):
    item = {"name" : name, "qty": qty, "price": price}
    return item

def calc_total(items):
    total = 0
    for i in items:
        total += i["price"] * i["qty"]
    return total

def format_invoice(customer, items):
    hoadon = f"customer : {customer}"
    hoadon += "\n---------------------"
    hoadon += "\nProduct   Qty    Price    Subtotal "
    total = 0
    for i in items:
        name = i["name"]
        qty = i["qty"]
        price = i["price"]
        subtotal = qty * price
        total += subtotal
        hoadon += f"\n{name}        {qty}      {price}       {subtotal}"
    hoadon += f"\nTOTAL : {total}"
    return hoadon

def export_text(invoice_string):
    dong = invoice_string.split("\n")
    return "\n".join(dong)



print(create_item("Pen", 2, 5.0))

items = []
items.append(create_item("Pen", 2, 5.0))
items.append(create_item("Ipad", 1, 15.0))
print(calc_total(items))

h = format_invoice("Nguyen Tien Dat", items)
print(h)

print(export_text(h))