# v0.6.4 // NOT FINISHED YET 
#V V V V |UPDATE NOTES| V V V V V V 
#! ! ! The STORE function is NOT WORKING (partially)! ! ! !
#-Added other and storage functions
#-Added sigurd function (not working yet)
#Happy Birthday Lethal Company 1st year annivesrary (23/10/2023 - 23/10/2024)

import math 
import datetime 
from function import the_moon_info
from function import the_bestiary_info
import re
import random



x = datetime.datetime.now()





print("""
      
BG IG, A System-Act Ally
Copyright (C) 2084-2108, Halden Electronics inc.
Courtesy of the Company.  
      
Bios for the FORTUNE-9 87.7/10MHZ SYSTEM               
                                                              """)
print(x.strftime("Current date is %A    %d-%m-2532"))
print(x.strftime("Current time is %H:%M:%S"))

input("Please enter favourite animal: ")
print("                                         ")
input("Please describe your role in a team dynamic:")
print("""                                         






                                                        
                        
                         
                             
                   
 """)














print(""" 
    

__        _______ _     ____ ___  __  __ _____ 
\ \      / | ____| |   / ___/ _ \|  \/  | ____|
 \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|  
  \ V  V / | |___| |__| |__| |_| | |  | | |___ 
   \_/\_/  |_____|_____\____\___/|_|  |_|_____|
                                                      """)
print("""
         
         Welcome to the FORTUNE-9 OS
                   Courtesy of the Company   
                                                                                      """)
print(x.strftime(" Happy %A"))
print('            ')
user_cmd = input("Type \"Help\" for a list of commands: ").strip().lower()
print("""




                                                                 """)
def handle_first_command(cmd, credits):
    if cmd == "help":
        credits = menu(credits)
    elif cmd in ["moons", "moo", "m"]:
        credits = moons(credits)
    elif cmd in ["store"]:
        credits = store(credits)
    elif cmd in ["bestiary", "b"]:
        credits = bestiary(credits)
    elif cmd in ["storage"]:
        credits = storage(credits)
    elif cmd in ["other", "ot", "o"]:
        credits = other(credits)
    elif cmd in ["sigurd"]:
        sigurd()
    else:
        print("[This action was not compatible with this object.]")
    return credits

def main():
    credits = 60
    last_day = datetime.datetime.now().day

    
    global user_cmd
    credits = handle_first_command(user_cmd, credits)

    while True:
        now = datetime.datetime.now()
        current_day = now.day
# probably will delete this later, really useless 
        if current_day != last_day:
            credits = 60
            print("\nA new day has started! Credits have been reset to 60 (experimental feature).\n")
            last_day = current_day
        credits = menu(credits)

#-----------[  Item Prices ]---------- 

def store(credits):
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
        
        for shortcut, full_name in shortcuts.items():
            if item_lower.startswith(shortcut):
                return full_name

        return next((k for k in menu_items if k.lower() == item_lower), None)

    
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

    
    return credits


#    -------------------------------====MENU===-----------------------------------------------



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
    if choice.lower() in ["moons", "moo", "m"]:
        credits = moons(credits)
        return credits
    elif choice.lower() in ["store"]:
        credits = store(credits)
        return credits
    elif choice.lower() in ["bestiary", "b"]:
        credits = bestiary(credits)
        return credits
    elif choice.lower() in ["storage"]:
        credits = storage(credits)
        return credits
    elif choice.lower() in ["other", "ot", "o"]:
        credits = other(credits)
        return credits
    elif choice.lower() in ["sigurd"]:
        sigurd()
        return credits
    else:
        print("[This action was not compatible with this object.]")
        return credits

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

   
    def resolve_moon(user_input):
        user_input = user_input.lower()
        for moon, aliases in moon_aliases.items():
            for alias in aliases:
                if alias == user_input:
                    return moon
        
        for moon, aliases in moon_aliases.items():
            for alias in aliases:
                if user_input in alias:
                    return moon
        return None
 
    
    
    def print_moon_info(moon):
        the_moon_info(moon)


  


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

    return credits
    
