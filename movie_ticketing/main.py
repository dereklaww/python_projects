# Name: Derek Pin Jie Law
# unikey: dlaw7849

import sys

# Greeting message
print("""-=-=-=-=-=-=-=-=-=-=-=-=-=-=
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~ Welcome to Pizzaz cinema ~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
print('')

# Movie list
movie1 = 'The Shining; 1980; 2h 26m; 10:00; Room 1'.split('; ')
movie2 = 'Your Name; 2016; 1h 52m; 13:00; Room 1'.split('; ')
movie3 = "Fate/Stay Night: Heaven's Feel - III. Spring Song; 2020; 2h 0m; 15:00; Room 1".split(
    '; ')
movie4 = "The Night Is Short, Walk on Girl; 2017; 1h 32m; 17:30; Room 1".split(
    '; ')
movie5 = "The Truman Show; 1998; 1h 47m; 19:30; Room 1".split('; ')
movie6 = "Genocidal Organ; 2017; 1hr 55m; 21:45; Room 1".split('; ')

movie7 = "Jacob's Ladder; 1990; 1h 56m; 10:00; Room 2".split('; ')
movie8 = "Parasite; 2019; 2h 12m; 12:15; Room 2".split('; ')
movie9 = "The Dark Knight; 2008; 2h 32min; 14:45; Room 2".split('; ')
movie10 = "Blade Runner 2049; 2017; 2h 44m; 17:45; Room 2".split('; ')
movie11 = "The Mist; 2007; 2h 6m; 21:00; Room 2".split('; ')
movie12 = "Demon Slayer: Mugen Train; 2020; 1h59min; 23:20; Room 2".split('; ')

movie13 = "The Matrix; 1999; 2h 16m; 10:00; Room 3".split('; ')
movie14 = "Inception; 2010; 2h 42m; 11:30; Room 3".split('; ')
movie15 = "Shutter Island; 2010; 2h 19m; 14:30; Room 3".split('; ')
movie16 = "Soul; 2020; 1hr 40m; 17:00; Room 3".split('; ')
movie17 = "Mrs. Brown; 1997; 1h 41min; 19:00; Room 3".split('; ')
movie18 = "Peppa Pig: Festival of Fun; 2019; 1h 8min; 21:00; Room 3".split(
    '; ')
movie19 = "Titanic; 1997; 3h 30min; 22:15; Room 3".split('; ')

movie = [movie1, movie2, movie3, movie4, movie5, movie6, movie7,
         movie8, movie9, movie10, movie11, movie12, movie13, movie14, movie15, movie16,
         movie17, movie18, movie19]

# Check valid commands
if len(sys.argv) > 1:
    com = sys.argv[1]
else:
    exit('Usage: python3 pizzaz.py [--show <timenow> | --book | --group]')

if (len(sys.argv) == 2 and (com == '--book' or com == '--group')) \
        or (len(sys.argv) == 3 and (com == '--show')):
    # Valid command
    pass
else:
    print('Sorry. This program does not recognise the switch options. ')
    print('')
    exit('Bye.')

# Switch command = [show]
if com == '--show':
    time = sys.argv[2]
    invalid_time = False

    # Check for ":" and length
    if list(time)[2] == ':' and len(time) == 5:
        time_input = time.split(':')

        # Check for digit input
        if time_input[0].isdigit() == True\
                and time_input[1].isdigit() == True:
            time_list = list(int(i)for i in time_input)

            # Check for valid values
            if 0 <= time_list[0] <= 23 and\
                    0 <= time_list[1] <= 59:
                # If true convert input time to minutes
                time_in_min = time_list[0]*60 + time_list[1]

                for i in range(0, len(movie)):
                    # Convert movie time to minutes
                    movie_time = movie[i][3].split(':')
                    t = list(int(j) for j in movie_time)
                    t_in_min = t[0]*60 + t[1]

                    # Compare movie time to input time in minutes
                    if t_in_min >= time_in_min:
                        print('. '.join(movie[i]))
                    else:
                        pass
            else:
                invalid_time = True
        else:
            invalid_time = True
    else:
        invalid_time = True

    if invalid_time == True:
        print('Sorry. This program does not recognise' +
              ' the time format entered.')

    # End of [show] function
    print('')
    exit('Bye.')

# Switch command = [book]
if com == '--book':
    num_person = 1
    break_all = False

    # Search for movie
    while break_all == False:
        invalid_name = False
        movie_input = list(input('What is the name of the movie' +
                                 ' you want to watch? '))

        i = 0
        j = 0
        valid_movie = False

        while i < len(movie) and valid_movie == False:

            # Check matching length in input and movie
            if len(movie_input) == len(movie[i][0]):
                while j < len(movie[i][0]):

                    # Check matching letters in input and movie
                    if movie_input[j].lower() == \
                            list(movie[i][0])[j].lower():
                        j += 1

                        # Matching letters and length
                        if j == len(movie[i][0]):
                            correct_movie = movie[i]
                            break_all = True
                            valid_movie = True
                            break
                    else:
                        # Letters in input and movie do not match
                        j = 0
                        i += 1
                        if i == len(movie):
                            invalid_name = True
                        break
            else:
                # Length of input and movie do not match
                i += 1
                if i == len(movie):
                    invalid_name = True

        if invalid_name == True:
            while True:
                continue_name = input('Sorry, we could not find that movie.' +
                                      ' Enter Y to try again or N to quit. ').lower()

                if continue_name == 'y' or continue_name == 'n':
                    break

            if continue_name == 'n':
                print('')
                exit('Bye.')

            if continue_name == 'y':
                continue

# Ordering popcorn - individual
    if invalid_name == False:
        while True:
            popcorn_order = input('Would you like to order popcorn?' +
                                  ' Y/N ').lower()
            if popcorn_order == 'y' or popcorn_order == 'n':
                break

        if popcorn_order == 'y':
            while True:
                popcorn_size = input('You want popcorn. ' +
                                     'What size Small, Medium or Large? (S/M/L) ').lower()
                if popcorn_size == 's'\
                        or popcorn_size == 'm'\
                        or popcorn_size == 'l':
                    break

            # Popcorn pricing - individual
            if popcorn_size == 's':
                popcorn_price = 3.50
                popcorn_size_ls = ['Small']
                popcorn_price_ls = ['3.50']

            if popcorn_size == 'm':
                popcorn_price = 5.00
                popcorn_size_ls = ['Medium']
                popcorn_price_ls = ['5.00']

            if popcorn_size == 'l':
                popcorn_price = 7.00
                popcorn_size_ls = ['Large']
                popcorn_price_ls = ['7.00']

        if popcorn_order == 'n':
            popcorn_size_ls = [' ']
            popcorn_price = 0

# Seat allocation - individual
        print('')
        print('The seat number for person 1 is #17')
        print('')

# Ticket_pricing = individual
    if (int((correct_movie[3].split(':'))[0])) < 16:
        ticket_price = 13.00
        ticket_time_ls = ['before 16:00']
        ticket_price_ls = ['13.00']

    elif (int((correct_movie[3].split(':'))[0])) >= 16:
        ticket_price = 15.00
        ticket_time_ls = ['from 16:00']
        ticket_price_ls = ['15.00']


# Switch command = [group]
if com == '--group':

    # Search for movie
    break_all = False
    while break_all == False:
        invalid_name = False
        movie_input = list(input('What is the name of' +
                                 ' the movie you want to watch? '))

        i = 0
        j = 0
        valid_movie = False

        while i < len(movie) and valid_movie == False:
            # Check matching length in input and movie
            if len(movie_input) == len(movie[i][0]):

                while j < len(movie[i][0]):
                    # Check matching letters in input and movie
                    if movie_input[j].lower() == \
                            list(movie[i][0])[j].lower():
                        j += 1

                        # Matching letters and length
                        if j == len(movie[i][0]):
                            correct_movie = movie[i]
                            break_all = True
                            valid_movie = True
                            break
                    else:
                        # Letters in input and movie do not match
                        j = 0
                        i += 1
                        if i == len(movie):
                            invalid_name = True
                        break
            else:
                # Length of input and movie do not match
                i += 1
                if i == len(movie):
                    invalid_name = True

        if invalid_name == True:
            while True:
                continue_name = input('Sorry, we could not find that movie.' +
                                      ' Enter Y to try again or N to quit. ').lower()
                if continue_name == "y" or continue_name == "n":
                    break

            if continue_name == 'n':
                print('')
                exit('Bye.')
            if continue_name == 'y':
                continue

# Ticket booking for group
        # Check valid number of people
        while True:
            print('')
            num_person = int(
                input('How many persons will you like to book for? '))
            print('')

            if num_person <= 1:
                continue_num = input('Sorry, you must have at least' +
                                     ' two customers for a group booking.' +
                                     ' Enter Y to try again or N to quit. ').lower()

                if continue_num == "n":
                    print('')
                    exit('Bye.')
            else:
                break

        # Room capacity
        if correct_movie[4] == 'Room 1':
            room_capacity = 18
        elif correct_movie[4] == 'Room 2':
            room_capacity = 68
        elif correct_movie[4] == 'Room 3':
            room_capacity = 21

        # Check room capacity
        if num_person <= room_capacity:
            pass
        else:
            while True:
                continue_seat = input('Sorry, we do not have enough space' +
                                      ' to hold {} people in the theater room of {} seats.'
                                      .format(num_person, room_capacity) +
                                      ' Enter Y to try a different movie name or N to quit. ').lower()

                if continue_seat == "y" or continue_seat == "n":
                    break

            if continue_seat == 'n':
                print('')
                exit('Bye.')
            if continue_seat == 'y':
                break_all = False

# Ticket pricing - group
    if (int((correct_movie[3].split(':'))[0])) < 16:
        ticket_price = 13.00
        ticket_time_ls = ['before 16:00']*num_person
        ticket_price_ls = ['13.00']*num_person

    elif (int((correct_movie[3].split(':'))[0])) >= 16:
        ticket_price = 15.00
        ticket_time_ls = ['from 16:00']*num_person
        ticket_price_ls = ['15.00']*num_person

    ticket_price *= num_person


# Ordering popcorn - group
    count_s = 0
    count_m = 0
    count_l = 0
    ps_ls = []
    popcorn_size_ls = []
    popcorn_price_ls = []

    for i in range(1, num_person+1):
        ps_ls.append(str(i))
        while True:
            popcorn_order = input('For person {},'.format(i) +
                                  ' would you like to order popcorn? Y/N ').lower()
            if popcorn_order == 'y' or popcorn_order == 'n':
                break

        if popcorn_order == 'y':
            while True:
                popcorn_size = input('Person {} wants popcorn.'.format(i) +
                                     ' What size Small, Medium or Large? (S/M/L) ').lower()

                if popcorn_size == 's'\
                        or popcorn_size == 'm'\
                        or popcorn_size == 'l':
                    break

            if popcorn_size == 's':
                count_s += 1
                popcorn_size_ls.append('Small')
                popcorn_price_ls.append('3.50')

            elif popcorn_size == 'm':
                count_m += 1
                popcorn_size_ls.append('Medium')
                popcorn_price_ls.append('5.00')

            elif popcorn_size == 'l':
                count_l += 1
                popcorn_size_ls.append('Large')
                popcorn_price_ls.append('7.00')

        elif popcorn_order == 'n':
            popcorn_size_ls.append(' ')
            popcorn_price_ls.append(' ')

# Popcorn pricing - group
    price_s = 3.50 * count_s
    price_m = 5.00 * count_m
    price_l = 7.00 * count_l

    popcorn_count = count_s + count_m + count_l
    popcorn_price = price_s + price_m + price_l

# Seat allocation - group
    for i in range(1, num_person+1):
        seat_number = 2*i-1
        print('The seat number for person {} is #{}'.format(i, seat_number))

# Calculating price and itemise details
initial_cost = ticket_price + popcorn_price

# Print receipt - individual
if num_person == 1:
    final_cost = initial_cost
    print('For 1 person, the initial cost is ${:.2f}'.format(initial_cost))
    print(' Person 1: Ticket {}'.format(ticket_time_ls[0]).ljust(34, ' ') +
          '$' + '{}'.format(ticket_price_ls[0]).rjust(5, ' '))

    if popcorn_size_ls[0] != ' ':
        print(' Person 1: {} popcorn'.format(popcorn_size_ls[0]).ljust(34, ' ') +
              '$' + '{}'.format(popcorn_price_ls[0]).rjust(5, ' '))
    print('')
    print(' No discounts applied'.ljust(34, ' ') + '$' + '0.00'.rjust(5, ' '))
    print('')

# Print receipt - group
if num_person >= 2:
    print('For {} persons, the initial cost is ${:.2f}'
          .format(num_person, initial_cost))
    for i in range(0, num_person):
        print(' Person {}: Ticket {}'.format(ps_ls[i], ticket_time_ls[i]).ljust(34, ' ') +
              '$' + '{}'.format(ticket_price_ls[i]).rjust(5, ' '))
        if popcorn_size_ls[i] == ' ':
            continue
        else:
            print(' Person {}: {} popcorn'.format(ps_ls[i], popcorn_size_ls[i]).ljust(34, ' ') +
                  '$' + '{}'.format(popcorn_price_ls[i]).rjust(5, ' '))

    # Group discounts
    if initial_cost >= 100.00:
        dis_ticket = ticket_price*0.1
        dis_pop = popcorn_price*0.2
        final_cost = initial_cost - dis_ticket - dis_pop

        print('')
        print(' Discount applied tickets x{}'.format(num_person).ljust(33, ' ') +
              '-$' + '{:.2f}'.format(dis_ticket).rjust(5, ' '))
        print(' Discount applied popcorn x{}'.format(popcorn_count).ljust(33, ' ') +
              '-$' + '{:.2f}'.format(dis_pop).rjust(5, ' '))
        print('')

    else:
        print('')
        print(' No discounts applied'.ljust(34, ' ') +
              '$' + '0.00'.rjust(5, ' '))
        print('')
        final_cost = initial_cost

# Final price
print('The final price is'.ljust(34, ' ') +
      '$' + '{:.2f}'.format(final_cost).rjust(5, ' '))
print('')

# Transact and give change
# Check valid payment
while True:
    payment_received = float(input('Enter the amount paid: $'))
    if (payment_received*100) % 5 != 0:
        print('The input given is not divisible by 5c. Enter a valid payment.')
    elif payment_received < final_cost:
        diff_payment = final_cost - payment_received
        print('The user is ${:.2f} short.'.format(diff_payment) +
              ' Ask the user to pay the correct amount.')
    else:
        break

# Print change
change = payment_received - final_cost
print('Change: ${:.2f}'.format(change))

# Print currency
count_100d = 0
count_50d = 0
count_20d = 0
count_10d = 0
count_5d = 0
count_2d = 0
count_1d = 0
count_50c = 0
count_20c = 0
count_10c = 0
count_5c = 0

currency = ['$100', '$50', '$20', '$10', '$ 5',
            '$ 2', '$ 1', '50c', '20c', '10c', ' 5c']
count_currency = [count_100d, count_50d, count_20d, count_10d, count_5d,
                  count_2d, count_1d, count_50c, count_20c, count_10c, count_5c]
value_currency = [100, 50, 20, 10, 5,
                  2, 1, 0.50, 0.20, 0.10, 0.05]

i = 0
while i < len(currency):
    if change >= float(value_currency[i]):
        count_currency[i] = change // value_currency[i]
        change %= value_currency[i]
        print(' {}: {}'.format(currency[i], int(count_currency[i])))

    i += 1

# End of program
print('')
exit('Bye.')
