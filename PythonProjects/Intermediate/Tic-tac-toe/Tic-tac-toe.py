from Classes import Player

def makeBoard():
    template = ["___","___","___","___","___","___","   ","   ","   "]
    
    r_1 = template[0] + "|" + template[1] + "|" + template[2]
    r_2 = template[3] + "|" + template[4] + "|" + template[5]
    r_3 = template[6] + "|" + template[7] + "|" + template[8] 
    
    return r_1,r_2,r_3


def run():
    welcome = """ 
    Welcome to Tic-tac-toe
    
    This a solo player or 2 players game, please select the mode you want to play by input the corresponding number (1 = Solo player , 2 = Two players):
    
    """
    mode = int(input(welcome))
    
    while mode <=0 or mode > 2:
        mode = int(input("Please select a correct value for a mode: "))
    
    if mode == 1:
        
        pass
    
    else:
        pass


if __name__ == '__main__':
    run()


