import numpy as np
import time
dict_utilties = {}
dict_start = {}
dict_directions = {
     0: 0,
     1: 2,
     2: 3,
     3: 1
}
    #NSEW:NWSE
dict_uti = {

}
t1 = time.time()



def maxim(list):
     maxv = np.float64(list[0])
     loc = 0
     for i in range(1, 4, 1):
         if list[i] > maxv:
             maxv = np.float64(list[i])
             loc = i
     return maxv, loc
def policy(matrix, size_Grid,row,col):
    current_Utility = [[0 for i in range(size_Grid)] for j in range(size_Grid)]
    previous_Utility = [[0 for i in range(size_Grid)] for j in range(size_Grid)]
    for i in range(size_Grid):
        for j in range(size_Grid):
            current_Utility[i][j] = matrix[i][j]
            previous_Utility[i][j] = matrix[i][j]
    utility_Actions = [[0 for i in range(size_Grid)] for j in range(size_Grid)]
    Flag = True
    gamma = np.float64(0.9)
    wrongProbability = np.float64(0.1)
    default_value = np.float64(wrongProbability) * np.float64((1 - gamma) / gamma)
    count = 1
    rightProbability = np.float64(0.7)
    while Flag != False:
        difference = [[np.float64(current_Utility[x][y])-np.float64(previous_Utility[x][y]) for x in range(size_Grid)]for y in range(size_Grid)]
        if max(max(difference)) < default_value and min(min(difference))*-1 < default_value and count != 1:
            Flag = False
        else:
            previous_Utility = np.float64(current_Utility)
            del(current_Utility)
            current_Utility = [[0 for i in range(size_Grid)] for j in range(size_Grid)]
            for i in range(size_Grid):
                for j in range(size_Grid):
                    temp = [0 for x in range(4)]
                    if i == row and j == col:
                        current_Utility[i][j] = matrix[i][j]
                        #print current_Utility[i][j]
                        utility_Actions[i][j] = 4
                        #print utility_Actions[i][j]
                    elif i == 0:
                        if j == 0:
                            #North
                            temp[0] = np.float64(rightProbability * previous_Utility[i][j]) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                        wrongProbability * previous_Utility[i][j + 1])) + (np.float64(wrongProbability * previous_Utility[i + 1][j]))
                            #South
                            temp[1] = np.float64(rightProbability * previous_Utility[i + 1][j]) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                        wrongProbability * previous_Utility[i][j])) + (np.float64(wrongProbability * previous_Utility[i][j + 1]))
                            # East
                            temp[2] = np.float64(rightProbability * previous_Utility[i][j + 1]) + (np.float64(wrongProbability * previous_Utility[i][j]))+(np.float64(
                                        wrongProbability * previous_Utility[i][j])) + (np.float64(wrongProbability * previous_Utility[i + 1][j]))
                            #West
                            temp[3] = np.float64(rightProbability * previous_Utility[i][j]) +(np.float64 (wrongProbability * previous_Utility[i][j])) +(np.float64 (
                                        wrongProbability * previous_Utility[i][j + 1])) +(np.float64 (wrongProbability * previous_Utility[i + 1][j]))
                            maxy, loc = maxim(temp)
                            current_Utility[i][j] = np.float64(matrix[i][j] + np.float64(gamma * maxy))
                            utility_Actions[i][j] = loc
                        elif j == size_Grid-1:
                            #North
                            temp[0] = np.float64(rightProbability * previous_Utility[i][j]) +(np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                        wrongProbability * previous_Utility[i][j - 1])) + (np.float64(wrongProbability * previous_Utility[i + 1][j]))
                            # South
                            temp[1] = np.float64(rightProbability * previous_Utility[i + 1][j]) + (np.float64(wrongProbability * previous_Utility[i][j])) +(np.float64(
                                        wrongProbability * previous_Utility[i][j])) +(np.float64(wrongProbability * previous_Utility[i][j - 1]))
                            # East
                            temp[2] = np.float64(rightProbability * previous_Utility[i][j]) +(np.float64(wrongProbability * previous_Utility[i][j])) +(np.float64(
                                        wrongProbability * previous_Utility[i][j - 1])) + (np.float64(wrongProbability * previous_Utility[i + 1][j]))
                            #West
                            temp[3] = np.float64(rightProbability * previous_Utility[i][j - 1]) +(np.float64(
                                        wrongProbability * previous_Utility[i + 1][j])) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                                  wrongProbability * previous_Utility[i][j]))
                            maxy, loc = maxim(temp)
                            current_Utility[i][j] = np.float64(matrix[i][j] + np.float64(gamma * maxy))
                            utility_Actions[i][j] = loc
                        else:
                            #North
                            temp[0] = np.float64(rightProbability * previous_Utility[i][j]) + (np.float64(wrongProbability * previous_Utility[i][j + 1])) + (np.float64(
                                        wrongProbability * previous_Utility[i + 1][j])) + (np.float64(wrongProbability * previous_Utility[i][j - 1]))
                            # South
                            temp[1] = np.float64(rightProbability * previous_Utility[i + 1][j]) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                        wrongProbability * previous_Utility[i][j - 1])) + (np.float64(wrongProbability * previous_Utility[i][j + 1]))
                            # East
                            temp[2] = np.float64(rightProbability * previous_Utility[i][j + 1]) + (np.float64(wrongProbability * previous_Utility[i][j])) +(np.float64(
                                        wrongProbability * previous_Utility[i][j - 1])) + (np.float64(wrongProbability * previous_Utility[i + 1][j]))
                            #West
                            temp[3] = np.float64(rightProbability * previous_Utility[i][j - 1]) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                        wrongProbability * previous_Utility[i + 1][j])) + (np.float64(wrongProbability * previous_Utility[i][j + 1]))
                            maxy, loc = maxim(temp)
                            current_Utility[i][j] = np.float64(matrix[i][j] + np.float64(gamma * maxy))
                            utility_Actions[i][j] = loc
                    elif i == size_Grid-1:
                        if j == 0:
                            #North
                            temp[0] = np.float64(rightProbability * previous_Utility[i - 1][j]) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                        wrongProbability * previous_Utility[i][j])) + (np.float64(wrongProbability * previous_Utility[i][j + 1]))
                            # South
                            temp[1] = np.float64(rightProbability * previous_Utility[i][j]) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                        wrongProbability * previous_Utility[i][j + 1])) + (np.float64(wrongProbability * previous_Utility[i - 1][j]))
                            # East
                            temp[2] = np.float64(rightProbability * previous_Utility[i][j + 1]) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                        wrongProbability * previous_Utility[i][j])) + (np.float64(wrongProbability * previous_Utility[i - 1][j]))
                            #West
                            temp[3] = np.float64(rightProbability * previous_Utility[i][j]) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                        wrongProbability * previous_Utility[i][j + 1])) + (np.float64(wrongProbability * previous_Utility[i - 1][j]))
                            maxy, loc = maxim(temp)
                            current_Utility[i][j] = np.float64(matrix[i][j] + np.float64(gamma * maxy))
                            utility_Actions[i][j] = loc
                        elif j == size_Grid-1:
                            #North
                             temp[0] = np.float64(rightProbability * previous_Utility[i - 1][j]) + (np.float64(
                                         wrongProbability * previous_Utility[i][j])) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                                   wrongProbability * previous_Utility[i][j - 1]))
                            # South
                             temp[1] = np.float64(rightProbability * previous_Utility[i][j]) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                         wrongProbability * previous_Utility[i][j - 1])) + (np.float64(wrongProbability * previous_Utility[i - 1][j]))
                            # East
                             temp[2] = np.float64(rightProbability * previous_Utility[i][j]) + (np.float64(wrongProbability * previous_Utility[i][j]) + (np.float64(
                                         wrongProbability * previous_Utility[i][j - 1]))) + (np.float64(wrongProbability * previous_Utility[i - 1][j]))
                            #West
                             temp[3] = np.float64(rightProbability * previous_Utility[i][j - 1]) + (np.float64(
                                         wrongProbability * previous_Utility[i][j])) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                                   wrongProbability * previous_Utility[i - 1][j]))

                             maxy, loc = maxim(temp)
                             current_Utility[i][j] = np.float64(matrix[i][j] + np.float64(gamma * maxy))
                             utility_Actions[i][j] = loc
                        else:
                            #North
                             temp[0] = np.float64(rightProbability * previous_Utility[i - 1][j]) + (
                                         wrongProbability * previous_Utility[i][j]) + (wrongProbability * previous_Utility[i][j + 1]) + (
                                                   wrongProbability * previous_Utility[i][j - 1])
                            # South
                             temp[1] = np.float64(rightProbability * previous_Utility[i][j]) +( np.float64(
                                         wrongProbability * previous_Utility[i][j - 1])) + (np.float64(wrongProbability * previous_Utility[i - 1][j])) + (np.float64(
                                                   wrongProbability * previous_Utility[i][j + 1]))
                            # East
                             temp[2] = np.float64(rightProbability * previous_Utility[i][j + 1]) + (np.float64(
                                         wrongProbability * previous_Utility[i][j])) + (np.float64(wrongProbability * previous_Utility[i][j - 1])) + (np.float64(
                                                   wrongProbability * previous_Utility[i - 1][j]))
                            #West
                             temp[3] = np.float64(rightProbability * previous_Utility[i][j - 1]) + (np.float64(
                                         wrongProbability * previous_Utility[i][j])) + (np.float64(wrongProbability * previous_Utility[i - 1][j])) + (np.float64(
                                                   wrongProbability * previous_Utility[i][j + 1]))

                             maxy, loc = maxim(temp)
                             current_Utility[i][j] = np.float64(matrix[i][j] + np.float64(gamma * maxy))
                             utility_Actions[i][j] = loc
                    elif j == 0:
                        if i > 0 and i < size_Grid-1:
                            #North
                            temp[0] = np.float64(rightProbability * previous_Utility[i - 1][j]) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                        wrongProbability * previous_Utility[i][j + 1])) + (np.float64(wrongProbability * previous_Utility[i + 1][j]))
                            # South
                            temp[1] = np.float64(rightProbability * previous_Utility[i + 1][j]) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                        wrongProbability * previous_Utility[i][j + 1])) +(np.float64(wrongProbability * previous_Utility[i - 1][j]))
                            # East
                            temp[2] = np.float64(rightProbability * previous_Utility[i][j + 1]) + (np.float64(wrongProbability * previous_Utility[i][j])) + (np.float64(
                                        wrongProbability * previous_Utility[i + 1][j])) + (np.float64(wrongProbability * previous_Utility[i - 1][j]))
                            #West
                            temp[3] = np.float64(rightProbability * previous_Utility[i][j]) + (np.float64(wrongProbability * previous_Utility[i][j + 1])) + (np.float64(
                                        wrongProbability * previous_Utility[i - 1][j])) + (np.float64(wrongProbability * previous_Utility[i + 1][j]))
                            maxy, loc = maxim(temp)
                            current_Utility[i][j] = np.float64(matrix[i][j] + np.float64(gamma * maxy))
                            utility_Actions[i][j] = loc
                    elif j == size_Grid-1:
                        if i > 0 and i < size_Grid-1:
                            #North
                              temp[0] = np.float64(rightProbability * previous_Utility[i - 1][j]) + (np.float64(
                                          wrongProbability * previous_Utility[i][j])) + (np.float64(wrongProbability * previous_Utility[i][j - 1])) + (np.float64(
                                                    wrongProbability * previous_Utility[i + 1][j]))
                            # South
                              temp[1] = np.float64(rightProbability * previous_Utility[i + 1][j]) + (np.float64(
                                          wrongProbability * previous_Utility[i][j])) + (np.float64(wrongProbability * previous_Utility[i - 1][j])) + (np.float64(
                                                    wrongProbability * previous_Utility[i][j - 1]))
                            # East
                              temp[2] = np.float64(rightProbability * previous_Utility[i][j]) + (np.float64(
                                          wrongProbability * previous_Utility[i - 1][j])) + (np.float64(wrongProbability * previous_Utility[i][j - 1])) + (np.float64(
                                                    wrongProbability * previous_Utility[i + 1][j]))
                            #West
                              temp[3] = np.float64(rightProbability * previous_Utility[i][j - 1]) + (np.float64(
                                          wrongProbability * previous_Utility[i][j])) + (np.float64(wrongProbability * previous_Utility[i + 1][j])) + (np.float64(
                                                    wrongProbability * previous_Utility[i - 1][j]))
                              maxy, loc = maxim(temp)
                              current_Utility[i][j] = np.float64(matrix[i][j] + np.float64(gamma * maxy))
                              utility_Actions[i][j] = loc
                    else:
                        #North
                         temp[0] = np.float64(rightProbability * previous_Utility[i - 1][j]) +(np.float64(
                                     wrongProbability * previous_Utility[i][j - 1])) + (np.float64(wrongProbability * previous_Utility[i + 1][j])) + (np.float64(
                                               wrongProbability * previous_Utility[i][j + 1]))
                        # South
                         temp[1] = np.float64(rightProbability * previous_Utility[i + 1][j]) + (np.float64(
                                     wrongProbability * previous_Utility[i - 1][j])) + (np.float64(wrongProbability * previous_Utility[i][j - 1])) + (np.float64(
                                               wrongProbability * previous_Utility[i][j + 1]))
                        # East
                         temp[2] = np.float64(rightProbability * previous_Utility[i][j + 1]) + (np.float64(
                                     wrongProbability * previous_Utility[i - 1][j])) + (np.float64(wrongProbability * previous_Utility[i][j - 1])) + (np.float64(
                                               wrongProbability * previous_Utility[i + 1][j]))
                        #West
                         temp[3] = np.float64(rightProbability * previous_Utility[i][j - 1]) + (np.float64(
                                     wrongProbability * previous_Utility[i - 1][j])) + (np.float64(wrongProbability * previous_Utility[i + 1][j])) + (np.float64(
                                               wrongProbability * previous_Utility[i][j + 1]))
                         maxy, loc = maxim(temp)
                         current_Utility[i][j] = np.float64(matrix[i][j] + np.float64(gamma * maxy))
                         utility_Actions[i][j] = loc
            dict_uti[count] = utility_Actions
            count += 1
    return dict_uti[count-2]

