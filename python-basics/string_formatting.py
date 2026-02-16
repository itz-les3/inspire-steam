# Name: Mark Leslie
# Date: 11/02/2026
#string formatting

#Get string  length
sentence = "I am learning Python"

string_length = len(sentence)

print(f"The length is:{string_length}")

#splitting  a string 
sentence_2 ="Mathematics Physics"
split=sentence_2.split(" ")

print(f"the first subject is: {split[0]}")


#Make everthing CAPS
mpesa_code ="us24htfhfn"

capitalized = mpesa_code.upper()

print("New mpesa code : ", capitalized)
#Make everything small
mpesa_code_2 = "US24HTHFNFN"
small = mpesa_code_2.lower()
print("New mpesa code : ", small)

#Replacing characters in a string

balance = "100Kshs"
amount_added = "50Kshs"

cleaned_balance = balance.replace("Kshs", "")

print(f"Cleaned balance: ",cleaned_balance)
 # asssignment
Mpesa_message = "CONFIRMED you have received 40Kshs from John Doe"
print(Mpesa_message)
split1= Mpesa_message.split(" ")
print(f"The amount received is: {split1[5]}")

#Assignment
Mpesa_message= "CONFIRMED you have received 40Kshs from John Doe"

split1 = Mpesa_message.split(" ")

print("Split 1 contents: ", split1)

print("the amount is: ",split1[4])

amount_added1 = split1[4]

cleaned_amount_added1 = amount_added1.replace("Kshs", "")

print("Cleaned amount added: ",cleaned_amount_added1)

balance1 = 50

new_balance1 = int(balance1) + int(cleaned_amount_added1)

print("New balance = ",new_balance1)


