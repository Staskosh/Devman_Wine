import argparse
import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    parser = argparse.ArgumentParser()
    parser.add_argument('user_file_link', nargs='?', default='wine.xlsx')
    args = parser.parse_args()
    user_file =  pd.read_excel(args.user_file_link, sheet_name='Лист1', na_values=' ', keep_default_na=False)
    user_file = user_file.to_dict(orient='records')
    grouped_wines = collections.defaultdict(list)
    for wine in user_file:
        category = wine['Категория']
        grouped_wines[category].append(wine)
    grouped_wines = collections.OrderedDict(sorted(grouped_wines.items()))
    actual_date = datetime.datetime.now().year
    foundation_year = 1921
    age = actual_date-foundation_year

    rendered_page = template.render(
        grouped_wines = grouped_wines,
        age = age,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()
