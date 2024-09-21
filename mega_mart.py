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
    shopping_cart.append(Cart(name, price))
    calc_cart_total()


def calc_cart_total():
    global shopping_cart_total
    global shopping_cart

    shopping_cart_total = calc_total(shopping_cart)
    set_cart_total_dom()
    update_shipping_icons()
    update_tax_dom()


def calc_total(shopping_cart):
    return sum(item.price for item in shopping_cart)


def set_cart_total_dom():
    global shopping_cart_total
    print(shopping_cart_total)


def update_shipping_icons():
    global shopping_cart_total
    buy_buttons = get_buy_buttons_dom()
    for buy_button in buy_buttons:
        item = buy_button.item
        if item.price + shopping_cart_total >= 20:
            buy_button.show_free_shipping_icon()
        else:
            buy_button.hide_free_shipping_icon()


show_free_shipping = lambda: print("show free shipping")
hide_free_shipping = lambda: print("hide free shipping")


def get_buy_buttons_dom():
    return [
        Button(Cart("item1", 5), show_free_shipping, hide_free_shipping),
        Button(Cart("item2", 7), show_free_shipping, hide_free_shipping),
    ]


def update_tax_dom():
    global shopping_cart_total
    set_tax_dom(shopping_cart_total * 0.10)


def set_tax_dom(tax):
    print("set tax dom")
