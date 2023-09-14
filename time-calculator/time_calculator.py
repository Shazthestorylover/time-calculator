def add_time(start, duration, day_of_week=False):
    #
    #----------------------------------------------------Variables------------------------------------------------------
    # Used to associate a day of the week with an index.
    days_of_the_week_dict = {"sunday":0, "monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6}

    # Used to keep track of what day of the week the new time may be if the user inputs a day.
    days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Take the time in the start variable and split it into hours and mins, and the time of day.
    colon_pos = start.find(":")
    start_hour = int(start[colon_pos-1: :-1])
    #print(f'start_hour: {start_hour}')
    start_mins_list = start[colon_pos+1: ].split(" ")
    start_mins = int(start_mins_list[0])
    #print(f'start_mins: {type(start_mins)}')
    time_period = start_mins_list[1]

    # Take the hours and mins in the duration variable and split it into hours and mins
    #colon_pos_2 = duration.find(":")
    dur_list = duration.split(":")
    #print(f'dur_list: {dur_list}')
    dur_hour = int(dur_list[0])
    dur_mins = int(dur_list[1])

    # Used to convert "AM" to "PM", and vice versa (PM to AM)
    time_period_flip = {"AM":"PM", "PM":"AM"}

    # Used to convert the number of hours into days (e.g. 120 hours --> 5 days)
    num_of_days = int(dur_hour / 24)
    #--------------------------------------------------------------------------------------------------------------------
    #
    
    # Add the hours and mins together to get a new time.
    new_mins = int(start_mins + dur_mins)

    # Chech to see if the mins are greater than 60.
    if new_mins >= 60:
        # Increase the start hour by 1, then add the remainder of the number of mins greater than 60
        # to the new mins.
        start_hour += 1
        new_mins %= 60
    # Calculate the new hour for the new time.
    new_hour = int(start_hour + dur_hour) % 12
    # Used to keep track of how many times the time period alternates between "AM" and "PM"
    flip_count = int((start_hour + dur_hour) / 12)

    # if the new mins have a double digit answer:
    if new_mins > 9:
        # Then, leave it be.
        new_mins = new_mins
    else:
        # Add a "0" digit in front of the minute digit so the answer will display as (e.g. "05" instead of "5")
        new_mins = f'0{new_mins}'

    # if the new hour is equal to 0:
    if new_hour == 0:
        # then the new hour is in the 12 to 1 range.
        new_hour = 12
    else:
        # the digit remains the same.
        new_hour = new_hour

    # if the starting time is in the evening/night and the new hour ends up being 12
    # or greater than 12.
    if time_period == "PM" and start_hour + (dur_hour % 12) >= 12:
        # increase the number of days by 1.
        num_of_days += 1

    # If the number for time of flips between AM and PM
    #i.e. start in AM range and ends in PM range, and vice versa.
    if flip_count % 2 == 1:
        # then change the time period (e.g. AM) into the new time period (e.g. PM)
        time_period = time_period_flip[time_period]
    else:
        # Leave the time period as it is.
        time_period = time_period

    # Format the answer into the desired output.
    new_time = f'{new_hour}:{new_mins} {time_period}'

    # If the user enters a day of the week:
    if day_of_week:
        # Convert the day of the week to lowercase so that it can be used by the user
        # no matter how the user enters the day.
        day_of_week = day_of_week.lower()
        # Get the index for the day of the week entered by the user, which has only 7
        #options ranging from 0 - 6.
        i = int((days_of_the_week_dict[day_of_week]) + num_of_days) % 7
        # Use the index to get the day of the week for the new time.
        new_day = days_of_the_week[i]
        # Add the new day to the time.
        new_time += f', {new_day}'

    # If number of days for the new time is 1
    if num_of_days == 1:
        # Output (next day) beside the answer.
        return f'{new_time} (next day)'
    # If the number of days is greater than 1:
    elif num_of_days > 1:
        # Output how many days later the new time will be in.
        return f'{new_time} ({str(int(num_of_days))} days later)'

    return new_time