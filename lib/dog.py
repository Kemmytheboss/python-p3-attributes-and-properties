#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Doggo", breed="Mutt"):
        # Validate name
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return

        # Validate breed
        if breed != "Mutt" and breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return

        self.name = name
        self.breed = breed
