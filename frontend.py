# A simple script to calculate BMI
from pywebio.input import input, TEXT
from pywebio.output import put_text, put_table

def flight_covid():
    put_text('we shoud put some relevant covid milestones here to aid in data exploration')
    query = input("What is your query", type=TEXT)

    #connect database here

    #make query request here using the query variable

    #output the query here
    put_table([
        ['header 1', 'header 2', '...'],
        ['value 1', 'value 2', '...']
    ])

if __name__ == '__main__':
    flight_covid()