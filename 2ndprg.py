import flask
app = flask.Flask(__name__)
@app.route('/')
def home():
    return 'HARIRAMAN BUILDERS'
@app.route('/contact')
def contact():
    return 'contact me @ 9025119360'
@app.route('/testimonials')
def testimonial():
    return 'testimonial'
app.run()