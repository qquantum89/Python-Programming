# Tuples
food_items = ("apple", "banana", "cucumber");
print(f"Food items are: {food_items}");
print(f"Food items are: {food_items[1]}");
print(f"Length of the tuples is : {len(food_items)}");

thistuple = ("item1",);
print(type(thistuple));
thistuple = ("item1");
print(type(thistuple));

a_student = ('Anirban', 23, "male", "seven", "Kolkata");
(name, roll, sex, clas, place) = a_student
print(f"Student's Name {a_student[0]}")
print(f"Student's Roll {a_student[1]}")
print(f"Student's Sex {a_student[2]}")
print(f"Student's Class {a_student[3]}")
print(f"Student's Place {a_student[4]}")
print(f"Student's detials:  {a_student}")
print(f"Length of the tuples:  {len(a_student)}")
name,place = place,name
print(f"name: {name}")
print(f"place: {place}")

print(f"After changes the values")
print(f"Student's Name {a_student[0]}")
print(f"Student's Roll {a_student[1]}")
print(f"Student's Sex {a_student[2]}")
print(f"Student's Class {a_student[3]}")
print(f"Student's Place {a_student[4]}")
print(f"Student's detials:  {a_student}")
print(f"Length of the tuples:  {len(a_student)}")

# Membershimp testing
print(f"Is Banana in food items list: {'Banana' in food_items}");