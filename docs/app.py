from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Process form data (e.g., save to database, send email, etc.)
        # Here we just print it to the console
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        
        return redirect(url_for('thank_you', name=name))

@app.route('/thank-you')
def thank_you():
    name = request.args.get('name')
    return f"Thank you, {name}. We have received your message."

if __name__ == '__main__':
    app.run(debug=True)
