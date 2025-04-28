from flask import Flask, render_template, request
from ScheduleMixer import find_ingredient_path_simulated_real, base_products, effects_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        start_product = request.form.get("start_product")
        selected_effects = request.form.getlist("effects")
        path = find_ingredient_path_simulated_real(start_product, set(selected_effects))
        result = path
    return render_template("index.html", base_products=base_products, effects=list(effects_data.keys()), result=result)

if __name__ == "__main__":
    app.run(debug=True)
