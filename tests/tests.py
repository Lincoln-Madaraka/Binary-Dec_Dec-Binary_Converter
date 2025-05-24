from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
 return '<h1>Hello World</h1>'
if __name__ == '__main__':
 app.run()

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit')
def submit():
    return render_template('submit.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Binary to Decimal Converter</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }
    input[type="text"], .output-box {
      padding: 10px;
      width: 300px;
      margin-top: 10px;
      display: block;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
    button {
      margin-top: 10px;
      padding: 10px 20px;
    }
    #output {
      margin-top: 15px;
      font-weight: bold;
      color: #333;
    }
  </style>
</head>
<body>

  <h2>Binary to Decimal Converter</h2>

  <form method="POST">
    <label>Enter a Binary Number:</label>
    <input type="text" name="binaryInput" placeholder="e.g. 1010">
    <button type="submit">Convert</button>
  </form>

  <div id="output">{{ message }}</div>

  {% if decimal_value %}
    <label>Decimal Equivalent:</label>
    <input type="text" class="output-box" value="{{ decimal_value }}" readonly>
  {% endif %}

</body>
</html>

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bin_dec', methods=['GET', 'POST'])
def bin_dec():
    message = ""
    decimal_value = ""
    if request.method == 'POST':
        binary_value = request.form.get('binaryInput', '')
        if any(char in binary_value for char in '23456789'):
            message = "❌ Invalid input: only 0 and 1 are allowed."
        elif all(char in '01' for char in binary_value) and binary_value:
            decimal_value = str(int(binary_value, 2))
            message = "A valid binary number was entered."
        else:
            message = "Please enter a binary number."
    return render_template('bin_dec.html', message=message, decimal_value=decimal_value)

if __name__ == '__main__':
    app.run(debug=True)
