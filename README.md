# HW3
Team Members: Zeplyn Kelley, Trevor Young

This project shows how to use Flask and PostgreSQL to insert new rows and show unique fruits in tables for a database.

## Quick Start
### Local Test Setup
Install the virtual environment:
```
sudo apt-get install python3-venv
```
Create the virtual environment:
```
python3 -m venv python_venv
```
Activate the virtual environment:
```
source python_venv/bin/activate
```
Install server requirements:
```
pip3 install -r requirements.txt
```
Start server:
```
python3 main.py
```

## Accessing Server
Insert a new row (5, 'Cherry') into basket_a:
```
127.0.0.1:5000/api/update_basket_a
```
Show unique fruits in basket_a and basket_b:
```
127.0.0.1:5000/api/unique
```