def bestiary(credits):
     print("                                   ")
     print("                   '" ,credits , " ")
     bchoice = input("""
                      BESTIARY
                     

                      To access a creature's file type \"INFO\" after its name.
                      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

                       Baboon Hawk
                       Barber  
                       Bracken 
                       Bunker Spider 
                       Butler
                       Coil-Head
                       Circuit Bees
                       Earth Leviathan
                       Eyeless Dog
                       Forest Keeper
                       Giant Sapsucker
                       Hoarding Bug
                       Hygrodere
                       Jester
                       Kidnapper Fox
                       Maneater
                       Manticoil
                       Mask Hornets
                       Nutcracker
                       Old Bird
                       Roaming Locusts
                       Snare Flea
                       Spore Lizard
                       Thumper 
                       Tulip Snake
                       Vain Shrouds

                      
                                                                                           
                                                                                                 """)
     
     bestiary_aliases = {
        "Baboon Hawk": ["Baboon Hawk", "baboon hawk"],
        "Barber": ["Barber", "barber"],
        "Bracken": ["Bracken", "bracken"],
        "Bunker Spider": ["Bunker Spider", "bunker spider"],
        "Butler": ["Butler", "butler"],
        "Coil-Head": ["Coil-Head", "coil-head", "coil head", "coilhead", "Coil Head"],
        "Circuit Bees": ["Circuit Bees", "circuit bees"],
        "Earth Leviathan": ["Earth Leviathan", "earth leviathan"],
        "Eyeless Dog": ["Eyeless Dog", "eyeless dog"],
        "Forest Keeper": ["Forest Keeper", "forest keeper"],
        "Hoarding Bug": ["Hoarding Bug", "hoarding bug"],
        "Hygrodere": ["Hygrodere", "hygrodere"],
        "Jester": ["Jester", "jester"],
        "Kidnapper Fox": ["Kidnapper Fox", "kidnapper fox"],
        "Maneater": ["Maneater", "maneater"],
        "Manticoil": ["Manticoil", "manticoil"],
        "Mask Hornets": ["Mask Hornets", "mask hornets"],
        "Nutcracker": ["Nutcracker", "nutcracker"],
        "Old Bird": ["Old Bird", "old bird"],
        "Roaming Locusts": ["Roaming Locusts", "roaming locusts"],
        "Snare Flea": ["Snare Flea", "snare flea"],
        "Spore Lizard": ["Spore Lizard", "spore lizard"],
        "Thumper": ["Thumper", "thumper"],
        "Tulip Snake": ["Tulip Snake", "tulip snake"],
        "Vain Shrouds": ["Vain Shrouds", "vain shrouds"],
        "Giant Sapsucker": ["Giant Sapsucker", "giant sapsucker"]
    }
     

     

     def resolve_bestiary(user_input):
         user_input = user_input.lower()
         for creature, aliases in bestiary_aliases.items():
            for alias in aliases:
                if alias == user_input:
                    return creature
       
         for creature, aliases in bestiary_aliases.items():
            for alias in aliases:
               if user_input in alias:
                    return creature
         return None
     


     def print_bestiary_info(creature):
          the_bestiary_info(creature)

      
      
      
      
     import re
     match = re.match(r'\s*(INFO|ROUTE)\s+(.+)', bchoice, re.IGNORECASE)
     if not match:
         print("[This action was not compatible with this object.]")
         return bestiary(credits)

     command = match.group(1).strip().upper()
     creature_input = match.group(2).strip()
     creature = resolve_bestiary(creature_input)

     if not creature:
         print("[This action was not compatible with this object.]")
         return bestiary(credits)

     if command == "INFO":
         print_bestiary_info(creature)
     else:
          print("[This action was not compatible with this object.]")
     return credits


