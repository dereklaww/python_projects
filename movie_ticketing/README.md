Name : Derek Pin Jie Law
unikey ; dlaw7849

# How i store and access the movie data
Movie data is written as a string and formatted into a list through 
split() function which made it easier to call different data when 
needed (name, time). The 'period's in the given names were changed 
to 'semicolon's as there were 'period's in the movie name, which 
contradicts the split(';') function. The movie data is joined back 
using join() function with 'period's connecting each data.

# How i perform error checking
Start by getting time input, check valid time format (hh:mm) by checking 
if ":" in input and length of input. Then check if input are digits and 
digits for 'hh' and 'mm' are between [0,23" and [0,59] respectively. 

# How i compare two different times
To compare two different times, the input time and movie time are converted 
into minutes and compared through loops. If movie time is greater than 
input time, then the movie data is printed.

# List of idioms used
- calling for command arguments
    - "if, else" functions used to validate command arguments
- search movies through [--show] command
    - "if, else" functions used to validate format and values of input time 
    - "for" loops and "if, else" are used to compare input time and movie time
- search movies through [--book] or [--group] command
    - 'while' loops are used to call for input of movie names
    - "while" loops and "if, else" functions are used to compare input 
    movie and movies from movie list
    - Boolean values are used to break out of nested loops
- booking seats and ordering popcorn
    - "while" loops are used to call for input by each person 
    in group bookings (popcorn order and size)
    - "while" loops and "if, else" functions are used to validate correct data types 
    and valid values of inputs (valid number of persons, inputs for y/n questions, 
    popcorn orders and size)
- itemizing details
    - "for" loops are used to itemize details of group bookings since the order 
    of each person is different (popcorn size and price).
- making payments
    - "if, else" functions to validate payment input values (sufficient amount 
    and divisible by 0.05)

# Comments 13/Sep/2023
- could use json key pair values to store movie details.
- functions could be implmented to improve readability

