#!/usr/bin/python3
# Date: 27.07.24
# Author: Stocklasser
# Diplomarbeit, Optimierung einer Schweisspruefanlage
# json functions

import json
import pandas as pd


def json_writer(json_name, variable, value, json_path):
    data = pd.read_json(json_path + json_name + ".json", encoding="utf-8")
    index = data.index[data['var'] == variable].tolist()

    if index:
        data.at[index[0], 'val'] = value
    else:
        new_row = pd.DataFrame([{'var': variable, 'val': value}])
        data = pd.concat([data, new_row], ignore_index=True)
        print("NEW ROW ADDED")

    with open(json_path + json_name + ".json", "w", encoding="utf-8") as file:
        data.to_json(file, orient="records", indent=2, force_ascii=False)


def json_reader(json_name, variable, json_path):
    with open(json_path + json_name + ".json", encoding="utf-8") as file:
        data = pd.read_json(file)
    if variable in data['var'].values:
        read_value = data.loc[data['var'] == variable, "val"].values[0]
        return read_value
    else:
        print("ERROR WHILE TRYING TO READ")
        print(json_name)
        print(json_path)
        print(variable)


def json_creator(json_name, json_path, first_var, first_val):
    data = [
        {
            'var': first_var,
            'val': first_val,
        }
    ]
    with open(f"{json_path}{json_name}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
