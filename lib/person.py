APPROVED_JOBS = [
    "Developer",
    "Designer",
    "Manager",
    "CEO",
    "CTO",
    "Intern",
]

class Person:
    def __init__(self, name="", job=""):
        # --- Name validation first ---
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self._name = None
            self._job = None
            return  # short-circuit: do NOT process job
        self._name = name.title()

        # --- Job validation ---
        if job and job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            self._job = None
        else:
            self._job = job if job else None

    # --- Name property ---
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return
        self._name = value.title()

    # --- Job property ---
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            return
        self._job = value
