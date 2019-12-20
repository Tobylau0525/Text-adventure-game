#Text advenature game
import sys

def start():
    print("""In an old town in Australia, a middle-class family just have a newborn
baby name Santi, born in 1961 on a rainy night, his family was so happy to meet
him, one week later someone with a bad heart and without feelings stole him.
What do you think is gonna happen next?

    A) His family got him back

    B) Santi disappeared from the earth

    C) The someone who stole him sold him to a rich couple

""")
start()
while True:
    first_choice=input("Please enter your choice ").upper()
    if (first_choice =="A") or (first_choice =="B"):
        print ("Game over, try again \n")
        
        start()
    elif (first_choice =="C"):
        break
        
    else:
        print ("you have enter something else")
        continue

print ("""The rich couple will adopt him

    A) After all, the rich couple felt guilty and decided
       to find his blood family and take him back to them

    B) They keep him and raise him as their adoptive son

""")
while True:
    second_choice=input("Please enter your choice ").upper()
    if (second_choice=="A"):
        print ("Game over, try again \n")
        
        start()
    elif (second_choice=="B"):
        break
    else:
        print ("you have enter something else")


print("""
After that Louis Parton-Brant studied and did his career on the criminal
investigation to help find kids that were stolen from their families, lost
children, but as most of the rich families, his adoptive parents made him
study another career besides that one. They made him study business, what
do you think will happen with his life after this?

    A) He became a businessman

    B) He started applying and finding for jobs

    C) He got a job finding lost children and children who were stolen from their families
""")

while True:
    forth_choice=input("Please enter your choice ").upper()
    if (forth_choice=="A"):
        print ("He became a businessman, try again to see other outcomes \n")
        start()
    elif (forth_choice=="B"):
        print("He did not find a job after all his years of studies :(, try again to see other outcomes \n")
    elif (forth_choice=="C"):
        break
    else:
        print ("you have enter something else")

print("""The mansion caught on fire with the adoptive couple inside it

    A) The Parton-Brant couple survive to the accident

    B) The Parton-Brant family did not survive the accident, they burn inside the mansion
""")

while True:
    fifth_choice=input("Please enter your choice ").upper()
    if (fifth_choice=="A"):
        continue
    elif (fifth_choice=="B"):
        break
    else:
        print ("you have enter something else")
        
print(""" The rich couple was sleeping when it happened so they just died inside the mansion

    After the tragedy he discovered that he was adopted

    A) By clues, he found in a case from 1961 about a stolen child never found

    B)By a letter that his adoptive mom wrote him and could only be open when something happens to her or her husband

""")
while True:
    sixth_choice=input("Please enter your choice ").upper()
    if (sixth_choice=="A"):
        continue
    elif (sixth_choice=="B"):
        break
    else:
        print ("you have enter something else")

print(""" He started to find his blood family

    A)He flew to Australia to find clues about his blood family

    B)He stayed where he lived and did not find anything about it


""")
while True:
    seventh_choice=input("Please enter your choice ").upper()
    if (seventh_choice=="A"):
        break
    elif (seventh_choice=="B"):
        print("Game over")
        sys.exit()
        
    else:
        print ("you have enter something else")

print(""" He went to the house that his blood family lived(The Gabino). They were not living there anymore


    A)He stayed there to keep finding clues about his blood family

    B)He paid a few days in a hotel to find more clues, he started having some dreams



""")
while True:
    eighth_choice=input("Please enter your choice ").upper()
    if (eighth_choice=="A"):
        continue
    elif (eighth_choice=="B"):
        break
        
    else:
        print ("you have enter something else")

print("""
    A)The second dream: He dreamed with the name of every member of the family

    B)The first dream: He dreamed with the name of the hospital that he was born

    C)The third dream: was the face of the women who stole him
""")
while True:
    ninth_choice=input("Please enter your choice ").upper()
    if (ninth_choice=="B") or (sixith_choicr=="C"):
        continue
    elif (ninth_choice=="A"):
        break
        
    else:
        print ("you have enter something else")


print("""
The woman died a few days after she stole him, what do you think happened next?
With those names he found information about them, he discovered it was a
middle-class family. After a week of finding clues, he got the address of
Gabino’s family. He went to find about that address and found them, he told
them that he was the child they lost

    A)They rejected him because they did not believe him

    B)They accepted him and together they found out that the woman that stole him was because of revenge

""")

while True:
    tenth_choice=input("Please enter your choice ").upper()
    if (tenth_choice=="A"):
        continue
    elif (tenth_choice=="B"):
        print("They lived together and happy, he met his new family")
        print("Congrats, you've beat the game :D")
        break
        
    else:
        print ("you have enter something else")

