import os
import json
import filecmp

data_path = "../logs/"
src_path = "../src/most_active_cookie.py"
output_path = "outputs/"
answer_path = "answers/"

with open("inputs.json") as file:
    inputs = json.load(file)

for input in inputs:
    id = input["test_num"]
    file_path = data_path + input["log_csv"]
    query = input["-d"]
    output_file = output_path + input["output_file"]
    answer_file = answer_path + input["answer_file"]
    os.system(f"python3 {src_path} {file_path} -d {query} > {output_file}")
    is_correct = filecmp.cmp(output_file, answer_file)
    if is_correct:
        print(f"test_{id} PASSED")
    else:
        print(f"test_{id} FAILED")
