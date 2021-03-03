import random



   
LandingStats = [ ]   



FlareComponent = ['Poor and Late Flare', 'Poor and Early Flare', 'Good Flare', 'Good but Early Flare', 'Good but Late Flare']


random.shuffle(FlareComponent)
for x in range (0,1,5):
    LandingStats.append (FlareComponent.pop(x))
 
CenterlineManagment  = ['Left Marginal', 'Left Extreme', 'Centered!', 'Right Marginal', 'Right Extreme' ]

random.shuffle(CenterlineManagment)
for x in range (0,1,5):
    LandingStats.append (CenterlineManagment.pop(x)) 
Landing = input("Enter descent rate in Negative Vertical Speed (values between 1 and 1000 accepted) here:      ")
   
if (int(Landing)) <150:  
    LandingStats.append("Butter!")
    print(LandingStats)
elif (int(Landing)) <230:  
    LandingStats.append("Great Landing")
    print(LandingStats)

elif (int(Landing))<460:  
    LandingStats.append("Acceptable")
    print(LandingStats)
elif (int(Landing))  <600:  
    LandingStats.append("Oof! That one really hurt!")
    print(LandingStats)
elif (int(Landing))  <1001:  
    LandingStats.append("RIP Landing Gear")
    print(LandingStats)
else:
    print("User Error Occured")


                

        