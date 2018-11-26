import schedule
import time

def job(t):
    print("Good morning beautiful ^_^!", t)
    return

schedule.every().day.at("10:10").do(job,'It is nice to see you my love <3')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute