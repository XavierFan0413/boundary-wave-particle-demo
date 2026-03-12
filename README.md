# Boundary Between Wave and Particle

Compact demo/research project showing how a wave-like visual structure can emerge from discrete particles.

This repository contains two implementations of the same conceptual simulation:

- Python desktop demo (local exploration)
- Web demo (browser/mobile sharing)

They are not a shared runtime codebase. They are conceptually aligned implementations.

## Concept Source Of Truth

The simulation model and alignment contract live in:

- `docs/model.md`

Use that document as the reference when changing either implementation.

## Repository Layout

```text
.
├─ docs/
│  └─ model.md
├─ python/
│  ├─ __init__.py
│  └─ boundary_wave_particle_demo.py
├─ web/
│  └─ index.html
├─ boundary_wave_particle_demo.py   # compatibility entry point
├─ index.html                       # redirects to web/index.html
├─ requirements.txt
└─ LICENSE
```

## Implementation Roles

### Python Demo

- Purpose: desktop-oriented parameter exploration and quick local experimentation.
- Canonical file: `python/boundary_wave_particle_demo.py`
- Compatibility entry point: `boundary_wave_particle_demo.py`

### Web Demo

- Purpose: easy sharing, mobile-friendly interaction, and lightweight in-browser usage.
- Canonical file: `web/index.html`
- Root `index.html` redirects to `web/index.html`.

## Parity Expectations

- Expected: conceptual parity (same simulation idea and core update rules).
- Not expected: exact frame-by-frame parity or identical UI/visual effects.

The web implementation includes extra interaction features (for example play mode collision feedback) that are intentionally implementation-specific.

## Run

### Python

Requirements:

- Python 3
- matplotlib
- numpy

Install:

```bash
pip install -r requirements.txt
```

Run (either command):

```bash
python boundary_wave_particle_demo.py
```

```bash
python python/boundary_wave_particle_demo.py
```

### Web

Open either file in a browser:

- `index.html` (redirects)
- `web/index.html` (direct)

If GitHub Pages is enabled, serve repository root as usual.

## Notes

This is a conceptual reconstruction for learning and visualization, not a source-level recreation of the original Touhou implementation.

## License

MIT License.
