#!/usr/bin/env bash

for name in FOOD_DES NUT_DATA WEIGHT FD_GROUP NUTR_DEF; do
  wget https://www.ars.usda.gov/ARSUserFiles/80400525/Data/SR/SR28/asc/${name}.txt
done
