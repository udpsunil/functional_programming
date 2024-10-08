from dataclasses import dataclass


@dataclass
class Cart:
    name: str
    price: float


@dataclass
class Button:
    item: Cart
    show_free_shipping_icon: function
    hide_free_shipping_icon: function


shopping_cart = []
shopping_cart_total = 0


def add_item_to_cart(name, price):
    global shopping_cart
    shopping_cart = add_item(shopping_cart, name, price)
    calc_cart_total()


def add_item(cart, name, price):
    cart.append(Cart(name, price))
    return cart


def calc_cart_total():
    global shopping_cart_total
    global shopping_cart

    shopping_cart_total = calc_total(shopping_cart)
    set_cart_total_dom()
    update_shipping_icons()
    update_tax_dom()


def calc_total(cart):
    return sum(item.price for item in cart)


def set_cart_total_dom():
    global shopping_cart_total
    print(shopping_cart_total)


def update_shipping_icons():
    global shopping_cart_total
    buy_buttons = get_buy_buttons_dom()
    for buy_button in buy_buttons:
        item = buy_button.item
        if get_free_shipping(shopping_cart_total, item.price):
            buy_button.show_free_shipping_icon()
        else:
            buy_button.hide_free_shipping_icon()


def get_free_shipping(total, price):
    return total + price >= 20


show_free_shipping = lambda: print("show free shipping")
hide_free_shipping = lambda: print("hide free shipping")


def get_buy_buttons_dom():
    return [
        Button(Cart("item1", 5), show_free_shipping, hide_free_shipping),
        Button(Cart("item2", 7), show_free_shipping, hide_free_shipping),
    ]


def update_tax_dom():
    global shopping_cart_total
    set_tax_dom(calc_tax(shopping_cart_total))


def calc_tax(amount):
    return amount * 0.10


def set_tax_dom(tax):
    print("set tax dom")
