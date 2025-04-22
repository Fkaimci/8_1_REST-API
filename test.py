from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":
    # Erstellen eines Leistungstests
    supervisor = Supervisor("Franka", "Kaiser")
    subject = Subject("Marius", "Valenta", "male", 19)

    experiment = Experiment("Leistungstest", "2025-04-07")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment)
