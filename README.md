# Address parser

Simple command line tool to parse street and housenumber data from an input string:

Input: string of address

Output: string of street and string of street-number as JSON object

## Instructions

* Create a Python 3.8.5 virtual environment. 
* Add the directory containing this `README.md` file to your `PYTHONPATH`:
```bash
export PYTHONPATH="${PYTHONPATH}:path/to/directory
```
* Install required libraries:
```bash
pip install requirements.txt
```

### To run unit tests
```bash
pytest test.py
```

### To use CLI tool
```bash
python main.py "Winterallee 3" -> {"street": "Winterallee", "housenumber": "3"}
python main.py "Auf der Vogelwiese 23 b" -> {"street": "Auf der Vogelwiese", "housenumber": "23 b"}
python main.py "Calle 39 No 1540" -> {"street": "Calle 39", "housenumber": "No 1540"}
```

# Approach taken
I decided to use the opensource https://github.com/openvenues/pypostal library for 
address parsing for a number of reasons:

* Correctly parsing data from arbitrary strings (which is pretty much what 
international addresses are in practice) is a very difficult problem. So it's better 
to use existing tools to tackle the job than developing your own ad hoc solution.
* This approach produces a solid, production-grade solution using opensource software
in just a few lines of code.
* I have heard Natural Language Processing experts recommend
this address parsing tool as the best available in the past.
