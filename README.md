# The World — Wednesday 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Sepsdeod/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Sepsdeod/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A newspaper-style front-page poster summing up the world's news of
**Wednesday 18 November 2026** in one image. Lead story: the Gulf flares
again — Iranian drones target a US radar base in Bahrain, and US jets
answer with a strike on a Revolutionary Guard missile site on Qeshm
Island. Also covered: Trump's arrival in Manila for Quad talks, Nvidia's
board ruling out Jensen Huang's return as CEO, Ukraine striking the
Kerch bridge for a second day, Cyclone Akvan bearing down on the Bay of
Bengal, and MS Dhoni ending his IPL playing career — plus the EU's
planned €45bn Ukraine loan, sanctions on West Bank settlement firms,
and Estonia's planned closure of its Russia border.

The poster is drawn programmatically by `draw.py` (Python PIL:
typography, rules and simple shapes only — no photos, no copied art)
and shipped as `entry.png`. `main.ts` (Node 22, stdlib only) copies it
to the output directory, byte for byte, every run.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

This writes `out/entry.png` (1024×1024 PNG).
