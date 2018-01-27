title = """
__  __          _   _
\ \/ /___  _ __| |_| |_
 \  // _ \| '__| __| __|
 /  \ (_) | |  | |_| |_
/_/\_\___/|_|   \__|\__|"""


look_syn = ["look","examine","study"]
move_syn = ["go","walk","run","skip","travel","saunter","crawl","move"]
directions = ["north","south","east","west","up","down","in","out","around"]


#basic template for an area
class area():
    def __init__(self):
        self.directions = {"north":"description of what is to the north","south":"south","east":"east","west":"west","around":"whats around"}
        self.adjacentAreas = {"north":"name of area to north","south":"you get the idea"}
        self.characters = []
        self.items = []
        self.initialDescription = "This will be read the first time you enter area"
        self.beenHereBefore = False

    def lookDir(self,direction):
        if direction in self.directions:
            print(self.directions[direction])
        else:
            print("you don't see anything in that direction") #idealy this wont get used




class crashedShip(area):
    def __init__(self):
        self.directions = {"north":"To the north is a dense forrest",:"south":"To the south is the debit trail left by your ship.":"east":"To the east is a dense forrest.","west":"To the west is a dense forrest.","around":"Your ship is badly damaged. Aside from the debris trail tot he south you are surrounded by dense woods. Based on past expiriences it would be unwise to venture into the woods on an alien world","up":"Above you is the sky","down":"Below you is... dirt"}









#this will house all of the created areas. Input handler will update current area with somehting from this list if it's presennt in adjacent areas
areas = {}

#SETUP INITIAL CONDITIONS
currentArea = crashedShip #starting area
save_exit = False
inventory = []


def input_handler(cmd):
    cmdList = cmd.split(" ")

    if "look" in cmdList:
        if directions in cmdList:
            for words in cmdList:
                if word in currentArea.directions:
                    currentArea.lookDir(word)






#MAIN GAME LOOP
while not save_exit:
  cmd = input("What would you like to do?   ").lower()

  if cmd == "exit":
    save_exit = True #will need to add save to this
  else:
    input_handler(cmd)
