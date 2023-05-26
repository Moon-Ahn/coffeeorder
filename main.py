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
        size = request.form['size']

        # Add the order to the list
        coffee_orders.append({'name': name, 'type': coffee_type, 'size': size})

    return render_template('index.html', orders=coffee_orders)

if __name__ == '__main__':
    app.run(host='192.168.1.46',debug=True)