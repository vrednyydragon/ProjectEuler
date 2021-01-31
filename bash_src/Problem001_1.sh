#!/bin/bash
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
number1=1
number2=10
sum=0
while [ $number1 -lt $number2 ]
do
	if [ $((number1%3)) == "0"  ] || [ $((number1%5)) == "0"  ]
	then
		echo "number $number1 divided into 3 or 5"
		sum=$(( $sum + number1 ))
	fi
# number1=$(( $number1 + 1 ))
(( number1++ ))
# sum=$(( $sum + number1 ))
# echo "sum = $sum"
done
echo "sum = $sum"



	