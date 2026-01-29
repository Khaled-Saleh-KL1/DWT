# Enums in Python are used to define a set of named constant values. 
# They make code cleaner, more readable and prevent using invalid 
# values. Each member of an Enum has a name and a value 
#       -- GeeksforGeeks

from enum import Enum

class LLMEnum(Enum):
    MAX_NEW_TOKENS = 265
    TEMPERATRUE = 0.7
    TOP_P = 0.3
    DO_SAMPLE = True