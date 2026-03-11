# Boundary Between Wave and Particle Demo

A small visualization project inspired by Touhou Project spell card design, especially the idea of creating a wave-like visual effect from discrete particles.

This repository now includes two versions:

- a Python desktop demo for local experimentation
- a mobile-friendly web demo for easy sharing

## Versions

### 1. Python Desktop Demo

The Python version is useful for local testing and interactive parameter exploration with a desktop GUI.

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

### 2. Mobile-Friendly Web Demo

The web version is designed for quick access on phone or desktop browser.

File:

```text
index.html
```

You can open it locally in a browser, or publish it with GitHub Pages.

## Web Demo Controls

Buttons:

- Pause
- Reset
- Dreamy

Sliders:

- ways
- alpha
- emit
- speed
- spawn
- lifetime

## What This Demonstrates

This project explores how a pattern made entirely of discrete particles can appear wave-like when emitted with a changing angular phase.

Even though the system only contains individual particles, the overall structure can visually resemble a continuous wavefront.

## Notes

This is a conceptual reconstruction for learning and visualization. It is not a source-level recreation of the original Touhou implementation.

## License

This repository's source code is licensed under the MIT License.