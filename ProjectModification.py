import speech_recognition as sr

responses=["Welcome To Smart Calculator","My Name Is Singh","Thanks","Sorry,This Is Beyond My Ability"]
def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
              return L
        L+=1
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def big(a,b):
    return a if a>b else b
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divison (a,b):
    return a/b
def end():
    print(responses[2])
    input("Press enter key to exit")
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[3])
def help():
    print("List of valid commands")
    for k in operations:
        print(k)
    for k in commands:
        print(k)
operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,
            "MINUS":sub,"SUBTRACTION":sub,"SUBTRACT":sub,"DIFFERENCE ": sub,
            "PRODUCT":multiply,"MULTIPLICATION":multiply,"MULTIPLY":multiply,
            "DIVIDE":divison,"DIVISION":divison,
            "LCM":lcm,"HCF":hcf,"BIG":big,"MAX":big,"GREATER":big
            }
commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end,"HELP":help}
def main():
    print(responses[0])
    print(responses[1])
    while True:
        print()
        r = sr.Recognizer()
        with sr.Microphone() as source:
              print("Speak something...")
              audio = r.listen(source)
        
        try:
            # Use the recognizer to convert speech to text
            text = r.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
             print("Sorry, I couldn't understand your speech.")
        except sr.RequestError as e:
          print("Sorry, I couldn't request results from the speech recognition service; {0}".format(e))
     #   text=input("Enter some text: ")
        for word in text.split(' '):
            if word.upper()in operations.keys():
                try:
                    l=extract_numbers_from_text(text)
                    r=operations[word.upper()](l[0],l[1])
                    print(r)
                except:
                    print("Something is wrong please retry")
                finally:
                    break
            elif word.upper()in commands.keys():
                commands[word.upper()]()
                break
        else:
            sorry()
if __name__== "__main__":
    main()














        


