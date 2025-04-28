from flask import Flask, render_template, request
from mixer_core import base_products, effects_mapping, find_ingredient_path_simulated_real

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        selected_product = request.form.get('base_product')
        selected_effects = request.form.getlist('desired_effects')
        
        if selected_product and selected_effects:
            desired_effects_set = set(selected_effects)
            path = find_ingredient_path_simulated_real(selected_product, desired_effects_set)
            if path:
                result = [(ingredient, effect) for ingredient, effect in path]
            else:
                result = []  # No valid path found

    return render_template('index.html', base_products=base_products, effects_list=get_effects_list(), result=result)

def get_effects_list():
    effects_set = set(unlocks_effect for (_, _), unlocks_effect in effects_mapping.items())
    return sorted(effects_set)

if __name__ == '__main__':
    app.run(debug=True)

