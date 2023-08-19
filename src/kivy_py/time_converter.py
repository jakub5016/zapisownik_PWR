def time_converter(time):
    # Converts time to a decimal number that tells us how many pixels we should move a button
    # Time have to be given in special format:
    #   Hours should start at 0 if it's one number, 7:30 = 07:30
    #   Full size of string should = 5

    try:
        hour = int(time[0:2])
        minute = int(time[3:5])

    except:
        print(time[0:2])
        return("Bad time format")

    finally:
        timer = 60 *hour + minute

        return int(((timer- 420)*400/1290))

# time_converter("07:30")
