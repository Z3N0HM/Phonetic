import random
import os
import webbrowser
import sys


# Python program to print 
# colored text and background 
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk)) 
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk)) 
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk)) 

prCyan("Hello World, ") 
prYellow("It's") 
prGreen("Geeks") 
prRed("For") 
prGreen("Geeks") 


def Phonetic():
    x = 0
    y = 0
    while x == 0:

        
        if y == 0:
            prYellow("-----------------")
            print("Type :qa! to quit")
            prYellow("-----------------")
        y = y + 1
        answer = input(str("Select Needed Letter:   "))

        if answer == ":qa!":
            Ask()
        
        elif answer == "a" or answer == "A":
            print("Alpha")
        elif answer == "b" or answer == "B":
            print ("Bravo")
        elif answer == "c" or answer == "C":
            print("Charlie")
        elif answer == "d" or answer == "D":
            print("Delta")
        elif answer == "e" or answer == "E":
            print("Echo")
        elif answer == "f" or answer == "F":
            print("Foxtrot")
        elif answer == "g" or answer == "G":
            print("Golf")
        elif answer == "h" or answer == "H":
            print("Hotel")
        elif answer == "i" or answer == "I":
            print("India")
        elif answer == "j" or answer == "J":
            print("Juliet")
        elif answer == "k" or answer == "K":
            print("Kilo")
        elif answer == "l" or answer == "L":
            print("Lima")
        elif answer == "m" or answer == "M":
            print("Mike")
        elif answer == "n" or answer == "N":
            print("November")
        elif answer == "o" or answer == "O":
            print("Oscar")
        elif answer == "p" or answer == "P":
            print("Papa")
        elif answer == "q" or answer == "Q":
            print("Quebec")
        elif answer == "r" or answer == "R":
            print("Romeo")
        elif answer == "s" or answer == "S":
            print("Sierra")
        elif answer == "t" or answer == "T":
            print("Tango")
        elif answer == "u" or answer == "U":
            print("Unorm")
        elif answer == "v" or answer == "V":
            print("Victor")
        elif answer == "w" or answer == "W":
            print("Whiskey")
        elif answer == "x" or answer == "X":
            print("X-Ray")
        elif answer == "y" or answer == "Y":
            print("Yankee")
        elif answer == "z" or answer == "Z":
            print("Zulu") 


