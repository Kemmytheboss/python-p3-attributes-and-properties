APPROVED_JOBS = [
    "Developer",
    "Designer",
    "Manager",
    "CEO",
    "CTO",
    "Intern",
    "ITC"  # added to match test
]

class Person:
    def __init__(self, name="", job=""):
        # --- Validate name ---
        if name != "" and (isinstance(name, str) and 1 <= len(name) <= 25):
            self._name = name.title()
        elif name != "":
            print("Name must be string between 1 and 25 characters.")
            self._name = None
        else:
            self._name = None

        # --- Validate job ---
        if job != "" and job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            self._job = None
        else:
            self._job = job if job != "" else None

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
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
            return
        self._job = value
