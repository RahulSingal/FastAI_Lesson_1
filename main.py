# ------------------------------------------------------------------------------------------------------------
# | Programmer: Rahul Singal
# | File Name: main.py
# | Date Created: 10/16/2024 
# | Date Last Modified: 10/26/2024
# | Description: This will run my program similar to an ipython notebook
# ------------------------------------------------------------------------------------------------------------

import library # Importing the library.py file
import functions # Importing the functions.py file

#  -------------------------------------------------------------------------------------------
# | Function Name:      main
# | Description:        TBD
# | Input Parameters:   TBD
# | Returns:            TBD
#  -------------------------------------------------------------------------------------------
def main():

  print("Hello from Main")

  # Tuple of my search criteria
  # searches = 'tennis racket', 'squash racket'

  # path will hold image's in the 'tennis_or_squash' directory
  # path = multiple_searches(searches, 'tennis_or_squash', max_images=100)

  # delete_corrupted_images(path)

  # Using my function
  # dls = create_dataloaders(path)

  # Using my function to learn
  # learn = train_classifier(dls)

  # Using my function to test
  # test_classifier(learn, "tennis rackets")

if __name__ == '__main__':
  main()