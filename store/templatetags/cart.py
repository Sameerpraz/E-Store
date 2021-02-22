from django import template

register = template.Library() 


@register.filter(name='is_in_cart')
def is_in_cart(product , cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='quantity_in_cart')
def quantity_in_cart(product , cart):
    keys=cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='multiply')
def multiply(product , cart):
    return product.price * quantity_in_cart(product , cart)

@register.filter(name='total_sum')
def total_sum(products , cart):
    sum = 0
    for i in products:
        sum += multiply(i,cart)
    return sum