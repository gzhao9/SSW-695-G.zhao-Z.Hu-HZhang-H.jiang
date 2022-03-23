from flask import Flask,make_response,json,render_template
import json
import get_food_nutrient

app = Flask(__name__)

@app.route('/foodNutrient')
def foodNutrient():
    foodName = 'Apple'
    ans = get_food_nutrient.call_API(foodName, 'JkdjMHjQobEeEAVSkii5eg1n5NtTKH0AAL0FgXBb')
    nutrientProtein = ans['foods'][1]['foodNutrients'][0]['value']
    nutrientFat = ans['foods'][1]['foodNutrients'][1]['value']
    nutrientCarbohydrate = ans['foods'][1]['foodNutrients'][2]['value']
    data = {
        'food name:': foodName,
        'nutrient protein:': nutrientProtein,
        'nutrient fat': nutrientFat,
        'nutrient Carbohydrate': nutrientCarbohydrate
    }
    # return data.json()
    return make_response(data)

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()