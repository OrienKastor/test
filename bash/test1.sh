#!/bin/bash

cp $1 $2

# Verify the copy worked:

echo Details for $2
ls -lh $2

myVar=Hello
myVar2=2

echo $myVar $myVar2
