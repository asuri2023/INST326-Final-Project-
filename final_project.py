import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

class Apartment:
    
    def __init__(self):
        #Member who worked on this method: Avi
        #Technique used: Merging operation on Pandas DataFrames
        
        # Read the CSV files
        self.apartments_df = pd.read_csv(r"CP Apartments_Version3.csv")
        self.amenities_df = pd.read_csv(r"Amenitites_Version2.csv")
        self.historical_df = pd.read_csv(r"Major Historical Data_Version3.csv")
        
        # Merging operation on Pandas DataFrames
        self.merged_data = self.apartments_df.merge(self.amenities_df, 
                                                    on=["Apartment Name"])
        
            
        # Will be used in the future:
            # Store the apartment names and minimum budgets in a dictionary
            #self.min_budgets = dict(zip(self.merged_data["Apartment Name"], 
            # self.merged_data["Minimum Price"]))
            
        self.terrapin_row, self.university_view, self.the_varsity, self.south_campus_commons = self.merged_data["Apartment Name"].unique()
        self.min_budget = {"Terrapin Row":1250, "University View":1200, 
                           "The Varsity":1104, "South Campus Commons":1016} 
        self.major_campus_dictionary=  {1: ["University View","The Varsity"],
                                   2:["Terrapin Row","South Campus Commons"],
                                   3: ["Terrapin Row","South Campus Commons"],
                                   4:["University View","The Varsity"],
                                   5:["Terrapin Row","South Campus Commons"]}
        
             
       
        # Initialize user attributes to None
        self.user_name = None
        self.user_budget = None
        self.user_location = None
        self.user_pool = None
        self.user_gym = None
        self.user_parking = None
        self.user_electronic_entry_locks = None
        self.user_study_rooms = None
        self.user_game_lounge = None
        self.user_input_budget=None  
        self.major_category_input=None
        

    def amenityCheck(self,apartment1,apartment2,amenity):
        #Member who worked on this method: Philip
        #Technique used: 
        apartment1_amenity = self.amenities_df.loc[self.amenities_df ['Apartment Name'] == apartment1, amenity].values[0]
        apartment2_amenity = self.amenities_df.loc[self.amenities_df ['Apartment Name'] == apartment2, amenity].values[0]
        
        if apartment1_amenity == 1:
            print(f"{apartment1} has a {amenity}.")
        else:
            print(f"{apartment1} does not have a {amenity}.")

        if apartment2_amenity == 1:
            print(f"{apartment2} has a {amenity}.")
        else:
            print(f"{apartment2} does not have a {amenity}.")     
    
    def userInput(self):
        #Member who worked on this method: Philip
        #Technique used:Visualizing data with seaborn 
        
        #INTRODUCTION
        print("Welcome to the College Park Apartment Portal! There are four "
              "apartments to choose from: Terrapin Row, University View, " 
              "The Varsity, and South Campus Commons.")
        print("The University of Maryland, College Park is divided into "
              "North and South campus, with Mckeldin Mall being the division "
              "line.")
        print("Facing the front of Mckeldin Library, any land to the right of "
              "the library is North and any land to the left of the library is "
              "South.")
        print("Terrapin Row and South Campus Commons are located in "
              "South campus.")
        print("University View and The Varsity are located in North campus.")
        print("Answer some questions to find your ideal apartment!")

        user_name = input("Please enter your full name:")
        
        #MAJOR CATEGORIES
        self.major_category_input = int(input("Which one of the following categories "
                                     "would your major fall under?\n"
          "Type 1 for STEM (Classes in North campus)\n"
          "Type 2 for Business (Classes in South campus)\n"
          "Type 3 for Public Policy (Classes in South campus)\n"
          "Type 4 for Fine Arts (Classes in North campus)\n"
          "Type 5 for Architecture (South campus)"))
        
        major_number_dictionary = {1:"STEM",2:"Business", 3:"Public Policy",
                                     4:"Fine Arts",5:"Architecture"}
        
        
        major_proximity_dictionary = {1:"University View and The Varsity "
                                     "are located near STEM buildings",
                                     2:"Terrapin Row and South Campus Commons "
                                     "are located near Business buildings",
                                     3:"Terrapin Row and South Campus Commons "
                                     "are located near Public Policy buildings",
                                     4:"University View and The Varsity "
                                     "are located near Fine arts buildings",
                                     5:"Terrapin Row and South Campus Commons "
                                     "are located near Architecture buildings"}
        print(major_proximity_dictionary[self.major_category_input])
        
        
        print(f"Let's see what most "
              f"{major_number_dictionary[self.major_category_input]} majors in "
              f"previous years chose as their apartment.")
        #Visualizing historical data with seaborn
        
        #Filter historical database by user's specific major.
        df_major = self.historical_df[self.historical_df["Major"] 
                        == (major_number_dictionary[self.major_category_input])]
        sns.countplot(x = "Apartment", data = df_major)
        plt.show()
        
        if self.major_category_input == 1 or self.major_category_input == 4:
            print("Between University View and The Varsity, let's see which "
                  "apartment best fits your amenity needs.")
        else: 
            print("Between Terrapin Row and South Campus Commons, let's pick one "
                  "apartment that best fits your amenity needs.")   
            
        #The two apartments in the side of campus where the user's classes 
        # for major are.
        apartment1 = self.major_campus_dictionary[self.major_category_input][0]
        apartment2 = self.major_campus_dictionary[self.major_category_input][1]
         
        #Amenities questions (make this its own method in the future)
            #'Pool' question and check
        user_pool=int(input("Are you looking for a pool? Type 0 for no pool or 1"  
                        " for pool:"))
        self.amenityCheck(apartment1,apartment2, 'Pool')
        
            #'Gym'question and check
        user_gym=int(input("Are you looking for a gym? Type 0 for no gym or 1" 
                        " for gym:"))
        self.amenityCheck(apartment1,apartment2, 'Gym')
        
            #'Parking' question and check
        user_parking=int(input("Are you looking for parking? Type 0 for no" 
                            " parking and 1 for parking:" ))
        self.amenityCheck(apartment1,apartment2, 'Parking')
            
            #'Electronic Key Locks' question and check
        user_electronic_entry_locks=int(input("Do you want an apartment with an"
                                        " electronic entry lock system? Type 0"
                                        " for no system and 1 for a system:"  )) 
        self.amenityCheck(apartment1,apartment2, 'Electronic Key Locks')
        
            #'Study Rooms' question and check
        user_study_rooms=int(input("Are you looking for study rooms? Type 0 for"
                               " no study rooms and 1 for study rooms:"))
        self.amenityCheck(apartment1,apartment2, 'Study Rooms')
            
            #'Game Lounge' question and check
        
        user_game_lounge=int(input("Are you looking for game lounge? Type 0 for" 
                                   " no game lounge and 1 for a game lounge:"))
        self.amenityCheck(apartment1,apartment2, 'Game Lounge')
    
        # BUDGET QUESTIONS
        self.user_input_budget = int(input("What is your minimum budget?")) 

    def userBudget(self):
        #Member who worked on this method: Shishir
        #Technique used: List comprehension

        cheapest_apt=min(self.min_budget.values())
        matching_apartments = [key for key in self.min_budget if 
                               self.min_budget[key] <= self.user_input_budget]
        if not matching_apartments:
            raise ValueError("Your budget does not meet the minimum budget" 
                             " for any of the apartments")
        elif self.user_input_budget >= self.min_budget["Terrapin Row"]:
            print (f'Your budget satisfies the minimum budget of all the'
                   ' apartments:' 
        f' Terrapin Row:({self.min_budget["Terrapin Row"]}), University View:' 
        f' ({self.min_budget["University View"]}), and The Varsity:' 
        f' ({self.min_budget["The Varsity"]})')
        elif self.user_input_budget >= self.min_budget["University View"]:
            print (f'You meet the minimum budget of University View:'
            f' {self.min_budget["University View"]}')
        else:
            print (f'You meet the minimum budget of The Varsity:' 
            f'{self.min_budget["The Varsity"]}')
            
        #STEP 2 :CALCULATE ADDITIONAL EXPENSES (EXPENSES THE MONTHLY RENT DOES NOT COVER)
       # Additional expenses:
         
      
       #STEP 3 :DOES USER HAVE ENOUGH MONEY TO PAY RENT FOR THEIR DURATION (FULL YEAR OR HALF A YEAR) OF STAY
       
        # Will be used in the future:
            #return cheapest_apt
            #Or find a way to use cheapest_apt later in this program.


        
    def check_eligibility(self):
        """
        Check if user meets all the proper documentation for leasing.

        Args:
        - identity_proof: string, proof of identity (e.g. driver's license, 
            passport)
        - income_proof: string, proof of income (e.g. pay stub, 
            bank statement)
        - residency_proof: string, proof of current residency (e.g. utility 
            bill, lease agreement)
        - insurance_proof: string, proof of insurance (e.g. auto insurance, 
            renters insurance)

        Returns:
        - eligible: boolean, True if user meets all the proper documentation, 
            False otherwise
        """
        #Member who worked on this method: Jhemel
        #Technique used:
        
        identity_proof = int(input("Do you have proof of identity" 
            " (e.g. driver's license, passport) ? Type 0 for no, 1 for yes:")) 
        income_proof = int(input("Do you have proof of income (e.g. pay stub," 
                                " bank statement) ? Type 0 for no, 1 for yes:")) 
        residency_proof = int(input("Do you have proof of current residency" 
        " (e.g. utility bill, lease agreement) ? Type 0 for no, 1 for yes:")) 
        insurance_proof = int(input("Do you have proof of insurance (e.g. auto" 
                " insurance, renters insurance) ? Type 0 for no, 1 for yes:"))                
       
        # Check if all proofs of documentation are provided
        if (identity_proof == 1 and income_proof == 1 and residency_proof == 1 
            and insurance_proof == 1):
            return("You have all the required documentation to live in" 
                   " these apartments")
            
        else:
            return("Please provide all the required documentation.")
        
        # Will be used in the future:
            # Check if the user meets the minimum income requirement
            #min_income_requirement = 30000  # set a minimum income requirement of $30,000
            #if income_proof < min_income_requirement:
                
                #print("Your income does not meet the minimum requirement.")
                #return False
            
            # Check if the residency proof is current
            # You could implement this check by comparing the date on the residency_proof to today's date
            
            # Check if the insurance proof is valid
            # You could implement this check by verifying that the insurance policy is currently active
            
            # If all checks pass, the user is eligible
            #print("Congratulations, you are eligible to lease!")
            #return True

#We will implement this main method in the future.
def main():
    apt = Apartment()
    
    apt.userInput()
    apt.userBudget()
    
if __name__=='__main__':
    main()

        



            
        
   
              
                
                







