#!/bin/bash

################################################################################################

#Script name		      :apibscript.sh

#Description		      :Access data from API and organize it in a csv file.

#Author			          :Faye Beerom-Henry

#Date			            :September 15, 2022

#Programming Language :Python, Bash

#API                  :OpenWeatherMap

################################################################################################

# run script
python3 main.py



# data captured in csv file created

echo "--------------------------------"

cat weather.csv | column -s, -t

echo "--------------------------------"


