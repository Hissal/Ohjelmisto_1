import inputHandler

GENDER_MALE = ("m","male", "man", "mies", "alfa")
GENDER_FEMALE = ("f", "female", "w", "woman", "n", "nainen")

LEGAL_GENDERS = [*GENDER_MALE, *GENDER_FEMALE]

def isMale(genderStr: str) -> bool:
    return genderStr in GENDER_MALE

def isFemale(genderStr: str) -> bool:
    return genderStr in GENDER_FEMALE

def printForMale(hemoglobin: float):
    if hemoglobin < 134:
        print("Hemoglobin is under the normal range for men.")
    elif hemoglobin > 195:
        print("Hemoglobin is over the normal range for men.")
    else:
        print("Hemoglobin is within the normal range for men.")

def printForFemale(hemoglobin: float):
    if hemoglobin < 117:
        print("Hemoglobin is under the normal range for women.")
    elif hemoglobin > 175:
        print("Hemoglobin is over the normal range for women.")
    else:
        print("Hemoglobin is within the normal range for women.")

genderInput = inputHandler.getStringInputLowercased(LEGAL_GENDERS, "Input Gender: ", "Invalid input. Please enter a valid gender")
hemoglobinInput = inputHandler.getFloatInput("Input Hemoglobin: ", "Invalid input. Please enter a valid number")

if isMale(genderInput):
    printForMale(hemoglobinInput)
elif isFemale(genderInput):
    printForFemale(hemoglobinInput)
else:
    raise ValueError("Invalid input. Please enter a valid gender")