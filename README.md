# Two Robots in an Elevator

One funny line of awkward small talk that one robot says to another
while riding an elevator together.

## The line

> So… we both pressed 7. My sensors say 0.3% coincidence. My fan says act normal.

79 characters, one line.

## Why this line

- **It is elevator small talk.** Two robots discover they both pressed
  the same floor, and neither knows what to say about it.
- **Machine logic shows through.** The speaker checks its sensors,
  quotes a probability (0.3% coincidence), and even its cooling fan
  gets a vote.
- **The awkwardness lands.** The line opens with a hesitant "So…",
  then the fan — the anxious, overheating part of the robot — tells it
  to act normal. That is the thing neither robot wants to name: they
  are both quietly panicking about a shared ride.
- **It is tight.** Every word earns its place; there is no setup
  wasted on a stale pun.

## How to run

```sh
python3 main.py
```

This writes `/output/entry.txt` containing exactly the line above.

To write somewhere else (for example while testing locally), set
`OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## Determinism

The program writes a fixed string. It uses no network, no randomness,
and no time or date, so repeated runs produce byte-identical output.
Verified locally: two separate runs produced identical `entry.txt`
files with matching SHA-256 digests.
