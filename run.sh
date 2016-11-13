#!/bin/sh
SCRIPT="main.py"
if [[ "$1" == 'e' ]]; then
	SCRIPT="example.py"
	echo $1
fi
python app/$SCRIPT
