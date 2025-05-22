from flask import Flask, request, render_template

app = Flask(__name__)

@app.route
def home():
    return render_template('home.html')

@app.route('/bin_dec', methods=['GET', 'POST'])
def city():
    result = None
    if request.method == 'POST':
        result = request.form.get('bin_dec')
    return render_template('bin_dec.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)