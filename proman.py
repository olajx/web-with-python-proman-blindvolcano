from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, current_app, escape

app = Flask(__name__)  # create the application instance :)
app.config.from_object(__name__)

app.config.update(dict(
    DEBUG=True, SECRET_KEY='any_random_string'))


@app.route('/')
def root():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)