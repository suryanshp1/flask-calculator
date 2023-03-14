from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/math", methods=["POST"])
def math_ops():
    if request.method == "POST":
        ops = request.form["operation"]
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        if ops == "add":
            r = num1+num2
            result = f"The sum of {str(num1)} and {str(num2)} is {str(r)}"
        if ops == "subtract":
            r = num1-num2
            result = f"The subtract of {str(num1)} and {str(num2)} is {str(r)}"
        if ops == "multiply":
            r = num1*num2
            result = f"The multiply of {str(num1)} and {str(num2)} is {str(r)}"
        if ops == "divide":
            r = num1/num2
            result = f"The divide of {str(num1)} and {str(num2)} is {str(r)}"
        return render_template("results.html", result=result)

@app.route("/raw", methods=["POST"])
def math_ops1():
    if request.method == "POST":
        try:
            ops = request.json["operation"]
            num1 = int(request.json["num1"])
            num2 = int(request.json["num2"])
            if ops == "add":
                r = num1+num2
                result = f"The sum of {str(num1)} and {str(num2)} is {str(r)}"
            if ops == "subtract":
                r = num1-num2
                result = f"The subtract of {str(num1)} and {str(num2)} is {str(r)}"
            if ops == "multiply":
                r = num1*num2
                result = f"The multiply of {str(num1)} and {str(num2)} is {str(r)}"
            if ops == "divide":
                r = num1/num2
                result = f"The divide of {str(num1)} and {str(num2)} is {str(r)}"
                
        except Exception as e:
            result = f"Something Went wrong | {e}"

        return jsonify(result)

if __name__=="__main__":
    app.run(host="0.0.0.0")
