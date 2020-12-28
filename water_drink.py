# drink water reminder

import time 
from plyer import notification

if __name__ == "__main__":
    while true:
    notification.notify(
    title = "Please Drink Water",
    message = "The National Academic of Sciences, Engineering and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluid for men. About 11.5 cups (2.7 liters of fluid a day for women.",
    timeout = 5
)
time.sleep(60*60)
#reminds ever hour to drink water