from flask import Flask, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = "dev-secret"   
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return "Invalid credentials — try again"
    return """
    <h2>Login page</h2>
    <form method="post">
      username: <input type="text" name="username"><br>
      password: <input type="password" name="password"><br>
      <input type="submit" value="Login">
    </form>
    """
@app.route("/welcome")
def welcome():
    if "user" in session:
        user = session["user"]
        return f"""
        <h2>Welcome, {user}!</h2>
        <a href="{url_for('logout')}">Logout</a>
        """
    return redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)

