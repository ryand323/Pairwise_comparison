print(
    'Hello! step one is to list alternatives\n'
    'Please enter each followed by a return character\n'
    'When finished enter "stop"\n'
)

#Ask user for the alternatives that will be ranked.
counter = 1
alternative_list = list()
new_alternative = input("alternative " + str(counter) + ": ")
while new_alternative != "stop":
    if new_alternative != "stop":
        alternative_list.append(new_alternative)
    counter = counter + 1
    new_alternative = input("alternative " + str(counter) + ": ")

#Print the list of alternatives.
print("\nalternatives: " + str(alternative_list))

print(
    '\nStep 2 is to sort alternatives by comparison.\n'
    'If alternative A more important than alternative B\n'
    'key in y, otherwise B is more important\n')

alternative_count = len(alternative_list)

#Sort the alternatives by taking user inputs.
A = 0
while A < alternative_count:
    B = A+1
    while B < alternative_count:
        print(alternative_list[A] + " > ", alternative_list[B])
        decision = input()
        if decision != "y":
            dummy = alternative_list[A]
            alternative_list[A] = alternative_list[B]
            alternative_list[B] = dummy
        B+=1
    A+=1

#Print ranked alternatives.
for i in range(alternative_count):
    print("#" + str((i+1)) + " " + alternative_list[i] + "\n")

#Wait for user.
input()