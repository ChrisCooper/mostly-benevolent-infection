from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def visualization():
    """
    Displays the graph and controls
    """
    return render_template('visualization.html')


if __name__ == '__main__':
    app.run()
