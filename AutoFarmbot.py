from farmbot import Farmbot, FarmbotToken
import time

raw_token = FarmbotToken.download_token("shaylah1.fleming@famu.edu",
                                        "HydroTeam309!",
                                        "https://my.farm.bot")

fb = Farmbot(raw_token)

class MyHandler:
    
    def on_connect(self, bot, mqtt_client):
        
        request_id1 = bot.move_absolute(x=10, y=20, z=30)

        print("MOVE_ABS REQUEST ID: " + request_id1)

        request_id2 = bot.send_message("Hello, world!")

        print("SEND_MESSAGE REQUEST ID: " + request_id2)

    def on_change(self, bot, state):
       
        print("NEW BOT STATE TREE AVAILABLE:")
        print(state)

        print("Current position: (%.2f, %.2f, %.2f)" % bot.position())

        pos = state["location_data"]["position"]
        xyz = (pos["x"], pos["y"], pos["z"])
        print("Same information as before: " + str(xyz))

    def on_log(self, bot, log):
        print("New message from FarmBot: " + log['message'])

    def on_response(self, bot, response):
        print("ID of successful request: " + response.id)

    def on_error(self, bot, response):
 
        print("ID of failed request: " + response.id)

        print("Reason(s) for failure: " + str(response.errors))

    def move_to_position():
        x = float(input("Enter X coordinate: "))
        y = float(input("Enter Y coordinate: "))
        z = float(input("Enter Z coordinate: "))
        request_id = fb.move_absolute(x=x, y=y, z=z, speed=100.0)
        print(f"MOVE_ABS REQUEST ID: {request_id}")


    def gohome(self,bot,mqtt_client):
        request_id3 = bot.find_home()
        print("FIND_HOME REQUEST ID: " + request_id3)
        #gohome(fb)

    def menu():
        while True:
            print("\n===== FarmBot Control Menu =====")
            print("1. Move to a specific position")
            print("2. Go back to home position")
            print("3. Quit")
            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                move_to_position()
            elif choice == '2':
             gohome()
            elif choice == '3':
            #fb.disconnect()
                exit()
            else:
                print("Invalid choice. Please try again.")

handler = MyHandler()  
fb.connect(handler)
print("This line will not execute. `connect()` is a blocking call.")          

MyHandler.menu()
    #fb.disconnect()