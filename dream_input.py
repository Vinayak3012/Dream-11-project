def getInputTeam():
    teams = input("Enter number of teams you want generate ( 1 , 2 ,... ) : ")
    if teams.isdigit():
        return int(teams)
    else :
        print("Please Enter valid number ( 1 , 2 ,... ) : ")
        getInputTeam()
        
# getInput()  
def getWicketkeepers():
    wik = input("Enter number of wicketkeepers of your team : ")
    if wik.isdigit():
        if int(wik) < 5:
            return int(wik)
        else:
            print("You can only select max 4 WicketKeepers in your team") 
            getWicketkeepers()       
    else:
        print("Enter valid number ( 1 , 2 ,... )") 
        getWicketkeepers() 
        
def getBatsmen():
    bat = input("Enter number of batsmen of your team : ")
    if bat.isdigit():
        if int(bat) < 7:
            return int(bat)
        else:
            print("you can only select max 6 batsmen in your team") 
            getBatsmen()
    else:
        print("Enter valid number") 
        getBatsmen()
        
def getAllRounders():
    all = input("Enter number of all-rounder of your team :  ")
    if all.isdigit():
        if int(all) < 5:
            return int(all)
        else:
            print("You can only select max 4  all rounder in your team") 
            getAllRounders()
    else:
        print("Enter valid number") 
        getAllRounders()        

def getBowlers():
    bowl = input("Enter number of bowler of your team : ")
    if bowl.isdigit():
        if int(bowl) < 7:
            return int(bowl)
        else:
            print("You can only select max 6 bowlers in your team") 
            getBowlers() 
    else:
        print("Enter valid number") 
        getBowlers()                           
        
def getPersonalTeamCombo():

    play_NO = input("Enter number of players in your team ( 1 , 2 ,... ) : ")
    if play_NO.isdigit():
        if int(play_NO) < 12:
            return int(play_NO)
        else:
            print("You can only select max 11 players in your team") 
            getBowlers() 
    else :
        print("Please Enter a valid number")
        getInputTeam()  
                          