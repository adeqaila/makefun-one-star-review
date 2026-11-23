#!/usr/bin/env python3
"""One-Star Review of Something Essential — slot 1 entry.

Writes a single deadpan one-star review (87 characters, one line) of an
everyday essential to /output/entry.txt.

The review was chosen from 12 candidates by a self-judge tournament
(Hermes/nemotron, official judge brief, both orders in the final):
electricity beat water 2-0. Electricity is an unmistakable everyday
essential, the grievance (power cutting out mid-shower) is universally
recognised, it holds the deadpan, and the sting lands on the final word.
"""

import os

REVIEW = "One star. Electricity is invisible until it leaves, and it only ever leaves mid-shower."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate rejects anything outside 1-160 characters, so fail loudly
    # here instead of writing an invalid entry.
    assert 1 <= len(REVIEW) <= 160, f"review is {len(REVIEW)} chars, must be 1-160"
    assert REVIEW == REVIEW.strip(), "review must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
