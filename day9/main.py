# # DICTIONARIES
# prog_dict = {
#     "bug": "An error in a code that stops it from running",
#     "function": "A code you can easily call over again",
#     "loop": "The action of doing a code over again"
# }
#
# # for i, e in enumerate(prog_dict):
# #     print(f"{i}:{e}")
#
# for entry in prog_dict:
#     print(f"{entry}: {prog_dict[entry]}")


# NESTED LIST AND DICTIONARIES
# capital = {
#     "france": "paris",
#     "germany": "berlin"
# }
# print(capital['germany'])

# nested
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }
# print(travel_log['France'][1])
#
#
# nested_list = ['A', 'B', ['C', 'D', 'E', ['F', 'G', 'H', 'I', 'J']]]
# print(nested_list[2][3][4])


nested_dict = {
    "france": {
        "travel_nums": 21,
        "cities": ['paris', 'dijon']
    },
    "germany": {
        "travel_nums": 17,
        "cities": ['berlin', 'stuttgart']
    }
}

print(nested_dict['germany']['cities'][1])
