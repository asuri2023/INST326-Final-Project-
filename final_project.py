import pandas as pd
#df = pd.read_csv(r"/Users/shishirporeddy/Documents/GitHub/INST326-Final-Project-/College Park Apartment Database_Version1 - Sheet1.csv")
#print(df) 

#df = pd.read_excel(r"/Users/shishirporeddy/Desktop/INST326/College Park Apartment Database_Version1.xlsx#")
#print(df)
#url="https://docs.google.com/spreadsheets/d/1F8AL1BA8NFl0uHObNFIyygi7sBF6MP3TBv1jbXa7OWg/edit?usp=sharing" 
#s=requests.get(url).content 
#c=pd.read_csv(s)
class Apartment:
    
    def __init__(self, csv1, csv2, merged_data, min_budget, num_rooms, apt_names, location, amenities, floorplan="A1"):
        #Merging "CP Apartments_Version2.csv" and "Amenitites.csv"
        self.csv1 = pd.read_csv(r"CP Apartments_Version2.csv")
        self.csv1.head()
        self.csv2 = pd.read_csv(r"Amenitites.csv")
        self.csv2.head()
        self.merged_data = self.csv1.merge(self.csv2, on=["Apartment Name"]) 
        self.merged_data.head()
        # End of merging
        
        self.min_budget = {"Terrapin Row":1250, "University View":1200, "The Varsity":1104}
        self.num_rooms = num_rooms
        self.apt_names = ["Terrapin Row","University View","The Varsity"]
        self.location = location 
        self.amenities = self.merged_data["Apartment Name"]
        self.floorplan = floorplan
        

    def userBudget(self,user_input_budget):

        user_input_budget = int(input("What is your minimum budget?")) 
        cheapest_apt=min(self.min_budget.values)
        matching_apartments = [key for key in self.min_budget if self.min_budget[key] <= user_input_budget]
        if not matching_apartments:
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
        
        print("Please answer the following questions for us to help provide you with your ideal apartment")
        user_name = input("Please enter your full name:")
        
        self.userBudget 
        #Goes to userBudget method and asks user budget questions.
        
        user_location = input("Which part of UMD campus would be ideal for you. Type North or South: ") 
                 
        apt_some_location = ["Terrapin Row is South","University View is North","The Varsity is North"] 

        user_pool=input("Are you looking for a pool? Type 0 for no pool or 1 for pool:") 
        user_gym=int(input("Are you looking for a gym? Type 0 for no gym or 1 for gym:"))
        user_parking=int(input("Are you looking for parking? Type 0 for no parking and 1 for parking:" ))
        user_electronic_entry_locks=int(input("Do you want an apartment with an electronic entry lock system? Type 0 for no system and 1 for a system:"  )) 
        user_study_rooms=int(input("Are you looking for study rooms? Type 0 for no study rooms and 1 for study rooms:"))
        user_game_lounge=int(input("Are you looking for game lounge? Type 0 for no game lounge and 1 for a game lounge:"))

    #Possible way to find apartment that fits user's amenitites needs:
    #if user_pool==1 and user_gym==1 and user_parking==1 and \
            #user_electronic_entry_locks==1 and user_study_rooms==1 and \
               # user_game_lounge ==1:
                #return "Terrapin Row"
    #Find a more efficent way to do this by traversing the merged csv file.

    def check_eligibility(identity_proof, income_proof, residency_proof, insurance_proof):
        """
        Check if user meets all the proper documentation for leasing.

        Args:
        - identity_proof: string, proof of identity (e.g. driver's license, passport)
        - income_proof: string, proof of income (e.g. pay stub, bank statement)
        - residency_proof: string, proof of current residency (e.g. utility bill, lease agreement)
        - insurance_proof: string, proof of insurance (e.g. auto insurance, renters insurance)

        Returns:
        - eligible: boolean, True if user meets all the proper documentation, False otherwise
        """
    # Check if all proofs of documentation are provided
        if identity_proof is None or income_proof is None or residency_proof is None or insurance_proof is None:
            print("Please provide all the required documentation.")
            return False
        
        # Check if the user meets the minimum income requirement
        min_income_requirement = 30000  # set a minimum income requirement of $30,000
        if income_proof < min_income_requirement:
            print("Your income does not meet the minimum requirement.")
            return False
    
    # Check if the residency proof is current
    # You could implement this check by comparing the date on the residency_proof to today's date
    
    # Check if the insurance proof is valid
    # You could implement this check by verifying that the insurance policy is currently active
    
    # If all checks pass, the user is eligible
        print("Congratulations, you are eligible to lease!")
        return True
        

def main():
    apt = Apartment("CP Apartments_Version2.csv", "Amenities.csv", None, None, None, None, None, None)
    apt.userInput()
    
if __name__=='__main__':
    main()
    

            
        



            
        
   
              
                
                







