from flask import Flask, render_template, request
from Happynumber import Solution

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    raw_number = request.form.get('number')
    
    if not raw_number:
        return render_template('error.html', message='Input cannot be empty.')

    try:
        number = int(raw_number)
        if number < 0:
            raise ValueError('Number cannot be negative.')
        elif number > 10**100:  # A limit set for the maximum size of the number.
            raise ValueError('Number is too large.')
    except ValueError as e:
        if "invalid literal" in str(e):
            return render_template('error.html', message='Input must be an integer.')
        else:
            return render_template('error.html', message=str(e))
    
    solution = Solution()
    is_happy = solution.isHappy(number)
    return render_template('result.html', number=number, is_happy=is_happy)

if __name__ == '__main__':
    app.run(debug=True)