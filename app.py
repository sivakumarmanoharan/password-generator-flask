from flask import Flask, request, render_template
import string
import random

app = Flask(__name__)


def generate_password(string_length, upper_case_choice, lower_case_choice, number_choice, special_choice):
    if string_length < 1:
        return "Please enter a password length >= 1."

    char_sets = []
    if upper_case_choice == 'y':
        char_sets.append(string.ascii_uppercase)
    if lower_case_choice == 'y':
        char_sets.append(string.ascii_lowercase)
    if number_choice == 'y':
        char_sets.append(string.digits)
    if special_choice == 'y':
        char_sets.append(string.punctuation)

    if not char_sets:
        return "Please select at least one type of character."

    combined_chars = ''.join(char_sets)
    return ''.join(random.choice(combined_chars) for _ in range(string_length))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    string_length = int(request.form['length'])
    upper_case_choice = request.form.get('uppercase', 'n')
    lower_case_choice = request.form.get('lowercase', 'n')
    number_choice = request.form.get('numbers', 'n')
    special_choice = request.form.get('special', 'n')

    password = generate_password(string_length, upper_case_choice, lower_case_choice, number_choice, special_choice)
    return render_template('index.html', password=password)


if __name__ == '__main__':
    app.run(debug=True)
