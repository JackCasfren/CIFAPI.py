
import sys, os, json
# import the interactions for each section of the API.
import interactions.full_pantry as full_pantry
import interactions.full_basket as full_basket

# todo make variable that if true it will make a continuos async funciton that constantly counts to 20 days and freshes the api. It will also refresh once initiated.

#* START OF THE CLI CODE:
def main():
    #start puting in here the CLI stuff
    # TODO finish CLI
    
    print("""
    Welcome to the Pantry CLI!
    Type 'help' for a list of commands. Type 'exit' to quit.
    These are the options:
    Pantry interactions:
    [1] get_pantry_data
    [2] update_pantry_account
    Basket Interactions:
    [3] get_pantry_data
    [4] make_pantry_insert
    [5] 
    [6] 
    [7]
    """)


    
    while True:

        command = input("> ")
        match command:
            case "exit" | "e" :
                break
            case "help" | "h":
                # todo make proper help section
                print("Available commands: exit, help")
            
            case "get_pantry_data" | "1":
                
                print(full_pantry.get_pantry_data())
                

            case "get_pantry_data" | "2":
                # todo allow the user to escape this option incase they accessed accidentaly
                print("We would recomend not changing this. for now it break many things")
                print("insert the name and the descrption")
                name = input("Name: ")
                description = input("Description: ")
                # todo format the json it appears with tabs and not a straight line
                print(full_pantry.update_pantry_account(name,description ))
            
            #* the basket interactions:


            case "3":
                # todo add list of all of the baskets
                #! working on it!
                full_pantry.list_all_baskets()
                
                print("What is the name of the basket you read?")
                sel_pantry = input("Name: ").lower()
                print(full_basket.get_basket_data(sel_pantry))

            case "4" | "insert_basket": #! this works :D
                # todo UX to allow user to insert data. could be allowing the user to make their won json structure. or it could be just adding values inside a json structure. for now im going to go for the second option.
                print("Insert values into a basket selected.")
                print("Into what basket do you want to insert?")
                full_pantry.list_all_baskets()
                # todo proper function to make new baskets
                sel_pantry = input("Name: ").lower()

                # Collect input from the user
                company_name = input("Insert the company name: ")
                product = input("Insert the product: ")
                main_color = input("Insert the main color: ")
                logo_shape = input("Insert the logo shape: ")
                industry = input("Insert the industry: ")
                usage = input("Insert the usage: ")
                additional_features = input("Insert additional features (separated by commas): ").split(',')

                # todo When the api is made, one should check the format of the inserted query.
                # Create the JSON structure
                new_data = {
                    "company": {
                        "name": company_name,
                        "product": product,
                        "main_color": main_color,
                        "Logo_shape": logo_shape,
                        "industry": industry,
                        "usage": usage,
                        "additional_features": [feature.strip() for feature in additional_features if feature.strip()]
                    }
                }
                

                # Convert the dictionary to JSON and print it
                json_data = json.dumps(new_data, indent=4)
                print(json_data)
                print(sel_pantry, new_data)
                full_basket.insert_basket(sel_pantry, new_data )


            case "5" | "update_basket":
                #update_pantry_basket(basket_name, new_data)
                # todo work on this latter it isn't urgent.
                # Idk how the UX would be. [basket_name] -> list value -> pick which value wants to be changed -> new value
                print("What is the name of the basket you want to update?")
                full_pantry.list_all_baskets()
                sel_pantry = input("Name: ").lower()

                
            case "6" | "delete_pantry_basket":
                # list baskets:
                print("What is the name of the basket you want to delete?")
                full_pantry.list_all_baskets()
                sel_pantry = input("Name: ").lower()
                full_basket.delete_pantry_basket(sel_pantry)
                print("Basket deleted")
                
            case "7":
                print("test")

            case _:
                print("Invalid command.")
                



if __name__ == "__main__":
    main()




