print("what's the total bill for today, please?")
total_bill = float(input("your value: $"))
eighteen = round(((total_bill / 100)* 18))
twenty = round(((total_bill / 100)* 20))
twenty_five = round(((total_bill / 100)* 25))

total1 = round((eighteen + total_bill))
total2 = round((twenty + total_bill))
total3 = round((twenty_five + total_bill))

print("18% tip is $" + str(eighteen) + " which brings your total bill for 18% to $" + str(total1))
print("20% tip is $" + str(twenty) + " which brings your total bill for 20% to $" + str(total2))
print("25% tip is $" + str(twenty_five) + " which brings your total bill for 25% to $" + str(total3))

print("How many people where involved?")
num = int(input("Your value: "))

if(num == 2):
    print("18% tip is $" + str(round(eighteen/2)) + " which brings your total bill for 18% to $" + str(round(total1/2)))
    print("20% tip is $" + str(twenty) + " which brings your total bill for 20% to $" + str(round(total2/2)))
    print("25% tip is $" + str(round(twenty_five/2)) + " which brings your total bill for 25% to $" + str(round(total3/2)))
else:
    seventy = round(((total_bill / 100) * 70))
    thirty = round(((total_bill / 100) * 30))
    first_person = seventy
    second_person = thirty

    total4 = round((first_person + total_bill))
    total5 = round((second_person + total_bill))

    print("Are you the first person or second? Please answer with first or second")
    answer = input("answer: ")

    if(answer == "first"):
        print("70% tip is $" + str(first_person) + " which brings your total bill for 70% to $" + str(total4))
    elif(answer == "second"):
        print("30% tip is $" + str(second_person) + " which brings your total bill for 30% to $" + str(total5))
    else:
        print("This is a null value as he was being paid for.")