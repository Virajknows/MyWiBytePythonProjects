print('Welcome to the WiByte Bakery')
print()

menu = ['Milkshake', 'Ice Cream', 'Chocolate', 'Eclairs', 'CupCake']
price = [99.99, 120.99, 89.99, 37.99, 51.99]
TAX_RATE = 0.05

print('ITEM', 'PRICE (INR), excl. Tax', sep='\t\t\t')
for kk in range(len(menu)):
    print(str(kk + 1) + '. ' + menu[kk], price[kk], sep='\t\t')

shopping_cart = []
shopping_quant = []

num_items = len(menu)
checkout_option = num_items + 1
view_cart_option = num_items + 2
remove_option = num_items + 3

shopping_complete = 0

while shopping_complete == 0:
    print()
    print(f'Enter 1 to {num_items} to select an item.')
    print(f'Enter {checkout_option} to proceed to checkout.')
    print(f'Enter {view_cart_option} to view your current cart.')
    print(f'Enter {remove_option} to remove an item from your cart.')

    try:
        order = int(input('Your choice: '))
    except ValueError:
        print("Sorry, that was not a valid input. Please enter a number.")
        continue

    if 1 <= order <= num_items:
        print('You selected', menu[order - 1])
        try:
            quant = int(input('How many units do you wish to purchase?\n'))
        except ValueError:
            print("Sorry, that was not a valid quantity.")
            continue

        if quant <= 0:
            print("Quantity must be a positive whole number. Try again.")
            continue

        if menu[order - 1] in shopping_cart:
            idx = shopping_cart.index(menu[order - 1])
            shopping_quant[idx] += quant
        else:
            shopping_cart.append(menu[order - 1])
            shopping_quant.append(quant)

        print('Added to shopping cart:', quant, 'units of', menu[order - 1])

    elif order == checkout_option:
        if len(shopping_cart) == 0:
            print("Your cart is empty! Please add at least one item before checking out.")
        else:
            shopping_complete = 1

    elif order == view_cart_option:
        if len(shopping_cart) == 0:
            print("Your cart is currently empty.")
        else:
            print()
            print('--- Current Cart ---')
            for kk in range(len(shopping_cart)):
                print(f'{shopping_cart[kk]} x {shopping_quant[kk]}')

    elif order == remove_option:
        if len(shopping_cart) == 0:
            print("Your cart is already empty.")
        else:
            print("Items in your cart:")
            for kk in range(len(shopping_cart)):
                print(f'{kk + 1}. {shopping_cart[kk]} (x{shopping_quant[kk]})')
            try:
                remove_idx = int(input('Enter the number of the item to remove: ')) - 1
            except ValueError:
                remove_idx = -1

            if 0 <= remove_idx < len(shopping_cart):
                removed_item = shopping_cart.pop(remove_idx)
                shopping_quant.pop(remove_idx)
                print(f'Removed {removed_item} from your cart.')
            else:
                print("That wasn't a valid cart item number.")

    else:
        print("Sorry that was not a valid input.")

print()
print('=' * 60)
print('Your Shopping Cart:')
print('=' * 60)

grand_tot = 0.0
print('ITEM', 'QUANT', 'UNIT PRICE', 'TOTAL', sep='\t\t\t')

for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    unit_price = price[idx]
    tot_price = round(unit_price * shopping_quant[kk], 2)
    grand_tot += tot_price
    print(shopping_cart[kk], shopping_quant[kk], unit_price, tot_price, sep='\t\t\t')

grand_tot = round(grand_tot, 2)
tax_amount = round(grand_tot * TAX_RATE, 2)
final_total = round(grand_tot + tax_amount, 2)

print('-' * 60)
print('Subtotal (INR):', grand_tot)
print(f'Sales Tax ({int(TAX_RATE * 100)}%):', tax_amount)
print('=' * 60)
print('Your final total is (INR):', final_total)
print('=' * 60)
print()
print('Thank you for shopping at WiByte Bakery. Visit again!')
