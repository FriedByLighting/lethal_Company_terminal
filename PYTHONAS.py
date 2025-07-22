# v0.6 // NOT FINISHED YET 
#V V V V |UPDATE NOTES| V V V V V V 
#! ! ! The STORE function is NOT WORKING! ! ! ! (yet i will fix it in the next updates)
##-Added the SIGURD() function
#-Added bestiary() function and finished it 
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
    #Shortcuts
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
    elif choice == "SIGURD" or choice == "sigurd":
        sigurd()
    
    
    
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
        if creature == "Baboon Hawk":
            print("""
                     Sigurd's danger level: 75%
                      
                     Scientific name: Papio-volturius
                    
                     Baboon hawks are a primate of the family Cercopithecidae. They are hunchbacked but can stand up to 8 feet on average. 
                     Their heads are boney, with bird-like beaks and long horns, which they use like skewers to gore and feed on prey. 
                     Their horns are made of keratin instead of bone like the rest of their skulls, and they do not contain nerves or blood vessels. 
                     As a result, baboon hawks can often break their horns from the force they apply, then fully regrow them within the same season. Baboon hawks partly
                     owe their name to their large wings, which could never carry their large body mass and are used instead for intimidation and protection from the elements.
                  
                     The largest baboon hawk troop ever observed was made up of 18 baboon hawks. They are loosely territorial, and much of their behavior is motivated by intimidation and display. 
                     They can become collectors, using any flashy or colorful object to mark their territory. As lone scouts, baboon hawks are generally timid and won't attack unless provoked. 
                     In greater numbers they can become a great danger; sticking close to others and making yourself seem dangerous is the best ways to prevent an attack.
                     They prefer smaller mammals, but when desperate they are known to use their numbers to attack animals even twice their size, such as eyeless dogs. THEY TOOK M Y PICKLES

                    
                  

                                                                               """)
        elif creature == "Barber":
            print("""
                    Barber


                    I had a dream about the Barber

                    One day he made me a wig

                    Because his scissors were too big




                                                         """)
        elif creature == "Bracken":
            print("""
                  
                  Sigurd's danger level: 70%
                  
                  Scientific name: Rapax-folium
                  
                  There is debate on the genus to which the Bracken belongs. It is a bipedal vertebrate with skin 
                  the color and texture of a red beet. 
                  The name is coined for what appear to be leaves protruding from its upper spine. The purpose of these is believed 
                  to be for intimidation, however not much is known about 
                  the specifics of bracken behavior due to its elusiveness and low population.

                  We know a little from accounts by wildlife experts who have encountered it. It is a lone hunter with high intelligence. 
                  Its behavior can seem aloof; it exhibits high aggression even when unprovoked, yet quickly backs off when confronted. However, brackens are known to up 
                  their hostility when cornered or simply watched for a long time. It's theorized that upon death their bodies undergo
                   a rapid decomposition process which is unique from other large animals.
           
                  
                  
                  
                  
                  
                                                                                                         """)
        elif creature == "Bunker Spider":
            print("""
                      Sigurd's danger level: 30%
                      
                      Scientific name: Theraphosa-ficedula

                      Bunker spiders, of the genus Theraphosa, are the largest arachnid found in the Thistle Nebula and the second largest ever discovered. It's believed they evolved 
                      to prey on large mammals over the course of a measly several hundred years after 
                      the Boat made its trip around the Thistle Nebula. (Refer to: Speculation on Increased Speciation Around the Fading Nebulae)
                  
                      Bunker spiders produce silk and lay it around their chosen nesting area, then wait for it to be tripped on. They can be seen waiting on walls, often over doorways where prey could enter unaware. If you find a bunker spider 'unprepared' 
                      it may freeze as a defensive reaction. In this case they are best left alone. If a bunker spider reacts aggressively, it is best not to fight with ordinary tools. They use their webs 
                      to make up for their rather slow movement, so take note of your surroundings. Their webs can be broken easily with any blunt tool.
                      
                      Bunker spiders can pose a great danger to humans and urban explorers especially, without a great benefit to their ecosystems. A resulting kill-on-sight order has been informally 
                      agreed upon between many states home to the Bunker spider, and it is currently approved by the ITDA as of 10/6/1965.









            
                                                                                               """)
        elif creature == "Butler":
            print("""
                      Sigurd's danger level: 70%

                      Theres no file on ths one so i'm MAKING it myself. we keep finding 
                      these stinky freaks in the mansion, they wont talk to us, they dont even 
                      pay attention to us and they look like deflated ballloons. the smell is like rotten meat, it's so bad it puts 
                      richard to shame. i hear flies buzzing around inside their bodies. Jess said she saw something crawl 
                      out of its eye socket and go back in.

                      I don't know what to make of this man

                      they just walk aroun and sweep the floor, I guess thats why the mansion is so clean. At least they 
                      do their job. But I swear the stinky freaks stare at me when I'm not looking

                      update: They chased Rich with a knife. we didnt see it, but he says when he got into the room, the butler just 
                      took out its broom and started sweeping like nothing happened. So we're all sticking together from now on. 
                      Screw these butlers! Now i have to stay closer to rich and he probably pissed in his suit










                                                                                                                                                       """)
        elif creature == "Coil-Head":
            print("""
                  
                  Sigurd's danger level: 80%
                  
                  Scientific name: Vir colligerus
                  
                  Vir colligerus, or colloquially named Coil-heads, are a recent discovery and have not been studied 
                  extensively due to their extreme unpredictability and dangerous properties. They have been known to combust into flames 
                  when being dissected or even deactivated, and they carry
                  
                  dangerously high levels of radioactive particles. Due to this and other reasons, it has been 
                  highly speculated they were created as biological weapons of war, although this has not been proven.

                  Coil-heads' visual appearance is that of a bloody mannequin with its head 
                  connected by a spring. Their defining behavioral characteristic is to stop when being looked at. However, this does not 
                  appear to be a hard-and-fast rule. When they encounter a loud noise or bright light
                  they appear to enter a long reset mode. Just stare at htem or use a stun grenade! - Sigurd
            
                  
                  """)
        elif creature == "Circuit Bees":
            print("""
                  
                  Sigurd's danger level: 90%
                  
                  Scientific name: Crabro-coruscus

                  The circuit bee, also known as red bee, is a eusocial flying insect of the genus Apis, a descendant of the honey bee. Their appearance is 
                  quite recognizable from their hairy, red bodies and two sets of wings. Like their ancestors, they are well-known for their intelligent 
                  social BEEhavior, large colony size, building wax nests which they use to store honey, and their important role in pollination. Unlike the honey bee, which often chose 
                  high places such as trees to construct its hive, red bees create their hives on the ground.

                  Red bees are highly defensive. They will leave the nest to attack any creature that comes 
                  within several meters, leaving BEEhind only the queen and drone bees. This bold BEEhavior is enabled by their most defining 
                  aBEElity, which is their electrostatic charge. Red bees produce friction with the air. They also produce friction by rubbing their 
                  two pairs of wings against each other any by rubbing against one another while in the hive. What allows them to create such a surplus of electric field compared to 
                  the honey bee is still under research, as they generate a stronger electric field when panicked or angered. This ability is especially useful for them around water.
                  
                  It’s BEEst to keep your distance. If a red bee hive is stolen, red bee swarms 
                  will enter an onslaught in which they attack any living creature. This destructive BEEhavior will last until they have located the hive or completely 
                  exhausted themselves, which can take hours to days. They have BEEn known to leave BEEhind fields of bodies of small rodents, insects and even some 
                  larger mammals, and in rare cases they can start fires. Their strong BEEnefits and drawbacks to their ecosystems are highly debated. BEEbated!! – the indomitable Sigurd”
            
                  
                  """)
        elif creature == "Earth Leviathan":
            print("""
                  Sigurd's danger level: 2% cause they can't hide from the ship cmaeras!!
                  
                  Scientific name: Hemibdella-gigantis

                  The reverently named Earth Leviathan, of the family Piscicolidae, is one of the largest invertebrates found around 
                  the Thistle Nebula. None have been captured, so not much is known of their biology.

                  They seem to behave as predators. It's speculated they can burrow 
                  as far as 40 meters underground, judging by the incredible excavations they can leave behind. They can detect even 
                  the slightest vibrations, and for this reason it's not recommended to stay still if they are nearby; that is a myth. Instead, if you hear 
                  them burrowing, retrace your steps.
            
                  
                  """)
        elif creature == "Eyeless Dog":
            print("""
                  Scientific name: Leo caecus

                  A large mammal of the class Saeptivus. They are social, hunting in very large packs. They have also been called “breathing lions” for their recognizable 
                  sound and large mouths. They are endurance hunters and attempt to make up for their lack of sight with their sense of hearing. It's a popular myth that 
                  they often mistake the sounds of their own kind for prey, entering fights within their own packs.
                  
                  Their behaviour is unique from other pack animals in their tendency to spread out far to cover distance. When an eyeless 
                  dog has found prey, it roars to alert others in the near vicinity, who will also sound the alarm, sometimes resulting 
                  in a kind of chain reaction. Eyeless dogs can be dangerous in swarms. However, they are characteristically clumsy, taking guesses at 
                  their prey's exact location which are often incorrect.
            
                  
                   """)
        elif creature == "Forest Keeper":
            print("""
                  
                  Sigurd's danger level: 50%

                  Scientific name: Satyrid-proceritas

                  Believed to share a common ancestor with rapax-folium, these behemoths are called Forest Keepers for the biomes they often inhabit. Their bodies bare markings on 
                  their front and back which mimic eyes--this trait is more helpful in their youth, as they are not agile. Their skin is a unique, dense material which hardens 
                  further throughout their lives; the large spikes and bumps across their bodies form as a result of aging.

                  It's been said Forest Keepers exhibit a curious behavior similar to that of a human child the age of 5 or 6. They will eat anything they 
                  find fascinating. Forest Keepers don't actually need to put anything into their mouths, and it's theorized their main source of energy is a process similar 
                  to photosynthesis. Still, this makes them relatively dangerous to observe. They can see across long distances, so staying low and making use of cover is a must. They cannot enter small spaces and are not generally 
                  destructive, so stay close to shelter or overhangs.
                                                                                                                                      """)
        elif creature == "Hoarding Bug":
            print("""
                  Sigurd's danger level: 0%

                  Scientific name: Linepithema-crassus

                  Hoarding bugs (of the order Hymenoptera) are large, social insects. While often found living alone, they have been found to share their nests with members 
                  of their own species. They measure a height of 3 feet on average, with bulbous bodies. The thinness of their fluid and blood and the material of their carapaces contributes to 
                  their low weight, making them capable of flight with their membranous wings. It also makes their bodies somewhat transparent.

                  Hoarding bugs were given their name due to their territorial nature. Once they have chosen a place as their nest, they will seek to 
                  adorn it with any object they can find and will protect these objects as a part of the nest. Hoarding bugs are not so dangerous alone as they are in large hives. However, if left alone, hoarding 
                  bugs are surprisingly neutral and pose little danger. wWe love the stupid cuddle bugs.!! - tjhis has been a note from the indomitable Sigurd
           
                                                                                                                                  """)
        elif creature == "Hygrodere":
            print("""
                  
                  Sigurd's danger level: 0%, if you're faster than a snail!

                  Scientific name: Hydrogere

                  A eukaryotic organism classified within the paraphyletic group Prostita. With the incredible speed of reproduction, these small organisms can 
                  multiply to millions. Hygrodere rarely split apart, instead choosing to form large, viscous masses which can take up large amounts of space and become a danger to deal with, requiring large tools or lures to relocate.

                  Hygrodere are drawn to heat and oxygen and can detect it from seemingly anywhere. There's almost nothing organic they can't convert to their own body mass. Nothing has been found to poison them. Constantly replacing 
                  themselves, they can persist for hundreds of thousands of years. If you ever find yourself cornered, find a tall object to stand on top of; hygroderes have trouble climbing. they have great taste! 
                  cause I made a friend with one somehow,, and we think it was my music.
           
                   """)
        elif creature == "Jester":
            print("""
                  
                  Sigurd's danger level: 90% Get out o fthere before it goes APE!! You cant hide 
                  from it, just evacuate. i think it goes back in its box if everyone stays outside long enough

                  Scientific name: INSANEUS THINGUS

                  THERE'S NO FREAKING SCIENTIFIC RECORD! good luck, you know as much as us. we just call it the jester
           
                   """)
        elif creature == "Giant Sapsucker":
            print("""
                  
                  Giant Sapsucker

                  Sigurd's danger level: 10% NEVERMIND 80% whose idea was that

                  Scientific name: Sphyrapicus cursus

                  The Giant Sapsucker is a woodpecker belonging to the genus Sphyrapicus, also known as sapsuckers. As the name suggests, they are by far the largest 
                  of the species. Males on average are 5 feet tall, while females vary anywhere from 7 to 9 feet. They are flightless birds, although they have vestigial wing structure which 
                  is usually hidden by their plumage. Their bodies are brown or black, with white and red face markings. They are sharp-sighted, with nearly 360 degree range of vision. A fully grown 
                  adult's body is one of the most athletically capable of all species in the forest planets it typically inhabits.

                  Their diet consists of insects and tree sap, with the inclusion of small rodents. Giant Sapsuckers mate for life, and 
                  the adult male typically hunts and forages while the female protects the ground nest. They are fiercely protective mothers, partly due to their opportunistic
                  nature, and if anything crosses their boundaries, they will attempt to feed it to their young in pieces. They are dangerous to humans as well, and it's recommended to stay out of their territory.

                  They have been destructive to some forests and ecosystems; although they do not multiply as quickly as other species, they have 
                  been known as nomads, travelling very far very quickly, which makes their populations difficult to track.

                  Richard is also a giant sapsucker
                   
                  """)
        elif creature == "Kidnapper Fox":
            print("""
                  Sigurd's danger level: 80% GOOD JOB he gets an A+ in creep schcool

                  Scientific name: Vulpes raptor\nA large mammal of the family Canidae, the Kidnapper fox has many unique biological traits. Two of these are 
                  its horizontal jaw and unique skull shape giving it a great biting strength, and its long, frog-like tongue which can reach even twice the length of its spindly body. 
                  They are solitary hunters and mate for life.

                  Kidnapper foxes have a very long, bushy neck and tail with a more reddish coloration, which is thought to blend in well with the 
                  numerous Vain Shroud, where it can almost always be found hiding and waiting for prey. The Kidnapper fox and Vain shrouds together form one of the most infamously 
                  known and unique mutualistic relationships between two invasive species. Together they continue to spread across planetary systems, stowing away on large spacecraft. Excluding a select few nature preserves, the ITDA has issued a kill-on-sight order 
                  for the Kidnapper fox and Vain shrouds due to their impact on ecosystems.

                  The Kidnapper fox earns its name from its aggressive yet timid and territorial behaviour, preferring to finish off 
                  prey out of sight and usually in the comfort of the Vain shrouds. It usually chooses to lie low and wait for things to come its way. But if it grows restless, it can use its long, sticky tongue 
                  to snatch its prey from great distances and drag them as far as it needs. If there are Vain shrouds in your area, carry a weapon and do not stray far from others; its tongue is quite soft and fragile and can be struck easily, forcing it 
                  to stop an assault. Today there are relatively few human deaths attributed to Kidnapper foxes per year, and most victims are unsupervised children or adults hiking alone.
           
                                                                     """)
        elif creature == "Maneater":
            print("""
                     
                  Maneater
                  
                  Sigurd's danger level: 1000%

                  yOU WERE LIKE A SON

                  Scientific name: Periplaneta clamorus

                  The Maneater has been linked to a genus of cockroaches known as Periplaneta. It was first nicknamed by workers of the Caswella Mine, one of 
                  many copper mines along the asteroid belt of Lepus, in 1951. The Caswella Mine had begun to languish since the end of wartime and would soon close after operating for twelve years; working 
                  conditions had worsened long before the rumor of the Maneater had begun to spread, and as a result, it was not taken seriously by the higher ups or media at the time. On June 23 of that year, however, an eviscerated 
                  corpse was rescued from the lowest level of Caswella Mine. It was later identified as Brett Goldent, a senior mining operator. Autopsy recorded the death an accident resulting from faulty equipment. However the story became 
                  a sensation, and the Maneater rose up as a famous myth until six years later, when it would be first recorded in the DEEP57 cave expedition headed by Simon Goldent to put to rest the mystery of his father's death. This was a revelation to the scientific world, as it is 
                  now known as the largest troglobite (cave-dwelling species). A creature of this size confined to underground caves was thought impossible. Simon Goldent, who had seeked to disprove the myth, described his discovery as "traumatic."

                  Periplaneta clamorus is thought to live off of mainly plant debri and animal carcasses, both of which can be carried into the caves by running water. It seems to have never 
                  developed the instinctive fear of larger predators while living underground. Thus, as a larva it may be fascinated or indifferent to human presence. However, as larvae, they can react fearfully to loud noises or to the sight 
                  of blood and injury. Some researchers have observed the larvae to show signs of loneliness.

                  Being unhappy or afraid seems to exacerbate Periplaneta clamorus' symptoms of growth. Its metamorphosis is remarkably sudden and is a 
                  dangerous phenomenon to observe. The most telling sign that a larva is approaching metamorphosis is an excretion of an acidic, foamy liquid at its lower jaw; this substance is believed to be a catalyst and exits 
                  its body in large quantities once metamorphosis begins.

                  An adult can move incredibly fast and is capable of creating loud noise by clicking its mandibles at high frequency. In an encounter with Periplaneta clamorus, recommended procedure 
                  is to back away slowly and keep your distance, as it seems to wait for you to approach and avoids line of sight. Stopping and exhaling suddenly while arching its legs backwards 
                  is a sign that an adult is entering chase. God help[ you
            
                  
                  """)
        elif creature == "Manticoil":
            print("""

                  Sigurd's danger level: 0%

                  Scientific name: Quadrupes-manta

                  Mantacoils are a passerine bird of the family corvidae. Their bodies are quite large compared to their early descendants, and their wingspan 
                  ranges from 55 to 64 inches. Their most defining characteristic is their set of four wings. Their back wings are mostly used to stabilize when at low speed, while their front two wings
                  create the majority of lift. Their round bodies are a striking yellow but with black outlines or stripes along their primary (rear) feathers.

                  Manticoils mostly feed on small insects but can also feed on small rodents. They are highly intelligent and social. They pose little threat and have a generally passive 
                  temperament towards humans, although they are capable of transmitting Rabies, Rubenchloria, and Pitt Virus.



                                                                                                                                                            """)
        elif creature == "Mask Hornets":
            print("""
                   MASKED HORNETS
                  
                   Masked Hornets
                                                        """)    
        elif creature == "Nutcracker":
            print("""
                  The guardians of the house.

                  They watch with one tireless eye, which only senses movement; It remembers the last creature 
                  it noticed, whether they are moving or not.
                  
                   """)
        elif creature == "Old Bird":
            print("""
                  
                  
                  The Old Bird is an autonomous, offensive weapon of war with a humanoid design. Measured at 19 feet tall and 11 feet wide, its two most defining visual 
                  features are the spotlight positioned on its head, capable of emitting 100,000 lumens, and the long-range acoustic device on its chest, sometimes referred 
                  to as a sound cannon. There are additional speakers 
                  on its shoulders used to broadcast sound a long distance. The Old Bird's left arm is a claw, and its right arm 
                  is a nozzle capable of both launching rocket-propelled grenades and torching 
                  at close-range with a very hot flame. Old Birds are one of the first 
                  extra-orbital weapons to be used and mass-produced.

                  The subject of who developed the Old Birds has been an intense debate since their first recorded appearance on 
                  December 18 of 2143, when over fifty Old Birds invaded the Anglen Capital. This is considered one of the first major causes for the downfall of the Anglen Empire. The most 
                  commonly upheld theory takes into account the tension between the Anglen and Buemoch military throughout the 2100's, however nothing has been proven in the centuries since. 
                  The design of the Old Bird, down to the tempering of metals, appears 
                  intended to conceal its origin. It has been called the "walking ransom letter."

                  Old Birds' legs function as rockets, which allows them to travel long distances and find targets efficiently. But the most likely reason this feature 
                  exists is to help them enter and land from orbit. The material and fuel Old Birds rely on is similar to those of passenger space craft from around 2130.

                  Old Birds land and stay at their target planet forever. Although they often have more than enough fuel for just one trip, no behavior has been found in their programming which suggests they 
                  could choose to "migrate". Still, there are unverified accounts of Old Birds travelling autonomously to a new planet after hundreds of years of dormancy.

                  The Old Bird was historically referred to as the "Al", based off the code name it was given by the English military, the "A16-L31". In 2384, however, the song "Old Birds" released as a cult hit by the post-punk project Under Remora; just three years 
                  later, in his most famous work of the same name, street artist Land Eyrie depicted the automotons flying and landing between planets in an arrangement similar to a flock of geese--this is generally considered one of the most iconic and influential images of 
                  modern culture and solidified the modern nickname.

                  In 2356, 5-Embrion was classified as Condemned for the purposes of travel or settlement by the Boat; Old Birds were described by witness accounts as "lining the horizon". Though to this day they appear 
                  inoperative, there is a reasonable risk that many are still in sleep mode, so the planet will likely keep its status. The small moon was likely used as a testing ground for the Old Bird's flying and landing capabilities.
                  
                  
                   """)
        elif creature == "Roaming Locusts":
            print("""
                  
                  Sigurd's danger level: 0%

                  Scientific name: Anacridium-vega

                  Known as Roaming Locusts, this is a species of grasshopper. Unlike some species which are more prone to jump or fly, Roaming Locusts 
                  are almost never grounded and stay close together even when in smaller numbers. They will quickly disperse 
                  when a predator disrupts them but are highly attracted to light.
                   
                  """)
        elif creature == "Snare Flea":
            print("""
                  
                  Sigurd's danger level: 30%

                  Scientific name: Dolus-scolopendra

                  A very large arthropod of the class Chilopoda. Its body produces a silk which it primarily uses to propel itself to places 
                  where it is concealed. Its exoskeleton is somewhat fragile, and they can die from long falls. The snare flea does not produce venom, nor does 
                  it have a strong bite. It makes up for this 
                  weakness with its ability to tighten itself around large prey to suffocate.

                  The snare flea thrives in dark, warm areas. It cannot survive low temperatures 
                  and generally avoids open air and sunlight take the rats outside or just beat the hell otu of them! i think their insides could make a good milkshake,,
                  
                   """)
        elif creature == "Spore Lizard":
            print("""
                  
                  Sigurd's danger level: i ,dont know probably 5% i just hate this pudgy legged little sh it

                  Scientific name: Lacerta-glomerorum

                  Colloquially named Puffers or Spore Lizards, Lacerta-glomerorum (of the family Alligatoridae) is one of the largest and heaviest reptiles. Despite their 
                  large mouths, they are herbivores and do not have a strong bite. The bulbs on their tails are believed to secrete a chemical which attracts and accelerates the growth of the fungus 
                  species Lycoperdon perlatum, which it can then shake to release spores as a defense mechanism--an unique example of a mutualistic symbiotic relationship.

                  Spore Lizards have a very timid temperament, avoiding confrontation if at all possible. If their attempts at threat display 
                  are not effective, they may attempt to attack. It is therefore not recommended to corner or chase one. There are historical records that Spore Lizards were at least partially domesticated hundreds of years ago, however this effort 
                  was set aside by an initiative to harvest their tails for their medicinal properties.
                   
                  """)
        elif creature == "Thumper":
            print("""
                  
                  Sigurd's danger level: 70%

                  Scientific name: Pistris-saevus

                  Halves, or Thumpers, are a highly aggressive, carnivorous species of the order Chondrichthyes. Their skeletons are cartilaginous, giving their 
                  bodies a stretchy and rubbery quality. Their name comes from the fact that they must eat their bottom legs in order to escape the shell of their hatched egg; their bottom legs 
                  are hardly functional to begin with. Their arms, or front legs, are very strong, and they occasionally use them to stomp prey. They can reach great speeds in a straight line.

                  They are relentless hunters, typically at the top of their food chain. Their main weaknesses are their intelligence and complete lack of hearing. If you come across a thumper, your best means of survival are 
                  leaving its line of sight, as it is slower around corners and can't easily track prey.

                  Due to the fast and volatile evolution of this species, some theorize that Halves are one of the examples of an increased number of mutations 
                  causing higher levels of speciation in planets around the Thistle Nebula.
                   """)
        elif creature == "Tulip Snake":
            print("""
                  
                  Tulip Snakes

                  Sigurd's danger level: 1%

                  Scientific name: Draco tulipa

                  Tulip snakes, or tulip lizards, are a type of flying lizard which are easily distinguished by their long arms and wings, which can reach twice the size of other members 
                  of their genus (Draco) and sport unusually bright colors and patterns. Their name comes from the flaps under their neck and behind their head, 
                  which resemble large flower petals. (Their other unusual characteristics include 
                  an extra pair of eyes and a deeply forked tail.)

                  Their behaviour is stubborn and fearless to a fault. Indeed, tulip snakes will rarely 
                  flee a predator. But ironically, many biologists theorize that their flowery appearance aids them more as a camoflauge than an intimidation display. It also takes an important part in 
                  their elaborate courtship rituals, which are more similar to that of birds.

                  Uniquely, lifting heavy and large objects into the air has often been observed as a part of the tulip snake's 
                  mating display; they are capable of carrying rocks and plants at least twice their size in an effort to impress their potential mate. Protective, jealous, and in a frenzy, the males may end 
                  up tug-of-war fights over objects they take a liking to, which can even include other living creatures.
                   """)
        elif creature == "Vain Shroud":
            print("""
                  
                  Vain Shrouds


                 Sigurd's danger level:  THIS IS NT A CREATURE.


                 Scientific name: Phlebodium ruber 

                 Vain Shrouds, also commonly referred to as Vains, are a type of rhizomatous fern of the family Polypodiaceae. 
                 In ideal conditions, Vain Shrouds' fronds can reach a height of 8 feet, though they average 6'11'', and are 30-50 centimeters wide. 
                 Their roots are unusually large, and they are somewhat SOMEWHATTTTTTTTTTTTTTTTprickly.


                 With their aggressive reproduction and remarkable size, they take up a lot of space, making visibility 
                 difficult, and are difficult to remove. They crowd out healthy plants and offer little nutritional value. They are also highly flammable. A strongly 
                 correlated mutualistic relationship has been observed between Vain Shrouds and the Kidnapper Fox, and for this reason Vains are a danger when they are allowed 
                 to expand to great numbers. Due to this and their other harmful effects on many ecosystems and agriculture, 
                 Vains have been classified as a noxious weed by the ITDA since 2147.




                 Their planet of origin is unknown, and they were first recorded by plant researcher Alex Kurt in CoRoT-7b in 2143 
                 before being found on the other side of its same interplanetary system just weeks later. A common myth is that the Vains were first 
                 spread across planets due to their mild hallucinogenic properties when ingested, but their history is shrouded in mystery.


                 WAKE UP.. THE COMPAN Y LACED THE DROP POD WITH THE SEEDS,THEY UPSELL 
                 US FOR WEED KILLER CAUSE THEY KNOW WWE HATE THIS CHERRY RED MENACE sorry caps
                   
                  
                  """)
        else:
            print("[This action was not compatible with this object.]")

       # checking command and bestiary
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






















def storage(): 
    print("WALLET")

def other():
    print("klll")

def sigurd():
    print("SIGURD")

if __name__ == "__main__":
    main()




