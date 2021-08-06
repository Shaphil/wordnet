"""Update model (app) names"""

import json
import os


def transform(filename, app_name):
    updated_data = []
    with open(filename, encoding='utf-8') as f:
        content = f.read()
        data = json.loads(content)
        for item in data:
            model = item['model'].split(".")
            model[0] = app_name
            model = '.'.join(model)
            item['model'] = model
            updated_data.append(item)

    file_copy = filename.split(".")[0] + "_copy.json"
    with open(file_copy, 'w', encoding='utf-8') as f:
        json.dump(updated_data, f, ensure_ascii=False)

    try:
        print("Deleting file", filename)
        os.remove(filename)
    except Exception as e:
        print(e)

    os.rename(file_copy, filename)


def main():
    filename = 'senses.json'
    app_name = 'bangla'
    transform(filename, app_name)


if __name__ == '__main__':
    main()
