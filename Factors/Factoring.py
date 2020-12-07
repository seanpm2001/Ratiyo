# Start of script
print ("Factoring - Ratiyo")
print ("Please mention any of the account types to factor in, as a good answer can't be given without factoring these in.")
# Family check
familyBoolIn = str(input("Do you have any family members following you on GitHub? (y/N)"))
familyBoolIn == familyBoolIn.upper()
if (familyBoolIn = "Y"):
  familyBool = bool(true)
  familyCountIn = int(input("How many family member accounts are following you on GitHub (each family member counts as 1-5 followers/subscribers, depending on the platform)"))
  try: # Script to make sure input is a number and isn't NaN
        int(familyCountIn)
        return True
    except ValueError:
        return False
else:
  familyBool = bool(false)
# Friend check
friendBoolIn = str(input("Do you have any friends following you on GitHub? (y/N)"))
friendBoolIn == friendBoolIn.upper()
if (friendBoolIn = "Y"):
  friendBool = bool(true)
  friendCountIn = int(input("How many friend accounts are following you on GitHub (each friend account counts as 1-5 followers/subscribers, depending on the platform)"))
  try: # Script to make sure input is a number and isn't NaN
        int(friendCountIn)
        return True
    except ValueError:
        return False
else:
  friendBool = bool(false)
# Other check
'''
This section is coming soon
'''
# Final section
noMore = input("Factoring is complete!\nPress [ENTER] key to quit")
print ("This program should now be closed. If the window is not closed, try pressing the close button. If this doesn't work, try killing the task/process with a task manager / process/resource manager")
# End of script
"""
File info
File version: 1 (Sunday, December 6th 2020 at 7:13 pm)
File type: Python script file (*.py)
Line count (including blank lines and compiler line): 44
"""
