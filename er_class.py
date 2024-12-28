import random

class Emergency:
    patient = []
    triage = []
    directory = {}
    appointment = {}
    patients = []
    sort_values = {}

    def arrive(self, person):
        self.patient.append(person)
        self.triage.append(random.randint(0, 10))
        return self.patient

    def schedule(self):
        for index in range(len(self.patient)):
            self.directory[self.patient[index]] = self.triage[index]

        self.sort_values = sorted(self.directory.values())
        for i in self.sort_values:
            for j in self.directory.keys():
                if self.directory[j] == i:
                    self.appointment[j] = self.directory[j]

        print("\nPRIORITY APPOINTMENTS\n--------------")
        for key, value in self.appointment.items():
            print("Patient:", key, "\t Priority Level:", value)

        self.patients = list(self.appointment.keys())
        return self.patients, self.appointment

    def announce(self):
        del self.appointment[next(iter(self.appointment))]
        self.patients.pop(0)
        print("\nUPDATED APPOINTMENTS\n--------------")
        for key, value in self.appointment.items():
            print("Patient:", key, "\t Priority Level:", value)
        print("------------\nANNOUNCEMENT: Calling for", self.patients[0], "\n------------",)

        return self.appointment
