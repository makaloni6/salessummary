import pickle 
import os
import re
import csv
from utils import acc_list

def get_data(acc:str) -> dict:
    with open('sales_data/{}_order_history.pickle'.format(acc), 'rb') as f:
        data = pickle.load(f)

    count_dict = {}
    for d in data:
        code = data[d]['ItemId']
        if code in count_dict:
            count_dict[code] += 1
        else:
            count_dict[code] = 1

    return count_dict

def get_codedict(acc:str) -> dict:
    with open('pickle/code_dict_{}.pickle'.format(acc), 'rb') as f:
        code_dict = pickle.load(f)
    code_dict = {v: k for k, v in code_dict.items()}
    return code_dict

def convert_data(data:dict, code_dict:dict) -> dict:
    convert_dict = {}
    for d, v in data.items():
        a = code_dict[d]
        convert_dict[a] = v
    
    
    return convert_dict

def update_count(count_dict:dict, count:dict) -> dict:
    for k, v in count.items():
        if k in count_dict:
            count_dict[k] += v
        else:
            count_dict[k] = v

    return count_dict

def write_csv(count_history:dict) -> None:
    with open('pickle/title.pickle', 'rb') as f:
        title = pickle.load(f)
    with open('sales_rank.csv', 'w') as f: 
        writer = csv.writer(f)
        for k, v in count_history.items():
            writer.writerow([k, v, title[k]])
            

def main():
    count_dict = {}
    for acc in acc_list:
        data = get_data(acc)
        code_dict = get_codedict(acc)
        converted_data = convert_data(data, code_dict)

        updata_count(count_dict, converted_data)

    write_csv(count_dict)

if __name__ == '__main__':
    main()
   