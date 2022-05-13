# 361microservice
A microservice Python program for Holly Lucas for CS 361.

It calculates compound interest with monthly contributions. 

Here are the set variables:
interest_rate = .10 (10 percent)
compounds_per_year = 12 (monthly)
principal = 0 (for this use assume no principal investment) 

And here are the variables that the user can change:
monthly_contributions = $(user input) 
years = (user input) 

Given these five variables, my micro service spits out the total amount returned with interest. 

The microservice utilizes two txt pipelines. The data.txt pipeline accepts 2 inputs,monthly contributions and years. 
My program writes the output to result.txt

To test my program, first run compound_interest.py, then run test.py. 
Check the result.txt file to check for periodic changes.