def move_Action(move,start_row, start_col, size_Grid):
    if move == 0:
        if start_row > 0:
            start_row -= 1
    elif move == 1:
        if start_col > 0:
            start_col -= 1
    elif move == 2:
        if start_row < size_Grid-1:
            start_row += 1
    elif move == 3:
        if start_col < size_Grid - 1:
            start_col += 1
    return start_row, start_col
def simulate(start_row, start_col, terminal_row, terminal_col, matrix, utility_Actions, swerve, size_Grid):
    k = 0
    reward = 0
    index_terminal = (size_Grid * terminal_row) + terminal_col
    index_start = (size_Grid * start_row) + start_col
    while index_start != index_terminal:
        if swerve[k] <= 0.7:
            move = dict_directions[utility_Actions[start_row][start_col]]
            start_row , start_col = move_Action(move,start_row, start_col,size_Grid)
        elif swerve[k] <= 0.8:
            move = ((dict_directions[utility_Actions[start_row][start_col]]) + 1) % 4
            start_row, start_col = move_Action(move, start_row, start_col, size_Grid)
        elif swerve[k] <= 0.9:
            move = ((dict_directions[utility_Actions[start_row][start_col]]) + 3) % 4
            start_row, start_col = move_Action(move, start_row, start_col, size_Grid)
        else:
            move = ((dict_directions[utility_Actions[start_row][start_col]]) + 2) % 4
            start_row, start_col = move_Action(move, start_row, start_col, size_Grid)
        reward += matrix[start_row][start_col]
        index_start = (size_Grid * start_row) + start_col
        k += 1
    #print reward
    return reward




