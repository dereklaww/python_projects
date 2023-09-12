
# # spearman1, archer1, knight1, scout1 = [], [], [], []
# # spearman2, archer2, knight2, scout2 = [], [], [], []

# # class piece:
# #     def __init__(self, army, type, coord, sym, power):
# #         self.type = type
# #         self.army = army
# #         self.coord = coord
# #         self.sym = sym
# #         self.power = power

# # s1 = piece("base_1", "Spearman", spearman1, "S1", 4)
# # s2 = piece("base_2", "Spearman", spearman2, "S2", 4)
# # k1 = piece("base_1", "Knight", knight1, "K1", 3)
# # k2 = piece("base_2", "Knight", knight2, "K2", 3)
# # a1 = piece("base_1", "Archer", archer1, "A1", 2)
# # a2 = piece("base_2", "Archer", archer2, "A2", 2)
# # t1 = piece("base_1", "Scout", scout1, "T1", 1)
# # t2 = piece("base_2", "Scout", scout2, "T2", 1)

# # pieces = [s1, s2, k1, k2, a1, a2, t1, t2]

# # curr_army = []

# # for elem in pieces:
# #     if elem.army == "base_1":
# #         curr_army.append(elem)

# # for elem in curr_army:
# #     if elem.type == "Spearman":
# #         print(elem.sym)

# initial_resources = ["WW"] * \
#     2 + ["FF"] * 2 + ["GG"] * 2
# player_1 = initial_resources

# curr_player = "1"
# curr_ls = player_1


# w = curr_ls.count("WW")
# f = curr_ls.count("FF")
# g = curr_ls.count("GG")


# def get_piece(input, ls):

#     if input == "S":
#         if (w or f) < 1:
#             print("Insufficient resources. Try again.")
#             print("")
#             return False
#         else:
#             ls.remove("WW")
#             ls.remove("FF")
#             return True

#     elif input == "A":
#         if (w or g) < 1:
#             print("Insufficient resources. Try again.")
#             print("")
#             return False
#         else:
#             ls.remove("WW")
#             ls.remove("GG")
#             return True
#     elif input == "K":
#         if (f or g) < 1:
#             print("Insufficient resources. Try again.")
#             print("")
#             return False
#         else:
#             ls.remove("FF")
#             ls.remove("GG")
#             return True
#     elif input == "K":
#         if (f or g) < 1:
#             print("Insufficient resources. Try again.")
#             print("")
#             return False
#         else:
#             ls.remove("WW")
#             ls.remove("FF")
#             ls.remove("GG")
#             return True




# get_piece("S", curr_ls)
# w = curr_ls.count("WW")
# f = curr_ls.count("FF")
# g = curr_ls.count("GG")

# print(w, f, g)


# while True:
#     print("You want to recruit a {}.".format("ps") +
#             " Enter two integers as format ‘x y’ to place your army.")
#     recruit_piece_coord = input()
#     if recruit_piece_coord in ["QUIT", "DIS", "PRIS"]:
#         pass
#     else:
#         recruit_piece_coord.split()
#         break
    
# print(recruit_piece_coord)

# price = ("""
# Recruiting Prices:
#   Spearman (S) - 1W, 1F
#   Archer (A) - 1W, 1G;
#   Knight (K) - 1F, 1G;
#   Scout (T) - 1W, 1F, 1G;
# """)

# print(price)

# a = ["a", "a", "b", "c"]

# curr_ls = a
# count = curr_ls.count("a")

# curr_ls.remove("a")
# print(curr_ls)
# print(count)

# a = 0
# b = 0
# if (a or b) < 1:
#     print(True)

# x = [elem[0] for elem in my_dict.get(key, [])]
#         y = [elem[1] for elem in my_dict.get(key, [])]
#         for i in x:
#             if i > width:
#                 raise ArithmeticError(
#                     "Invalid Configuration File: <{}> contains a position that is out of map".format(key))
#         for j in y:
#             if j > height:
#                 raise ArithmeticError(
#                     "Invalid Configuration File: <{}> contains a position that is out of map".format(key))


# check if final coord in grid
    # def valid_move(self, piece, curr_army, x0, y0, x1, y1):    
    #     if x1 < 0 or x1 > width - 1 or y1 < 0 or y1 > height - 1:
    #         return False

    #     # check if final coord is a valid move
    #     if piece.piece_type_full == "Scout":
    #         valid_postion = [
    #             (x0+1, y0), (x0-1, y0), (x0+2, y0), (x0-2, y0), (x0, y0+1), (x0, y0-1), (x0, y0+2), (x0, y0-2)]
    #     else:
    #         valid_postion = [
    #             (x0+1, y0), (x0-1, y0), (x0, y0+1), (x0, y0-1)]

    #     if (x1, y1) not in valid_postion:
    #         print("Invalid move. Try again")
    #         return False

    #     # check if final coord conflicts with home base
    #     if (x1, y1) == self_base:
    #         print("Invalid move. Try again")
    #         return False

    #     # check if final coord conficts with self pieces
    #     ls = []
    #     for elem in curr_army:
    #         if elem.coord != []:
    #             ls += elem.coord
    #     if (x1, y1) in ls:
    #         print("Invalid move. Try again.")
    #         return False

# (x, y) = (3, 3)
# print(x)

# price = (
# """Recruiting Prices:
#   Spearman (S) - 1W, 1F
#   Archer (A) - 1W, 1G;
#   Knight (K) - 1F, 1G;
#   Scout (T) - 1W, 1F, 1G;
# """)

# print(price)
# config_file = "notestfile.txt"
#   try:  
#     load_config_file(folder_path + config_file) 
#     assert True, "test 1 failed"
#   except:
#     FileNotFoundError
# import re

# line = "Wood: 0 0 2 1 3 1 4 1"
# ln = re.split("[:, ]+", str(line))
# ln = list(filter(None, ln))
# print(ln)

# ls_1 = [(0, 0), (2, 1), (3, 1), (4, 1), (0, 4), (4, 2), (0, 3), (1, 3), (1, 4)]
# ls_2 = [(1, 1), (3, 3), (0, 1), (1, 0), (2, 1), (1, 2), (2, 3), (3, 2), (4, 3), (3, 4)]

# for elem in ls_1:
#     if elem in ls_2:
#         print("pass")

# price = (
# """Recruit Prices:
#   Spearman (S) - 1W, 1F
#   Archer (A) - 1W, 1G
#   Knight (K) - 1F, 1G
#   Scout (T) - 1W, 1F, 1G""")

# print(price)
# import re

# string = "Frame: 5x5"


# # x = re.compile("\\\d{1}\s\d{1}\\")
# # if x.match(string):
# #     print(True)

# print(re.match("^Frame:\s[0-9]x[0-9]$", string))

# mydict = {}
# mydict["a"] = ("b", "c")
# print (mydict["a"][0])

num = 2
num =+ 2
print (num)