from flask import Flask, render_template, request, jsonify
from time import sleep

app = Flask(__name__)

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
    
    total_tax = 0  
    last_tax_percentage = 0  
    
    steps = []

    if taxable_income >= first_taxable_amount:
        first_tax = 0.05 * first_taxable_amount
        steps.append({'message': 'First Tax:', 'amount': first_tax})
        total_tax += first_tax
        taxable_income = taxable_income - first_taxable_amount
        last_tax_percentage = 0.1

    if taxable_income >= second_taxable_amount:
        second_tax = 0.1 * second_taxable_amount
        steps.append({'message': 'Second Tax:', 'amount': second_tax})
        total_tax += second_tax
        taxable_income = taxable_income - second_taxable_amount
        last_tax_percentage = 0.175

    if taxable_income >= third_taxable_amount:
        third_tax = 0.175 * third_taxable_amount
        steps.append({'message': 'Third Tax:', 'amount': third_tax})
        total_tax += third_tax
        taxable_income = taxable_income - third_taxable_amount
        last_tax_percentage = 0.25

    if taxable_income >= fourth_taxable_amount:
        fourth_tax = 0.25 * fourth_taxable_amount
        steps.append({'message': 'Fourth Tax:', 'amount': fourth_tax})
        total_tax += fourth_tax
        taxable_income = taxable_income - fourth_taxable_amount
        last_tax_percentage = 0.3

    if taxable_income >= fifth_taxable_amount:
        fifth_tax = 0.3 * fifth_taxable_amount
        steps.append({'message': 'Fifth Tax:', 'amount': fifth_tax})
        total_tax += fifth_tax
        taxable_income = taxable_income - fifth_taxable_amount
        last_tax_percentage = 0.35

    if taxable_income >= sixth_taxable_amount:
        sixth_tax = 0.35 * sixth_taxable_amount
        steps.append({'message': 'Sixth Tax:', 'amount': sixth_tax})
        total_tax += sixth_tax
        taxable_income = taxable_income - sixth_taxable_amount
        last_tax_percentage = 0.35
    
    if taxable_income == 0:
        steps.append({'message': 'No Tax', 'amount': 0})
    
    steps.append({'message': 'Last Taxable Income:', 'amount': taxable_income})
    
    last_tax = last_tax_percentage * taxable_income
    total_tax += last_tax
    steps.append({'message': 'Tax on Last Income:', 'amount': last_tax})
    steps.append({'message': 'Total Tax:', 'amount': total_tax})
    
    return steps

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_tax', methods=['POST'])
def calculate_tax():
    data = request.get_json()
    annual_income = float(data['annual_income'])
    period = data['period']
    steps = calc_tax(annual_income, period)
    sleep(1.5)  # Add a delay for demonstration purposes
    return jsonify(steps)

if __name__ == '__main__':
    app.run(debug=True)
