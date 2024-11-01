import random
# Importing the 'random' module for generating random numbers
class Patient:
    def __init__(self, time):
        """
        Initialize a Patient object with a randomly generated age between 20 and 60
        """
        self.age = random.randrange(20, 61)
        self.arrivaltime = time  # Set the arrival time for the patient

    def getAge(self):
        # Return the age of the patient
        return self.age

    def getTime(self):
        # Return the arrival time of the patient
        return self.arrivaltime

    def waitTime(self, currentsec):
        """
        Calculate and return the wait time of the patient by
        subtracting arrival time from the current time
        """
        return currentsec - self.arrivaltime



