# electric-field-and-equipotentials-mapping-lab

## Instructions
**Assuming python3 and pip are already installed**
### Virtual Environment 
- To prevent conflicts with globally installed packages, it is recommended to run everything below in a virtual environment. 

Set up a virtual environment by running the following in your terminal:
```
python -m venv env 
# replace env with anything you want 
# If the above does not work, run with python3 (this may be the case if a version of python2 is also installed)
```

To enter your virtual environment, run the following:
```
. env/bin/activate
```

To exit your virtual environment, run the following:
```
deactivate
```

### Dependencies 
Run the following line in your virtual environment
```
pip install -r doc/requirements.txt
```

### Run the app
Run the following line in your virtual environment
```
python lab0.py
```

## What you're supposed to see
![alt text](https://raw.githubusercontent.com/raymondlee00/electric-field-and-equipotentials-mapping-lab/master/contour-map.PNG)