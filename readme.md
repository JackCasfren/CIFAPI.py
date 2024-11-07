Greetings, welcome to the DTT repo.
Here you will be able to find the asked for excersises.

# the project.
![image](https://github.com/user-attachments/assets/7f67add9-9ada-4cd5-b1b3-8c06ea764298)

# Name of the project:
CIFAPI.py -> Company Identifiers for Forpass API.

# How to setup project:
first step is aquiring a pantry api key. It's easy, from there create a file in the base directory called creds.py in it insert your apy key under a variable called "api_key".
The api key can be made here: https://getpantry.cloud/#

I use IDX, if you just import the repo it should do everything automatically.
Otherwise some dependencies will have to be installed manually.

after writting the key, everything should work

# Main Objectives
Make a piece of Software that does the following:
1. Base: Interact with the Pantry Json api.
    This api will store all of the "Base" Variables of many companies. 
        Incase you haven't see ForPass.js base variables are variables used in Formula based passwords that don't change. 
    > So in microsoft it would include the word microsoft, blue as their main color, the windows squares as their logo, and so on.
2. Place rate limiters so this doesn't happen:
![image](https://github.com/user-attachments/assets/9e4f6290-8ec3-45ed-b880-45e760b75d9b)

3. Self Updating: Every X ammount of time the software will consult a LLM and other methods, if the values of this company have changed.
4. Back up json to multiple places, including github.
5. request feed back from users, if multiple users alert that a value is wrong, it will store the alert, so it is prioritized to be inspected

- later on it will integrate with for pass js. a JavaScript API from the client side will call python to get the values and make reports. (but not edit)



## Context
i found this service called pantry json api and i wanted to try it out.
its 100MB free to CRUD a json file.
Wanted to test it out but i don't konw how much time i have ill ask tomorow.

Then thinking about what i should do with this API what i would say is a good idea.
complement the ForPass.js project with a API that gets the values for you.
this is the repository for the other project: https://github.com/JackCasfren/ForPassJS

This project got me far and I appreciate what it has done for me :) just got the opportunity to have a meeting on the subject.

# Second section:

read only API. For-pass user will ask for a domain, and from there give the result.
that uses the pythoneverywhere.com domain.
if people want more requests, they can pay.

From there integrate it into Forpass.JS



