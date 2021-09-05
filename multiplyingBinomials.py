def main():
    nomialOne = input("First Nomial: ")
    nomialTwo = input("Second Nomial: ")
    nomialOne = nomialOne.split(' ')
    nomialTwo = nomialTwo.split(' ')
    if(nomialOne[1].rfind('+') != -1):
        nomialOne[1] = nomialOne[1].lstrip("+")
    
    if(nomialTwo[1].rfind('+') != -1):
        nomialTwo[1] = nomialTwo[1].lstrip("+")
    nomialOne[0] = nomialOne[0].rstrip("x")
    nomialTwo[0] = nomialTwo[0].rstrip("x")
    if(nomialOne[0] == ''):
        nomialOne[0] = "1"
    if(nomialTwo[0] == ''):
        nomialTwo[0] = "1"
    
    nomialOne[0] = int(nomialOne[0])
    nomialOne[1] = int(nomialOne[1])
    nomialTwo[0] = int(nomialTwo[0])
    nomialTwo[1] = int(nomialTwo[1])
    ans1 = nomialOne[0] * nomialTwo[0]
    ans2 = nomialOne[0] * nomialTwo[1]
    ans3 = nomialOne[1] * nomialTwo[0]
    ans4 = nomialOne[1] * nomialTwo[1]
    print("{nom1}x * {nom2}x = {ans}x\u00B2".format(nom1 = nomialOne[0], nom2 = nomialTwo[0], ans = ans1)) 
    print("{nom1}x * {nom2} = {ans}x".format(nom1 = nomialOne[0], nom2 = nomialTwo[1], ans = ans2)) 
    print("{nom2}x * {nom1} = {ans}x".format(nom1 = nomialOne[1], nom2 = nomialTwo[0], ans = ans3)) 
    print("{nom1} * {nom2} = {ans}".format(nom1 = nomialOne[1], nom2 = nomialTwo[1], ans = ans4)) 
    print("{ans1}x\u00B2 + {ans23}x + {ans4}".format(ans1 = ans1, ans23 = ans2 + ans3, ans4 = ans4))

while(True):
    main()






