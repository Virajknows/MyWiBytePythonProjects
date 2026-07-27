print('Welcome to Virajs Bakery')
print('All items are priced per kilogram (INR/kg). Enter weight in kg (e.g. 0.5 for 500g).')
print()

menu = ['Gulab Jamun', 'Samosa', 'Salt Biscuit', 'Jaggery', 'Veg Puffs', 'Cookies', 'Bread Loaf', 'Rusk']
price_per_kg = [400.00, 240.00, 300.00, 350.00, 320.00, 450.00, 180.00, 220.00]

TAX_RATE = 0.05

DISCOUNT_TIERS = [
    (500, 5),
    (1000, 10),
    (2000, 15),
]

LOYALTY_POINTS_PER_100 = 1

print(f'{"ITEM":<20}{"PRICE (INR/kg)":>15}')
for kk in range(len(menu)):
    label = f'{kk + 1}. {menu[kk]}'
    print(f'{label:<20}{price_per_kg[kk]:>15.2f}')

shopping_cart = []
shopping_weight = []

num_items = len(menu)
checkout_option = num_items + 1
view_cart_option = num_items + 2
remove_option = num_items + 3

shopping_complete = 0


def calculate_subtotal():
    total = 0.0
    for kk in range(len(shopping_cart)):
        idx = menu.index(shopping_cart[kk])
        total += price_per_kg[idx] * shopping_weight[kk]
    return round(total, 2)


def get_current_tier(subtotal):
    qualified = None
    for min_spend, pct in DISCOUNT_TIERS:
        if subtotal >= min_spend:
            qualified = (min_spend, pct)
    return qualified


def get_next_tier(subtotal):
    for min_spend, pct in DISCOUNT_TIERS:
        if subtotal < min_spend:
            return (min_spend, pct)
    return None


def show_next_order_nudge(subtotal):
    next_tier = get_next_tier(subtotal)
    if next_tier is not None:
        amount_needed = round(next_tier[0] - subtotal, 2)
        print(f'Add Rs.{amount_needed} more to unlock a {next_tier[1]}% discount (spend Rs.{next_tier[0]}+)!')
    else:
        print("You've unlocked our highest discount tier. Nice haul!")


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
            weight = float(input('Enter weight in kg you wish to purchase (e.g. 0.5): '))
        except ValueError:
            print("Sorry, that was not a valid weight.")
            continue
        if weight <= 0:
            print("Weight must be a positive number. Try again.")
            continue
        weight = round(weight, 3)
        if menu[order - 1] in shopping_cart:
            idx = shopping_cart.index(menu[order - 1])
            shopping_weight[idx] += weight
        else:
            shopping_cart.append(menu[order - 1])
            shopping_weight.append(weight)
        print(f'Added to shopping cart: {weight} kg of {menu[order - 1]}')
        show_next_order_nudge(calculate_subtotal())

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
            print(f'{"ITEM":<16}{"WEIGHT (kg)":>14}{"LINE TOTAL":>16}')
            for kk in range(len(shopping_cart)):
                idx = menu.index(shopping_cart[kk])
                line_total = round(price_per_kg[idx] * shopping_weight[kk], 2)
                print(f'{shopping_cart[kk]:<16}{shopping_weight[kk]:>14.3f}{"Rs." + format(line_total, ".2f"):>16}')
            print(f'Subtotal so far: Rs.{calculate_subtotal()}')
            show_next_order_nudge(calculate_subtotal())

    elif order == remove_option:
        if len(shopping_cart) == 0:
            print("Your cart is already empty.")
        else:
            print("Items in your cart:")
            for kk in range(len(shopping_cart)):
                print(f'{kk + 1}. {shopping_cart[kk]} ({shopping_weight[kk]} kg)')
            try:
                remove_idx = int(input('Enter the number of the item to remove: ')) - 1
            except ValueError:
                remove_idx = -1
            if 0 <= remove_idx < len(shopping_cart):
                removed_item = shopping_cart.pop(remove_idx)
                shopping_weight.pop(remove_idx)
                print(f'Removed {removed_item} from your cart.')
            else:
                print("That wasn't a valid cart item number.")
    else:
        print("Sorry that was not a valid input.")

