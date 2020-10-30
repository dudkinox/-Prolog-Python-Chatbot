from pyswip import *
def loop():
    choice = str(input("\n==============\nRUN AGAIN (Y/N)\n : "))
    while (choice != "N" or choice != "n"):
        pro()
    print("END TO PROGRAM")

def chat():
    text = str(input("Enter your text : "))
    return text
def pro():
    text = chat()
    p = Prolog()
    p.consult("hardware.pl")
    if (text == "have"):
        dilicious = Functor("hardware", 1)
        print("Hardware have....")
        X = Variable()
        r = Query(dilicious(X))
        count = 1
        while r.nextSolution():
            print(count , ". = ", X.value)
            count += 1
        r.closeQuery()
    else:
        print(str(text) + " Example....")
        lao = Functor(text, 1)
        X = Variable()
        q = Query(lao(X))
        count = 1
        while q.nextSolution():
	        print(count , ". = ", X.value)
	        count += 1
    loop()

pro()