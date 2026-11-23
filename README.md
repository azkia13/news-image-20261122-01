# news-image-20261122-01

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122)
[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122)
[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/c/news-image-20261122)

One image summing up the world news of **Sunday 22 November 2026**,
for the [make.fun news-image-20261122](https://make.fun/c/news-image-20261122)
bounty ($100 prize, free entry).

## The day in the picture

- **Lead — COP31 collapses, no deal.** After two days of overtime in
  Antalya, the climate summit ends with no agreement — the longest UN
  climate talks on record. The EU and about 130 parties rejected a draft
  that never mentioned fossil fuels.
- **Drone hits flats near Kyiv** — a Russian drone partly destroys a
  five-storey block in Dymer; Zelensky says 14 people are missing.
- **Russian warship hit in Libya** — suspected Ukrainian sea drones hit
  the corvette Merkury at Benghazi; a second, Maltese-flagged ship is
  hit offshore.
- **Gulf strikes spread** — Iran hits a civilian site in Bahrain (two
  hurt, one critically); Houthis say they struck the Rabigh refinery.
- **Democrats' biggest House win since 1992** — a recount win in North
  Carolina gives them at least 258 seats.
- **AI sell-off deepens** — S&P 500 −3.7%, Nikkei −5.1% as Nvidia slides
  on reports of an SEC accounting inquiry.
- **Mexico captures 'El Chapo Isidro'** — FBI most-wanted cartel boss
  Fausto Isidro Meza Flores is seized in Sinaloa.
- **BepiColombo reaches Mercury** — after eight years, the ESA–JAXA
  craft enters Mercury orbit, only the second mission to do so.
- **World chess title match begins** — Gukesh vs Sindarov.
- **Also today:** the Banten candy factory fire, the Nigeria boat
  disaster, West Bank settler attacks, the EU–Indonesia trade deal,
  a CRISPR cholesterol result, and more.

Every fact was checked against live reporting (AP, Reuters, BBC and
others) before drawing. Where sources conflicted, no number is stated:
no single death toll for Dymer or for the Sinaloa operation, no
body-bag count for the Banten fire, and the Benghazi corvette is
described only as "hit", not sunk.

## How it works

`draw_front.py` (Python + Pillow) drew `entry.png` (1024×1024,
deterministic, no network) at build time. `main.py` — standard library
only — just copies `entry.png` to `MAKEFUN_OUTPUT_DIR` (or `/output`)
and verifies the size and PNG header.

```sh
python3 draw_front.py   # regenerate entry.png
python3 -P -s main.py   # copy it to the output directory
```

## License

MIT — see [LICENSE](LICENSE).
