import random
import time
def div():
    print("********************************")
div()
print("WELKIN GIVEAWAY")
div()
Participants=list()
while (Users := input("Enter Participant's Name: ")) != "gg":
    Participants.append(Users)
div()
print("ALL THE MEMBERS HAVE BEEN REGISTERED!")
div()
for i in range(20,0,-1):
    print(f"RAFFLE STARTING IN {i} second!")
    time.sleep(2)
div()
print("ENTERED USERS ARE THE FOLLOWING...(=^.^=)")
div()
for i,x in enumerate(Participants):
    print(f"{i+1} - {x}")
div()
String2=input("Type 'Yes' To Start!: ")
String3=String2.lower()
if String3=="yes":
    pass
div()
counter=1
while True:
    print("")
    print(counter)
    print(f"😇Program😇: Thinking who should I kick....")
    time.sleep(5)
    number=random.randint(0,len(Participants)-1)
    print(f"🤡Program🤡: !p poku {Participants[number]} 🔪")
    counter+=1
    Participants.pop(number)
    if len(Participants)==1:
        break
    if len(Participants)==0:
        break
div()
for i in Participants:
    print(f"🥳Congratulations! 🥳Winner of the Welkin is🥳 >>>>>>{i}<<<<<<")
    print("Please Message me your UID in Discord! Thank you everyone for participating!")
div()
