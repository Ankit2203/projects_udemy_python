def display(gamebox,play):
    for row in range(5):
        for col in range(11):
            if row in [1,3]:
                print("-", end =" ") if col <10 else print("-")
            else:
                if col in [3,7]:
                    print("|", end =" ") if col <10 else print("|")
                elif col in [1,5,9]:
                    inp = get_val(gamebox,play,row,col)
                    print(inp, end ="") if col<10 else print(inp)
                else:
                    print(" ", end =" ") if col<10 else print(" ")

def get_val(gamebox,play,row,col):
    position = ""
    for i in range(len(gamebox)):
        if (row,col)==gamebox[i][1]:
            position=gamebox[i][0]
            break
    if position in play["X"]:
        return "X"
    elif position in play["0"]:
        return "0"
    else:
        return " "

def get_user_input(places):
    userInput = 0
    while True:
        try:
           userInput = int(input("Enter the position : "))
        except ValueError:
            print("Not an Integer")
            continue
        else:
            if userInput not in places:
               print("Wrong choice for position Enter again")
               continue
            return userInput



def tic_tac_toe():
    display_position()
    play = {'X':[], '0':[]}
    gamebox = [(1,(0,1)),(2,(0,5)),(3,(0,9)),(4,(2,1)),(5,(2,5)),(6,(2,9)),(7,(4,1)),(8,(4,5)),(9,(4,9))]
    places = [1,2,3,4,5,6,7,8,9]
    win = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7]]
    return game_on(places,play,win,gamebox)

    

    
def game_on(places,play,win,gamebox): 
    usr=1   
    while len(places)!=0:
        position = get_user_input(places)
        for i in range(len(places)):
            if (places[i]==position):
               places.pop(i)
               break
        if usr==1:
           print("For USER 1")
           play["X"].append(position)
           usr=0
        else:
            print("For USER 2")
            play["0"].append(position)
            usr=1
        display(gamebox,play)
        for i in range(len(win)):
            if (set(win[i]).issubset(set(play["X"]))):
                return "winner is USER 1"
            elif (set(win[i]).issubset(set(play["0"]))):
                return  "Winner is USER 2"

def display_position():
    count = 0
    for row in range(5):
        for col in range(11):
            if row in [1,3]:
                print("-", end =" ") if col <10 else print("-")
            else:
                if col in [3,7]:
                    print("|", end =" ") if col <10 else print("|")
                elif col in [1,5,9]:
                    count = count+1
                    print(count, end ="") if col<10 else print(inp)
                else:
                    print(" ", end =" ") if col<10 else print(" ")
                     
statement = tic_tac_toe()        
print("\n{}".format(statement))
            