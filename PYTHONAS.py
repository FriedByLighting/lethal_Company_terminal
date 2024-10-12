
# v0.2 // NOT FINISHED YET 
#V V V V |UPDATE NOTES| V V V V V V 
#-Added some moons on the info category (continued this)
#-fixed an issue where moons() came first instead of menu()
#-done the route()


print("Welcome To The Company!")

credits = input("Enter your credits: ")








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
               #start of info       
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
                       
                      NAME of the MOON: 
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
            elif choici == "vow" or choici == "VOW" or choici == "v":
                print("""
                      56-Vow
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      POPULATION: Abandoned. 
                       
                      CONDITIONS: Humid, Rough terrain. Teeming with plant 
                      life.

                      HISTORY: Vow appears to have been inhabited by several colonies 
                      across its continents, but there is now no sign 
                      of life, and they have become a mystery.
                      
                      FAUNA: Diverse , teeming with plant-life. A competitive
                      ecosystem supports aggressive lifeforms.
                      
                                                       
                                                                                        """)
            elif choici == "offense" or choici == "Off" or choici == "off" or choici == "Offense" or choici == "OFFENSE":
                print ("""
                      21-Offense
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      POPULATION: Abandoned. 
                       
                      CONDITIONS: Believed to have splitnered off from its cousin 220 - Assurance, 
                      Offense features similar jagged and dry conditions but differs in its ecosystem.

                      HISTORY: 21-Offense is categorized as an asteroid moon and seems to have not existed 
                      on its own for more than several hundred years. The industrial artifacts here have 
                      suffered damage; its believed they were built long before 
                      21-Offense was splintered off.

                      FAUNA: A competitive and toughened ecosystem supports 
                      aggressive lifeforms. Travelers to 21-Offense should know it's not 
                      for the faint of heart.
                      
                                                       
                                                                                        """)      
            elif choici == "March" or choici == "march" or choici == "Mar" or choici == "mar":  
                print("""
                      61-March
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      POPULATION: Abandoned. 
                       
                      CONDITIONS: March undergoes constant drizzling weather.
                      Its terrain is more expansive.

                      HISTORY: This moon is overlooked due to its twin moon,
                      Vow.
                      
                      FAUNA: Diverse 
                      
                                                       
                                                                                        """)
            elif choici == "Adamance" or choici == "Ada" or choici == "ada" or choici == "adamance":
                print("""
                      20-Adamance 
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      POPULATION: Abandoned. 
                       
                      CONDITIONS: Erosion and geographical forces have resulted in a landscape of 
                      deep valleys and mountains.

                      HISTORY: Adamance is the biggest and oldest of what are colloquially 
                      referred to as the "Green Witches": Vow, March , and Adamance, which orbit 
                      No Service.
                      
                      FAUNA: Adamance is home to a lively, diverse ecosystem of smaller-sized 
                      omnivores.
                      
                                                       
                                                                                        """) 
            elif choici == "rend" or choici == "Rend" or choici == "R" or choici == "re":
                print("""
                      85-Rend 
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      POPULATION: Abandoned. 
                       
                      CONDITIONS: Its planet orbits a white dwarf star, making for 
                      inhospitable, cold conditions. Constant blizzards decrease 
                      visibility.

                      HISTORY: Several famous travellers went missing here, 
                      giving it some reputation. Their bodies are unlikely to 
                      be found due to the planet's conditions.
                      
                      FAUNA: It's highly unlikely for complex lifr to exist
                      here.
                      
                                                       
                                                                                        """) 
            elif choici == "dine" or choici == "Dine" or choici == "di" or choici == "d":
                print("""
                      7-Dine 
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      POPULATION: Abandoned. 
                       
                      CONDITIONS: Its planet orbits a white dwarf star, making for 
                      inhospitable, cold conditions. Constant blizzards decrease 
                      visibility.

                      HISTORY: Several famous travellers went missing here, 
                      giving it some reputation. Their bodies are unlikely to 
                      be found due to the planet's conditions.
                      
                      FAUNA: It's highly unlikely for complex lifr to exist
                      here.
                      
                                                       
                                                                                        """)
            elif choici ==  "titan" or choici == "Titan" or choici == "T" or choici == "t" or choici == "tit":
                print("""
                      8-Titan
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      POPULATION: Abandoned. 
                       
                      CONDITIONS: Frozen, rocky. This moon was mined for
                      resources. It's easy to get lost here.

                      HISTORY: It looks like this moon was mined for 
                      resources. It's easy to get lost within the giant 
                      industrial complex. There are many entrances to it 
                      littered about the landscape.
                      
                      FAUNA: Dangerous entities have been rumored to take
                      residence in the vast network of tunnels.
                
                      
                                                       
                                                                                        """)
            elif choici == "art" or choici == "Art" or choici == "Artifice" or choici == "artifice":
                print("""
                      68-Artifice
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
                       
                      CONDITIONS: Abandoned facilities are littered across the
                      landscape, which was once teeming with life.

                      HISTORY: Weapons and classified technology has been found 
                      at various sites on the surface, dating back at least two
                      hundred years.
                      
                      FAUNA: It's rumored that active machinery has been left 
                      behind.
                
                      
                                                       
                                                                                        """)
            elif choici == "embrion" or choici == "Embrion" :
                print("""
                      5-Embrion
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
                       
                      POPULATION: Abandoned

                      CONDITIONS: Desolate and flat with unbreathable air,
                      Embrion's surface layer is almost entirely made of
                      amethyst quartz, which is made possible by Embrion's
                      distance to its nearest star and its resulting geothermal
                      activity. The surface of Embrion is scorchingly hot.

                      HISTORY: Embrion was discovered in just the last century.
                      It appears to have been used as a testing ground for Old
                      Birds long before it was officially discovered. As a 
                      result of this danger, its status has been marked as 
                      Condemned. There are theories that a diverse geothermal 
                      ecosystem may be thriving within a vast cave network 
                      under Embrion's surface.
                      
                      FAUNA: Embrion is devoid of biological life.
                
                      
                                                       
                                                                                        """) 
            elif choici == "Liquidation" or choici == "liquidation" or choici == "L":
                print("""
                      44-Liquidation
                      
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
                       
                      POPULATION: None.

                      CONDITIONS: Previously mined for its rich industrial 
                      resources , Liquidation is now largely an ocean moon.
 
                      FAUNA: 
                
                      
                                                       
                                                                                        """)
            else: 
                print("[This action was not compatible with this object.]")
                menu()
            #end of Info 
                                                                                                                                           
       
        info()

    elif mchoice == "route" or mchoice =="ROUTE" :
        #routes the ships to a moon 
        def route():
            print("")
            choicr = input("""
                      Welcome to the exomoons catalogue. 
                      Give the name of the MOON to ROUTE the autopilot
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
                       
                      NAME of the MOON: 
                                                                                        """) 
            if choicr == "Experimentation" or choicr == "experimentation" or choicr == "Expe" or choicr == "expe" or choicr == "EXPERIMENTATION":
                moonsr = "Experimentation" 
                print("    The autopilot is ROUTED to " + moonsr )
            elif choicr == "Assurance" or choicr == "assurance" or choicr == "Ass" or choicr == "ass" or choicr == "ASSURANCE":
                moonsr = "Assurance" 
                print("    The autopilot is ROUTED to " + moonsr)
            elif choicr == "Vow" or choicr == "vow" or choicr =="VOW":
                moonsr = "Vow"
                print("     The autopilot is ROUTED to " + moonsr)
            elif choicr =="Offense" or choicr == "offense" or choicr == "OFF" or choicr == "off" or choicr == "Off" or choicr == "OFFENSE":
                moonsr = "Offense"
                print("     The autopilot is ROUTED to " + moonsr)
            elif choicr =="March" or choicr == "march" or choicr == "Mar" or choicr == "mar"  or choicr == "MARCH":
                moonsr = "March"
                print("     The autopilot is ROUTED to " + moonsr)
            elif choicr =="adamance" or choicr == "Adamance" or choicr == "ada" or choicr == "Ada" or choicr == "ADA" or choicr == "ADAMANCE":
                moonsr = "Adamance"
                print("     The autopilot is ROUTED to " + moonsr)
            elif choicr =="Rend" or choicr == "rend" or choicr == "REND" or choicr == "ren" or choicr == "REN" or choicr == "Ren":
                moonsr = "Rend"
                print("     The autopilot is ROUTED to " + moonsr)
            elif choicr =="Dine" or choicr == "DINE" or choicr == "dine" :
                moonsr = "Dine"
                print("     The autopilot is ROUTED to " + moonsr)
            elif choicr =="Titan" or choicr == "TITAN" or choicr == "titan" or choicr == "tit" or choicr == "TIT" or choicr == "Tit":
                moonsr = "Titan"
                print("     The autopilot is ROUTED to " + moonsr)
            elif choicr =="Art" or choicr == "art" or choicr == "ART" or choicr == "artifice" or choicr == "Artifice" or choicr == "ARTIFICE":
                moonsr = "Artifice"
                print("     The autopilot is ROUTED to " + moonsr)
            elif choicr =="Embrion" or choicr == "EMBRION" or choicr == "embrion" :
                moonsr = "Embrion"
                print("     The autopilot is ROUTED to " + moonsr)
            else:
                print("[This action was not compatible with this object.]")
                menu()
            
                      
        
            









        route()    
    else: 
        print("You must only select one of the ACTION words first and then the MOON")
        print("Please Try Again")
        moons()
    


menu()





def store():
    print("test")  

def bestiary():
    print("lolll")

def storage(): 
    print("WALLET")

def other():
    print("klll")









