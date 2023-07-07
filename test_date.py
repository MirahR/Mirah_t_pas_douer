from datetime import datetime, timedelta


if __name__=='__main__':
    ini_time_for_now = datetime.now()
    print ("initial_date", str(ini_time_for_now))
    future_date_after_2yrs = ini_time_for_now + timedelta(days = 730)
    future_date_after_2days = ini_time_for_now + timedelta(days = 2)
    print('future_date_after_2yrs:', str(future_date_after_2yrs))
    print('future_date_after_2days:', str(future_date_after_2days))