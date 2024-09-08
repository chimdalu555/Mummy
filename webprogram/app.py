from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bi-Chizzy Ventures Official Website</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Bi-Chizzy Ventures Official Website</h1>
    </header>

    <div class="container">
        <section class="form-section">
            <h2>Fill Out Your Information</h2>
            <form method="post" action="/submit">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="address">Address:</label>
                <input type="text" id="address" name="address" required>

                <label for="date">Expected Date for Delivery:</label>
                <input type="date" id="date" name="date" required>

                <label for="state">State of Residence:</label>
                <select id="state" name="state" required>
                    <option value="">Select State</option>
                    <option value="Abuja">Abuja</option>
                    <option value="Abia">Abia</option>
                    <option value="Adamawa">Adamawa</option>
                    <option value="Akwa Ibom">Akwa Ibom</option>
                    <option value="Anambra">Anambra</option>
                    <option value="Bauchi">Bauchi</option>
                    <option value="Bayelsa">Bayelsa</option>
                    <option value="Benue">Benue</option>
                    <option value="Borno">Borno</option>
                    <option value="Cross River">Cross River</option>
                    <option value="Delta">Delta</option>
                    <option value="Ebonyi">Ebonyi</option>
                    <option value="Edo">Edo</option>
                    <option value="Ekiti">Ekiti</option>
                    <option value="Enugu">Enugu</option>
                    <option value="Gombe">Gombe</option>
                    <option value="Imo">Imo</option>
                    <option value="Jigawa">Jigawa</option>
                    <option value="Kaduna">Kaduna</option>
                    <option value="Kano">Kano</option>
                    <option value="Kogi">Kogi</option>
                    <option value="Kwara">Kwara</option>
                    <option value="Lagos">Lagos</option>
                    <option value="Nasarawa">Nasarawa</option>
                    <option value="Niger">Niger</option>
                    <option value="Ogun">Ogun</option>
                    <option value="Ondo">Ondo</option>
                    <option value="Osun">Osun</option>
                    <option value="Oyo">Oyo</option>
                    <option value="Plateau">Plateau</option>
                    <option value="Rivers">Rivers</option>
                    <option value="Sokoto">Sokoto</option>
                    <option value="Taraba">Taraba</option>
                    <option value="Yobe">Yobe</option>
                    <option value="Zamfara">Zamfara</option>
                </select>

                <button type="submit">Submit</button>
            </form>
        </section>

        <section class="services-section">
            <h2>Our Services</h2>
            <p>We offer a range of household foodstuffs available in Nigeria. Here are some of our products and their current prices in 2024:</p>
            <ul class="services-list">
                <li>Rice: ₦90,000 per bag</li>
                <li>Chivita Exotic: ₦6,000 per carton</li>
                <li>Hollandia Yoghurt: ₦2,500 per pack</li>
                <li>Chivita Small Pack: ₦1,200 per pack</li>
                <li>Detergent: ₦1,500 per carton</li>
                <li>Schweppes: ₦5,000 per carton</li>
                <li>Fanta: ₦5,000 per carton</li>
                <li>Coca-Cola: ₦5,000 per carton</li>
                <li>Sprite: ₦5,000 per carton</li>
                <li>Beta Malt: ₦4,500 per carton</li>
            </ul>
            <p><strong>Note:</strong> Prices are subject to change due to market fluctuations and may increase or decrease. Please contact us for the most current prices.</p>
        </section>

        <section class="contact-section">
            <h2>Contact Us</h2>
            <p>For inquiries, please reach out to us through the following phone numbers:</p>
            <p>+234 806 025 5703</p>
            <p>+234 703 811 0200</p>
        </section>
    </div>

    <footer>
        <p>&copy; 2024 Bi-Chizzy Ventures. All rights reserved.</p>
    </footer>
</body>
</html>
'''

@app.route('/')
def index():
    return HTML_TEMPLATE

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    address = request.form['address']
    date = request.form['date']
    state = request.form['state']
    # Here you can handle the form data as needed (e.g., save to a database, send an email, etc.)
    return f"<h1>Thank you, {name}!</h1><p>Your submission has been received.</p>"

if __name__ == '__main__':
    app.run(debug=True)


