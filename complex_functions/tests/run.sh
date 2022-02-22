#!/bin/bash
coverage run -m pytest
rm -r spiralPrint.txt __pycache__
clear
coverage report