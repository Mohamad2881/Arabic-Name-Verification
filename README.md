# Arabic-Name-Verification

<!-- Installation -->
## Installation

run the following command to bulid docker image and start the server
```sh
docker-compose up --build -d
  ```
  
<!-- USAGES -->
## Usage
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


