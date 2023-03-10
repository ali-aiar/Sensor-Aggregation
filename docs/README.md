# Sensor Aggregation
Sensor Aggregation is app to get statics min, max, median, and avg from sensors’ values (temperature, humidity) group by room and day.
## Getting Started
### Prerequisites
What things do you need to install the software and how to install them
1. Python 3.6 or higher
2. If you are in windows, there is a chance to get an error because of the execution policy. If you get the error, run this program as an administrator
```console
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```
### Installation
1. Clone this repository
```bash
git clone https://github.com/ali-aiar/Sensor-Aggregation.git
```
2. Go to the main directory 
```bash
cd Sensor-Aggregation
```
3. Create a virtual environment 
```bash
python -m venv venv
```
4. Activate the virtual environment
```bash
source venv/bin/activate  # Linux or macOS
.\venv\Scripts\activate  # Windows
```
5. Install the required packages by running the following command:
```bash
pip install -r requirements.txt
```
6. Run the program by executing the following command:
```bash
python main.py
```
7. To deactivate the virtual environment, run:
```bash
deactivate
```
## Running the tests
To run the test you must be in the ./ directory. 
### Test the models
The test will use unittest library, to know if the model working as intended.
```bash
python -m unittest ./tests/test_models.py
```
### Test the controllers
The controllers use to manage the flow of data between models, and views. 
```bash
python -m unittest ./tests/test_controllers.py
```