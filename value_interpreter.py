from enum import IntEnum

class GasLevel(IntEnum):
    SAFE = 0
    CAUTION = 1
    HAZARDOUS = 2
    CRITICAL = 3

class ValueInterpreter:

    @staticmethod
    def interpret_values_for_mq2(value):
        if 200 <= value <= 600:
            return GasLevel.SAFE
        elif 601 <= value <= 1200:
            return GasLevel.CAUTION
        elif 1201 <= value <= 2000:
            return GasLevel.HAZARDOUS
        elif value > 2000:
            return GasLevel.CRITICAL
        else: # This should never happen
            return GasLevel.SAFE

    @staticmethod
    def interpret_values_for_mq3(value):
        if 100 <= value <= 500:
            return GasLevel.SAFE
        elif 501 <= value <= 1000:
            return GasLevel.CAUTION
        elif 1001 <= value <= 1800:
            return GasLevel.HAZARDOUS
        elif value > 1800:
            return GasLevel.CRITICAL
        else:  # This should never happen
            return GasLevel.SAFE

    @staticmethod
    def interpret_values_for_mq135(value):
        if 150 <= value <= 700:
            return GasLevel.SAFE
        elif 701 <= value <= 1400:
            return GasLevel.CAUTION
        elif 1401 <= value <= 2200:
            return GasLevel.HAZARDOUS
        elif value > 2200:
            return GasLevel.CRITICAL
        else: # This should never happen
            return GasLevel.SAFE