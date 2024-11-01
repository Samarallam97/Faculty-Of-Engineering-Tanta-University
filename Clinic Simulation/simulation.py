
from patient import *
from doctor import *
from queue import*

def simulation(totalTime, rate):
    totalTime *= 3600
    # Convert the totalTime to seconds

    clinicDoctor = Doctor(rate)
    patientqueue = Queue()
    waitingTime = []

    # Loop through each second within the total time
    for cursec in range(totalTime):
        # Randomly generate patients arriving and enqueue them based on a probability
        if random.randrange(1, 361) == 300:
            newPatient = Patient(cursec)
            patientqueue.enqueue(newPatient)

        # Check if the doctor is available and there are patients in the queue
        if (not clinicDoctor.busy()) and (not patientqueue.isEmpty()):
            nextPatient = patientqueue.dequeue()
            # Dequeue the next patient from the queue
            clinicDoctor.nextPatient(nextPatient)
            # Assign the next patient to the clinic for treatment

            # Calculate and store the waiting time for the patient who just started treatment
            waitingTime.append(nextPatient.waitTime(cursec))

        clinicDoctor.tick()  # Simulate the passage of 1 second in the clinic for the current patient

    # Calculate the average wait time in minutes
    averageWaitTime = sum(waitingTime) / len(waitingTime) / 60
    # Print the average wait time and the number of remaining patients in the queue
    print(f'average wait time: {averageWaitTime:.2f} minutes, remaining patients: {patientqueue.size()}')

# Run simulations for Age/5 and Age/10 ten times each
print("In case of (Age/5): ")
for i in range(10):
    simulation(4, 5)  # Simulate with a total time of 4 hours and a patient rate of 5

print("#" * 60)

print("In case of (Age/10): ")
for i in range(10):
    simulation(4, 10)  # Simulate with a total time of 4 hours a
