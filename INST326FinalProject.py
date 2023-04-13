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
