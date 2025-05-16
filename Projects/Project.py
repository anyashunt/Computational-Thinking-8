###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

q1 = codesters.Square (100, 100, 200, 'LightYellow')
q2 = codesters.Square (-100, 100, 200, 'Honeydew')
q3 = codesters.Square (-100, -100, 200, 'MistyRose')
q4 = codesters.Square (100, -100, 200, 'AliceBlue')

s1 = codesters.Sprite ("Alani", 100, 100)
s1.set_size(0.1)
s2 = codesters.Sprite ("Spotify", -100, -100)
s2.set_size(0.2)
s3 = codesters.Sprite ("Brandy", 100, -100)
s3.set_size(0.05)
s4 = codesters.Sprite ("Starbucks", -100, 100)
s4.set_size(0.2)

message1 = codesters.Text ("Anya Hunt",0,220,"White")
message2 = codesters.Text ("Idk what to put here",0,-220,"Cornflowerblue")