import random
import time
import webbrowser

while True:
    sites = random.choice(['google.com','facebook.com','youtube.com'])
    visit = "https://{}".formate(sites)
    webbrowser.open(visit)
    seconds = random.randint(2,5)
    time.sleep(seconds)