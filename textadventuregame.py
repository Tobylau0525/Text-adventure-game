#Text advenature game
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
    third_choice=input("Please enter your choice ").upper()
    if (third_choice=="A"):
        print ("He became a businessman, try again to see other outcomes \n")
        start()
    elif (third_choice=="B"):
        print("He did not find a job after all his years of studies :(, try again to see other outcomes \n")
    elif (third_choice=="C"):
        break
    else:
        print ("you have enter something else")

print("""The mansion caught on fire with the adoptive couple inside it

    A) The Parton-Brant couple survive to the accident

    B) The Parton-Brant family did not survive the accident, they burn inside the mansion
""")

while True:
    third_choice=input("Please enter your choice ").upper()
    if (third_choice=="A"):
        continue
    elif (choice=="B"):
        break
    else:
        print ("you have enter something else")



