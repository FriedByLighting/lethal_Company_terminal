
# v0.1 // NOT FINISHED YET 
print("Welcome To The Company!")

credits = input("Enter your credits: ")

#Added some moons on the info category 
#fixed an issue where moons() came first instead of menu()





def main():
   menu()





def menu():
    print("                    '" + credits + " ")
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
    print("                   '" + credits + " ")
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
                       

                      First type the ACTION you want and THEN which moon: 
                                                                                           """)
                     
    if mchoice == "info" or mchoice =="INFO": 
        def info():
            choici = input("""
                      Welcome to the exomoons catalogue. 
                      Give the name of the MOON for more INFORMATION
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      * The Company Building 
                      
                      * Experimentation 
                      * Assurance 
                      * Vow 
                      
                      * Offense 
                      * March 
                      * Adamance 
                   
                      * Rend 
                      * Dine 
                      * Titan 
                       
                      Name of the MOON: 
                                                                                        """) 
            if choici == "The Company Building" or choici == "comp" or choici == "com" or choici == "c":
                print("""
                      71-Gordion
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      POPULATION: Unkown 
                       
                      CONDITIONS:No land masses. Continual Storms.

                      FAUNA: Unkown 

                      Where the Company resides.

                      Status: UNKNOWN                                                   """)
                
            elif choici == "Experimentation" or choici == "expe" or choici == "exp" or choici == "Expe" or choici == "Exp" :
                print("""
                      41-Experimentation
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      POPULATION: Abandoned. 
                       
                      CONDITIONS: Arid. Thick haze, worsened by industrial artifacts

                      FAUNA: Dominated by a few species. 
                      
                      HISTORY: Not discovered for quite some time due to its 
                      close orbit around gas giant Big Grin. However it appears  
                      to have been used in secret.                                               
                                                                                        """)
                     
            elif choici == "Ass" or choici == "ass" or choici == "Assurance" or choici == "assurance" or choici == "assura":
                print("""
                      220-Assurance
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      POPULATION: Abandoned. 
                       
                      CONDITIONS: Similar to its moon, 41-experimentation,
                      featuring far more jagged and weathered terrain.

                      HISTORY: 220-Assurance is far younger than its 
                      counterpart. Discovered not long before 41-
                      Experimentaton.
                      
                      FAUNA: Ecosystem supports territorial behavior.
                      
                                                       
                                                                                        """)
            elif choici == "vow":
                print(" ima add vow later LMFAOOO")
                  
            
            
         
        
        
        
        
        info()

    elif mchoice == "route" or mchoice =="ROUTE" :
        route()
    else: 
        print("You must only select one of the ACTION words first and then the MOON")
        print("Please Try Again")
        moons()
    


menu()

def route():
    print("route")



def store():
    print("test")  

def bestiary():
    print("lolll")

def storage(): 
    print("WALLET")

def other():
    print("klll")









