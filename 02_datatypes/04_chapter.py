is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f'Total Actions : {total_actions}')

milk_present = 100000_0000
print(f"Is there milk? {bool(milk_present)}")

# Logical operations

water_hot = True
tea_added = not False

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")