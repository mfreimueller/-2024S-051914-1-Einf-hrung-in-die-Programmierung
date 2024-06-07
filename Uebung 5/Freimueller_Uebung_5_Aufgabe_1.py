workshop1 = ["Anna", "Ben", "Clara", "David", "Eva"]
workshop2 = ["Frank", "Clara", "Ben", "George", "Hanna"]

unique_participants = set(workshop1) | set(workshop2)
shared_participants = set(workshop1) & set(workshop2)
exclusive_participants = (set(workshop1) - set(workshop2)) | (set(workshop2) - set(workshop1))

print("Einzigartige Teilnehmer:", sorted(unique_participants))
print("Teilnehmer an beiden Workshops:", sorted(shared_participants))
print("Teilnehmer, die nur an einem Workshop teilgenommen haben:", sorted(exclusive_participants))