import random
import matplotlib.pyplot as plt

def Monty_Hall(switch_doors):
    doors = ['car'] + ['goat']*2
    initial_choice = random.choice(range(len(doors)))
    host_reveal = [i for i in range(len(doors)) if i != initial_choice and doors[i] == 'goat'][0]
    if switch_doors:
        final_choice = [i for i in range(len(doors)) if i !=initial_choice and i != host_reveal][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == "car"

def simulation_game(num_games):
    plt.figure(figsize=(10,5))
    num_games += 1
    win_if_switch = 0
    win_if_keep = 0
    percent_win0 = []; percent_win1 = []; run_time0 = []; run_time1 =[]

    for num in range(1,num_games):
        if Monty_Hall(True):
            win_if_switch  += 1
        percent_win0.append(win_if_switch/num*100)
    
        if Monty_Hall(False):
            win_if_keep += 1
        percent_win1.append(win_if_keep/num*100)

    plt.subplot(1,2,1)
    plt.plot(range(1,num_games), percent_win0)
    plt.scatter(range(1,num_games,int(num_games/100)), [66.6666666 for _ in range(1,num_games,int(num_games/100))], color = 'orange', marker = '_')
    plt.yticks([0,10,20,30,40,50,60,66.6,70,80,90,100],['0', '10', '20', '30', '40', '50', '60', '66.6', '70', '80', '90', '100'])
    plt.title("Winning by Switching the Door")
    plt.ylabel("win counter (%)")
    plt.xlabel("number of running the simulation")
    plt.subplot(1,2,2)
    plt.plot(range(1,num_games), percent_win1)
    plt.scatter(range(1,num_games,int(num_games/100)), [33.3333333 for _ in range(1,num_games,int(num_games/100))], color = 'orange', marker = '_')
    plt.yticks([0,10,20,30,33.3,40,50,60,70,80,90,100],['0', '10', '20', '30','33.3', '40', '50', '60', '70', '80', '90', '100'])
    plt.title("Winning by Keeping the initial choice")
    plt.ylabel("win counter (%)")
    plt.xlabel("number of running the simulation")
    plt.show()

if __name__ == "__main__":
    simulation_game(100)