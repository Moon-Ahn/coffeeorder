from flask import Flask, render_template, request

app = Flask(__name__)

# List to store the coffee orders
coffee_orders = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the coffee order details from the form
        name = request.form['name']
        coffee_type = request.form['coffee_type']
        temp = request.form['temp']

        # Add the order to the list
        coffee_orders.append({'name': name, 'type': coffee_type, 'temp': temp})

    return render_template('index.html', orders=coffee_orders)


@app.route('/beverage_data')
def beverage_data():
    # Create a dictionary to store the drink quantities
    drink_quantities = {}

    # Iterate over the coffee orders
    for order in coffee_orders:
        drink_type = order['type']
        temp = order['temp']
        key = (drink_type, temp)

        # Increment the drink quantity if the key exists, otherwise initialize it to 1
        if key in drink_quantities:
            drink_quantities[key] += 1
        else:
            drink_quantities[key] = 1

    return render_template('beverage_data.html', drink_quantities=drink_quantities)

if __name__ == '__main__':
    app.run(host='192.168.1.46',debug=True)