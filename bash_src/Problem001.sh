#!/bin/bash
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
number1=1
number2=10
#for(( i=$number1; i<=$number2; i++))
for (( i=$number1 ; i <= $number2 ; ++i ))
do
	# echo "number $i%3 = <"$((i%3))">"
	#div3=$(($i%3))
	# echo "div1 = $div1"
	if [[ $((i%3)) == "0" ]] 
	then
		echo "number $i divided into 3"
	elif [ $((i%5)) == 0 ] 
	then
		echo "number $i divided into 5"
	fi
done