def other(credits):
    global monitor_on
    print("                                   ")
    print("                    '", credits, " ")
    ochoice = input("""

                      Other commands:
                     
                      >VIEW MONITOR
                      To toggle on AND off the main monitor's map cam
                      
                      >SWITCH [Player name]
                      To switch view to a player on the main monitor.
            
                      >PING [Radar booster name] 
                      To make a radar booster play a noise.
                   
                      >SCAN 
                      To scan for the number of items left on the current planet.
                   

                                                                                     """).strip()

    
    if ochoice.lower() == "view monitor":
        monitor_on = not monitor_on
        if monitor_on:
            print("The monitor is on.")
        else:
            print("The monitor is off.")
        return credits

    
    match_switch = re.match(r'^switch\s+(.+)', ochoice, re.IGNORECASE)
    if match_switch:
        player_name = match_switch.group(1).strip()
        print(f"Now you are viewing '{player_name}'.")
        return credits

    
    match_ping = re.match(r'^ping\s+(.+)', ochoice, re.IGNORECASE)
    if match_ping:
        print("Pinged radar booster.")
        return credits


    if ochoice.lower() == "scan":
        objects = random.randint(10, 71)
        value = random.randint(257, 1380)
        print(f"There are {objects} objects outside the ship, totalling at an approximate value of {value}.")
        return credits

    print("""
                   
                     [This action was not compatible with this object.]
                                                                             
                                                                                       """)
    return credits



































    

def storage():
    print("                                   ")
    print("                   '" ,credits , " ")
    storage_choice = input(""" 
                      While moving furniture with [B], you can press [X]
                      to send it to storage. You can call it back from storage here.     

                      These are the items in storage:

                       Classic painting
                       Cozy lights
                       Disco ball
                       Dog house 
                       Electric chair
                       Fridge
                       Goldfish
                       Inverse Teleporter
                       Jack-o-lantern
                       Microwave
                       Plushie Pajama Man
                       Record player
                       Shower
                       Sofa Chair
                       Table
                       Teleporter
                       Televisiom
                       Toilet
                       Welcome mat
                                                                                                 """)
    storage_aliases = {
        "Classic painting": ["Classic painting", "classic painting"],
        "Cozy lights": ["Cozy lights", "cozy lights"],
        "Disco ball": ["Disco ball", "disco ball"],
        "Dog house": ["Dog house", "dog house"],
        "Electric chair": ["Electric chair", "electric chair"],
        "Fridge": ["Fridge", "fridge"],
        "Goldfish": ["Goldfish", "goldfish"],
        "Inverse Teleporter": ["Inverse Teleporter", "inverse teleporter"],
        "Jack-o-lantern": ["Jack-o-lantern", "jack-o-lantern"],
        "Microwave": ["Microwave", "microwave"],
        "Plushie Pajama Man": ["Plushie Pajama Man", "plushie pajama man"],
        "Record player": ["Record player", "record player"],
        "Shower": ["Shower", "shower"],
        "Sofa Chair": ["Sofa Chair", "sofa chair"],
        "Table": ["Table", "table"],
        "Teleporter": ["Teleporter", "teleporter"],
        "Television": ["Television", "television"],
        "Toilet": ["Toilet", "toilet"],
        "Welcome mat": ["Welcome mat", "welcome mat"]
    }

    def resolve_storage(user_input):
        user_input = user_input.lower()
        for item, aliases in storage_aliases.items():
            for alias in aliases:
                if alias == user_input:
                    return item
        for item, aliases in storage_aliases.items():
            for alias in aliases:
                if user_input in alias:
                    return item
        return None

    item = resolve_storage(storage_choice.strip())
    if item:
        print("Returned the item from storage!")
    else:
        print("[This action was not compatible with this object.]")
    

def sigurd():
    print("Sigurd is not available yet, please wait for the next update.")
    print("This is a placeholder function for future updates.")
    print("Thank you for your patience!")

if __name__ == "__main__":
    main()