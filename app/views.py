
from flask import render_template, request, session, json, flash
from app import app
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/login')
def login():
    return render_template("login.html")
@app.route('/register')
def register():
    return render_template("register.html")
@app.route('/create')
def create():
    return render_template("create.html")
@app.route('/save_bucketlist', methods=['POST'])
def save_bucketlist():
    data = {(request.form['activity']):request.form['date']}
    with open('bucket_view.json', 'w') as account:
        json.dump(data, account)
    return create()
@app.route('/view')
def view():
    with open('bucket_view.json', 'r') as account:
        data = json.load(account)
    return render_template('view.html', data=data)
@app.route('/add_bucket')
def add_bucket():
    return render_template("add_bucket.html")
@app.route('/save_new', methods=['POST'])
def save_new():
    activity=request.form['activity']
    dates=request.form['date']
    with open('bucket_view.json', 'r') as account:
        data = json.load(account)
        data.append(dict({activity:dates}))
    return add_bucket()
@app.route('/register_submit', methods=['POST'])
def register_submit():
    data = {request.form['username']:request.form['password']}
    with open('data.json', 'w') as account:
        json.dump(data, account)
        session['logged_in'] = True
    return create()
@app.route('/login_submit', methods=['POST'])
def login_submit():
    with open('data.json', 'r') as account:
        data = json.load(account)
    for key, value in data.items():
        if key == request.form['username'] and value == request.form['password']:
            session['logged_in'] = True
            return create()
        else:
            flash('wrong password!')
            return login()
@app.route('/delete')
def delete():
    with open('bucket_view.json', 'r') as account:
        data = json.load(account)
        keys = request.args.get('id')
        data.pop(keys, None)
    return render_template('view.html', data=data)
@app.route('/edit')
def edit():
    with open('bucket_view.json', 'r') as account:
        data = json.load(account)
    return render_template('edit.html', data=data)
@app.route('/logout')
def logout():
    session['logged_in'] = False
    return index()
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
