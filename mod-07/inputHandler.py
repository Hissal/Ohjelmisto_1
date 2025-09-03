import sys
from enum import IntFlag

class StringBuilder:
    def __init__(self) -> None:
        self._strings: list[str] = []

    def append(self, string: str) -> None:
        self._strings.append(string)

    def toString(self) -> str:
        return ''.join(self._strings)

class InputFlags(IntFlag):
    NONE = 0
    POSITIVE = 1
    NON_ZERO = 2

def buildInvalidInputString(valueName: str, max: float, flags: InputFlags) -> str:
    sb = StringBuilder()
    sb.append("Invalid input, please enter a")

    if (flags & InputFlags.POSITIVE):
        sb.append(" positive")

    if (flags & InputFlags.NON_ZERO):
        sb.append(" non zero")

    sb.append(f" {valueName}")

    if max != sys.maxsize:
        sb.append(f" less than or equal to {max}")

    return sb.toString()

def isValidNumber(value: float, max: float, flags: InputFlags) -> bool:
    if value > max:
        return False

    if (flags & InputFlags.POSITIVE) and value < 0:
        return False
    if (flags & InputFlags.NON_ZERO) and value == 0:
        return False
    return True

def getFloatInput(message: str, invalidValueMessage: str = "", max: float = sys.maxsize, flags: InputFlags = InputFlags.NONE) -> float:
    def invalidMessage() -> str:
        if (invalidValueMessage == ""):
            return buildInvalidInputString("number", max, flags)
        return invalidValueMessage

    while True:
        try:
            value = float(input(message))
            if isValidNumber(value, max, flags):
                return value

            print(invalidMessage())
        except ValueError:
            print(invalidMessage())

def getFloatInputOrNone(message: str, invalidValueMessage: str = "", max: float = sys.maxsize, flags: InputFlags = InputFlags.NONE) -> float | None:
    def invalidMessage() -> str:
        if (invalidValueMessage == ""):
            return buildInvalidInputString("number", max, flags)
        return invalidValueMessage

    while True:
        value = input(message)
        if value == "":
            return None
        try:
            value = float(value)
            if isValidNumber(value, max, flags):
                return value

            print(invalidMessage())
        except ValueError:
            print(invalidMessage())
def getIntInput(message: str, invalidValueMessage: str = "", max: int = sys.maxsize, flags: InputFlags = InputFlags.NONE) -> int:
    def invalidMessage() -> str:
        if (invalidValueMessage == ""):
            return buildInvalidInputString("integer", max, flags)
        return invalidValueMessage

    while True:
        try:
            value = int(input(message))
            if isValidNumber(value, max, flags):
                return value

            print(invalidMessage())
        except ValueError:
            print(invalidMessage())

def getIntInputOrNone(message: str, invalidValueMessage: str = "", max: int = sys.maxsize, flags: InputFlags = InputFlags.NONE) -> int | None:
    def invalidMessage() -> str:
        if (invalidValueMessage == ""):
            return buildInvalidInputString("integer", max, flags)
        return invalidValueMessage

    while True:
        value = input(message)
        if value == "":
            return None
        try:
            value = int(value)
            if isValidNumber(value, max, flags):
                return value

            print(invalidMessage())
        except ValueError:
            print(invalidMessage())

def getStringInput(allowedStrings: list[str], message: str, invalidValueMessage: str) -> str:
    while True:
        value = input(message)
        if value in allowedStrings:
            return value
        else:
            print(invalidValueMessage)

def getStringInputLowercased(allowedStrings: list[str], message: str, invalidValueMessage: str) -> str:
    while True:
        value = input(message).lower()
        if value in allowedStrings:
            return value
        else:
            print(invalidValueMessage)