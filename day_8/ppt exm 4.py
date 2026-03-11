def example(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

example(1, 2, 3, 4, name="Ali", score=95)



def order_summary(main_item, quantity, *extras, **preferences):
    print("Main Item:", main_item)        # string
    print("Quantity:", quantity)          # number
    print("Extras:", extras)              # tuple of extra items (strings/numbers)
    print("Preferences:", preferences)    # dict of named options

# Example call
order_summary(
    "Burger", 2,             # main item & quantity
    "Cheese", "Bacon", 1,    # extras: mix of strings and number
    drink="Coke", sauce="Mayo", tip=5  # preferences: strings & numbers
    )