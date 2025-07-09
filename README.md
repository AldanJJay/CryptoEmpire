# CryptoEmpire

*A Bitcoin‑driven, real‑time 4X strategy game built on a fork of **Microcosm** (Pyxel/Python).*
This repository accompanies **Paper 1 – “Real‑Time Financial 4X: CryptoEmpire”** and will evolve as development progresses.

---

## 1. Project Vision

CryptoEmpire turns live Bitcoin market data into dynamic gameplay events. Each in‑game turn pulls WebSocket metrics (price, volume, volatility) and maps them to core 4X mechanics—exploration, expansion, exploitation, extermination—creating a living laboratory for robust RL training and financial intuition.

### Key Features

* **Fork of Microcosm**: Compact Python 4X code‑base (Pyxel) reused for rapid prototyping.
* **Real‑Time BTC Bridge**: `bridge/btc_bridge.py` streams Binance data into game state.
* **Market‑Driven Events**: Bull runs, flash crashes, fog‑of‑war density and unit costs all follow the market.
* **Gym API**: `CryptoEmpireEnv` for reinforcement‑learning agents (week 3 deliverable).
* **Reproducible Experiments**: Scripts to replay historical data, log runs, and compute RKE metrics.

For the full development roadmap see **docs/plan.md** (generated from the *Detailed Development Plan v1.2*).

---

## 2. Quick Start

```bash
# 1. Clone fork (requires Git 2.30+)
$ git clone https://github.com/<your‑org>/crypto‑empire.git
$ cd crypto‑empire

# 2. Create virtualenv + install deps
$ python -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt

# 3. Run the game (offline/historical mode)
$ python run_static.py --dataset data/btc_sample.csv

# 4. Live mode (needs internet & WebSocket)
$ python run_dynamic.py --exchange binance --pair BTCUSDT
```

> **Note:** On CI/headless servers we use **Xvfb** to emulate a display for Pyxel. See `.github/workflows/python‑package.yml` for details.

---

## 3. Repository Structure

```
crypto‑empire/
├── microcosm/            # Original game core (forked)
├── bridge/               # btc_bridge + event modifiers
├── experiments/          # Batch runners, analysis notebooks
├── docs/                 # Architecture, mapping spec, plan
├── envs/                 # Gym API implementation
├── tests/                # pytest suites (≥80% coverage target)
└── README.md             # (this file)
```

---

## 4. Contributing

| Step | Action                                                                     |
| ---- | -------------------------------------------------------------------------- |
| 1    | Check **CryptoEmpire\_Task\_Master** in the project canvas for open tasks. |
| 2    | Create a feature branch (`feat/<id>_<short_description>`).                 |
| 3    | Write tests; ensure `pytest` passes locally.                               |
| 4    | Open a Pull Request; link the task ID.                                     |
| 5    | At least one reviewer approval + CI green required before merge.           |

Guidelines will expand in `CONTRIBUTING.md` (Week 1 • Day 5).

---

## 5. Roadmap Snapshot (v1.2)

* **Week 1**: MVP hook `apply_modifiers()`, price→gold mapping, banner events.
* **Week 2**: Live WebSocket integration, performance profiling, code freeze `v1.0‑mvp`.
* **Week 3**: Experiments, RL Gym API, RKE analysis.
* **Week 4**: Paper writing, video demo, final QA.

See *docs/plan.md* and project Gantt for daily granularity.

---

## 6. License

* **Code**: GPL‑3.0 (inherits from Microcosm).
* **Custom assets** (art/audio) reside in `assets/` and may be CC‑BY‑SA 4.0 or proprietary; see individual files.

---

## 7. Acknowledgements

* **Microcosm** by Chris Needham (GPL‑3) – the foundation of our 4X mechanics.
* **Pyxel** by @kitao – minimalistic retro game engine.
* **Binance API** – real‑time BTC market data.

---

*README generated **Day 1** of the project.  Update status badges, installation notes and roadmap as milestones are completed.*
