from flask import Flask, render_template

from controllers.g_classes_controller import g_classes_blueprint
from controllers.members_controller import members_blueprint
from controllers.gym_controller import gym_blueprint


app = Flask(__name__)

app.register_blueprint(g_classes_blueprint)
app.register_blueprint(members_blueprint)
app.register_blueprint(gym_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)