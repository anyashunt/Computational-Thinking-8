Alani_points = 0
Celsius_points = 0
Redbull_points = 0

answer = input("if you see a stray kitten on the side of the road do you    A) leave it B) call the pound C) take it home ")
if answer == "A" :
    Redbull_points += 1
elif answer == "B" :
    Celsius_points += 1
elif answer == "C" :
    Alani_points += 1

answer = input("theres an old lady and a pregnant woman on your bus, do you     A) give your seat to the pregnant woman B) give your seat to the old lady C) don't give up your seat ")
if answer == "A" :
    Alani_points += 1
elif answer == "B" :
    Redbull_points += 1
elif answer == "C" :
    Celsius_points += 1

answer = input ("Are you an     A) Extrovert B) Ambivert C) Introvert ")
if answer == "A" :
    Celsius_points += 1
elif answer == "B" :
    Redbull_points += 1
elif answer == "C" :
    Alani_points += 1

answer = input ("What would you rather do on a Friday night     A) Go to a party B) Chill at your house C) do a small getogether with friends ")
if answer == "A" :
    Redbull_Points =+ 1
elif answer == "B" :
    Celsius_points += 1
elif answer == "C" :
    Alani_points += 1

answer = input ("Do you prefer  A) Winter B) Spring C) Summer D) Fall ")
if answer == "A" :
    Redbull_Points += 1
elif answer == "B" :
    Alani_points += 1
elif answer == "C" :
    Celsius_points += 1
elif answer == "D" :
    Redbull_Points

# end of quiz:
if Alani_points > Celsius_points and Alani_points > Redbull_points :
    print ("you are Alani!")
elif Celsius_points > Alani_points and Celsius_points > Redbull_points :
    print ("you are Celsius!")
elif Redbull_points > Alani_points and Redbull_points > Celsius_points :
    print ("you are Redbull!")