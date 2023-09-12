from little_battle import load_config_file
# Don't remove any comments in this file
folder_path = "/Users/derek/Class_Projects/assignment_2/invalid_flies/"

# Please create appropriate invalid files in the folder "invalid_files"
# for each unit test according to the comments below and
# then complete them according to the function name


def test_file_not_found():
    # no need to create a file for FileNotFound
    config_file = "notestfile.txt"
    try:
        load_config_file(folder_path + config_file)
        assert False, "test 1 failed"
    except FileNotFoundError:
        assert True, "test 1 wrong error type"


def test_format_error():
    # add "format_error_file.txt" in "invalid_files"
    config_file = "format_error_file.txt"
    try:
        load_config_file(folder_path + config_file)
        assert False, "test 2 failed"
    except SyntaxError as e:
        assert str(
            e) == "Invalid Configuration File: format error!", \
            "test 2 incorrect error message"
    except Exception:
        assert False, "test 2 wrong error type"


def test_frame_format_error():
    # add "frame_format_error_file.txt" in "invalid_files"
    config_file = "frame_format_error_file.txt"
    try:
        load_config_file(folder_path + config_file)
        assert False, "test 3 failed"
    except SyntaxError as e:
        assert str(
            e) == "Invalid Configuration File: frame should be in format widthxheight!", \
            "test 3 incorrect error message"
    except Exception:
        assert False, "test 3 wrong error type"


def test_frame_out_of_range():
    # add "format_out_of_range_file.txt" in "invalid_files"
    config_file = "format_out_of_range_file.txt"
    try:
        load_config_file(folder_path + config_file)
        assert False, "test 4 failed"
    except ArithmeticError as e:
        assert str(
            e) == "Invalid Configuration File: width and height should range from 5 to 7!", \
            "test 4 incorrect error message"
    except Exception:
        assert False, "test 4 wrong error type"


def test_non_integer():
    # add "non_integer_file.txt" in "invalid_files"
    config_file = "non_integer_file.txt"
    try:
        load_config_file(folder_path + config_file)
        assert False, "test 5 failed"
    except ValueError as e:
        assert str(
            e) == "Invalid Configuration File: Wood contains non integer characters!", \
            "test 5 incorrect error message"
    except Exception:
        assert False, "test 5 wrong error type"


def test_out_of_map():
    # add "out_of_map_file.txt" in "invalid_files"
    config_file = "out_of_map_file.txt"
    try:
        load_config_file(folder_path + config_file)
        assert False, "test 6 failed"
    except ArithmeticError as e:
        assert str(
            e) == "Invalid Configuration File: Wood contains a position that is out of map.", \
            "test 6 incorrect error message"
    except Exception:
        assert False, "test 6 wrong error type"


def test_occupy_home_or_next_to_home():
    # add two invalid files: "occupy_home_file.txt" and
    # "occupy_next_to_home_file.txt" in "invalid_files"
    config_file_1 = "occupy_home_file.txt"
    try:
        load_config_file(folder_path + config_file_1)
        assert False, "test 7a failed"
    except ValueError as e:
        assert str(e) == "Invalid Configuration File: " + \
            "The positions of home bases or the positions next to the home bases are occupied!", \
            "test 7a incorrect error message"
    except Exception:
        assert False, "test 7a wrong error type"

    config_file_2 = "occupy_next_to_home_file.txt"
    try:
        load_config_file(folder_path + config_file_2)
        assert False, "test 7b failed"
    except ValueError as e:
        assert str(e) == "Invalid Configuration File: " + \
            "The positions of home bases or the positions next to the home bases are occupied!", \
            "test 7a incorrect error message"
    except Exception:
        assert False, "test 7b wrong error type"


def test_duplicate_position():
    # add two files: "dupli_pos_in_single_line.txt" and
    # "dupli_pos_in_multiple_lines.txt" in "invalid_files"
    config_file_1 = "dupli_pos_in_single_line.txt"
    try:
        load_config_file(folder_path + config_file_1)
        assert False, "test 8a failed"
    except SyntaxError as e:
        assert str(
            e) == "Invalid Configuration File: Duplicate position (0, 0)!", \
            "test 8a incorrect error message"
    except Exception:
        assert False, "test 8a wrong error type"

    config_file_2 = "dupli_pos_in_multiple_lines.txt"
    try:
        load_config_file(folder_path + config_file_2)
        assert False, "test 8b failed"
    except SyntaxError as e:
        assert str(
            e) == "Invalid Configuration File: Duplicate position (0, 0)!", \
            "test 8b incorrect error message"
    except Exception:
        assert False, "test 8b wrong error type"


def test_odd_length():
    # add "odd_length_file.txt" in "invalid_files"
    config_file = "odd_length_file.txt"
    try:
        load_config_file(folder_path + config_file)
        assert False, "test 9 failed"
    except SyntaxError as e:
        assert str(
            e) == "Invalid Configuration File: Water has an odd number of elements!", \
            "test 9 incorrect error message"
    except Exception:
        assert False, "test 9 wrong error type"


def test_valid_file():
    # no need to create file for this one, just test loading config.txt
    # function will return the following variables:
    # width, height, waters, woods, foods,
    # golds, homebase1, homebase2, armybase_1,
    # armybase_2
    config_file = "config.txt"
    assert load_config_file(config_file) == (
        5, 5, [(0, 0), (4, 2), (1, 3)], [(0, 2), (2, 4)], [(0, 4), (3, 1)],
        [(4, 1), (2, 2)], [(1, 1)], [(3, 3)], [(0, 1), (1, 0), (2, 1), (1, 2)],
        [(2, 3), (3, 2), (4, 3), (3, 4)]
    ), "test 10 failed"


# you can run this test file to check tests and load_config_file
if __name__ == "__main__":
    test_file_not_found()
    test_format_error()
    test_frame_format_error()
    test_frame_out_of_range()
    test_non_integer()
    test_out_of_map()
    test_occupy_home_or_next_to_home()
    test_duplicate_position()
    test_odd_length()
    test_valid_file()
