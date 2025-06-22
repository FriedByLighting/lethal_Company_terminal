
# v0.5 // NOT FINISHED YET 
#V V V V |UPDATE NOTES| V V V V V V 
#! ! ! The STORE function is NOT WORKING! ! ! ! (yet i will fix it in the next updates)
#-fixed info() so it's easier now to understand
#-Added daytime and fixed the welcoming message
#fixed the moons() function so it now works with shortcuts and partial matches
#Happy Birthday Lethal Company 1st year annivesrary (23/10/2023 - 23/10/2024)

import math 
import datetime 

import re


x = datetime.datetime.now()

print("""
         
         Welcome to the FORTUNE-9 OS
                   Courtesy of the Company   
                       """)
print(x.strftime(" Happy %A"))

credits = int(input("Enter your credits: "))
walk = 12 







def main():
    menu(credits)
# Item prices 
def store(credits, walk):
    menu_items = {
        "Walkie-talkie": 12,
        "Flashlight": 15,
        "Shovel": 30,
        "Lockpicker": 20,
        "Pro-flashlight": 25,
        "Stun grenade": 30,
        "Boombox": 60,
        "TZP-Inhalant": 120,
        "Zap gun": 400,
        "Jetpack": 700,
        "Extension ladder": 60,
        "Radar-booster": 60,
        "Spray paint": 50,
        "Belt bag": 45,
        "Loud horn": 100,
        "Signal Translator": 250,
        "Teleporter": 375,
        "Inverse Teleporter": 425, 
        "Weed Killer": 25,
        "Cruiser": 370  
    }

    # Custom info messages for items
    info_messages = {
        "Flashlight": "The most affordable light source. it's even waterprof!",
        "Walkie-talkie": "Useful for keeping in touch! Hear other players when the walkie talkie is in your inventory. Must be in your hand and pressed down to transmit voice.",
        "Shovel": "For self-defense!",
        "Lockpicker": "Lock-pickers will unlock your limitless potential for efficiency on the job. Powered by proprietary AI software, they will get you access through any locked door",
        "Pro-flashlight": "With an extra battery life and even brigther bulb, your colleagues can never leave you in the dark again!",
        "Stun grenade": " [This action was not compatible with this object.]  ",
        "Boombox": "These jamming tunes are great for a morale boost on your crew!",
        "TZP-Inhalant": "This safe and legal medicine can be administered to see great benefits to your perfomance on the job! Your ability to move LONG distances while carrying HEFTY objects will be second to none! Warning: TZP gas may impact the brain with extended exposure. Follow instructions manual provided with the canister. Don't forget to share!",
        "Zap gun": "The most specialized self-protective equipment capable of sending upwards of 80,000 volts!                                                To keep it targeted as long as possible, pull the gun side-to-side to counter the bend and fight against the pull of the electric beam. It can only stun for as long as you keep the current flowing.",
        "Jetpack": "This device will get you around anywhere! Just use it responsibly!",
        "Extension ladder": "The extension ladder can reach as high as nine meters! Use it to scale any cliff and reach for the stars! To save batteries the extension ladder automatically stores itself after 18 seconds.",
        "Radar-booster": "Radar boosters come with many uses! Use the \"SWITCH\" command before the radar booster's name to view it on the main monitor. It must be activated.         Use the \"PING\" command before the radar booster's name to play a special sound from the device.      Use the \"FLASH\" command to cause a bright flash from the radar booster's bulb.",
        "Spray paint": "[This action was not compatible with this object.] ",
        "Weed Killer": " Deal with those pesky weeds! Repeated, firm presses on the trigger aimed at the root of the weed is all you need!",
        "Belt bag": " The Company's very own tactical belt bags are an absolute must-have for those who want to bring their all! They can hold 15 utillity items at one time. You'll never feel useless again! Just press [Q] to store an item in the bag, them click to check its contents and drag items out. Other players can also use the bag while it's fastened around your waist.",
        "Loud horn": "Used to communicate with any crew members from any distance, no walkie talkie required! The horn can be heard from anywhere. But what does it mean? That's up to you!",
        "Signal Translator": " Use the \"transmit\" command to broadcast a text message to all crewmates. The message must be under 10 letters.",
        "Teleporter": "Press the button to activate the teleporter. It will teleport whoever is currently being monitored on the ship's radar. They will not be able to keep any of their held items through the teleporter. It takes about ten seconds to recharge ",
        "Inverse Teleporter": " The inverse teleporter is a modified teleporter which will teleport you to a random position outside the ship. All your items will be dropped at the teleporter before transprt. The inverse teleporter can be used by everyyone at once and has a 3.5 minute cooldown.                                  DISCLAIMER: The inverse teleporter can obly transport you out, not in, and you may become trapped. The Company is not responsible for injury or replacement of heads and limbs induced by quantum entanglement and bad luck.",
        "Cruiser": "The Company Cruiser is an entire delivery truck capable of carrying as many items as you could ever need, including your fellow coworkers! Your purchase of a Company Cruiser comes with one free, life-time warranty, because we are that confident in its durability and usefulness!",

        
    }
    #Shortcuts for items 
    shortcuts = {
        "walk": "Walkie-talkie",
        "flash": "Flashlight",
        "shov": "Shovel",
        "lock": "Lockpicker",
        "pro": "Pro-flashlight",
        "stun": "Stun grenade",
        "boom": "Boombox",
        "tzp": "TZP-Inhalant",
        "zap": "Zap gun",
        "jet": "Jetpack",
        "ladder": "Extension ladder",
        "radar": "Radar-booster",
        "spray": "Spray paint",
        "belt": "Belt bag",
        "horn": "Loud horn",
        "signal": "Signal Translator",
        "weed": "Weed Killer",
        "tele": "Teleporter",
        "inverse": "Inverse Teleporter",
        "cruiser": "Cruiser"
    }

    print("                    '", credits, " ")
    Schoice = input("""
    Welcome to the Company store. 
    Use words BUY and INFO on any item.
    Order tools in bulk by typing a number.
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    * Walkie-talkie  //  Price: '12
    * Flashlight  //  Price: '15
    * Shovel  //  Price: '30 
    * Lockpicker  //  Price: '20
    * Pro-flashlight  //  Price: '25
    * Stun grenade  //  Price: '30
    * Boombox  //  Price: '60
    * TZP-Inhalant  //  Price: '120 
    * Zap gun  //  Price: '400 
    * Jetpack  //  Price: '700
    * Extension ladder  //  Price: '60
    * Radar-booster  //  Price: '60
    * Spray paint  //  Price: '50
    * Weed Killer //  Price: '25
    * Belt bag  //  Price: '45 
    
    * Cruiser //  Price: '370                
    SHIP UPGRADES
    * Loud horn  //  Price: '100
    * Signal Translator  //  Price: '250
    * Teleporter  //  Price: '375
    * Inverse Teleporter  //  Price: '425

    The selection of the ship decor rotates per-quota. Be 
    sure to check back next week:
    ----------------------------------------

    [UNDER DEVELOPMENT]

    
    """)

    def resolve_item(item):
        item_lower = item.lower()
        # Trying for shortcut match
        for shortcut, full_name in shortcuts.items():
            if item_lower.startswith(shortcut):
                return full_name
        # Trying for full name match
        return next((k for k in menu_items if k.lower() == item_lower), None)

    # Checking for BUY or INFO
    if "BUY" in Schoice.upper():
        match = re.search(r'\bBUY\s+(\d+)?\s*(.*)', Schoice, re.IGNORECASE)
        if match:
            quantity = int(match.group(1)) if match.group(1) else 1
            item = match.group(2).strip()
            resolved_item = resolve_item(item)
            if resolved_item and resolved_item in menu_items:
                total = quantity * menu_items[resolved_item]
                if credits >= total:
                    credits -= total
                    print(f"You bought {quantity} x {resolved_item} for {total} credits.")
                    print(f"Credits left: {credits}")
                else:
                    print("Not enough credits!")
                credits = 60  # Reset credits to 60 after purchase {will change later}
            else:
                print("Item not found in the menu.")
        else:
            print("Invalid BUY command format.")
    elif "INFO" in Schoice.upper():
        match = re.search(r'\bINFO\s+(.*)', Schoice, re.IGNORECASE)
        if match:
            item = match.group(1).strip()
            resolved_item = resolve_item(item)
            if resolved_item and resolved_item in menu_items:
                
                if resolved_item in info_messages:
                    print(info_messages[resolved_item])
                else:
                    print(f"{resolved_item}: {menu_items[resolved_item]}")
            else:
                print("[This action was not compatible with this object.]")
        else:
            print("[This action was not compatible with this object.]")
    else:
        print("[This action was not compatible with this object.]")

    
    menu(credits)
