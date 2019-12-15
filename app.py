from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/overview')
def overview():
    return render_template('overview.html')


@app.route('/text-fundamentals')
def text_fundamentals():
    return render_template('text-fundamentals.html')


@app.route('/what-hyperlink')
def what_hyperlink():
    return render_template('what-hyperlink.html')


@app.route('/advanced-text-formatting')
def advanced_text_formatting():
    return render_template('advanced-text-formatting.html')


@app.route('/structure')
def structure():
    return render_template('structure.html')


@app.route('/example')
def example():
    return render_template('example.html')


@app.route('/debugging')
def debugging():
    return render_template('debugging.html')


@app.route('/letter')
def letter():
    return render_template('letter.html')


@app.route('/exercise-website')
def exercise_website():
    return render_template('exercise-website.html')


@app.route('/mmimg')
def mmimg():
    return render_template('mmimg.html')


if __name__ == "__main__":
    app.run(debug=True)
