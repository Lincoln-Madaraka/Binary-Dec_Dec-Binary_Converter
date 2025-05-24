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
            message = "Invalid input: only 0's and 1's are allowed. TRY AGAIN!!"
        elif all(char in '01' for char in binary_value) and binary_value:
            decimal_value = str(int(binary_value, 2))
            message = f"Received {binary_value}"
        else:
            message = "Please enter a binary number."
    return render_template('bin_dec.html', message=message, decimal_value=decimal_value)

@app.route('/dec_bin', methods=['GET', 'POST'])
def dec_bin():
    message = ""
    binary_value = ""
    if request.method == 'POST':
        decimal_input = request.form.get('decimalInput', '').strip()
        if not decimal_input.isdigit():
            message = "Please Enter a Valid Number between 0 and 255"
        else:
            decimal_value = int(decimal_input)
            if decimal_value > 255:
                message = "Input should range from 0 to 255"
            else:
                binary_value = bin(decimal_value)[2:]
                message = f"Received {decimal_value}"
    return render_template('dec_bin.html', message=message, binary_value=binary_value)


if __name__ == '__main__':
    app.run(debug=True)