import re

from typing import List


# Splits a sentence into segments. For example, "Hi, what's hash table?" would
# turn into ["Hi" "what's hash table"]
def parse(sentence: str) -> List[str]:
    segments: List[str] = re.split(r"[,.?!]+", sentence)
    segments = [segment.strip() for segment in segments if segment.strip()]
    return segments


def is_question(question: str) -> bool:
    indicators: List[str] = [
        "why",
        "what",
        "who",
        "whose",
        "which",
        "when",
        "where",
        "how",
    ]

    ret: bool = False
    if "?" in question.lower():
        ret = True
    else:
        for segment in parse(question.lower()):
            if any(word == segment.split()[0] for word in indicators):
                ret = True
                break

    return ret
