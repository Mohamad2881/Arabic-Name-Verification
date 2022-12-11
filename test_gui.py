import tkinter
import requests
import json

from tkinter import filedialog

window = tkinter.Tk()
window.title("Name Verification Model")
window.geometry('840x500')


def get_response(end_point, name):
    # api endpoint for single input
    url = f'http://127.0.0.1:8000/{end_point}'
    

    if end_point == 'predict':
        # api params        
        params = {
        "Name": name
        }
    
    elif end_point == 'predict-batch':
        # api params
        params = {
            "name_list": name
        }

    # sending POST request
    r = requests.post(url = url, json=params)

    return r


def insert_data(dict_):
    for k, v in dict_.items():
        if k == 'score':
            v = round(v, 3)
        text.insert(tkinter.END, f'{k} = {v},  ')
    text.insert(tkinter.END, f' \n')


def predict_name(name=None):
    if name:
        text.delete('1.0', tkinter.END)
        r = get_response('predict', name)
        r_dict_ = json.loads(r.text)
        insert_data(r_dict_)

        text.insert(tkinter.END, f'\n\n Response Time: {r.elapsed.total_seconds()}')


        # for k, v in json.loads(r.text).items():
        #     if k == 'score':
        #         v = round(v, 3)
        #     text.insert(tkinter.END, f'{k} = {v},  ')
        #     print(k, v)

        return r.json


def open_txt():
    text_file = filedialog.askopenfilename( title='Open Text File', filetypes=(("Text Files", "*.txt"), ))
    
    with open(text_file, 'r', encoding='utf-8') as f:
        test_names = f.read().splitlines()
        
    r = get_response('predict-batch', test_names)
    r_dict = json.loads(r.text)['predictions']

    text.delete('1.0', tkinter.END)
    for dict_ in r_dict:
        insert_data(dict_)
    
    text.insert(tkinter.END, f'\n\n Response Time: {r.elapsed.total_seconds()}')

        # for k, v in dict_.items():
        #     if k == 'score':
        #         v = round(v, 3)
        #     text.insert(tkinter.END, f'{k} = {v},  ')
    

        

def predict_default():
    test_names = ["محمد أحمد شادى", 'باسم احمد حمادة', 'باسمم وحةد السد',
         'يتيلب يابثل ثتلى', 'محمد السعيد خليفة', 'مورجان أحمد مورجان', 'جزر جزر جزر', 'اسم المستخدم هنا' ]
   
    r = get_response('predict-batch', test_names)
    text.delete('1.0', tkinter.END) 
    r_dict = json.loads(r.text)['predictions']

    for dict_ in r_dict:
       insert_data(dict_)
        # for k, v in dict_.items():
        #     if k == 'score':
        #         v = round(v, 3)
        #     text.insert(tkinter.END, f'{k} = {v},  ')
    
    text.insert(tkinter.END, f'\n\n Response Time: {r.elapsed.total_seconds()}')

bg_color = '#03DAC6'

# Title
label = tkinter.Label(window, text='Arabic Name Verification', font=('Arial', 20), pady=30)
label.grid(row=0, column=0, columnspan=2, sticky='news')

# Name Label
name_lbl = tkinter.Label(window, text='Full Name: ', font=('Arial', 15), pady=20)
name_lbl.grid(row=1, column=0)

# Name TextBox
entry = tkinter.Entry(window, font=('Arial', 15))
entry.grid(row=1, column=1)

# Verify Button
button = tkinter.Button(window, text='Verify', font=('Arial', 15), command=lambda: predict_name(entry.get()), bg=bg_color)
button.grid(row=1, column=2, padx=10)

# Output Text
text = tkinter.Text(window, width=55, height=20, font=('Arial', 10))
text.grid(row=1, column=3, columnspan=2, padx=10)

# Run Default Button
run_def_btn = tkinter.Button(window, text='Run Default', font=('Arial', 15), command=predict_default, bg=bg_color)
run_def_btn.grid(row=2, column=3, pady=10)

# Browse Button
browse_btn = tkinter.Button(window, text='Browse txt', font=('Arial', 15), command=open_txt, bg=bg_color)
browse_btn.grid(row=2, column=4, pady=10)

window.mainloop()