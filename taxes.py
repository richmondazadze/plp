from time import sleep

def calc_tax(annual_income, period):
    if period == "a":
        taxable_income = annual_income - 5880

        first_taxable_amount = 1320
        second_taxable_amount = 1560
        third_taxable_amount = 38000
        fourth_taxable_amount = 192000
        fifth_taxable_amount = 366200
        sixth_taxable_amount = 600000

    elif period == "m":
        taxable_income = annual_income - 490

        first_taxable_amount = 110
        second_taxable_amount = 130
        third_taxable_amount = 3167
        fourth_taxable_amount = 16000
        fifth_taxable_amount = 30520
        sixth_taxable_amount = 50000
    
    total_tax = 0  # Variable to store the total tax
    last_tax_percentage = 0  # Variable to store the last tax percentage
    
    if taxable_income >= first_taxable_amount:
        first_tax = 0.05 * first_taxable_amount
        print("")
        print('First Tax: ', first_tax)
        sleep(1.5)
        print("")
        total_tax += first_tax
        taxable_income = taxable_income - first_taxable_amount
        last_tax_percentage = 0.1

    if taxable_income >= second_taxable_amount:
        second_tax = 0.1 * second_taxable_amount
        print("")
        print('Second Tax: ', second_tax)
        sleep(1.5)
        print("")
        total_tax += second_tax
        taxable_income = taxable_income - second_taxable_amount
        last_tax_percentage = 0.175

    if taxable_income >= third_taxable_amount:
        third_tax = 0.175 * third_taxable_amount
        print("")
        print('Third Tax: ', third_tax)
        sleep(1.5)
        print("")
        total_tax += third_tax
        taxable_income = taxable_income - third_taxable_amount
        last_tax_percentage = 0.25

    if taxable_income >= fourth_taxable_amount:
        fourth_tax = 0.25 * fourth_taxable_amount
        print("")
        print('Fourth Tax: ', fourth_tax)
        sleep(1.5)
        print("")
        total_tax += fourth_tax
        taxable_income = taxable_income - fourth_taxable_amount
        last_tax_percentage = 0.3

    if taxable_income >= fifth_taxable_amount:
        fifth_tax = 0.3 * fifth_taxable_amount
        print("")
        print('Fifth Tax: ', fifth_tax)
        sleep(1.5)
        print("")
        total_tax += fifth_tax
        taxable_income = taxable_income - fifth_taxable_amount
        last_tax_percentage = 0.35

    if taxable_income >= sixth_taxable_amount:
        sixth_tax = 0.35 * sixth_taxable_amount
        print("")
        print('Sixth Tax: ', sixth_tax)
        sleep(1.5)
        print("")
        total_tax += sixth_tax
        taxable_income = taxable_income - sixth_taxable_amount
        last_tax_percentage = 0.35
    
    if taxable_income == 0:
        print("")
        print("No Tax") 
        print("")
        sleep(1.5)
    
    print("Last Taxable Income:", taxable_income)
    
    # Calculate tax on the last taxable income using the last tax percentage
    last_tax = last_tax_percentage * taxable_income
    total_tax += last_tax
    print("")
    print("")
    print("Tax on Last Income:", last_tax)
    sleep(1.5)
    print("")
    print("")
    print("Total Tax:", total_tax)
    sleep(1.5)
    print("")

# Prompt user until correct input is given
print("**************************************")
print("**  Period of Tax to be Calculated: **")
print("**   Annually or Monthly            **")
print("**************************************")
print("")
print("   a for Annually  /  m for Monthly   ")
print("")

type = input("Which type of period will you be calculating : ")

while type not in ["a", "m"]:
    print("")
    print("")
    print("")
    print("Error Error Error")
    print("")
    print("Please try again")
    print("")
    print("**************************************")
    print("**  Period of Tax to be Calculated: **")
    print("**   Annually or Monthly            **")
    print("**************************************")
    print("")
    print("   a for Annually  /  m for Monthly   ")
    print("")
    type = input("Which type of period will you be calculating : ")
    print("")
    print("")

annual_income = float(input("Enter the annual income: "))

# Convert monthly income to annual if applicable
if type == "m":
    annual_income /= 12

calc_tax(annual_income, type)
