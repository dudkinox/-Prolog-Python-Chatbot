from pyswip import *
def chat():
    text = str(input("Enter your text : "))
    return text
def pro():
    text = chat()
    p = Prolog()
    p.consult("food.pl")
    if (text == "what food?"):    
        dilicious = Functor("food", 1)
        lao = Functor(text, 1)
        X = Variable()

        print("dilicious food....")
        r = Query(dilicious(X))
        count = 1
        while r.nextSolution():
            print(count , ". = ", X.value)
            count += 1
        r.closeQuery()
    else:   
        print(str(text) + " food....")
        q = Query(lao(X))
        count = 1
        while q.nextSolution():
	        print(count , ". = ", X.value)
	        count += 1
pro()