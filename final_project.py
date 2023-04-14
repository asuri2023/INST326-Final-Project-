import pandas as pd
#df = pd.read_csv(r"/Users/shishirporeddy/Documents/GitHub/INST326-Final-Project-/College Park Apartment Database_Version1 - Sheet1.csv")
#print(df) 

#df = pd.read_excel(r"/Users/shishirporeddy/Desktop/INST326/College Park Apartment Database_Version1.xlsx#")
#print(df)
#url="https://docs.google.com/spreadsheets/d/1F8AL1BA8NFl0uHObNFIyygi7sBF6MP3TBv1jbXa7OWg/edit?usp=sharing" 
#s=requests.get(url).content 
#c=pd.read_csv(s)
class Apartment:
    
    def __init__(self, csv1, csv2, merged_data, min_budget, num_rooms, apt_names, location, amenities, floorplan):
        #Merging "CP Apartments_Version2.csv" and "Amenitites.csv"
        self.csv1 = pd.read_csv(r"CP Apartments_Version2.csv")
        self.csv1.head()
        self.csv2 = pd.read_csv(r"Amenitites.csv")
        self.csv2.head()
        self.merged_data = csv1.merge(csv2, on=["Security Code"]) 
        self.merged_data.head()
        # End of merging
        
        self.min_budget = {"Terrapin Row":1250, "University View":1200, "The Varsity":1104}
        self.num_rooms = num_rooms
        self.apt_names = ["Terrapin Row","University View","The Varsity"]
        self.location = location 
        self.amenities = self.readDatabase["Amenities"]
        self.floorplan = floorplan
        

    def userBudget(self,user_input_budget):

        user_input_budget = int(input("What is your minimum budget?")) 
        if user_input_budget < self.min_budget["The Varsity"]:
            raise ValueError("Your budget does not meet the minimum budget for any of the apartments")
        elif user_input_budget >= self.min_budget["Terrapin Row"]:
            return f'You meet the minimum budget of Terrapin Row: {self.min_budget["Terrapin Row"]}'
        elif user_input_budget >= self.min_budget["University View"]:
            return f'You meet the minimum budget of University View: {self.min_budget["University View"]}'
        elif user_input_budget >= self.min_budget["The Varsity"]:
            return f'You meet the minimum budget of The Varsity: {self.min_budget["The Varsity"]}'
        else:
            return f'Your budget satisfies the minimum budget of Terrapin Row \
        ({self.min_budget["Terrapin Row"]}), University View \
        ({self.min_budget["University View"]}), and The Varsity \
        ({self.min_budget["The Varsity"]})'

    def userInput(self):
        
        print("Please answer the following questions for us to help provide you with \
              your ideal apartment")
        user_name = input("Please enter your full name:")
        
        self.userBudget 
        #Goes to userBudget method and asks user budget questions.
        
        user_location = input("Which part of UMD campus would be ideal for you. \
                               Type North or South: ") 
                 
        apt_some_location = ["Terrapin Row is South","University View is North",\
            "The Varsity is North"] 

        user_pool=input("Are you looking for a pool? Type 0 for no pool or 1 for\
                        pool:") 
        user_gym=int(input("Are you looking for a gym? Type 0 for no gym or 1 for \
                       gym:"))
        user_parking=int(input("Are you looking for parking? Type 0 for no parking \
                           and 1 for parking:" ))
        user_electronic_entry_locks=int(input("Do you want an apartment with an \
                                        electronic entry lock system? Type 0 \
                                        for no system and 1 for a system:"  )) 
        user_study_rooms=int(input("Are you looking for study rooms? Type 0 for \
                               no study rooms and 1 for study rooms:"))
        user_game_lounge=int(input("Are you looking for game lounge? Type 0 for \
                                no game lounge and 1 for a game lounge:"))

    #Possible way to find apartment that fits user's amenitites needs:
    #if user_pool==1 and user_gym==1 and user_parking==1 and \
            #user_electronic_entry_locks==1 and user_study_rooms==1 and \
               # user_game_lounge ==1:
                #return "Terrapin Row"
    #Find a more efficent way to do this by traversing the merged csv file.
        
        

#def main()
# Run all the methods here
            
        



            
        
   
              
                
                







