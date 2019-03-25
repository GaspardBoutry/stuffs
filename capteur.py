from random import randint
from time import sleep

def send_alert(niveau) :
    if niveau == 1 :
        print(1)
    elif niveau == 2 :
        print(2)
    else :
        print(3)

if __name__== "__main__" :
    seuil_alert_niveau_1 = 100
    seuil_alert_niveau_2 = 1000
    seuil_alert_niveau_3 = 10000
    trigger = 42

    while True :
        sleep(.05)
        if randint(0, seuil_alert_niveau_1) == trigger :
            send_alert(1)
        if randint(0, seuil_alert_niveau_2) == trigger :
            send_alert(2)
        if randint(0, seuil_alert_niveau_3) == trigger :
            send_alert(3)
