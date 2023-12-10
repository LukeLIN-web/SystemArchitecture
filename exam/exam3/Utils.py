from enum import IntEnum, Enum

class Size(IntEnum):
    B = 1
    KB = 1024
    MB = 1024 ** 2
    GB = 1024 ** 3


class Associativity(Enum):
    DirectMapped = 1
    FullyAssociative = 2
    SetAssociative = 3


class CacheReplaceAlgorithm(Enum):
    LRU = 1
    FIFO = 2
    Random = 3


class OP(Enum):
    MemoryRead = 0
    MemoryWrite = 1
    InstructionFetch = 2
    Ignore = 3
    Flush = 4


class CacheLevel(Enum):
    L1 = 1
    L2 = 2
    NoCache = 0