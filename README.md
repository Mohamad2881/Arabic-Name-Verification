# Arabic-Name-Verification
Given a Full Name, predicts if it is a valid name or a fake name (garbage).

<!-- Installation -->
## Installation

run the following command to bulid docker image and start the server
```sh
docker-compose up --build -d
  ```
  
<!-- USAGES -->
## Usage
- To run the test GUI
```sh
python test_gui.py
  ```

- To run the default test cases
```sh
python test_script.py
  ```
  
- To Enter a test Name
```sh
python test_script.py -n "First_name Middle_name Last_name"
```
  
- To Enter a test file (.txt). This will output a response.txt containing the results
```sh
python test_script.py -p FilePath.txt
```

- To run using  Swagger UI  

  * http://127.0.0.1:8000/docs

<!-- RESULTS -->
## Results
![out](https://user-images.githubusercontent.com/68511263/206886162-9d342b4c-ac7f-4a40-bf23-c01ce1a50f08.png)

![out1](https://user-images.githubusercontent.com/68511263/206886306-c2c26d51-6679-41ec-9369-497d2de9884f.png)



