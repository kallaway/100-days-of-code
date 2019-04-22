#Day 5 - Towers of Hanoi Problem - Binary Code and Efficiency
#
#Great explanation for this courtesy of Youtube user 3Blue1Brown:
#[https://www.youtube.com/watch?v=2SUvWfNJSsM]
#
#In the Towers of Hanoi problem, the priests in the temple are given 64 golden
#disks with holes in the middle of them and 3 towers (poles which the golden disks
#slide onto. They must move all of the disks, in the most efficient way possible, to
#another tower, but they must not put a larger disk on top of a smaller one. (The disks
#are distributed, and must always stay, in descending order.) When they finish moving the
#disks, as the story goes, the end of the world is upon us. When solved, the minimum
#amount of moves will always be two to the power of the amount of disks, minus one. This
#means that in binary, the most efficient amount of moves will always be represented 
#with all ones, and the same amount of ones as disks that we start with. (See below.)
#Of course, to move one disk we only need one move (1 or 1 in binary), to move two disks we
#need three moves (3 or 11 in binary), and the numbers increase exponentially after that.
#
# 
#    |Moves|                 |Binary|   |Disks to Move|
#       1              =         1    <----1 disk
#       2              =        10    
#       3              =        11    <----2 disks
#       4              =       100
#       5              =       101
#       6              =       110
#       7              =       111    <----3 disks
#       8              =      1000
#       9              =      1001
#      10              =      1010
#      11              =      1011
#      12              =      1100
#      13              =      1101
#      14              =      1110
#      15              =      1111    <----4 disks
#                              etc.
loop = 1
while loop == 1:
    disk_number = input("Please enter a number of disks, then press enter. ")
    moves_required = pow(2,(int(disk_number)))-1
    print("Moves required: " + str(moves_required))
    req_in_binary = bin(moves_required)
    print("In base 2: " + str(req_in_binary))
