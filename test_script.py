import argparse
import numpy as np
import requests


def predict_name(name=None):
    
    # api endpoint for single input
    url = 'http://127.0.0.1:8000/predict'

    # api params
    params = {
    "Name": name
    }

    # sending POST request
    r = requests.post(url = url, json=params)

    # Time Elaspsed
    print('Time delta between the Request was sent and the Response was received.', r.elapsed.total_seconds())
    print('result: ', r.text)


def predict_from_file(path):
    # api endpoint for single input
    url = 'http://127.0.0.1:8000/predict-batch'

    if path is None:
        test_names = ["محمد أحمد شادى", 'باسم احمد حمادة', 'باسمم وحةد السد', 'يتيلب يابثل ثتلى' ]
        
    else:
        # read data
        with open(path, 'r', encoding='utf-8') as f:
            test_names = f.read().splitlines()

    # api params
    params = {
         "name_list": test_names
    }
    
    # sending POST request
    r = requests.post(url = url, json=params)

    # Time Elaspsed
    print('Time delta between the Request was sent and the Response was received = ',
     r.elapsed.total_seconds(), '\n')

    # save response into txt file
    with open("response.txt", "w", encoding='utf-8') as f:
        f.write(r.text)
        print('result: ', r.text)


if __name__=='__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--name', help='Name', type=str)
    parser.add_argument('-p', '--path', help='txt file path', type=str)

    args = parser.parse_args()
    if args.name:
        predict_name(args.name)
    else:
        predict_from_file(args.path)


