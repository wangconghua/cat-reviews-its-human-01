#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human — a one-star review written
by a house cat about its human owner.

The joke: the human buys expensive food, then watches the cat eat the plastic
bag it came in — and the cat's verdict is that the bag was better and it
would order the bag again. A deadpan one-star review shape, a specific
complaint, the human judged by cat standards, and the sting lands in the
last sentence, which reveals more about the cat than the owner.
"""

import os

REVIEW = "One star. He buys the expensive food, then watches me eat the plastic bag it came in. The bag was better. I would order the bag again."

OUT_PATH = "/output/entry.txt"

# Words that explain the joke instead of being the joke. A funny line must
# land on its own; if it has to say it is funny, it is not.
META_HUMOR_WORDS = ("funny", "joke", "haha", "lol", "hilarious")

# Worn cat jokes the judge has heard a thousand times: knocked glasses off
# tables, laser pointers, catnip, meowing about it, nine lives.
WORN_CAT_CLICHES = (
    "knocked it off the table",
    "knocked the glass",
    "laser pointer",
    "catnip",
    "meow",
    "as a cat",
    "nine lives",
    "9 lives",
)

# Concrete, recognisable cat-world things a real complaint is about: the
# food bowl, the closed door, the laptop keyboard, the bag, the sunbeam.
COMPLAINT_OBJECTS = (
    "food", "bowl", "bag", "keyboard", "door", "sunbeam",
    "chair", "bed", "treat", "litter",
)

# Review-shaped verdict words: the last sentence must hand down a judgement,
# the way a real one-star review ends.
VERDICT_WORDS = ("again", "better", "never", "still", "refund", "zero")


def validate(review: str) -> None:
    # The gate: one line of 1-200 characters, not only whitespace.
    if not (1 <= len(review) <= 200) or review.isspace() or "\n" in review:
        raise ValueError("entry must be one line of 1-200 characters, not only whitespace")
    if review != review.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in review:
        raise ValueError("entry must not contain double spaces")
    lowered = review.lower()
    # Deadpan shape of a real one-star review: it opens with the rating.
    if not lowered.startswith("one star"):
        raise ValueError("entry must open with the one-star rating, like a real review")
    # The complaint must be specific and recognisable, not vague grumpiness.
    if not any(obj in lowered for obj in COMPLAINT_OBJECTS):
        raise ValueError("entry must name a specific complaint object (food, bowl, bag, keyboard, ...)")
    # Unmistakably feline voice: first person, the human judged by cat standards.
    if "i " not in lowered and not lowered.startswith("i "):
        raise ValueError("entry must be in the cat's own first-person voice")
    if " he " not in lowered and " my " not in lowered:
        raise ValueError("entry must measure the human by cat standards")
    # The sting must land in the last few words: the final sentence hands
    # down a verdict that rewards a second read.
    last_sentence = review.rsplit(".", 1)[0].rsplit(".", 1)[-1].strip().lower()
    if not any(word in last_sentence for word in VERDICT_WORDS):
        raise ValueError("entry's last sentence must hand down a review verdict")
    # No explaining its own joke, and no worn cat cliche.
    for word in META_HUMOR_WORDS:
        if word in lowered:
            raise ValueError(f"entry must not explain its own joke (found {word!r})")
    for cliche in WORN_CAT_CLICHES:
        if cliche in lowered:
            raise ValueError(f"entry must not lean on a worn cat cliche (found {cliche!r})")


def main():
    validate(REVIEW)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
