from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def visualization():
    """
    The main React app for displaying the graph and controls
    """
    return render_template('visualization.html')


@app.route('/graph', methods=['POST'])
def reset_graph():
    """
    Resets THE graph based on parameters
    """
    return '{"banner_message": "loaded :)"}'

if __name__ == '__main__':
    app.run()
