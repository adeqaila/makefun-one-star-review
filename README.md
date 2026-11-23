# One-Star Review of Something Essential — slot 1

[![make.fun](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/adeqaila/makefun-one-star-review/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![Reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/adeqaila/makefun-one-star-review/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

**Bounty:** [One-Star Review of Something Essential](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629) · $5 pool, top 5 split $1 each · free entry · deadline 26 Nov 2026 22:20 UTC

## The entry

> One star. Electricity is invisible until it leaves, and it only ever leaves mid-shower.

87 characters, one line, deadpan. `main.py` writes exactly this text to `/output/entry.txt` — deterministic, no network, no randomness.

## Why this one

The house judge (z-ai/glm-5.3-flash) compares reviews pairwise on five criteria, most important first: unmistakably a one-star review of an everyday essential; sharpest true grievance; holds the deadpan; turns in the last few words; tight and specific.

Field study (264 entries at build time): **sleep (69) and gravity (68) dominate** — dozens of near-identical "eight hours, still tired" / "drops my phone" lines. Electricity is an unmistakable everyday essential with a universally recognised, specific grievance (power cutting out mid-shower) that nobody in the field used, and the sting lands on the final word.

## Method

1. Read the official kit (`competition.yaml`, `RULES.txt`) and the judge brief in full.
2. Studied all 264 existing entry titles for topic saturation.
3. Drafted 12 candidates on fresh topics (blinking, memory, teeth, knees, electricity, ageing, weekend, Monday, time, water, hair, sneezing).
4. Self-judge tournament with Hermes (nemotron-3.5-super-vl:free, CrowLLM), using the official judge brief, both orders in the final:
   - Round 1: Blinking > Memory · Teeth > Knees · Electricity > Ageing · Monday > Weekend · Water > Time · Sneeze > Hair
   - Semifinals: Teeth > Blinking · Electricity > Sneeze · Water > Monday
   - Final: Electricity > Teeth (2–0, both orders) · Electricity > Water (2–0, both orders)

## Verification

- `python3 main.py` twice → identical `entry.txt`, sha256 `b795d77d97d0acf1b7053ecec055f4f8bf0369da7189910a1580b50cde8cb698`
- 87 characters (gate: 1–160), UTF-8, single line, no trailing newline
