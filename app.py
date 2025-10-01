from flask import Flask, render_template, request, redirect, url_for, flash
import math

app = Flask(__name__)
app.secret_key = "URrnorn"


def task1_logic(number):
    #task 1#
    #main function#
    def factorial(n):  #<--the "factorial(n)" is the recursion because it calls itself#
        #using math import function to use its stuff#
        return math.factorial(n) #<-- Where we return the value of factorial using math library#

    return factorial(number)


def task2_logic(numbers_str):
    #task 2#
    #main functions#
    def remove_duplicates():
        items = [int(x) for x in numbers_str.split() if x.strip() != ""]
        seen = set()
        out = []
        for v in items:
            if v not in seen:
                out.append(v)
                seen.add(v)
        return out

    return remove_duplicates()


def task3_logic(radius):
    #Task3 code#
    #math module usage, code will use this equation for when the user inputs a value#
    def circle_properties(radius):
       diameter = 2 * radius
       circumference = 2 * math.pi * radius
       area = math.pi * (radius ** 2)

       return diameter, circumference, area

    d, c, a = circle_properties(radius)
    return d, c, a


# Flask routes #

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        which = request.form.get("which")
        try:
            if which == "task1":
                n_raw = request.form.get("number", "").strip()
                if n_raw == "":
                    flash("Please enter a number for factorial.")
                    return redirect(url_for("index"))
                n = int(n_raw)
                if n < 0:
                    flash("Enter a non-negative integer.")
                    return redirect(url_for("index"))
                val = task1_logic(n)
                result = {"task": "task1", "n": n, "value": val}

            elif which == "task2":
                numbers_str = request.form.get("numbers", "")
                if numbers_str.strip() == "":
                    flash("Please enter some numbers (space-separated).")
                    return redirect(url_for("index"))
                val = task2_logic(numbers_str)
                result = {"task": "task2", "value": val}

            elif which == "task3":
                r_raw = request.form.get("radius", "").strip()
                if r_raw == "":
                    flash("Please enter a radius.")
                    return redirect(url_for("index"))
                r = float(r_raw)
                if r < 0:
                    flash("Enter a non-negative radius.")
                    return redirect(url_for("index"))
                d, c, a = task3_logic(r)
                result = {"task": "task3", "value": {"diameter": d, "circumference": c, "area": a}}

            else:
                flash("Unknown task")
                return redirect(url_for("index"))

        except ValueError:
            flash("Invalid numeric input; please check your entries.")
            return redirect(url_for("index"))
        except OverflowError:
            flash("Number too large for factorial.")
            return redirect(url_for("index"))

    return render_template("index.html", result=result)


if __name__== "__main__":
    app.run(debug=True)