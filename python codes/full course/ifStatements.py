is_hot=True

if is_hot:
    print("It's a hot day")
print("Enjoy your day\n")

is_hot=False

if is_hot:
    print("It's a hot day")
print("Enjoy your day\n")
is_hot=True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day\n")

is_hot=True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("it's a cold day")
    print("Wear worm clothes")
print("Enjoy your day")

is_hot=False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("it's a cold day")
    print("Wear worm clothes")
print("Enjoy your day\n")

is_hot=True
is_cold=True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("Wear worm clothes")
else:
    print("Lovely day")

is_hot=False
is_cold=True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("Wear worm clothes")
else:
    print("Lovely day")

is_hot=False
is_cold=False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("it's a cold day")
    print("Wear worm clothes")
else:
    print("Lovely day")



print('\n\n\n')
price=1000000
has_good_credit=True
if has_good_credit:
    down_payement=0.1*price
else:
    down_payement=0.2*price
print(f"DownPayement:${down_payement}")
