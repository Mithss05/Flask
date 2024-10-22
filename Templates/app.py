from flask import Flask, render_template, request, session, redirect, url_for, g, flash

app = Flask(__name__)
app.secret_key = "123"

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

# Sample user data
users = [
    User(id=1, username='sathya', password='sathya@123'),
    User(id=2, username='raghul', password='raghul@123'),
    User(id=3, username='sasi', password='sasi@123')
]

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        upass = request.form['password']

        for user in users:
            if user.username == uname and user.password == upass:
                session['userid'] = user.id
                return redirect(url_for('user', name=user.username))

        flash("Username or Password Mismatch...!!!", 'danger')
        return redirect(url_for('login'))

    return render_template("login.html")

@app.route('/user')
def user():
    if 'userid' not in session:
        return redirect(url_for('login'))
    user = next((u for u in users if u.id == session['userid']), None)
    return render_template('user.html', name=user.username)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
