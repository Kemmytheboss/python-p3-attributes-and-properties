# lib/person.py

approved_jobs = [
    "Admin",
    "Customer Service",
    "Finance",
    "General Management",
    "Human Resources",
    "ITC",
    "Legal",
    "Marketing",
    "Production",
    "Purchasing",
    "Research & Development",
    "Sales"
]

class Person:
    def __init__(self, name=None, job=None):
        if job is not None:
            self.job = job
        if name is not None:
            self.name = name


    # --- Name property ---
    @property
    def name(self):
        return getattr(self, "_name", None)

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return
        self._name = value.title()

    # --- Job property ---
    @property
    def job(self):
        return getattr(self, "_job", None)

    @job.setter
    def job(self, value):
        if value and value not in approved_jobs:
            print("Job must be in list of approved jobs.")
            return
        self._job = value if value else None