f = open("input.txt", "r")
f1 = open("output.txt", "w")
size_Grid = int(f.readline())
number_Cars = int(f.readline())
number_Obstacles = int(f.readline())
start_Location = []
terminal_Location = []
obstacle_Location = []

for obstacles in range(number_Obstacles):
    obstacles = f.readline()
    obstacle_Location.append(obstacles)

for cars in range(number_Cars):
    cars = f.readline()
    start_Location.append(cars)

for cars in range(number_Cars):
    cars = f.readline()
    terminal_Location.append(cars)
    #print terminal_Location
matrix = [[np.float64(-1) for i in range(size_Grid)]for j in range(size_Grid)]

for i in range(len(obstacle_Location)):
    x = obstacle_Location[i].split(',')
    obstacle_col = int(x[0])
    obstacle_row = int(x[1])
    matrix[obstacle_row][obstacle_col] -= 100
matrix_Policy =[[0 for i in range(size_Grid)]for j in range(size_Grid)]


swerve = [[0 for i in range(1000000)] for j in range(10)]
for j in range(10):
    np.random.seed(j)
    swerve[j] = np.random.random_sample(1000000)

i = 0
while i < number_Cars:
    x = start_Location[i].split(',')
    y = terminal_Location[i].split(',')
    i += 1
    start_col = int(x[0])
    start_row = int(x[1])
    terminal_col = int(y[0])
    terminal_row = int(y[1])
    index = terminal_row * size_Grid + terminal_col
    index1 = start_row * size_Grid + start_col
    reward_Initial = 0

    if start_row == terminal_row and start_col == terminal_col:
        Reward_Final = str(100)
        f1.write(Reward_Final)
        f1.write("\n")
    else:
        matrix[terminal_row][terminal_col] += np.float64(100)
        if index in dict_utilties:
            if index1 in dict_start:
                Reward_Final = dict_start[index1]
            else:
                for j in range(10):
                    reward_Initial += simulate(start_row, start_col, terminal_row, terminal_col, matrix, dict_utilties[index],
                                               swerve[j], size_Grid)
                Reward_Final = int(reward_Initial / 10)
        else:
            utility_Actions = policy(np.float64(matrix), size_Grid, terminal_row, terminal_col)
            dict_utilties[index] = utility_Actions
            for j in range(10):
                reward_Initial += simulate(start_row, start_col, terminal_row, terminal_col, matrix, utility_Actions,swerve[j], size_Grid)
            #print reward_Initial
            Reward_Final = int(reward_Initial / 10)
        dict_start[index1] = Reward_Final
        matrix[terminal_row][terminal_col] = np.float64(-1)
        #f1.write("\n")
        #f1.write("Final Answer")
        if number_Cars == 1:
            f1.write(str(Reward_Final))
        else:
            f1.write(str(Reward_Final))
            f1.write("\n")
f.close()
f1.close()
t2 = time.time()
print t2-t1
