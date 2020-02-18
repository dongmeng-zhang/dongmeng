
import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    new_game_library = data["game_library"];

    for game in new_game_library:
      new_platform = test_data.Platform(game["platform"]["name"],game["platform"]["launch year"])
      new_game = test_data.Game(game["title"],new_platform, game["year"])

      game_library.add_game(new_game)

    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###
    return game_library


#Part 2
input_json_file = "data/test_data.json"

json_file_name="data/test_data.json"

with open(json_file_name,"r")as reader:
    test_json_data = json.load(reader)

    game_library = make_game_library_from_json(test_json_data)
    print(game_library)



### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
