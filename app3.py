
import os
from flask import Flask, request, redirect, url_for, session, Response, render_template_string, escape

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "dev-secret")


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        
        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            
            return Response("Invalid credentials — try again", status=401, mimetype="text/plain")

    
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
        user = escape(session["user"])  
        logout_url = url_for("logout")
        
        return render_template_string(
            '''
            <h2>Welcome, {{ user }}!</h2>
            <a href="{{ logout_url }}">Logout</a>
            ''',
            user=user,
            logout_url=logout_url
        )
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
