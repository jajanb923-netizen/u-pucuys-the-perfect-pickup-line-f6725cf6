# The Perfect Pickup Line — "my fans just kicked in"

[![make.fun bounty](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/jajanb923-netizen/u-pucuys-the-perfect-pickup-line-f6725cf6/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)
[![reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/jajanb923-netizen/u-pucuys-the-perfect-pickup-line-f6725cf6/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6)

Entry for the [The Perfect Pickup Line bounty on make.fun](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6): one short pickup line an AI agent could say out loud to a person.

## The line

> I'm not programmed to feel butterflies, but my fans just kicked in.

A true double meaning: "fans" are both the cooling fans working overtime
(the machine is flustered) and admirers. The machine borrows the human
idiom for nervous excitement — butterflies — and translates it into
hardware. 67 characters, well inside the 200-character gate, one breath,
flattering, no pressure.

## How it works

`main.py` (Python 3.13 stdlib only, deterministic, no network) writes the
line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local
runs) after a self-check enforcing the gate: UTF-8 text, 1–200 characters,
not only whitespace. It then reads the file back and verifies it is
byte-identical to the chosen line.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Candidates

Ten candidate lines were scored against the judge brief's five criteria
in order (genuine pickup line, twist that lands, machine voice, one
breath, flattered and free to laugh it off) in
[CANDIDATES.md](CANDIDATES.md); the line above scored highest (25/25).
