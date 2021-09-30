import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

read_user_file =  pd.read_excel('wine.xlsx', sheet_name='Лист1', na_values=' ', keep_default_na=False)
user_dict = read_user_file.to_dict(orient='records')
sorted_wines = collections.defaultdict(list)
for wine in user_dict:
    category = wine['Категория']
    sorted_wines[category].append(wine)
sorted_wines = collections.OrderedDict(sorted(sorted_wines.items()))
actual_date = datetime.datetime.now().year
foundation_year = 1921
time_difference = actual_date-foundation_year

rendered_page = template.render(
    sorted_wines = sorted_wines,
    age = time_difference,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
