from data_loaders import load_csv, load_json


csv_data: list[dict] = load_csv('data/test.csv')
json_data: list[dict] = load_json('data/test.json')

print(csv_data)
print(json_data)