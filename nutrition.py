import json
import sqlite3
import sys
import fuzzyset

def find_food_nutrition(food_name):
    return find_nutrition(find_food(food_name))

def find_food(food):
    conn = sqlite3.connect('usda.sql3')
    search_clause = '%' + food + '%'
    c = conn.cursor()
    c.execute('SELECT id, long_desc FROM food WHERE long_desc LIKE ?', (search_clause,))
    strmatch = fuzzyset.FuzzySet()
    strmatch.add(food)

    best_score = -1
    best_food = ''
    best_id = -1

    for row in c:
        food_id = row[0]
        food_name = row[1].lower().split(',')[0]
        if strmatch.get(food_name) is None:
            continue
        score = strmatch.get(food_name)[0][0]

        if score > best_score and food_name.startswith(food):
            best_score = score
            best_food = row[1]
            best_id = food_id
        # if food_name.startswith(food):
            # print(row[1])

    # print(str(best_id) + " " + best_food)
    return (best_id, best_food)

def find_nutrition(food_id):
    conn = sqlite3.connect('usda.sql3')
    c = conn.cursor()
    c.execute("""
      SELECT
        name,
        units,
        amount
      FROM nutrition
      JOIN nutrient
      JOIN common_nutrient
      ON nutrition.food_id = ?
      AND nutrition.nutrient_id = nutrient.id
      AND nutrient.id = common_nutrient.id
    """, (food_id,))
    vals = {}
    for row in c:
      vals[row[0]] = str(row[2]) + ' ' + row[1]

    return vals
