import datetime


def main():
    # GET go home time from user
    go_home_time = input("What time do you want to go home? (HH:MM) ")
    go_home_time = datetime.datetime.strptime(go_home_time, "%H:%M").time()
    minutes = calculate_time_until_go_home(go_home_time)
    if(minutes < 0):
        print("You should have left already!")
        return
    hours, minutes = minutes_to_hours_minutes(minutes)
    print("You will go home at: {}, Time until go home: {} hours and {} minutes until home".format(go_home_time, hours, minutes))

def calculate_time_until_go_home(go_home_time):
    now = datetime.datetime.now()
    go_home = datetime.datetime.combine(now.date(), go_home_time)
    if now > go_home:
        return -1
    return (go_home - now).seconds // 60

def minutes_to_hours_minutes(minutes):
    return minutes // 60, minutes % 60

if __name__ == "__main__":
    main()