#Menu
def menu(credits):
    print("                                   ")
    print("                    '", credits, " ")
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

                      Please enter your choice: 
                                                                                     """)
    if choice == "MOONS" or choice == "moo" or choice == "moons" or choice == "m":
        moons(credits)
    elif choice == "STORE" or choice == "store":
        store(credits, walk)
    elif choice == "BESTIARY" or choice == "bestiary" or choice == "B" or choice == "b":
        bestiary()
    elif choice == "STORAGE" or choice == "storage":
        storage()
    elif choice == "OTHER" or choice == "ot" or choice == "O" or choice == "o":
        other()
    else:
        print("You must only select one of the capitalized words")
        print("Please Try Again :) ")
        menu(credits)

def moons(credits):
    print("                                   ")
    print("                   '" ,credits , " ")
    mchoice = input("""
                      
                      Welcome to the exomoons catalogue. 
                      To route the autopilot to a moon, use the command ROUTE.
                      To learn about any moon, use the command INFO.
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                      * The Company Building // Buying at 100%
                      * Experimentation 
                      * Assurance 
                      * Vow 
                      * Offense 
                      * March 
                      * Adamance 
                      * Rend 
                      * Dine 
                      * Titan 
                      * Artifice
                      * Embrion
                      * Liquidation

                      Please enter your command:
                      """)

    # Shortcuts for moons
    moon_aliases = {
        "the company building": ["the company building", "company", "comp"],
        "experimentation": ["experimentation", "expe", "exp"],
        "assurance": ["assurance", "assu", "ass"],
        "vow": ["vow", "v"],
        "offense": ["offense", "off"],
        "march": ["march", "mar"],
        "adamance": ["adamance", "ada"],
        "rend": ["rend"],
        "dine": ["dine"],
        "titan": ["titan", "tit"],
        "artifice": ["artifice", "art"],
        "embrion": ["embrion"],
        "liquidation": ["liquidation"]
    }

    # Helper to resolve moon name from input
    def resolve_moon(user_input):
        user_input = user_input.lower()
        for moon, aliases in moon_aliases.items():
            for alias in aliases:
                if alias == user_input:
                    return moon
        # Trying for partial match
        for moon, aliases in moon_aliases.items():
            for alias in aliases:
                if user_input in alias:
                    return moon
        return None

    # Info messages for each moon 
    def print_moon_info(moon):
        if moon == "the company building":
            print("""
                  71-Gordion

                  POPULATION: Unknown 
                  
                  CONDITIONS: No land masses. Continual Storms.
                 
                  FAUNA: Unknown 
                  Where the Company resides.
                  
                  Status: UNKNOWN
            """)
        elif moon == "experimentation":
            print("""
                  41-Experimentation

                  POPULATION: Abandoned. 
                 
                  CONDITIONS: Arid. Thick haze, worsened by industrial artifacts
                 
                  FAUNA: Dominated by a few species. 
                  
                  HISTORY: Not discovered for quite some time due to its 
                  close orbit around gas giant Big Grin. However it appears  
                  to have been used in secret.
            """)
        elif moon == "assurance":
            print("""
                  220-Assurance

                  POPULATION: Abandoned. 
                  
                  CONDITIONS: Similar to its moon, 41-experimentation,
                  featuring far more jagged and weathered terrain.
                  
                  HISTORY: 220-Assurance is far younger than its 
                  counterpart. Discovered not long before 41-
                  Experimentaton.
                  
                  FAUNA: Ecosystem supports territorial behavior.
            """)
        elif moon == "vow":
            print("""
                  56-Vow

                  POPULATION: Abandoned. 
                  
                  CONDITIONS: Humid, Rough terrain. Teeming with plant 
                  life.
                  
                  HISTORY: Vow appears to have been inhabited by several colonies 
                  across its continents, but there is now no sign 
                  of life, and they have become a mystery.
                  
                  FAUNA: Diverse , teeming with plant-life. A competitive
                  ecosystem supports aggressive lifeforms.
            """)
        elif moon == "offense":
            print("""
                  21-Offense

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
        elif moon == "march":
            print("""
                  61-March

                  POPULATION: Abandoned. 
                  
                  CONDITIONS: March undergoes constant drizzling weather.
                  Its terrain is more expansive.
                  
                  HISTORY: This moon is overlooked due to its twin moon,
                  Vow.
                  
                  FAUNA: Diverse 
            """)
        elif moon == "adamance":
            print("""
                  20-Adamance 

                  POPULATION: Abandoned. 
                  
                  CONDITIONS: Erosion and geographical forces have resulted in a landscape of 
                  deep valleys and mountains.
                  
                  HISTORY: Adamance is the biggest and oldest of what are colloquially 
                  referred to as the "Green Witches": Vow, March , and Adamance, which orbit 
                  No Service.
                  
                  FAUNA: Adamance is home to a lively, diverse ecosystem of smaller-sized 
                  omnivores.
            """)
        elif moon == "rend":
            print("""
                  85-Rend 

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
        elif moon == "dine":
            print("""
                  7-Dine 

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
        elif moon == "titan":
            print("""
                  8-Titan

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
        elif moon == "artifice":
            print("""
                  68-Artifice

                  CONDITIONS: Abandoned facilities are littered across the
                  landscape, which was once teeming with life.
                  
                  HISTORY: Weapons and classified technology has been found 
                  at various sites on the surface, dating back at least two
                  hundred years.
                  
                  FAUNA: It's rumored that active machinery has been left 
                  behind.
            """)
        elif moon == "embrion":
            print("""
                  5-Embrion

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
        elif moon == "liquidation":
            print("""
                  44-Liquidation

                  POPULATION: None.
                  
                  CONDITIONS: Previously mined for its rich industrial 
                  resources , Liquidation is now largely an ocean moon.
                  
                  FAUNA: 
            """)
        else:
            print("[This action was not compatible with this object.]")

    # checking command and moon
    import re
    match = re.match(r'\s*(INFO|ROUTE)\s+(.+)', mchoice, re.IGNORECASE)
    if not match:
        print("[This action was not compatible with this object.]")
        return moons(credits)

    command = match.group(1).strip().upper()
    moon_input = match.group(2).strip()
    moon = resolve_moon(moon_input)

    if not moon:
        print("[This action was not compatible with this object.]")
        return moons(credits)

    if command == "INFO":
        print_moon_info(moon)
    elif command == "ROUTE":
        print(f"The autopilot is ROUTED to {moon.title()}.")

    menu(credits)
    
def bestiary():
    print("lolll")

def storage(): 
    print("WALLET")

def other():
    print("klll")

if __name__ == "__main__":
    main()
