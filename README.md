# Boundary Between Wave and Particle

An interactive particle visualization showing how a smooth wave-like pattern can emerge from fully discrete bullet particles.

[![Live Demo](https://img.shields.io/badge/live-demo-brightgreen?logo=githubpages)](https://xavierfan0413.github.io/boundary-wave-particle-demo/web/index.html)
![Status](https://img.shields.io/badge/status-v1%20compact%20demo-0969da)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Live demo: https://xavierfan0413.github.io/boundary-wave-particle-demo/web/index.html

![Wave-particle demo preview](docs/assets/WP.gif)

## What This Project Is

This is a compact showcase project with two implementations of the same simulation concept:

- Python desktop demo for local exploration
- Browser demo for sharing and interactive play

The implementations do not share runtime code. They share a documented simulation model.

## Why This Is Interesting

- It demonstrates emergence: continuous-looking structure from simple discrete agents.
- It stays minimal: a small parameterized system can still produce rich visual behavior.
- It is interactive: you can adjust parameters in real time and immediately see pattern changes.

## Technical Highlights

- Two implementations of one concept: `python/` and `web/`.
- Shared model specification in [`docs/model.md`](docs/model.md).
- Real-time parameter controls (`ways`, `alpha`, `emit cadence`, speed, spawn radius, lifetime).
- Phase-driven radial emission with simple deterministic update rules.
- Optional lightweight play-mode interaction in the web demo.

## How It Works (High Level)

1. Keep simulation state: frame, phase, and active bullets.
2. On each frame, advance phase with `phase += frame * alpha`.
3. Every `emit_every` frames, emit `ways` bullets around a spawn ring.
4. Move bullets with constant velocity, age them, and cull by lifetime and bounds.
5. Render positions with implementation-specific visuals (Python scatter vs web canvas effects).

Full conceptual contract: [`docs/model.md`](docs/model.md).

## Project Structure

```text
.
├─ docs/
│  ├─ assets/
│  │  └─ WP.gif
│  └─ model.md
├─ python/
│  ├─ __init__.py
│  └─ boundary_wave_particle_demo.py
├─ web/
│  └─ index.html
├─ boundary_wave_particle_demo.py   # root compatibility entry point
├─ index.html                       # root redirect to web/index.html
├─ requirements.txt
└─ LICENSE
```

## Run Locally

### Python demo

```bash
pip install -r requirements.txt
python boundary_wave_particle_demo.py
```

You can also run the canonical path directly:

```bash
python python/boundary_wave_particle_demo.py
```

### Web demo

Open directly:

- `index.html` (redirects)
- `web/index.html` (direct entry)

Or serve locally:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000/web/index.html`.

## Model Alignment And Parity

- Expected: conceptual parity across Python and Web.
- Not expected: exact frame-by-frame visual parity.

Python and Web use different rendering/UI systems and parameter ranges, but follow the same core simulation model.

## Inspiration And Scope

Inspired by Touhou-style bullet pattern aesthetics, but presented primarily as a computational visualization study.

This project is a conceptual reconstruction for learning and demo purposes, not a source-level recreation of any original game implementation.

## License

MIT License.
