class Doctor:
    def __init__(self, rate):
        # Initialize the Clinic object with a patient treatment rate
        self.patientRate = rate

        self.remainingTime = 0
        # Initialize the remaining time for the current patient to be treated
        self.currentPatient = None
        # Initialize the current patient being treated as None

    def busy(self):
        # Check if the clinic is currently treating a patient or not
        return self.currentPatient is not None

    def nextPatient(self, patient):
        """
        Set the current patient and calculate the time required
         for treatment based on their age and patient rate
        """
        self.currentPatient = patient
        # Time taken to treat each patient = Age / patient rate (* 60 to get it in seconds)
        self.remainingTime = round(patient.getAge() / self.patientRate) * 60



    def tick(self):
        if self.currentPatient is not None:
            # Reduce the remaining treatment time for the current patient by 1 second
            self.remainingTime -= 1
            if self.remainingTime == 0:
                # If the treatment time is completed, set the current patient to None (treatment finished)
                self.currentPatient = None
