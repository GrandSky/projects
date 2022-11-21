def vigenereDecoder(initCipherText, initCipherKey):
    cipherText=initCipherText
    key = initCipherKey.lower()
    position=0
    plainText=""
    for x in cipherText:
        if x.isalpha():
            keyAt =key[position%len(key)]
            keyAt=ord(keyAt)-97
            if ord(x) <97:
                y=ord(x)-keyAt+26
                y=y%65
                y=y%26
                y+=65
                y=chr(y)
                plainText+=y
            else:
                y=ord(x)-keyAt+26
                y=y%97
                y=y%26
                y+=97
                y=chr(y)
                plainText+=y
            position+=1
        else:
            plainText+= x
    return plainText
        
def vigenereKeyBreaker(initCipherText, initLength):
    length=initLength
    cipherText=initCipherText
    position=0
    breakUpText=[]
    key=""
    for x in range(length):
        breakUpText.append("")

    for x in cipherText:
        if x.isalpha():
            y=breakUpText[position%length]
            y+=x
            breakUpText[position%length] = y
            position+=1
    for x in range(length):
        key+=frequencyAnalysis(breakUpText[x].lower())

    plainText = vigenereDecoder(cipherText,key)
    x = returnRepeated(key)
    if x== None:
        print(key)
    else :
        key = returnRepeated(key)
        print(key)
    return plainText

def returnRepeated(text):
    i = (text+text).find(text, 1, -1)
    return None if i == -1 else text[:i]

#call after separating ciphertext
def frequencyAnalysis(initGroup):
    Group=initGroup
    length = len(Group)
    text=""
    dictionary={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,
    'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    for x in Group:
        dictionary[x]+=1
    sorted_values = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    if length <12:
        for x in range(length):
            key =list(sorted_values)[25-x]
            text+=key
    else:
        for x in range(12):
            key =list(sorted_values)[25-x]
            text+=key

    return findBestOffset(text)

def findBestOffset(initGroup):
    Group = initGroup
    bestOffSetLoc=0
    bestOffSet=""
    for x in range(26):
        analysis=0
        z=97+x
        z=chr(z)
        y= vigenereDecoder(Group,z)
        if "e" in y:
            analysis+=12
        if "t" in y:
            analysis+=9
        if "a" in y:
            analysis+=8
        if "o" in y:
            analysis+=8
        if "i" in y:
            analysis+=7
        if "n" in y:
            analysis+=7
        if "s" in y:
            analysis+=6
        if "h" in y:
            analysis+=6
        if "r" in y:
            analysis+=6
        if "d" in y:
            analysis+=4
        if "l" in y:
            analysis+=4
        if "u" in y:
            analysis+=3
        if analysis >bestOffSetLoc:
            bestOffSetLoc = analysis
            bestOffSet=z
        
    return bestOffSet

def VigenereCipherBreaker(initCipherText):
    text = initCipherText
    commonCounter = 0
    highestCount = 0
    highestIndex = 0
    higherCount=0
    higherIndex=0
    highcount=0
    highIndex=0
    listOfCommon = []
    newText=""
    for i in text:
        if i.isalpha():
            newText += i
    newText.lower()
    newText = list(newText)
    tempText = newText.copy()
    for i in range(len(newText)-1):
        tempText.pop(len(tempText)-1)
        for j in range(len(tempText)):
            if newText[(i+1) + j] == tempText[j]:
                commonCounter += 1
        listOfCommon.append(commonCounter)
        if commonCounter > highestCount:
            highCount=higherCount
            highIndex=higherIndex
            higherCount=highestCount
            higherIndex=highestIndex
            highestCount = commonCounter
            highestIndex = i + 1
        elif commonCounter >higherCount:
            highCount=higherCount
            highIndex=higherIndex
            higherCount = commonCounter
            higherIndex = i + 1
        elif commonCounter >highCount:
            highCount = commonCounter
            highIndex = i + 1

        commonCounter = 0

    highestIndex= abs(highestIndex-higherIndex)
    higherIndex = abs(higherIndex-highIndex)
    key_length= computeGCD(highestIndex,higherIndex)

    return vigenereKeyBreaker(initCipherText,key_length)
    
def computeGCD(x, y):
    while(y):
       x, y = y, x % y

    return abs(x)

x=input()

print(VigenereCipherBreaker(x))