print()
print('=' * 65)
print('Your Shopping Cart:')
print('=' * 65)
print(f'{"ITEM":<16}{"WEIGHT (kg)":>13}{"RATE (INR/kg)":>16}{"LINE TOTAL":>14}')
subtotal = 0.0
for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    rate = price_per_kg[idx]
    line_total = round(rate * shopping_weight[kk], 2)
    subtotal += line_total
    print(f'{shopping_cart[kk]:<16}{shopping_weight[kk]:>13.3f}{rate:>16.2f}{line_total:>14.2f}')
subtotal = round(subtotal, 2)
print('-' * 65)
print('Subtotal (INR):', subtotal)

discount_pct = 0
discount_amount = 0.0

print()
current_tier = get_current_tier(subtotal)
if current_tier is not None:
    print(f'Good news: your order qualifies for a discount!')
else:
    show_next_order_nudge(subtotal)

avail_discount = input('Would you like to avail a discount? (Y/N): ').strip().lower()

if avail_discount == 'y':
    if current_tier is None:
        print("Sorry, your current subtotal doesn't yet qualify for any discount tier.")
        show_next_order_nudge(subtotal)
    else:
        print()
        print('--- Available Discount Options ---')
        eligible_tiers = [t for t in DISCOUNT_TIERS if subtotal >= t[0]]
        for i, (min_spend, pct) in enumerate(eligible_tiers, start=1):
            print(f'{i}. {pct}% off (unlocked at Rs.{min_spend}+ spend)')
        print(f'{len(eligible_tiers) + 1}. No discount, thanks')

        try:
            choice = int(input('Select an option: '))
        except ValueError:
            choice = -1

        if 1 <= choice <= len(eligible_tiers):
            discount_pct = eligible_tiers[choice - 1][1]
            discount_amount = round(subtotal * discount_pct / 100, 2)
            print(f'Applied a {discount_pct}% discount: -Rs.{discount_amount}')
        else:
            print('No discount applied.')
else:
    print('No discount applied.')

print()
print('=' * 65)
print('Updated Shopping Cart Summary')
print('=' * 65)
print(f'{"ITEM":<16}{"WEIGHT (kg)":>13}{"RATE (INR/kg)":>16}{"LINE TOTAL":>14}')
for kk in range(len(shopping_cart)):
    idx = menu.index(shopping_cart[kk])
    rate = price_per_kg[idx]
    line_total = round(rate * shopping_weight[kk], 2)
    print(f'{shopping_cart[kk]:<16}{shopping_weight[kk]:>13.3f}{rate:>16.2f}{line_total:>14.2f}')

taxable_amount = round(subtotal - discount_amount, 2)
tax_amount = round(taxable_amount * TAX_RATE, 2)
final_total = round(taxable_amount + tax_amount, 2)

print()
print('=' * 65)
print('FINAL BILL')
print('=' * 65)
print(f'{"Subtotal (INR):":<28}{subtotal:>10.2f}')
if discount_pct > 0:
    print(f'{f"Discount ({discount_pct}%):":<28}{"-Rs." + format(discount_amount, ".2f"):>10}')
print(f'{"Amount after discount:":<28}{taxable_amount:>10.2f}')
print(f'{f"Sales Tax ({int(TAX_RATE * 100)}%):":<28}{tax_amount:>10.2f}')
print('=' * 65)
print(f'{"Your final total is (INR):":<28}{final_total:>10.2f}')
print('=' * 65)

points_earned = int(final_total // 100) * LOYALTY_POINTS_PER_100
print()
print(f'Bonus: You earned {points_earned} loyalty points on this purchase!')
print('Collect 100 points for a free box of Gulab Jamun on your next visit.')

print()
print('Thank you for shopping at Virajs Bakery. Visit again!')
