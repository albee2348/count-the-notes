Amount= int(input("Please enter amount for withdrawl:"))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("Notes of 100 taka:", note_1)
print("Notes of 50 taka:", note_2)
print("Notes of 10 taka:", note_3)