def Passwords():
    Words = ["Selective", "Stuff", "Cry", "Lake", "Competition", "Boiling", "Pushy", "Drink", "Testy", "Murder", "Tub", "Gaze", "Help", "Settle", "Decisive", "Gather", "Disagreeable", "Motionless", "Press", "Sticky", "Abashed", "Happy", "Beef", "Adaptable", "Boast", "Brake", "Overwrought", "Creepy", "Deserve", "Ahead", "Switch", "Calm", "Bomb", "Careless", "Grotesque", "Chicken", "Gratis", "Mist", "Cabbage", "Mix", "Closed", "Hard-to-find", "Impossible", "Scorch", "Crack", "Kindhearted", "Birthday", "Faithful", "Worried", "Surround", "Useful", "Cars", "Accessible", "Letters", "Mourn", "Squash", "Absurd", "Profuse", "Cloudy", "Dream", "Nasty", "Title", "Achiever", "Deeply", "Habitual", "Van", "Glamorous", "Grease", "Repeat", "Touch", "Regret", "Frequent", "Dinosaurs", "Fireman", "Salty", "Married", "Raspy", "Angry", "Dog", "Homely", "Bells", "Adhoc", "Choke", "Silver", "Tacit", "Happen", "Respect", "First", "Sudden", "Cow", "Romantic", "Soothe", "Ashamed", "Wise", "Wilderness", "Mom", "Glue", "Call", "Thaw", "Ring", "Tray", "Squeamish", "Loud", "Furry", "Argue", "Perfect", "Divergent", "Eminent", "Laughable", "Fabulous", "Forgetful", "Damage", "Puzzled", "Beds", "Plane", "Request", "Bone", "Earn", "List", "Disapprove", "Versed", "Juice", "Annoying", "Spiteful", "Staking", "Clear", "Popcorn", "Laugh", "Violet", "Infamous", "File", "Amusement", "Tough", "Demonic", "Pan", "Bake", "Cloistered", "Fold", "Crown", "Chase", "Snore", "Observe", "Shirt", "Tightfisted", "Rough", "Wipe", "Saw", "Tense", "Cultured", "Liquid", "Curtain", "Neighborly", "Books", "Level", "Spray", "Noisy", "Veil", "Organic", "Alike", "Clever", "Hideous", "Frail", "Walk", "Grey", "Bawdy", "Need", "Far-flung", "Pear", "Guide", "Imported", "Uttermost", "Great", "Common", "Blot", "Obese", "Stupid", "Invention", "Side", "Cheat", "Suit", "Cough", "Long", "Sense", "Floor", "Thirsty", "Short", "Start", "Existence", "Entertain", "Shade", "Camp", "Identify", "Toothsome", "Badge", "Hop", "Company", "Bleach", "Quill", "Live", "Decorous", "Houses", "Prick", "Bless", "Shelter", "Obeisant", "Bell", "Steel", "Aggressive", "Tremendous", "Joyous", "Thick", "Thundering", "Living", "Same", "Pleasure", "Abstracted", "Room", "Sore", "Land", "Pen", "Unused", "Dam", "Noxious", "Calculating", "Stitch", "Hand", "Panicky", "Hollow", "Kick", "Periodic", "Overflow", "Worthless", "Care", "Grieving", "Tendency", "Internal", "Ray", "Irate", "Order", "Wealthy", "Plug", "Metal", "Superb", "Order", "Things", "Count", "Kill", "Rapid", "Thin", "Momentous", "Sofa", "Glorious", "Root", "Punishment", "Important", "Peck", "Roof", "Aunt", "Makeshift", "Spotted", "Nappy", "Disappear", "Intelligent", "Smiling", "Pastoral", "Rest", "Bottle", "Panoramic", "Maid", "Square", "Tire", "Pump", "Excellent", "Obey", "Reproduce", "Nondescript", "Wren", "Rainy", "Tasteless", "Salt", "Post", "Obnoxious", "Possess", "Monkey", "Strengthen", "Stimulating", "Juicy", "Idiotic", "Ask", "Kiss", "Interest", "Dry", "Glow", "Payment", "Baby", "Box", "Trace", "Good", "Tent", "Magenta", "Match", "Peel", "Friend", "Wandering", "Material", "Fire", "Lucky", "Long-term", "Yarn", "Remind", "Boorish", "Pin", "Curious", "Cannon", "Anxious", "Attack", "Float", "Frighten", "Disarm", "Pass", "Back", "Hospital", "Note", "Domineering", "Seemly", "Tender", "Aware", "Pretty", "Lackadaisical", "Exultant", "Throne", "Like", "Confused", "Fail", "Power", "Terrify", "Baseball", "Discreet", "Fill", "Grumpy", "Knot", "Jar", "Instruct", "Drown", "Screw", "Straw", "Whisper", "Marvelous", "Magic", "Scent", "Oval", "Degree", "Release", "Shaky", "Functional", "Savory", "Pipe", "Cushion", "Hammer", "Appliance", "Afford", "Dark", "Harsh", "Sisters", "Boring", "Basin", "Plain", "Plate", "Brainy", "False", "Filthy", "Naive", "Cobweb", "Coach", "Brass", "Super", "Oafish", "Ignore", "Truck", "Hammer", "Mindless", "Slim", "Dispensable", "Rabid", "Wave", "Increase", "Fax", "Army", "Appreciate", "Craven", "Behave", "Kind", "Majestic", "Pickle", "Hard", "Untidy", "Measure", "Chance", "Alleged", "Tooth", "Trail", "Enormous", "Shoes", "Influence", "Unlock", "Jolly", "Fancy", "Unit", "Bad", "Lock", "Sound", "Yielding", "Chilly", "Sidewalk", "Likeable", "Lying", "Consider", "Want", "Seat", "Tempt", "Wasteful", "Thinkable", "Flashy", "Huge", "Hill", "Face", "Adjoining", "Agonizing", "Rule", "Fit", "Half", "Cent", "Interrupt", "Example", "Injure", "Frightening", "Hateful", "Brave", "Black", "Fancy", "Bridge", "Shut", "Well-to-do", "Ruthless", "Detect", "Grandiose", "Greasy", "Bubble", "Far", "Spotty", "Destroy", "Scientific", "Parcel", "Hour", "Dusty", "Sour", "Dare", "Mine", "Lively", "Nimble", "Standing", "Alluring", "Arrive", "Wealth", "Lamp", "Overjoyed", "Wool", "Crowded", "Pig", "Robust", "Fixed", "Understood", "Driving", "Wriggle", "Capricious", "Plant", "Clumsy", "Tart", "Shock", "Believe", "Program", "Animated", "Ground", "Adamant", "Education", "Slave", "Grateful", "Reminiscent", "March", "Nosy", "Venomous", "Recognise", "Planes", "Grade", "Waste", "Ball", "Unhealthy", "Servant", "Knowledge", "Clean", "Abject", "Trick", "Nest", "Balance", "Pull", "Cable", "Supreme", "Well-off", "Scene", "Detailed", "Trade", "Instinctive", "Ceaseless", "Fork", "Wicked", "Cumbersome", "Reason", "Thank", "Billowy", "Tall", "Bee", "Wrong", "Roasted", "Lumpy", "Taste", "Possessive", "Shade", "Sparkle", "Page", "Run", "Cover", "Old-fashioned", "Collect", "Blow", "Helpful", "Paste", "Thirsty", "Point", "Boat", "Expect", "Tank", "High", "Juggle", "Carry", "Colorful", "Elastic", "Young", "Bubble", "Clover", "Admire", "Crayon", "Bright", "Suggest", "Bath", "Sturdy", "Imperfect", "Zonked", "Mysterious", "Point", "Crabby", "Burly", "Thoughtless", "Quixotic", "Glass", "Square", "Hope", "Answer", "Concentrate", "Locket", "Faulty", "Deep", "Try", "Cheese", "High-pitched", "Cuddly", "Marked", "Sweltering", "Heavenly", "Miniature", "Rely", "Street",
 "Gruesome", "Wonder", "Paltry", "Hat", "Foolish", "Absorbing", "Pigs", "Direction", "Recess", "Old", "Head", "Towering", "Buzz", "Unusual", "Judge", "Available", "Secretary", "Hungry", "Eggnog", "Protest", "Drain", "Lick", "Admit", "Divide", "Normal", "Quick", "Honorable", "Merciful", "Finger", "Snake", "Ducks", "Toothbrush", "Fang", "Beautiful", "Cheap", "Owe", "Enchanted", "Tan", "Fowl", "Cure", "Repair", "Thankful", "Prickly", "Offend", "Historical", "Many", "Undress", "Lonely", "Rain", "Whistle", "Sink", "Educate", "Spade", "Stick", "Mine", "Ordinary", "Polite", "Ignorant", "Righteous", "Grip", "Blue-eyed", "Gentle", "Labored", "Bloody", "Parched", "Flowers", "Oatmeal", "Pull", "Five", "Science", "Tie", "Grate", "Impress", "Spill", "Angle", "Extend", "Twist", "Marry", "Mean", "Sore", "Worry", "Voice", "Attract", "Dry", "Handle", "Juvenile", "Milk", "Berserk", "Irritating", "Advise", "Torpid", "Sleet", "System", "Mailbox", "Healthy", "Loving", "Pause", "Aloof", "Silent", "Knife", "Powerful", "Grouchy", "Paddle", "Cloth", "Birth", "Doubt", "Fear", "Hook", "Expert", "Snatch", "Yam", "Holiday", "Found", "Wrestle", "Practise", "Train", "Pies", "Machine", "Thumb", "Eyes", "Reflect", "Legs", "Dust", "Mother", "Current", "Chop", "Force", "Whine", "Symptomatic", "Fruit", "Abounding", "Object", "Fast", "Digestion", "Guarded", "Scatter", "Abundant", "Unknown", "Leg", "Spectacular", "Purple", "Uninterested", "Neck", "Well-made", "White", "Bird", "Laugh", "Toy", "Cattle", "Warm", "Reflective", "Creator", "Kick", "Sky", "Channel", "Wish", "Aberrant", "Teaching", "Prefer", "Coordinated", "Hobbies", "Airport", "Hand", "Loaf", "Library", "Jumbled", "Arrest", "Boot", "Expand", "Didactic", "Bounce", "Sweet", "Chalk", "Narrow", "Coast", "Heartbreaking", "Puffy", "Spark", "Whistle", "Picture", "Damaged", "Market", "Messup", "Dysfunctional", "Wiggly", "Risk", "Jittery", "Gaping", "Representative", "Attractive", "Knock", "Alcoholic", "Sharp", "Sick", "Placid", "Marble", "Second-hand", "Lowly", "Hose", "Somber", "Gaudy", "Scribble", "Squealing", "Zealous", "Brick", "Rod", "Arm", "Fish", "Cream", "Fence", "Introduce", "Desert", "Icy", "Elite", "Stranger", "Division", "Place", "Income", "Judge", "Immense", "Miscreant", "Jealous", "Optimal", "Open", "Trousers", "Punch", "Breathe", "Upset", "Riddle", "Gorgeous", "Women", "Smoke", "Lacking", "Bewildered", "Quiet", "Visitor", "Lush", "Melted", "Eight", "Expansion", "Puncture", "Evasive", "Glib", "Notice", "Apparel", "Obscene", "Furniture", "Knowing", "Smile", "Wood", "Muddle", "Pail", "Quiet", "Funny", "Madly", "Acrid", "Turn", "Calculate", "Yawn", "Eye", "True", "Stain", "Relax", "Territory", "Reject", "Lively", "Spoil", "Hall", "Letter", "Stale", "Windy", "Exist", "Skate", "Nebulous", "Push", "Tasty", "Bruise", "Empty", "Flimsy", "Ancient", "Bow", "Invite", "Subtract", "Taste", "Bustling", "Road", "Cold", "Rake", "Cooperative", "Witty", "Government", "Incompetent", "Fact", "Night", "Curve", "Inexpensive", "Slow", "Deranged", "Fortunate", "Talk", "Certain", "Pizzas", "Battle", "Chew", "Trouble", "Fly", "Trade", "Battle", "Rifle", "Invent", "Ruddy", "Husky", "Languid", "Dirty", "Refuse", "Wave", "Plant", "Cart", "Ragged", "Plausible", "Verse", "Ill", "Lame", "Twig", "Statuesque", "Flower", "Match", "Fair", "Awesome", "Caring", "Ship", "Parsimonious", "Crime", "Control", "Wooden", "Reaction", "Mammoth", "Cause", "Penitent", "Painful", "Size", "Paper", "Week", "Nation", "Bear", "Moan", "Curly", "Itchy", "Yoke", "General", "Overconfident", "Proud", "Amuck", "Guiltless", "Fog", "Steep", "Plucky", "Joke", "Day", "Dime", "Grass", "Excite", "Cub", "Verdant", "Poor", "Necessary", "Offbeat", "Snails", "Vessel", "Milk", "Sticks", "Keen", "Authority", "Industrious", "Pocket", "Window", "Compete", "Quarter", "Behavior", "Omniscient", "Attend", "Poison", "Dashing", "Sloppy", "Brother", "Flippant", "Hook", "Drop", "Plan", "Yummy", "Smoke", "Absorbed", "Dance", "Desk", "Sordid", "Lavish", "Tenuous", "Legal", "Ladybug", "Humorous", "Print", "Frightened", "Notebook", "Wail", "Stretch", "Precede", "Brush", "Plot", "Rural", "Pricey", "Shocking", "Border", "Unbecoming", "Listen", "Past", "Skillful", "Bushes", "Tip", "Guide", "Push", "Separate", "Afraid", "Clam", "Yak", "Handsomely", "Structure", "Cover", "Coal", "Warlike", "Workable", "Steam", "Educated", "Rich", "Dogs", "Smash", "Jog", "Uncle", "Announce", "Abortive", "Spot", "Cows", "Broken", "Ethereal", "Design", "Big", "Vacuous", "Unique", "Suit", "Rush", "Treat", "Stupendous", "Abrasive", "Clammy", "Thing", "Observant", "Pack", "Cynical", "Small", "Ghost", "Boil", "Private", "Volcano", "Offer", "Complete", "Ajar", "Bump", "Comparison", "Wing", "Type", "Wild", "Theory", "Fat", "Clip", "Embarrass", "Future", "Rot", "Pedal", "Dear", "Spring", "Geese", "Insurance", "Word", "Goofy", "Fertile", "Guitar", "Lamentable", "Weigh", "Pine", "Decorate", "Activity", "Next", "Lettuce", "Whimsical", "Solid", "Knee", "Complain", "Tremble", "Bait", "Woozy", "Argument", "Event", "Damaging", "Multiply", "Play", "Flap", "Furtive", "War", "Doctor", "Radiate", "Unnatural", "Tasteful", "Wander", "Full", "Jam", "Glistening", "Humdrum", "Story", "Base", "Encourage", "Harass", "Vigorous", "Scarf", "Wheel", "Acoustic", "Addicted", "Rightful", "Hurried", "Flag", "Scale", "Iron", "Pie", "Wistful", "Abandoned", "Number", "Vase", "Loss", "Direful", "Garrulous", "Smoggy", "Vest", "Phobic", "Worm", "Replace", "Nippy", "Stare", "One", "Ripe", "Toys", "Smash", "Land", "Reign", "Tangible", "Lighten", "Turkey", "Present", "Nail", "Vein", "Frog", "Unwritten", "Canvas", "Describe", "Account", "Spotless", "Piquant", "Copy", "Employ", "Rule", "Flood", "Rhetorical", "Pump", "Crook", "Kittens", "Knit", "Hands", "Level", "Ratty", "Even", "Tame", "Famous", "Earsplitting", "Smelly", "Electric", "Adventurous", "Alarm", "Rejoice", "Quartz", "Hate", "Part", "Aspiring",
  "Top", "Zoo", "Squeal", "Depressed", "Spy", "Scare", "Health", "Chin", "Peaceful", "Rustic", "Waiting", "Quickest", "Lopsided", "Daffy", "Psychotic", "Distance", "Safe", "Cap", "Seed", "Repulsive", "Splendid", "Aback", "Error", "Engine", "Race", "Number", "Boy", "Explain", "Hurt", "Claim", "Color", "Absent", "Comfortable", "Country", "Roomy", "Fetch", "Elated", "Bag", "Sincere", "Onerous", "Alert", "Hang", "Water", "Bashful", "Preserve", "Fluffy", "Ugliest", "Skinny", "Month", "Skirt", "Coat", "Cowardly", "Blue", "Sponge", "Circle", "Nutritious", "Trite", "Arrange", "Pollution", "Harm", "Apathetic", "Middle", "Bit", "North", "Ugly", "Delirious", "Increase", "Pale", "Futuristic", "Real", "Heal", "Heady", "Value", "Spiritual", "Animal", "Punish", "Rain", "Diligent", "Bathe", "Green", "Branch", "Church", "Look", "Transport", "Vague", "Equable", "Impartial", "Bite-sized", "Effect", "Credit", "Strange", "Resolute", "Threatening", "Question", "Sail", "Ossified", "Chemical", "Black-and-white", "Wrap", "Zinc", "Unable", "Fearless", "Chickens", "Spoon", "Ambitious", "Kindly", "Glove", "Note", "Magnificent", "Nice", "Preach", "Boundary", "Easy", "Belief", "Reply", "Difficult", "Grin", "Impulse", "Rigid", "Youthful", "Downtown", "Selfish", "Rub", "Woman", "Umbrella", "Befitting", "Prepare", "Earthquake", "Advice", "Substance", "Leather", "Thoughtful", "Kneel", "Basket", "Cake", "Quilt", "Cat", "Analyse", "Finger", "Wire", "Untidy", "Cook", "Sock", "Voyage", "Ultra", "Valuable", "Kettle", "Uneven", "Sleep", "Bed", "Imminent", "Scattered", "Crawl", "Last", "Mask", "Store", "Own", "Hot", "Carriage", "Drip", "Cough", "Temporary", "Stitch", "Include", "Meeting", "Pink", "Actually", "Puzzling", "Motion", "Relation", "Two", "End", "Halting", "Scissors", "Physical", "Icicle", "Mint", "Lunch", "Truculent", "Son", "Squirrel", "Horses", "Song", "Carve", "Vanish", "Card", "Blind", "Tame", "Jellyfish", "Pat", "Brown", "Thrill", "Careful", "Suspend", "Macabre", "Permissible", "Red", "Train", "Secret", "Fire", "Quarrelsome", "Silky", "Wakeful", "Lazy", "Slap", "Grandfather", "Lunchroom", "Promise", "Escape", "Man", "Vegetable", "Agreeable", "Measure", "Redundant", "Balance", "Disillusioned", "Sound", "Incredible", "Shake", "Tin", "Key", "Copper", "Comb", "Deer", "Double", "Childlike", "Cherries", "Retire", "Mass", "Gainful", "Governor", "Materialistic", "Scandalous", "Voiceless", "Fuel", "Advertisement", "Record", "Step", "Opposite", "Erratic", "Kaput", "Bouncy", "Uncovered", "Trip", "Dependent", "Trashy", "Heavy", "Six", "Language", "Premium", "Breath", "Beam", "Depend", "Queue", "Amusing", "Cactus", "Cakes", "Lie", "Face", "Fuzzy", "Accidental", "Deserted", "Wacky", "Wary", "Team", "Chunky", "Skin", "Snail", "Please", "Test", "Best", "Drawer", "Pencil", "Writer", "Rob", "Abaft", "Dangerous", "Flagrant", "Malicious", "Cherry", "Horrible", "Scared", "Pinch", "Unadvised", "Grip", "Dust", "Excited", "Part", "Relieved", "Realise", "Various", "Belong", "Hope", "Dynamic", "Trust", "Clean", "Complex", "Womanly", "Summer", "Butter", "Smooth", "Memory", "Hellish", "Toe", "Approval", "Spooky", "Limping", "Stir", "Endurable", "Energetic", "Alive", "Milky", "Duck", "Receptive", "Rub", "Separate", "Hypnotic", "Tired", "Wound", "Jail", "Desire", "Quirky", "Imaginary", "Jobless", "Flawless", "Invincible", "Camp", "Sweater", "Hydrant", "Supply", "Ambiguous", "Questionable", "Hushed", "Examine", "Men", "Inconclusive", "Grab", "Waggish", "Branch", "Bedroom", "Sail", "Messy", "Cheerful", "Pop", "Wonderful", "Trip", "Ski", "Frantic", "Interfere", "Zebra", "Prose", "Check", "Disastrous", "Simplistic", "Table", "Kitty", "Bizarre", "Rate", "Close", "Faint", "Bolt", "Like", "Scarecrow", "Obsequious", "Profit", "Beginner", "Tested", "Measly", "Little", "Sign", "Spare", "Rhythm", "Fairies", "Present", "Allow", "Charge", "Selection", "Foregoing", "Airplane", "Share", "Cause", "Condition", "Racial", "Known", "Year", "Sugar", "Interesting", "Swing", "Wish", "Different", "Silly", "Scold", "Awful", "Improve", "Obsolete", "Soap", "Intend", "Rude", "Unpack", "Suggestion", "Meat", "Gabby", "Appear", "Rotten", "Sneeze", "Hover", "Sip", "Smell", "Possible", "Deliver", "Creature", "Ink", "Stream", "Protective", "Unwieldy", "Hilarious", "Tickle", "Harmonious", "Rhyme", "Pathetic", "Anger", "Club", "Fretful", "Work", "Feeble", "Car", "Fold", "Doubtful", "Rambunctious", "Soft", "Follow", "Drum", "Macho", "Pointless", "Communicate", "Connect", "Thread", "Stove", "Zippy", "Harmony", "Flesh", "Sigh", "Elegant", "Vast", "Waves", "Smart", "Tense", "Property", "Pick", "Force", "Female", "Scratch", "Hunt", "Wash", "Unfasten", "Screw", "Annoyed", "String", "Stamp", "Pray", "Sassy", "Slow", "Knot", "Wall", "Terrible", "Volatile", "Brief", "Experience", "Mundane", "Highfalutin", "Striped", "Descriptive", "Noise", "Seal", "Shallow", "Quack", "Bikes", "Blink", "Drunk", "Arithmetic", "Medical", "Assorted", "Spiffy", "Moldy", "Belligerent", "Foamy", "Ill-fated", "Oceanic", "Sad", "Overt", "Second", "Crooked", "Sack", "Cats", "Heat", "Fragile", "Cross", "Rare", "Breezy", "Elfin", "View", "Applaud", "Paint", "Exuberant", "Judicious", "Girls", "Nerve", "Rescue", "Handsome", "Time", "Observation", "Yellow", "Aftermath", "Innocent", "Bucket", "Tongue", "Place", "Annoy", "Jumpy", "Illustrious", "Use", "Literate", "History", "River", "Spell", "Adhesive", "Pleasant", "Nifty", "Explode", "Nut", "Star", "Mark", "Dirt", "Aboriginal", "Tap", "Rock", "Surprise", "Uppity", "Courageous", "Lean", "Death", "Friction", "Position", "Nod", "Ill-informed", "Detail", "Amount", "Grubby", "Astonishing", "Jagged", "Erect", "Shop", "Tidy", "Economic", "Harbor", "Unaccountable", "Play", "Changeable", "Left", "Knowledgeable", "Shrill", "Flavor", "Sheet", "Addition", "Weight", "Trot", "Texture", "Plants", "Sand", "Sneeze", "Growth", "Stormy", "Oranges", "Pancake", "Voracious", "Tow",
   "Lock", "Can", "Quiver", "Bored", "Girl", "Mark", "Cagey", "Brawny", "Lyrical", "Stocking", "Touch", "Cast", "Bitter", "Grain", "Poke", "Military", "Disgusted", "Reach", "Pet", "Smile", "Auspicious", "Brash", "Remember", "Fluttering", "Back", "Thought", "Wholesale", "Draconian", "Calculator", "Evanescent", "Attraction", "Bite", "Toes", "Memorise", "Zesty", "Correct", "Head", "Sniff", "Round", "Plastic", "Record", "Elbow", "Nauseating", "Move", "Haunt", "Exchange", "Wry", "Debonair", "Beg", "Obtain", "Unite", "Slip", "Committee", "Sack", "Stiff", "Spiky", "Sin", "Fierce", "School", "Wash", "Dinner", "Return", "Shelf", "Fry", "Look", "Charming", "Rebel", "Noiseless", "Magical", "Class", "Earth", "Longing", "Loose", "Ruin", "Festive", "Lip", "Basketball", "Cute", "Lumber", "Pets", "Meaty", "Provide", "Poised", "Near", "Hair", "Hospitable", "Front", "Signal", "Silk", "Change", "Whip", "Sun", "Whole", "Murky", "Flash", "Gold", "Move", "Typical", "Stage", "Giraffe", "Snobbish", "Line", "Sneaky", "Cheer", "Lace", "Dress", "Few", "Sedate", "Maddening", "Victorious", "Statement", "Telling", "Elderly", "Shop", "Stop", "Familiar", "Friends", "Avoid", "Label", "Receipt", "Vivacious", "House", "Sparkling", "Fall", "Spurious", "Undesirable", "Develop", "Tramp", "Three", "Fallacious", "Soak", "Shock", "Discover", "Picayune", "Aromatic", "Blush", "Ice", "Crowd", "Money", "Stop", "Nose", "Awake", "Satisfy", "Action", "Time", "Colour", "Discussion", "Art", "Spicy", "Shoe", "Honey", "Trouble", "Afternoon", "Ants", "Envious", "Borrow", "Door", "Range", "Matter", "Drain", "Babies", "Rings", "Hurry", "Air", "Entertaining", "Tree", "Handy", "Insidious", "Steadfast", "Shave", "Meal", "Wretched", "Spot", "Defeated", "Vengeful", "Rat", "Smell", "Bumpy", "Confess", "Ablaze", "Wobble", "Used", "Coil", "Enchanting", "Mug", "Meek", "Change", "Trucks", "Corn", "Wrist", "Trick", "Inquisitive", "Glossy", "Swift", "Drop", "Strap", "Outstanding", "Teeth", "Film", "Greedy", "Violent", "License", "Route", "Dizzy", "Last", "Stay", "Abusive", "Apparatus", "Political", "Dock", "Embarrassed", "Groan", "Attach", "Learned", "Miss", "Royal", "Tug", "Telephone", "Cracker", "Unarmed", "Squeeze", "Phone", "Jump", "Deafening", "Gifted", "Delightful", "Hapless", "Flat", "Able", "Sign", "Boundless", "Passenger", "Low", "Mighty", "Grape", "Aboard", "Peace", "Disagree", "Heap", "Apologise", "Bat", "Form", "Tedious", "Start", "Damp", "Determined", "Scrape", "Knotty", "Early", "Zany", "Frame", "Incandescent", "Successful", "Suck", "Flower", "Hissing", "Society", "Suppose", "Unbiased", "Accurate", "Need", "Efficient", "Chess", "Low", "Egg", "Wrathful", "Straight", "Soda", "Dad", "Store", "Produce", "Mind", "Fear", "Fade", "Aquatic", "Colossal", "Haircut", "Callous", "Support", "Tail", "Brake", "Dead", "Bike", "Steady", "Queen", "Gamy", "Outrageous", "Treatment", "Unkempt", "Large", "Remove", "Adorable", "Fantastic", "Accept", "Guess", "Rail", "Chief", "Homeless", "Productive", "Confuse", "Watch", "Special", "Classy", "Odd", "Add", "Wax", "Man", "Responsible", "Cellar", "Godly", "Curve", "Chivalrous", "Raise", "Kiss", "Throat", "Winter", "Substantial", "Fresh", "Natural", "Ready", "Melodic", "Steer", "Tearful", "Sophisticated", "Feigned", "Abhorrent", "Stretch", "Receive", "Shape", "Slimy", "New", "Skip", "Tangy", "Book", "Weak", "Ritzy", "Numerous", "Jewel", "Nest", "Stem", "Carpenter", "Island", "Shaggy", "Long", "Acidic", "Cycle", "Psychedelic", "Book", "Uptight", "Amused", "Use", "Snakes", "Pot", "Giant", "Birds", "Resonant", "Laborer", "Squalid", "Polish", "Squeak", "Curved", "Calendar", "Rabbits", "Home", "Minister", "Enter", "Needle", "Building", "Tranquil", "Exercise", "Sea", "Groovy", "Abrupt", "Moaning", "Request", "Consist", "Deceive", "Willing", "Rose", "Mute", "Burst", "Disgusting", "Oven", "Scrub", "Group", "Crack", "Recondite", "Plough", "Approve", "Dull", "Null", "Spark", "Hot", "Reading", "Price", "Stone", "Bore", "Terrific", "Quince", "Acceptable", "Obtainable", "Open", "Eggs", "Save", "Delicate", "Lewd", "Misty", "Eatable", "Business", "End", "Acoustics", "Previous", "Mere", "Mountain", "Trains", "Test", "Potato", "Tick", "Yard", "Ten", "Exotic", "Vacation", "Tiresome", "Question", "Graceful", "Giants", "Well-groomed", "Jam", "Screeching", "Actor", "Gun", "Nine", "Plastic", "Flowery", "Enjoy", "Utopian", "Public", "Bat", "Surprise", "Painstaking", "Outgoing", "Slope", "Excuse", "Party", "Jazzy", "Bent", "Ubiquitous", "Horse", "Powder", "Concern", "Muddled", "Wine", "Offer", "Itch", "Strip", "Pour", "Crow", "Morning", "Guarantee", "Partner", "Enthusiastic", "Spiders", "Cute", "Eager", "Industry", "Wet", "Button", "Imagine", "Decision", "Self", "Stomach", "Exciting", "Station", "Delight", "Thunder", "Coach", "Distinct", "Stereotyped", "Whip", "Massive", "Support", "Vulgar", "Bulb", "Foot", "Love", "Adjustment", "Name", "Four", "Ticket", "Cluttered", "Crib", "Bright", "Shiver", "Unruly", "Field", "Zephyr", "Obedient", "Horn", "Needy", "Unequal", "Mice", "Innate", "Camera", "Greet", "Watery", "Numberless", "Deadpan", "Scary", "Learn", "Muscle", "Collar", "Manage", "Blood", "Gleaming", "Swim", "Jaded", "Instrument", "Connection", "Rampant", "Tax", "Wiry", "Tricky", "Prevent", "Capable", "Minor", "Mountainous", "Snow", "Soup", "Orange", "Frame", "Giddy", "Launch", "Purpose", "Succinct", "Meddle", "Care", "Hysterical", "Sort", "Nonchalant", "Jail", "Underwear", "Sprout", "Complete", "Flaky", "Distribution", "Compare", "Hug", "Turn", "Regular", "Naughty", "Scintillating", "Hallowed", "Weary", "Remarkable", "Celery", "Wide", "Doll", "Bury", "Swanky", "Dapper", "Quizzical", "Box", "Continue", "Luxuriant", "Devilish", "Modern", "Wink", "Curl", "Woebegone", "Late", "Act", "Maniacal", "Disturbed", "Mend", "Irritate", "Daughter", "Sable", "Idea", "Step", "Extra-large", "Wanting", "Name", "Town", "Fool", "Needless", "Wind", "Male", 
   "Inform", "Sleepy", "Oil", "Blade", "Insect", "Decide", "Mature", "Zip", "Drag", "Succeed", "Flock", "Daily", "Scream", "Farm", "Precious", "Warm", "Dreary", "Mushy", "Cooing", "Office", "Amazing", "Fine", "Grandmother", "Welcome", "Fearful", "Faded", "Pest", "Children", "Attempt", "Snow", "Sister", "Synonymous", "Blushing", "Water", "Amuse", "Silent", "Perform", "Yell", "Nostalgic", "Satisfying", "Temper", "Tease", "Travel", "Dolls", "Tight", "Protect", "Jump", "Tomatoes", "Fasten", "Songs", "Sheep", "Cave", "Condemned", "Lethal", "Soggy", "Vagabond", "Broad", "Abiding", "Wrench", "Nervous", "Discovery", "Tiger", "Command", "Secretive", "Shy", "Right", "Contain", "Snotty", "Serious", "Trap", "Subdued", "Development", "Serve", "Seashore", "Therapeutic", "Destruction", "Rainstorm", "Tawdry", "Overrated", "Rice", "Probable", "Pumped", "Defective", "Cruel", "Shivering", "Reward", "Toothpaste", "Bare", "Hum", "Automatic", "Coil", "Busy", "Bead", "Frogs", "Ocean", "Mellow", "Barbarous", "Attack", "Delicious", "Food", "Conscious", "Talented", "Show", "Suffer", "Useless", "Permit", "Exclusive", "Extra-small", "Mitten", "Parallel", "Alert", "Dress", "Encouraging", "Subsequent", "Load", "Dazzling", "Love", "Chubby", "Arrogant", "Neat", "Superficial", "Earthy", "Empty", "Shrug", "Teeny", "Hate", "Gullible", "Quaint", "Visit", "Hesitant", "Roll", "Stamp", "Donkey", "X-ray", "Free", "Simple", "Talk", "Teeny-tiny", "Moor", "Troubled", "Hanging", "Plant", "Dramatic", "Trees", "Roll", "Slippery", "Occur", "Helpless", "Board", "Coherent", "Crazy", "Humor", "Nutty", "Guard", "Slip", "Stingy", "Cut", "Drab", "Guttural", "Ludicrous", "Plantation", "Sulky", "Debt", "Cautious", "Dislike", "Writing", "Bang", "Decay", "Cemetery", "Religion", "Jelly", "Park", "Crush", "Flight", "Challenge", "Stew", "Edge", "Lovely", "Fascinated", "Unsuitable", "Third", "Warn", "Zipper", "Shiny", "Equal", "Whispering", "Average", "Pretend", "Transport", "Fumbling", "Search", "Gray", "Bomb", "Breakable", "Peep", "Scrawny", "Cup", "Linen", "Interest", "Afterthought", "Join", "Wait", "Rabbit", "Wide-eyed", "Hulking", "Strong", "Petite", "Crate", "Beneficial", "Curvy", "Way", "Light", "Hole", "Finicky", "Stroke", "Feeling", "Whirl", "Porter", "Combative", "Better", "Nonstop", "Melt", "Dusty", "Moon", "Friendly", "Mate", "Waste", "Suspect", "Taboo", "Berry", "Flame", "Tiny", "Quicksand", "Space", "Weather", "Remain", "Crash", "Ban", "Agreement", "Flow", "Toad", "Unsightly", "Concerned", "Upbeat", "Regret", "Ear", "Icky", "Illegal", "Twist", "Join", "Fanatical", "Petite", "Impolite", "Caption", "Mixed", "Puny", "Shame", "Minute", "Gate", "Perpetual", "Agree", "Loutish", "Playground", "Reduce", "Robin", "Heat", "Arch", "Limit", "Person", "Defiant", "Produce", "Purring", "Rock", "Clap", "Mouth", "Scarce", "Zoom", "Gigantic", "Walk", "Level", "Report", "Clear", "Watch", "Railway", "Unequaled", "Tumble", "Axiomatic", "Form", "Truthful", "Tacky", "Cool", "Efficacious", "Volleyball", "Utter", "Burn", "Wreck", "Rinse", "Jeans", "Abnormal", "Work", "Orange", "Tour", "Inject", "Freezing", "Fix", "Acid", "Expensive", "Gusty", "Holistic", "Delay", 
        ]
    
    

        

    Word1 = (random.choice(Words))
    Word2 = (random.choice(Words))
    Word3 = (random.choice(Words))
    Word4 = (random.choice(Words))

    print("Your Generated Password Is \n >> ")
    print(Word1 + Word2 + Word3 + Word4 + "\n")

    y = 0
    x = 0
    while x < 1000:

        if y == 0:

            print("(Type :qa! to quit)")

        y = y + 1

        Enter = input("\n Press Y to Generate a new pass:")
        if Enter == ("Y"):
                Passwords()
                x = x + 1
        elif Enter == ("y"):
                Passwords()
                x = x + 1
        elif Enter == ":qa!":
            Ask()





def Document():
    path = "C:/Users/tjoosten/Desktop"
    os.chdir(path)
    with open(input("File Name: "), 'a') as f:
        f.write(input("Write Text: "))



def Chrome():
    website=input("Wanted Website: ")

    webbrowser.get('chrome').open_new_tab(a_website)



def Ask():    
    choice = input("\nChoose what you'd like \n   [1] Phonetic \n   [2] Password Gen \n   [3] Create Document \n   [4] Chrome Search \n   Choice:  ")
    

    if choice == "1":
        Phonetic()
    elif choice == "2":
        Passwords()
    elif choice == "3":
        Document()
    elif choice == "4":
        Chrome()
    else:
        print("Invalid Answer \n Choose Again \n")
        Ask()

















    
Ask()
        
