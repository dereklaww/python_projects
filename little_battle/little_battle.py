import sys
import re
from types import WrapperDescriptorType
# Please implement this function according to Section "Read Configuration File"


def load_config_file(filepath):
    # It should return width, height, waters, woods, foods, golds based on the file
    # Complete the test driver of this function in file_loading_test.py
    with open("{}".format(filepath), "r") as f:

        # dictionary - store position tuples (water, wood, food, gold)
        my_dict = {}

        # labels of objects from the config file
        key_format = ["Frame: ", "Water: ", "Wood: ", "Food: ", "Gold: "]

        lines = f.readlines()
        i = 0
        # check if config file follows the correct label format
        for line in lines:
            if line.startswith(key_format[i]):
                i += 1
            else:
                raise SyntaxError("Invalid Configuration File: format error!")

        # if the format of the config file is correct, re-read the file from the start
        f.seek(0)

        # line[0] = frame dimension (height and width)
        frame_dimen = f.readline().strip()

        # check if the "frame" line is in the correct format
        if re.match("^Frame:\s[0-9]x[0-9]$", frame_dimen) is None:
            raise SyntaxError(
                "Invalid Configuration File: frame should be in format widthxheight!")

        else:
            frame_ln = re.split("[:x, ]+", frame_dimen)
            width, height = int(frame_ln[1]), int(frame_ln[2])

            if height not in range(5, 8) or width not in range(5, 8):
                raise ArithmeticError(
                    "Invalid Configuration File: width and height should range from 5 to 7!")

        # line[1:] = position of objects
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            # to store key-values pair of each object
            items = []
            ln = re.split("[:, ]+", str(line))
            ln = list(filter(None, ln))

            # ln is in format ["label", x0, y0, x1, y1 ...], 
            # if len(ln) is odd, one of the coordinate is invalid
            if len(ln) > 1 and len(ln) % 2 == 0:
                raise SyntaxError(
                    "Invalid Configuration File: {} has an odd number of elements!".format(ln[0]))

            items.append(ln[0])

            # check if tuple is comprised with integer elements and the position is within the map
            if len(ln) > 1:
                for i in range(1, len(ln), 2):
                    if ln[i].isdigit() and ln[i+1].isdigit():
                        if int(ln[i]) not in range(0, width) or int(ln[i+1]) not in range(0, height):
                            raise ArithmeticError(
                                "Invalid Configuration File: " + \
                                    "{} contains a position that is out of map.".format(ln[0]))

                        else:
                            items.append(tuple([int(ln[i]), int(ln[i+1])]))
                            # item = ["key", tuple1, tuple2...]
                            key = items[0]
                            values = items[1:]
                            my_dict[key] = values
                    else:
                        raise ValueError(
                            "Invalid Configuration File: " + \
                                "{} contains non integer characters!".format(ln[0]))

            else:
                key = items[0]
                values = []
                my_dict[key] = values

        f.close()

    # list - position coordinates
    waters, woods, foods, golds = my_dict["Water"], my_dict["Wood"], my_dict["Food"], my_dict["Gold"]
    hb1, hb2 = [(1, 1)], [(width - 2, height - 2)]
    armybase_1 = [(0, 1), (1, 0), (2, 1), (1, 2)]
    armybase_2 = [(width-3, height-2), (width-2, height-3),
                  (width-1, height-2), (width-2, height-1)]

    # check if the coordinates of objects conflicts with the position of home bases 
    # or positions next to the home bases.
    ls = []
    for key in my_dict.keys():
        for elem in my_dict.get(key, []):
            ls.append(elem)

    for elem in ls:
        if elem in hb1 + hb2 + armybase_1 + armybase_2:
            raise ValueError(
                "Invalid Configuration File: " + \
                    "The positions of home bases or the positions next to the home bases are occupied!")

    # check if there are duplicates of coordinates
    for elem in ls:
        if ls.count(elem) > 1:
            raise SyntaxError(
                "Invalid Configuration File: Duplicate position {}!".format(elem))
    return (width, height, waters, woods, foods, golds, hb1, hb2, armybase_1, armybase_2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 little_battle.py <filepath>")
        sys.exit()

    try:
        width, height, waters, woods, foods, golds, hb1, hb2, armybase_1, armybase_2 = load_config_file(
            sys.argv[1])
    except FileNotFoundError:
        print("FileNotFoundError : File {} not found.".format(sys.argv[1]))
        sys.exit()

    # list - position tuples for army
    spearman1, archer1, knight1, scout1 = [], [], [], []
    spearman2, archer2, knight2, scout2 = [], [], [], []

    # dictionary - piece symbols and coordinates
    # to be used in map
    piece_coord = {
        "~~": waters,
        "WW": woods,
        "FF": foods,
        "GG": golds,
        "H1": hb1,
        "H2": hb2,
        "S1": spearman1,
        "A1": archer1,
        "K1": knight1,
        "T1": scout1,
        "S2": spearman2,
        "A2": archer2,
        "K2": knight2,
        "T2": scout2,
    }

    # list - each player's resources
    player_1 = ["WW"] * 2 + ["FF"] * 2 + ["GG"] * 2
    player_2 = ["WW"] * 2 + ["FF"] * 2 + ["GG"] * 2

    # dictionary - resources and their symbols on the map
    resource_dict = {
        "WW": "Wood",
        "FF": "Food",
        "GG": "Gold"
    }

    # army piece class
    # to be used in recruiting and moving army pieces
    class piece:
        def __init__(self, army, piece_type_full, piece_type_alpha, coord, sym, power):
            self.army = army
            self.piece_type_full = piece_type_full
            self.piece_type_alpha = piece_type_alpha
            self.coord = coord
            self.sym = sym
            self.power = power

    s1 = piece("base_1", "Spearman", "S", spearman1, "S1", 4)
    s2 = piece("base_2", "Spearman", "S", spearman2, "S2", 4)
    a1 = piece("base_1", "Archer", "A", archer1, "A1", 2)
    a2 = piece("base_2", "Archer", "A", archer2, "A2", 2)
    k1 = piece("base_1", "Knight", "K", knight1, "K1", 3)
    k2 = piece("base_2", "Knight", "K", knight2, "K2", 3)
    t1 = piece("base_1", "Scout", "T", scout1, "T1", 1)
    t2 = piece("base_2", "Scout", "T", scout2, "T2", 1)

    pieces = [s1, s2, a1, a2, k1, k2, t1, t2]

    # splitting the army pieces into two lists (player 1 and player 2)
    curr_army_1 = []
    curr_army_2 = []
    for elem in pieces:
        if elem.army == "base_1":
            curr_army_1.append(elem)
        elif elem.army == "base_2":
            curr_army_2.append(elem)

    # price list
    price = (
        """Recruit Prices:
  Spearman (S) - 1W, 1F
  Archer (A) - 1W, 1G
  Knight (K) - 1F, 1G
  Scout (T) - 1W, 1F, 1G""")

    # function - check if a coordinate is occupied by a piece

    def in_coord(tuple):
        for key in piece_coord.keys():
            if tuple in piece_coord[key]:
                return key
        return "  "

    # basic functions of the game - map, moving, check win condition

    class battlefield:

        # map printing
        # 2-D lists which contains the data of each cell
        def __init__(self):
            self.grid = []
            for i in range(height):
                self.grid.append(["  "] * width)
            for i, row in enumerate(self.grid):
                for x, cell in enumerate(row):
                    self.grid[i][x] = in_coord((x, i))

        # updates the data of each cell
        def state_update(self):
            for i, row in enumerate(self.grid):
                for x, cell in enumerate(row):
                    self.grid[i][x] = in_coord((x, i))

        def curr_state(self):
            # Header:
            print("  X", end="")
            for i in range(width - 1):
                print("{:02d}".format(i), end=" ")
            print("{:02d}X".format(width - 1), end="")
            print("")  # New line

            # Upper axis: " Y+--------------+"
            print(" Y+", end="")
            for i in range(width - 1):
                print("---", end="")
            print("--+", end="")
            print("")  # New line

            # Rows and cells
            self.state_update()
            for i, row in enumerate(self.grid):
                print("{:02d}".format(i) + "|", end="")
                for x, cell in enumerate(row):
                    print("{}|".format(row[x]), end="")
                print("")

            # Lower axis: " Y+--------------+"
            print(" Y+", end="")
            for i in range(width - 1):
                print("---", end="")
            print("--+", end="")
            print("")  # New line

        # moving pieces
        # piece = items from the "piece" class
        # curr_ls = list of resources of player
        # curr_army = list of army pieces of player
        # (x0, y0) = intial position
        # (x1, y1) = final position

        def valid_move(self, piece, curr_army, x0, y0, x1, y1):
            if curr_army == curr_army_1:
                self_base_sym = "H1"
                self_base = piece_coord[self_base_sym]

            elif curr_army == curr_army_2:
                self_base_sym = "H2"
                self_base = piece_coord[self_base_sym]

            if x1 < 0 or x1 > width - 1 or y1 < 0 or y1 > height - 1:
                print("Invalid move. Try again.")
                return False

            # check if final coord is a valid move
            if piece.piece_type_full == "Scout":
                valid_postion = [
                    (x0+1, y0), (x0-1, y0), (x0+2, y0), (x0-2, y0),
                    (x0, y0+1), (x0, y0-1), (x0, y0+2), (x0, y0-2)
                    ]
            else:
                valid_postion = [
                    (x0+1, y0), (x0-1, y0),
                    (x0, y0+1), (x0, y0-1)
                    ]

            if (x1, y1) not in valid_postion:
                print("Invalid move. Try again.")
                return False

            # check if final coord conflicts with home base
            if (x1, y1) in self_base:
                print("Invalid move. Try again.")
                return False

            # check if final coord conficts with self pieces
            ls = []
            for elem in curr_army:
                if elem.coord != []:
                    ls += elem.coord
            if (x1, y1) in ls:
                print("Invalid move. Try again.")
                return False

            return True

        # function - move army piece
        def move(self, piece, curr_ls, curr_army, x0, y0, x1, y1):
            if curr_army == curr_army_1:
                enemy_army = curr_army_2
                enemy_base_sym = "H2"
                enemy_base = piece_coord[enemy_base_sym]

            elif curr_army == curr_army_2:
                enemy_army = curr_army_1
                enemy_base_sym = "H1"
                enemy_base = piece_coord[enemy_base_sym]

            print("")
            print("You have moved {} from ({}, {}) to ({}, {}).".format(
                piece.piece_type_full, x0, y0, x1, y1))
            # remove initial coord of the army piece
            piece.coord.remove((x0, y0))

            # "Scout" pieces affect the game even though the piece moves two steps.
            # (x_mid, y_mid) = position between the initial and final position of the "Scout" piece
            # if the piece moves two step

            if piece.piece_type_full == "Scout" and ((x1 in [(x0 + 2), (x0 - 2)]) or (y1 in [(y0 + 2), (y0 - 2)])):
                if x1 == x0 + 2:
                    x_mid = x0 + 1
                    y_mid = y0

                elif x1 == x0 - 2:
                    x_mid = x0 - 1
                    y_mid = y0

                elif y1 == y0 + 2:
                    x_mid = x0
                    y_mid = y0 + 1

                elif y1 == y0 - 2:
                    x_mid = x0
                    y_mid = y0 - 1

                p_mid = self.grid[y_mid][x_mid]

                # if the cell is occupied by an enermy piece
                for elem in enemy_army:
                    if elem.sym == p_mid:
                        enermy = elem
                        enermy_power = elem.power
                        enermy_type = elem.piece_type_full
                        player_power = piece.power

                        # enermy piece is removed from the game
                        if player_power > enermy_power:
                            print("Great! We defeated the enemy {}!".format(
                                enermy_type))
                            enermy.coord.remove((x_mid, y_mid))

                        # piece of both players are removed
                        elif player_power == enermy_power:
                            print("We destroyed the enemy {} with massive loss!".format(
                                enermy_type))
                            enermy.coord.remove((x_mid, y_mid))
                            return

                        # own piece is removed from the game
                        elif player_power < enermy_power:
                            print("We lost the army {} due to your command!".format(
                                piece.piece_type_full))
                            return

                # own piece is drowned
                if p_mid == "~~":
                    print("We lost the army {} due to your command!".format(
                        piece.piece_type_full))
                    return

                # player obtains resources from map
                # player's resources list is updated
                elif p_mid in ["FF", "WW", "GG"]:
                    piece_coord[p_mid].remove((x_mid, y_mid))
                    curr_ls.append(p_mid)
                    curr_ls.append(p_mid)
                    print("Good. We collected 2 {}.".format(
                        resource_dict[p_mid]))

                # "Scout" passes enemy home base - win
                elif p_mid == enemy_base_sym:
                    enemy_base.remove((x_mid, y_mid))
                    return

            # purpose of if-conditions from above applies below
            p = self.grid[y1][x1]
            for elem in enemy_army:
                if elem.sym == p:
                    enermy = elem
                    enermy_power = elem.power
                    enermy_type = elem.piece_type_full
                    player_power = piece.power

                    if piece.piece_type_full == "Spearman" and enermy_type == "Archer":
                        player_power = 0
                    elif piece.piece_type_full == "Archer" and enermy_type == "Spearman":
                        enermy_power = 0

                    if player_power > enermy_power:
                        print("Great! We defeated the enemy {}!".format(enermy_type))
                        enermy.coord.remove((x1, y1))
                        piece.coord.append((x1, y1))
                        return

                    elif player_power == enermy_power:
                        print("We destroyed the enemy {} with massive loss!".format(
                            enermy_type))
                        enermy.coord.remove((x1, y1))
                        return

                    elif player_power < enermy_power:
                        print("We lost the army {} due to your command!".format(
                            piece.piece_type_full))
                        return

            if p == "~~":
                print("We lost the army {} due to your command!".format(
                    piece.piece_type_full))
                return

            elif p in ["FF", "WW", "GG"]:
                piece_coord[p].remove((x1, y1))
                piece.coord.append((x1, y1))
                curr_ls.append(p)
                curr_ls.append(p)
                print("Good. We collected 2 {}.".format(resource_dict[p]))
                return

            # if cell is not occupied, army piece occupies the cell
            elif p == "  ":
                piece.coord.append((x1, y1))
                return

            # if final position is enemy base, army piece occupies the cell - win
            elif p == enemy_base_sym:
                enemy_base.remove((x1, y1))
                piece.coord.append((x1, y1))
                return

        # winning condition : enemy homebase is occupied by own army piece

        def check_finish(self, curr_player):
            if curr_player == "1":
                base = "H2"
                (x, y) = (width - 2, height - 2)
            elif curr_player == "2":
                base = "H1"
                (x, y) = (1, 1)

            if self.grid[y][x] == base:
                return False
            return True

    # game state and configuration inputs

    def check_input(user_input):
        if user_input == "QUIT":
            sys.exit()
        elif user_input == "DIS":
            print("Please check the battlefield, commander.")
            game.curr_state()
            return
        elif user_input == "PRIS":
            print(price)
            return

    # function - recruiting army pieces

    def get_piece(input, curr_ls):
        w = curr_ls.count("WW")
        f = curr_ls.count("FF")
        g = curr_ls.count("GG")

        # check sufficient resources
        # if sufficient, remove resources from list according to army type
        if input == "S":
            if w < 1 or f < 1:
                return False
            else:
                curr_ls.remove("WW")
                curr_ls.remove("FF")
                return True

        elif input == "A":
            if w < 1 or g < 1:
                return False
            else:
                curr_ls.remove("WW")
                curr_ls.remove("GG")
                return True

        elif input == "K":
            if f < 1 or g < 1:
                return False
            else:
                curr_ls.remove("FF")
                curr_ls.remove("GG")
                return True

        elif input == "T":
            if f < 1 or w < 1 or g < 1:
                return False
            else:
                curr_ls.remove("WW")
                curr_ls.remove("FF")
                curr_ls.remove("GG")
                return True

    curr_player = "1"
    curr_ls = player_1
    curr_army = curr_army_1
    year = 617
    game = battlefield()

    # Game execution starts here:
    print("Configuration file {} was loaded.".format(sys.argv[1]))
    print("Game Started: Little Battle! (enter QUIT to quit the game)")
    print("")

    # print map
    print("Please check the battlefield, commander.")
    game.curr_state()
    print("(enter DIS to display the map)")
    print("")

    # print price list
    print(price)
    print("(enter PRIS to display the price list)")
    print("")

    # Recruit phase
    while True:
        recruit_phase = True
        move_phase = False
        print("-Year {}-".format(year))
        print("")
        print("+++Player {}'s Stage: Recruit Armies+++".format(curr_player))
        print("")

        # print current resources
        while recruit_phase:
            w = curr_ls.count("WW")
            f = curr_ls.count("FF")
            g = curr_ls.count("GG")
            print("[Your Asset: Wood - {} Food - {} Gold - {}]".format(w, f, g))

            # check availability of resources to recruit army piece
            if (w < 1 or f < 1) and (w < 1 or g < 1) and (f < 1 or g < 1):
                print("No resources to recruit any armies.")
                recruit_phase = False
                move_phase = True
                break

            # check occupancy around homebase to recruit army piece
            if curr_player == "1":
                ls = []
                for elem in armybase_1:
                    (x, y) = elem
                    ls.append(game.grid[y][x])
                if "  " not in ls:
                    print("No place to recruit new armies.")
                    recruit_phase = False
                    move_phase = True
                    break

            elif curr_player == "2":
                ls = []
                for elem in armybase_2:
                    (x, y) = elem
                    ls.append(game.grid[y][x])
                if "  " not in ls:
                    print("No place to recruit new armies.")
                    recruit_phase = False
                    move_phase = True
                    break

            # recruit phase (specify which army piece to recruit)
            while recruit_phase:
                print("")
                print("Which type of army to recruit, (enter) ‘S’, ‘A’, ‘K’, or ‘T’?" + \
                      " Enter ‘NO’ to end this stage.")
                recruit_piece_type = input()

                if recruit_piece_type in ["QUIT", "DIS", "PRIS"]:
                    check_input(recruit_piece_type)

                # recruit piece using get_piece()
                # if successfull, break out from loop
                # find symbol and piece type using class objects
                elif recruit_piece_type in ["S", "A", "K", "T"]:
                    if get_piece(recruit_piece_type, curr_ls):
                        for elem in curr_army:
                            if elem.piece_type_alpha == recruit_piece_type:
                                sym = elem.sym
                                piece_type = elem.piece_type_full
                        break
                    else:
                        print("Insufficient resources. Try again.")
                        continue

                elif recruit_piece_type == "NO":
                    recruit_phase = False
                    move_phase = True
                    break
                else:
                    print("Sorry, invalid input. Try again.")

            # recruit phase (specify coordinates to place pieces)
            # ask and check input (function inputs or int inputs)
            # int inputs - check format of coordinates
            while recruit_phase:
                while True:
                    print("")
                    print("You want to recruit a {}.".format(piece_type) + \
                          " Enter two integers as format ‘x y’ to place your army.")
                    recruit_piece_coord = input()

                    if recruit_piece_coord in ["QUIT", "DIS", "PRIS"]:
                        check_input(recruit_piece_coord)
                        continue

                    elif re.match("^\d\s\d$", recruit_piece_coord) is not None:
                        recruit_piece_coord = recruit_piece_coord.split()
                        break

                    print("Sorry, invalid input. Try again.")

                if len(recruit_piece_coord) != 2:
                    print("Sorry, invalid input. Try again.")
                    continue

                # check validity of coordinates (around homebase and unoccupied)
                else:
                    try:
                        x, y = int(recruit_piece_coord[0]), int(
                            recruit_piece_coord[1])
                    except:
                        ValueError
                        print("Sorry, invalid input. Try again.")
                        continue

                    if curr_player == "1":
                        if (x, y) not in armybase_1:
                            print(
                                "You must place your newly recruited unit in an unoccupied position " + \
                                    "next to your home base. Try again.")
                            continue

                    elif curr_player == "2":
                        if (x, y) not in armybase_2:
                            print(
                                "You must place your newly recruited unit in an unoccupied position " + \
                                    "next to your home base. Try again.")
                            continue

                    if game.grid[y][x] != "  ":
                        print(
                            "You must place your newly recruited unit in an unoccupied position " + \
                                "next to your home base. Try again.")
                        continue

                    # successfully recruited army piece
                    game.grid[y][x] = sym
                    piece_coord[sym].append((x, y))
                    print("")
                    print("You has recruited a {}.".format(piece_type))
                    print("")
                    # update game state - changes in game data
                    game.state_update()
                    break

        # move phase starts
        if move_phase:
            print("")
            print("===Player {}'s Stage: Move Armies===".format(curr_player))

            # dictionary - store data of army pieces to move in the format :
            # (<piece type> : ((piece(class object), piece coordinates))
            armies_tomove = {}
            for elem in curr_army:
                coord_ls = []
                if elem.coord != []:
                    for coord in elem.coord:
                        coord_ls.append(coord)
                        armies_tomove[elem.piece_type_full] = (elem, coord_ls)

            # check available army pieces to move
            # note : elem = piece type in full name
            while move_phase:
                ls = []
                for elem in armies_tomove.keys():
                    ls += armies_tomove[elem][1]

                # if there are no more pieces to move, turn ends
                if ls == []:
                    print("")
                    print("No Army to Move: next turn.")
                    print("")
                    move_phase = False
                    break

                valid_move = False
                while not valid_move:
                    # print list of armies to move
                    # note : elem = piece type in full name
                    print("")
                    print("Armies to Move:")
                    for elem in armies_tomove.keys():
                        if armies_tomove[elem][1] != []:
                            print("  {}: {}".format(elem, ", ".join(
                                map(str, (armies_tomove[elem][1])))))
                    print("")

                    # ask user input initial and final coordinates
                    print(
                        "Enter four integers as a format ‘x0 y0 x1 y1’ to represent move unit" + \
                          " from (x0, y0) to (x1, y1) or ‘NO’ to end this turn.")
                    final_coords = input()

                    if final_coords in ["QUIT", "DIS", "PRIS"]:
                        check_input(final_coords)
                        continue
                    elif final_coords == "NO":
                        print("")
                        move_phase = False
                        break

                    # check validity of input
                    if re.match("^\d\s\d\s\d\s\d$", final_coords) is not None:
                        final_coords = final_coords.split()

                    else:
                        print("Invalid move. Try again.")
                        continue

                    # check if input contains non-integer characters
                    # initialize input as coordinates
                    try:
                        x0, y0, x1, y1 = int(final_coords[0]), int(
                            final_coords[1]), int(final_coords[2]), int(final_coords[3])
                    except:
                        ValueError
                        print("Invalid move. Try again.")
                        continue

                    # check if initial coordinates matches position of armies to move
                    ls = []
                    for elem in armies_tomove.keys():
                        ls += armies_tomove[elem][1]
                    if (x0, y0) not in ls:
                        print("Invalid move. Try again.")
                        continue
                    valid_move = True

                    while valid_move:
                        # find army piece which position matches initial position
                        for i in armies_tomove.keys():
                            elem = armies_tomove[i][0]
                            ls = armies_tomove[i][1]
                            for coord in ls:
                                if coord == (x0, y0):
                                    # check validity of move
                                    if game.valid_move(elem, curr_army, x0, y0, x1, y1):
                                        game.move(elem, curr_ls,
                                                  curr_army, x0, y0, x1, y1)
                                        # remove piece from army-to-move
                                        ls.remove(coord)
                                        # update game state - changes in game data
                                        game.state_update()
                                        # check win condition
                                        if game.check_finish(curr_player):
                                            print(
                                                "The army {} captured the enemy’s capital."
                                                .format(elem.piece_type_full))
                                            print("")
                                            print(
                                                "What’s your name, commander?")
                                            name = input()
                                            print("")
                                            print(
                                                "***Congratulation! Emperor {} unified the country in {}.***"
                                                .format(name, year))
                                            sys.exit()
                                    else:
                                        valid_move = False
                        # done moving army piece, next piece
                        break

        # turn complete, update player data
        if curr_player == "1":
            curr_player = "2"
            curr_ls = player_2
            curr_army = curr_army_2
        else:
            curr_player = "1"
            curr_ls = player_1
            curr_army = curr_army_1
            year += 1
