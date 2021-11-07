from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def Page():
    return render_template('Page.html')

@app.route('/', methods=['POST'])
def Calculator():
    try:
        inp = request.form['text']
        x, y, z = inp.split()
        x = float(x)
        z = float(z)
        if y == '+':
            add = (x + z)
            add = str(add)
            return "Ответ: " + add
        elif y == '-':
            sub = (x - z)
            sub = str(sub)
            return "Ответ: " + sub
        elif y == '*':
            mul = (x * z)
            mul = str(mul)
            return "Ответ: " + mul
        elif y == '/':
            div = (x / z)
            div = str(div)
            return "Ответ: " + div
    except:
        return ("Ошибка! Неправильно введены числа!")
if __name__ == "__main__":
    app.run(debug=True)