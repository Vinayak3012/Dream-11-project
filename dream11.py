import random
import dream_input

WicketKipper = [["Ishan Kishan"],["Rishabh Pant","Tristan Stubbs","Abishek Porel"]]
batsmen = [["Rohit Sharma", "Suryakumar Yadav","Tilak Varma","Tim David"],["David Warner","Prithvi Shaw"]]
allRounder = [["Hardik Pandya","Mohammad Nabi","Romario Shepard"],["Axar Patel","Lait Yadav"]] 
bowlers = [['Piyush Chawla',"Gerald Coetzee","Jasprit Bumrah"],["Jhye Richardson","Anrich Nortje","Ishant Sharma","khaleel Ahmed"]]
# DREAM_TEAM = []
# CAP_VC = []
# min_team1 = 3
# max_team2 = 8
MIN = 0

def randomPickPlayer(total_player,teamId,type):
    randNum = random.randint(MIN,total_player)
                # print(randNum)           
    if type == 1:
        return (WicketKipper[teamId][randNum])
    elif type == 2:
        return (batsmen[teamId][randNum])    
    elif type == 3:
        return (allRounder[teamId][randNum]) 
    elif type == 4:
        return (bowlers[teamId][randNum])   
    else:
        print("Please! Enter valid player type")         

def createTeam(keep,bat,allR,bowl,player_count,btn):
    DREAM_TEAM = []
    TEAM_COUNT = player_count
    i=0
    while TEAM_COUNT < player_count+1 and TEAM_COUNT > 0 and TEAM_COUNT<12: 
        while True :  
            randNum = random.randint(0,1)
            player = randomPickPlayer(len(WicketKipper[randNum])-1,randNum,1)
            if player not in DREAM_TEAM: 
                DREAM_TEAM.append(player)        
                TEAM_COUNT-=1
                i+=1
            if i == keep:
                i=0
                break
        while True :  
            randNum = random.randint(0,1)         
            player = randomPickPlayer(len(batsmen[randNum])-1,randNum,2)
            if player not in DREAM_TEAM: 
                DREAM_TEAM.append(player)        
                TEAM_COUNT-=1
                i+=1
            if i == bat:
                i=0
                break
        while True :  
            randNum = random.randint(0,1) 
            player = randomPickPlayer(len(allRounder[randNum])-1,randNum,3)
            if player not in DREAM_TEAM: 
                DREAM_TEAM.append(player)        
                TEAM_COUNT-=1
                i+=1
            if i == allR:
                i=0
                break 
        while True :  
            randNum = random.randint(0,1)         
            player = randomPickPlayer(len(bowlers[randNum])-1,randNum,4)
            if player not in DREAM_TEAM: 
                DREAM_TEAM.append(player)        
                TEAM_COUNT-=1
                i+=1
            if i == bowl:
                i=0
                break
        print(DREAM_TEAM)
        if btn == True:
            selectCVc(DREAM_TEAM,player_count)                    

def selectCVc(DREAM_TEAM,Team_count) :
    CAP_VC=[]
    i=0
    while True:
        randNum = random.randint(0,Team_count-1)
        player = DREAM_TEAM[randNum]
        if player not in CAP_VC:
            CAP_VC.append(player)
            i+=1 
        if i == 2 :
            break
    CAP_VC[0] = CAP_VC[0] + "( C )"
    CAP_VC[1] = CAP_VC[1] + "( VC )"
    print(CAP_VC)
    print("\n")

def genMulTeam(num,wik,bat,all,ball,player_count,btn):
    for i in range(0,num):
        createTeam(wik,bat,all,ball,player_count,btn) 

def main():
    print("********* Welcome to Dream11 Team-Picker App !*********")
    input("You want generate your dream team press any key to start ! ")
    team_count = dream_input.getInputTeam()
    req = input("Do you want generate custom Team ?   \n  Y-> custom team    OR     N-> default(11 player team)  (Y / N) : ").lower()
    if req == 'y':
        player_count = dream_input.getPersonalTeamCombo()  
        wicks = dream_input.getWicketkeepers()
        bats = dream_input.getBatsmen()
        alls = dream_input.getAllRounders()
        bowls = dream_input.getBowlers()
        total =  wicks + bats + alls + bowls
        if total == player_count:
            reqCvc = input("Do you want Captain  and Vice-Captain  ? \n  Y-> captain     and     N-> vice-captain  (Y / N) : ").lower() 
            if reqCvc == 'y':
                btn = True
                genMulTeam(team_count,wicks,bats,alls,bowls,player_count,btn)
            elif reqCvc == 'n' :
                btn = False
                genMulTeam(team_count,wicks,bats,alls,bowls,player_count,btn)  
            else:
                print("Enter valid response (Y / N) : ")            
        else:
            print("Team composition(total player) incorrect ! please check that! ")   
             
    elif req == 'n':
        player_count = 11
        wicks = dream_input.getWicketkeepers()
        bats = dream_input.getBatsmen()
        alls = dream_input.getAllRounders()
        bowls = dream_input.getBowlers()
        reqCvc = input("Do you want Captain  and Vice-Captain  ? \n  Y-> captain &  vice-captain     and     N->No (Y / N) : ").lower()
        if reqCvc == 'y':
            btn = True
            genMulTeam(team_count,wicks,bats,alls,bowls,player_count,btn)
        elif reqCvc == 'n' :
            btn = False
            genMulTeam(team_count,wicks,bats,alls,bowls,player_count,btn)  
        else:
            print("Enter valid response (Y / N) : ") 
    else:
        print("Enter valid input ( Y / N )")    
    print("********* THANKS FOR USING THIS APP ************")                    

if __name__ == "__main__":
    main()
               
# Test
# createTeam(2,4,2,3)
# selectCVc(DREAMTEAM)           
# # randomPickPlayer(2,0,2)               
# print(DREAMTEAM) 
# print(capVc)
# genMulTeam(0,2,4,2,3) 


#TODO: create personal choice player and 11 player separate teams
#TODO: fix input command sentences
#TODO: new output functions 
