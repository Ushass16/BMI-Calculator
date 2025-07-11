from flask import Flask, render_template, request

# Create Flask app
app = Flask(__name__)

# Function to calculate BMI
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert cm to meters
    return weight / (height_m ** 2)

# Function to classify BMI
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Home route with GET and POST handling
@app.route("/", methods=["GET", "POST"])
def index():
    bmi = category = None  # Default empty results

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)
        except ValueError:
            bmi = None
            category = "Invalid input"

    return render_template("index.html", bmi=bmi, category=category)

# Run the app
if __name__ == "__main__":
    app.run(debug=False)
