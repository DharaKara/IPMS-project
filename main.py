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
    {
        "id": "1",
        "name": "Life Cover",
        "image_link": "https://www.atherholdings.co.nz/wp-content/uploads/2021/01/life-insurance.png",
        "summary": "Life Cover provides financial protection for your loved ones in the event of your death. It pays out a lump sum benefit to your beneficiaries, helping them cover expenses and maintain their standard of living.",
    },
    {
        "id": "2",
        "name": "Funeral Cover",
        "image_link": "https://www.insurancechat.co.za/wp-content/uploads/2018/11/DfKrp6hWAAANJsJ.jpg",
        "summary": "Funeral Cover offers financial assistance to cover the costs associated with a funeral. It helps ease the financial burden on your family during a difficult time by providing a payout to cover funeral expenses.",
    },
    {
        "id": "3",
        "name": "Health Insurance",
        "image_link": "https://cdn9.dissolve.com/p/D9_8_987/D9_8_987_1200.jpg",
        "summary": "Health Insurance provides coverage for medical expenses incurred due to illness or injury. It ensures access to quality healthcare without worrying about the financial strain of medical bills.",
    },
    {
        "id": "4",
        "name": "Disability Insurance",
        "image_link": "https://2.bp.blogspot.com/-Mzw3qWlobVg/WscqK8I3VyI/AAAAAAAAr6w/mv0ZfyThYbg1L395NIw5PdQ-WstpiNaQgCLcBGAs/s1600/disability.jpg",
        "summary": "Disability Insurance offers financial protection in the event you become disabled and unable to work. It provides a regular income to help you maintain your lifestyle and cover expenses.",
    },
    {
        "id": "5",
        "name": "Income Protection",
        "image_link": "https://www.easymovefs.co.uk/wp-content/assets/income-protection.jpg",
        "summary": "Income Protection insurance replaces a portion of your income if you're unable to work due to illness or injury. It ensures you can still meet your financial obligations and maintain your standard of living.",
    },
    {
        "id": "6",
        "name": "Car Insurance",
        "image_link": "https://www.motoringresearch.com/wp-content/uploads/2020/01/Best-car-insurance-companies-of-2020-1920x1080.jpg",
        "summary": "Car Insurance provides coverage for your vehicle against damages, theft, and liability. It helps you financially recover from accidents and protects you from legal liabilities.",
    },
    {
        "id": "7",
        "name": "Home Insurance",
        "image_link": "https://www.beazer.com/content/images/beazer_difference_new_home.jpg",
        "summary": "Home Insurance protects your home and its contents against damages, theft, and other unforeseen events. It provides financial assistance to repair or replace your property.",
    },
    {
        "id": "8",
        "name": "Travel Insurance",
        "image_link": "https://wallpaperaccess.com/full/136008.jpg",
        "summary": "Travel Insurance offers coverage for unexpected expenses incurred during domestic or international travel. It includes medical coverage, trip cancellation, lost luggage, and other benefits.",
    },
]


@app.route("/products")
def policies_page():
    return render_template("products.html", policies=policies)


# @app.route("/movie-list")
# def movie_list_page():
#     return render_template("movie-list.html", movies=movies)


# @app.route("/products/<movie_id>")
# def movie_detail(movie_id):
#     movie = next((movie for movie in movies if movie["id"] == movie_id), None)
#     if movie:
#         return render_template("movie-detail.html", movie=movie)
#     else:
#         return "<h1>Movie not found</h1>", 404

# @app.route("/add_policy", methods=["POST"])
# def add_policy():
#     data = request.form
#     new_id = max(p["id"] for p in policies) + 1
#     new_policy = {
#         "id": new_id,
#         "type": data["type"],
#         "name": data["name"],
#         "premium": int(data["premium"]),
#     }
#     policies.append(new_policy)
#     message = f"Policy '{data['name']}' added successfully."
#     return render_template("policies.html", policies=policies, message=message)


