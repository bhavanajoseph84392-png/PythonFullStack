User_Information = {"Name" :"Bhavana",
                    "Mobile Number": " ",
                    "ATM PIN": "7789",
                    "Balance":98567,
                    "Transaction History" :[]
                    }#User data
print("Please insert your ATM card")
remaining_attempts = 3
pass
while remaining_attempts >0:
    User_pin=input("ENTER YOUR ATM PIN:")
    if len(User_pin)== 4 and User_pin == User_Information['ATM PIN'] :
        print("Welcome to the ATM")
        
    else:
        remaining_attempts-=1
        if(remaining_attempts>0):
            print(f"The remaining attempts are {remaining_attempts} ")
        else:
                print(f"The card gets blocked")

        
    
    
    
        
    
                    
    
