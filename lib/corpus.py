import string
import random
import math
from typing import List


def corpus() -> list[str]:
    """
    Defines a simple corpus for sample text generation. azAZ09+punctuation. No unicode/etc.
    """
    corpus = []
    corpus.extend(list(string.ascii_letters))
    corpus.extend(list(string.digits))
    corpus.extend(list(string.punctuation))
    corpus.extend([" ", "\n"])
    return corpus
