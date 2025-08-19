import inputHandler

CLASS_LUX = "LUX"
CLASS_A = "A"
CLASS_B = "B"
CLASS_C = "C"

CABIN_CLASSES = [CLASS_LUX, CLASS_A, CLASS_B, CLASS_C]

cabinClassInput = inputHandler.getStringInput(CABIN_CLASSES, "Choose a cabin class (LUX, A, B, C): ", "Virheellinen hyttiluokka. Valitse LUX, A, B tai C.")

if cabinClassInput == CLASS_LUX:
    print("LUX on parvekkeellinen hytti yläkannella.")
elif cabinClassInput == CLASS_A:
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif cabinClassInput == CLASS_B:
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif cabinClassInput == CLASS_C:
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
