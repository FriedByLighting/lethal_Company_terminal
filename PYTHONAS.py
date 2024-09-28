



# v0.0 // NOT FINISHED YET 
print("Welcome To The Company!")

credits = input("Enter your credits: ")







def main():
   
    
    menu()

def menu():
    print("'" + credits + " ")
    choice = input("""
                      >MOONS
                      To see the list of moons the autopilot can route to.
                      
                      >STORE 
                      To see the company store's selection of useful items.
            
                      >BESTIARY 
                      To see the list of wildlife on record.
                   
                      >STORAGE 
                      To access objects placed into storage. 
                   
                      >OTHER 
                      To see the list of other commands. 

                      Please enter your choice: """)
    if choice == "MOONS" or choice =="moo" or choice == "moons" or choice == "m": 
        moons()
    elif choice == "STORE" or choice =="store" :
        store()
    elif choice == "BESTIARY" or choice =="best" or choice == "B" or choice == "b": 
        bestiary()
    elif choice == "STORAGE" or choice =="storage" : 
        storage()
    elif choice == "OTHER" or choice =="ot" or choice == "O" or choice == "o": 
        other()
    else: 
        print("You must only select one of the capitalized words")
        print("Please Try Again :) ")
        menu()




def moons():
      print("'" + credits + " ")
mchoice = input("""
                      Welcome to the exomoons catalogue. 
                      To route the autopilot to a moon , use the word ROUTE.
                      To learn about any moon, use the word INFO.
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      * The Company building // Buying at 100%
                      
                      * Experimentation 
                      * Assurance 
                      * Vow 
                      
                      * Offense 
                      * March 
                      * Adamance 
                   
                      * Rend 
                      * Dine 
                      * Titan 
                       

                      Please enter your choice: """)
if mchoice == "INFO" or mchoice =="moo" or mchoice == "moons" or mchoice == "m": 
        info()
elif mchoice == "STORE" or mchoice =="store" :
        store()
elif mchoice == "BESTIARY" or mchoice =="best" or mchoice == "B" or mchoice == "b": 
        bestiary()
elif mchoice == "STORAGE" or mchoice =="storage" : 
        storage()
elif mchoice == "OTHER" or mchoice =="ot" or mchoice == "O" or mchoice == "o": 
        other()
else: 
        print("You must only select one of the capitalized words")
        print("Please Try Again :) ") 

def store():
    print("test")  

def bestiary():
    print("lolll")

def storage(): 
    print("WALLET")

def other():
    print("klll")

main()






