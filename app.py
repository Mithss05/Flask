from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

users = {
    "mithss": "mith@24",
    "keerthi": "keerthi25",
    "varma": "varma15"
}

@app.route('/')
@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route("/confirm", methods=['POST', 'GET'])
def confirm_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username] == password:
            return render_template('user.html', Name=username)
        else:
            flash("Invalid username or password", 'danger')
            return redirect(url_for('login_page'))

    return redirect(url_for('login_page'))  

@app.route('/signup')
def signup():
    return render_template('signup.html')
if __name__ == "__main__":
    app.run(debug=True)
