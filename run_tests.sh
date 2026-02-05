#!/bin/bash
pip install -r requirements.txt
coverage run --source=SimpleMath,SimpleWireless -m unittest discover tests
coverage report -m
