# Nathan Bonnes
# 5/5/22
# This is a micro-service python program written for my CS361 partner Holly Lucas.

# To get the correct output, run compound_interest.py and then send data.txt
# 2 variables of type 'str', delineated by a space. The output will be written to result.txt with type 'str'.

import time

# GLOBAL VARS
interest_rate = .10
compounds_per_year = 12
principal = 0


def get_variables():
    # listen to data.txt file.
    data_file = open('data.txt', 'r')
    line = data_file.readline()
    print(line)
    data = line.split()
    data_file.close()

    # once a line is read, process data.
    # set variables, calculate future value with formula function below.
    if line:
        monthly_contributions = int(data[0])
        years = int(data[1])
        data_file.close()
        future_value = compound_interest_formula(monthly_contributions, years)
        print(future_value)
        result_file = open('result.txt', 'w')
        result_file.write(str(future_value))
        time.sleep(3)
        result_file.close()
        return


# compound_interest_formula taken from https://structx.com/annual_compound_interest_with_contributions.html
def compound_interest_formula(monthly_contribution, years):
    future_value = (monthly_contribution * (((1 + interest_rate / compounds_per_year) **
                                             (years * compounds_per_year)) - 1)) / (interest_rate / compounds_per_year)
    return future_value


# Testing
if __name__ == "__main__":
    while True:
        time.sleep(3)
        get_variables()
