title = "\n\
__  __          _   _   \n\
\ \/ /___  _ __| |_| |_ \n\
 \  // _ \| '__| __| __|\n\
 /  \ (_) | |  | |_| |_ \n\
/_/\_\___/|_|   \__|\__|"


look_syn = ["look","examine","study"]
move_syn = ["go","walk","run","skip","travel","saunter","crawl","move"]
directions = ["north","south","east","west","up","down","in","out"]






def input_handler(cmd):
    cmdList = cmd.split(" ")
    if look_syn in cmdList:
        if "around" in cmdList:
            print("this is a test of looking around")





#MAIN GAME LOOP
save_exit = False
while not save_exit:
  cmd = input("What would you like to do?   ").lower()
  if cmd == "exit":
      save_exit = True #will need to add save to this
  else:
      input_handler(cmd)
