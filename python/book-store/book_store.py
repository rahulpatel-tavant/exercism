from collections import Counter

PRICE = {5: 3000, 4: 2560, 3: 2160, 2: 1520, 1: 800}

def total(basket):
    if not basket:
        return 0
    elif len(basket) == 1:
        return PRICE[1]

    basket_counter = Counter(basket)
    prices = [PRICE[1] * len(basket)]

    for i in range(2, len(basket_counter) + 1):
        cart_copy = basket_counter.copy()
        prices.append(0)
        while len(cart_copy) != 0:
            sub_set = Counter(dict(cart_copy.most_common(i)).keys())
            prices[-1] = prices[-1] + PRICE[len(sub_set)]
            cart_copy = cart_copy - sub_set

    return min(prices)