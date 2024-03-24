from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

# User registration and authentication
users = {"user1": "password1", "user2": "password2", "user3": "password3"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if len(username) < 3 or len(password) < 6:
            return render_template(
                "register.html",
                error="Username must be at least 3 characters long and password must be at least 6 characters long",
            )
        if username in users:
            return render_template(
                "register.html",
                error="Username already exists. Please choose a different one",
            )
        users[username] = password
        return redirect("/")
    return render_template("register.html", error=None)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Check if username exists and password is correct
        if username in users and users[username] == password:
            return jsonify({"message": "Login successful"})
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html", error=None)


# Policy Management
policies = [
    {"id": 1, "type": "health", "name": "Health Insurance Policy 1", "premium": 100},
    {"id": 2, "type": "vehicle", "name": "Car Insurance Policy 1", "premium": 200},
    {"id": 3, "type": "property", "name": "Home Insurance Policy 1", "premium": 300},
]


@app.route("/policy")
def policies_page():
    return render_template("policies.html", policies=policies)


@app.route("/add_policy", methods=["POST"])
def add_policy():
    data = request.form
    new_id = max(p["id"] for p in policies) + 1
    new_policy = {
        "id": new_id,
        "type": data["type"],
        "name": data["name"],
        "premium": int(data["premium"]),
    }
    policies.append(new_policy)
    message = f"Policy '{data['name']}' added successfully."
    return render_template("policies.html", policies=policies, message=message)


@app.route("/update_policy", methods=["POST"])
def update_policy():
    data = request.form
    policy_id = int(data["policy_id"])
    for policy in policies:
        if policy["id"] == policy_id:
            policy.update(
                {
                    "type": data["type"],
                    "name": data["name"],
                    "premium": int(data["premium"]),
                }
            )
            message = f"Policy {policy_id} updated successfully."
            return render_template("policies.html", policies=policies, message=message)
    return render_template(
        "policies.html",
        policies=policies,
        message=f"Policy with ID {policy_id} not found.",
    )


@app.route("/delete_policy", methods=["POST"])
def delete_policy():
    policy_id = int(request.form["policy_id"])
    for policy in policies:
        if policy["id"] == policy_id:
            policies.remove(policy)
            message = f"Policy {policy_id} deleted successfully."
            return render_template("policies.html", policies=policies, message=message)
    return render_template(
        "policies.html",
        policies=policies,
        message=f"Policy with ID {policy_id} not found.",
    )


if __name__ == "__main__":
    app.run(debug=True)
