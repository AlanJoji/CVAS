from datetime import datetime

def curr_date() :
    now = datetime.now()
    current_date = now.strftime("%Y-%m%d")
    return(current_date)

def curr_time() : 
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    return(current_time)