import time #pip install time
from plyer import notification # pip install plyer
import random #pip install random
# quotes variable is list of quotes
quotes = [    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
              "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
              "Successful and unsuccessful people do not vary greatly in their abilities. They vary in their desires to reach their potential. - John Maxwell",
              "The only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle. As with all matters of the heart, you’ll know when you find it. - Steve Jobs",
              "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
              "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett"]

def generate_quote():
    random_quote = random.choice(quotes)
    notification.notify(
        title="Motivational Quote",
        message=random_quote,
        app_name="Quote Generator",
        timeout=5
    )
while True:
    generate_quote()
    #Set sleep() to 60*60 so it will send notification on every 1hr
    #for testing purpose i have set sleep time to 2 seconds
    #1*2 mean sleep for 2 seconds. if sleep(60*2) then it means sleep for 2 minutes and so on.
    time.sleep(60*60)
    #Subscribe - WE ARE PYTHONEER