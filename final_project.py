import pandas as pd
import requests



#df = pd.read_excel(r"/Users/shishirporeddy/Desktop/INST326/College Park Apartment Database_Version1.xlsx#")
#print(df)
#url="https://docs.google.com/spreadsheets/d/1F8AL1BA8NFl0uHObNFIyygi7sBF6MP3TBv1jbXa7OWg/edit?usp=sharing" 
#s=requests.get(url).content 
#c=pd.read_csv(s)
class Apartment:
    
    def __init__(self, readDatabase, min_budget, num_rooms, apt_names, location, amenities, floorplan):
        
        self.readDatabase = pd.read_csv(r"CP Apartments.csv")
        self.min_budget = {"Terrapin Row":1250, "University View":1200, "The Varsity":1104}
        self.num_rooms = num_rooms
        self.apt_names = ["Terrapin Row","University View","The Varsity"]
        self.location = location 
        self.amenities = self.readDatabase["Amenities"]
        self.floorplan = floorplan
        

    def userBudget(self, filename):

        user_budget = int(input("What is your minimum budget?")) 
        if user_budget < self.min_budget["The Varsity"]:
            raise ValueError("Your budget does not meet the minimum budget for any of the apartments")
        elif user_budget >= self.min_budget["Terrapin Row"]:
            return f'You meet the minimum budget of Terrapin Row: {self.min_budget["Terrapin Row"]}'
        elif user_budget >= self.min_budget["University View"]:
            return f'You meet the minimum budget of University View: {self.min_budget["University View"]}'
        elif user_budget >= self.min_budget["The Varsity"]:
            return f'You meet the minimum budget of The Varsity: {self.min_budget["The Varsity"]}'

    def userInput(self):
       

        apt_location = ["North","South"]
        #apt_some_location = ["Terrapin Row is North","University View is South","The Varsity is South"]
        
        print("Please answer the following questions to help provide you with your ideal apartment")
        user_name = input("Please enter your full name:")
        user_location = input("Which part of UMD campus would be ideal for you. \
                               Type North or South: ") 
        
        correct_user_location = [x for x in apt_location if user_location in x]   
        #This list comprehension checks if the user properly wrote "North" or 
        # "South". 
            
        apt_some_location = ["Terrapin Row is South","University View is North","The Varsity is North"] 

        user_pool=input("Are you looking for a pool?") 
        user_Gym=input("Are you looking for a Gym?") 
        user_Parking=input("Are you looking for parking ")
        user_ElectronicEntryLocks=input("Do you want an apartment with an electronic entry lock system?") 

        
    
    def checkUserInput(self,question,answer):
        #set of correct answers
        while True:
            user_location 
            
        



            
        
   
              
                
                