# @app.route("/update_policy", methods=["POST"])
# def update_policy():
#     data = request.form
#     policy_id = int(data["policy_id"])
#     for policy in policies:
#         if policy["id"] == policy_id:
#             policy.update(
#                 {
#                     "type": data["type"],
#                     "name": data["name"],
#                     "premium": int(data["premium"]),
#                 }
#             )
#             message = f"Policy {policy_id} updated successfully."
#             return render_template("policies.html", policies=policies, message=message)
#     return render_template(
#         "policies.html",
#         policies=policies,
#         message=f"Policy with ID {policy_id} not found.",
#     )


# @app.route("/delete_policy", methods=["POST"])
# def delete_policy():
#     policy_id = int(request.form["policy_id"])
#     for policy in policies:
#         if policy["id"] == policy_id:
#             policies.remove(policy)
#             message = f"Policy {policy_id} deleted successfully."
#             return render_template("policies.html", policies=policies, message=message)
#     return render_template(
#         "policies.html",
#         policies=policies,
#         message=f"Policy with ID {policy_id} not found.",
# )


@app.route("/faqs")
def faqs_page():
    faqs = [
        {
            "question": "What is insurance?",
            "answer": "Insurance is a contract between an individual (the policyholder) and an insurance company. The policyholder pays premiums in exchange for financial protection or reimbursement against losses from specified risks.",
        },
        {
            "question": "Why do I need insurance?",
            "answer": "Insurance provides financial protection against unexpected events that could lead to significant financial loss. It helps individuals and businesses manage risks by transferring them to an insurance company.",
        },
        {
            "question": "What types of insurance are available?",
            "answer": "There are various types of insurance available, including life insurance, health insurance, auto insurance, home insurance, and business insurance. Each type of insurance offers protection against specific risks.",
        },
        {
            "question": "How do I choose the right insurance policy?",
            "answer": "Choosing the right insurance policy depends on your individual needs and circumstances. Consider factors such as coverage options, premiums, deductibles, and the financial stability of the insurance company.",
        },
        {
            "question": "What is a deductible?",
            "answer": "A deductible is the amount of money you must pay out of pocket before your insurance coverage kicks in. For example, if you have a $500 deductible on your auto insurance policy and you file a claim for $2,000 in damages, you would pay $500, and the insurance company would cover the remaining $1,500.",
        },
        {
            "question": "What is coverage limit?",
            "answer": "A coverage limit is the maximum amount an insurance company will pay for a covered loss. For example, if you have a coverage limit of $100,000 on your homeowner's insurance policy and your home is damaged in a covered event, the insurance company will pay up to $100,000 to repair or replace your home.",
        },
        {
            "question": "Can I cancel my insurance policy?",
            "answer": "Yes, you can typically cancel your insurance policy at any time. However, there may be cancellation fees or penalties depending on the terms of your policy. It's important to review your policy documents and contact your insurance company for specific details.",
        },
        {
            "question": "What happens if I miss a premium payment?",
            "answer": "If you miss a premium payment, your insurance coverage may lapse, meaning you will no longer be protected against covered risks. Some insurance companies offer a grace period during which you can make a late payment without penalty, but it's essential to contact your insurer as soon as possible to avoid any disruptions in coverage.",
        },
        {
            "question": "Can I change my insurance coverage?",
            "answer": "Yes, you can typically make changes to your insurance coverage, such as increasing or decreasing coverage limits, adding or removing coverage options, or updating your personal information. Contact your insurance company or agent to discuss any changes you would like to make to your policy.",
        },
        {
            "question": "What should I do if I need to file a claim?",
            "answer": "If you need to file a claim, contact your insurance company or agent as soon as possible to report the incident. Provide any necessary documentation, such as photos, police reports, or medical records, to support your claim. Your insurance company will guide you through the claims process and help you receive compensation for covered losses.",
        },
    ]
    return render_template("faqs.html", faqs=faqs)


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


contact = []


@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    contact.append({"name": name, "email": email, "message": message})
    print(contact)
    return (
        "<h1>Thank you for your message, {}! We will get back to you soon.</h1>".format(
            name
        )
    )


if __name__ == "__main__":
    app.run(debug=True)
