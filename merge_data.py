import json
import os


def merge_json_files(logs):
    prepared_data = {'model1': [], 'model2': [], 'model3': []}
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            # Extract the model number from the filename
            model_number = filename.split('.')[0][-1]
            with open(os.path.join(directory_path, filename), 'r') as file:
                data = json.load(file)
                # Append data to the corresponding model's list
                prepared_data[f'model{model_number}'].append(data)
    return prepared_data


directory_path = "logs"
output_file = "merged.json"
merged_data = merge_json_files(directory_path)
with open(output_file, 'w') as outfile:
    json.dump(merged_data, outfile)

print('Ok! Data is merged.')