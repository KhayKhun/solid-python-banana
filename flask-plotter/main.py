from flask import Flask, request, render_template

import matplotlib
matplotlib.use("Agg") # headless (non-interactive) backend, so mpl will not launch any GUI window

import matplotlib.pyplot as plt
import numpy as np
import os
import uuid

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("main.html")

@app.route("/calculate")
def show_calc_form():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    value = int(request.form['number'])
    return render_template("calculator.html", result=value**2)

plot_image_path = None
hist_path = None

@app.route("/plot", methods=["GET", "POST"])
def plot():
    global plot_image_path
    if request.method == "POST":
        print("from:",request.form)

        xleft = float(request.form["xleft"])
        xright = float(request.form["xright"])
        func = request.form.get("function", "sin")
        color = request.form.get("color", "blue")

        x = np.linspace(xleft, xright, 400)

        if func == "sin":
            y = np.sin(x)
        elif func == "cos":
            y = np.cos(x)
        elif func == "x2":
            y = x**2
        elif func == "sqrt":
            x = x[x >= 0]  # keep x >= 0
            y = np.sqrt(x)
        else:
            y = np.zeros_like(x)

        plt.figure()
        plt.plot(x, y, color=color, label=func)
        plt.title(f"{func} from {xleft} to {xright}")
        plt.legend()

        filename = f"plot_{uuid.uuid4().hex[:8]}.png"
        full_path = os.path.join("static", "images", filename)
        plt.savefig(full_path)
        plt.close()

        plot_image_path = full_path

    print("image path:", plot_image_path)
    return render_template("plotter.html", plot_image_path=plot_image_path, hist_path=hist_path)

@app.route("/histogram", methods=["POST"])
def histogram():
    global hist_path
    values_str = request.form.get("values", "")
    try:
        values_list = [float(v.strip()) for v in values_str.split(",") if v.strip() != ""]
    except ValueError:
        values_list = []

    if len(values_list) > 0:
        plt.figure()
        plt.hist(values_list, bins="auto", alpha=0.7, color="blue", edgecolor="black")
        plt.title("Histogram of Input Values")

        filename = f"hist_{uuid.uuid4().hex[:8]}.png"
        full_path = os.path.join("static", "images", filename)
        plt.savefig(full_path)
        plt.close()
        
        hist_path = os.path.join("static", "images", filename)

    return render_template("plotter.html", hist_path=hist_path, plot_image_path=plot_image_path)

if __name__ == '__main__':
    app.run(debug=True)