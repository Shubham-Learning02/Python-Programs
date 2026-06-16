print(". and - is used for indicating morse code, Words not available in morse are displayed between | like this: |....|")
aa=input("Enter the word:")
def incode(a):
    word={" ":" ","a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----",".":".-.-.-",",":"--..--","?":"..--.."}
    fin=""
    asx=word.values()
    print(asx)
    for i in a:
        s=i.lower()
        if s in word:
            fin+=word[s]+" "
        else:
            fin+="|"+s+"|"
    return fin
print("The converted word is: ",incode(aa))
