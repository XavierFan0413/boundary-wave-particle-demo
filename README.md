# Boundary Between Wave and Particle Demo

A small visualization project inspired by Touhou Project spell card design, focused on how a wave-like visual effect can emerge from discrete particles.

This repository currently includes two versions:

- a Python desktop demo for local experimentation
- a mobile-friendly web demo for easy sharing and interactive play

## Included Versions

### 1. Python Desktop Demo

The Python version is useful for local testing and parameter exploration with a desktop GUI.

File:

```text
boundary_wave_particle_demo.py
```

Requirements:

- Python 3
- matplotlib
- numpy

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
python boundary_wave_particle_demo.py
```

### 2. Web Demo

The web version is designed for phone and desktop browsers, with a cleaner interface for sharing and casual interaction.

File:

```text
index.html
```

If GitHub Pages is enabled for this repository, the web demo can be opened directly in a browser without installing anything.

## Web Demo Features

- bilingual interface with English and Chinese toggle
- collapsible mobile-friendly control panel
- real-time parameter adjustment
- presets for different visual moods
- optional play mode with cursor or touch-based collision
- lightweight single-file implementation with no external dependencies

## Main Web Controls

- language toggle: `EN` / `中`
- play mode toggle
- pause
- reset
- presets such as dreamy and calm

Adjustable parameters include:

- ways
- alpha
- emit interval
- bullet speed
- spawn radius
- lifetime

## What This Demonstrates

This project explores how a continuous-looking wave pattern can be produced entirely from discrete moving particles.

By changing the emission angle over time, the particles can form structures that visually resemble smooth rotating wavefronts, even though the system itself remains fully particle-based.

## Notes

This is a conceptual reconstruction for learning and visualization. It is not a source-level recreation of the original Touhou implementation.

## License

This repository's source code is licensed under the MIT License.