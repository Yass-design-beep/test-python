from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Hello, World!", "status": "success"}


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


@app.route("/users/<int:user_id>")
def get_user(user_id):
    if user_id == 1:
        return {"id": 1, "name": "John Doe", "email": "john@example.com"}
    elif user_id > 0:
        return {"id": user_id, "name": f"User {user_id}"}
    else:
        return {"error": "User not found"}, 404


@app.route("/calculate/<int:a>/<int:b>")
def calculate(a, b):
    return {"a": a, "b": b, "sum": a + b, "difference": a - b, "product": a * b}
