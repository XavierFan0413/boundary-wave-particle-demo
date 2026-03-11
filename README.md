# Boundary Between Wave and Particle Demo

A small Python visualization inspired by Touhou Project spell card design, especially the idea of creating a wave-like visual effect from discrete particles.

## Features

- Animated particle-based wave pattern
- Adjustable parameters such as ways, angular acceleration, and emission interval
- Simple keyboard controls for pause, reset, save snapshot, and quit

## Requirements

- Python 3
- matplotlib
- numpy

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python boundary_wave_particle_demo.py
```

You can also try custom parameters:

```bash
python boundary_wave_particle_demo.py --ways 8 --emit-every 1 --alpha 0.003
```

## Controls

- `Space`: pause or resume
- `r`: reset
- `s`: save snapshot
- `q`: quit

## Example Parameter Ideas

More particle-like:

```bash
python boundary_wave_particle_demo.py --ways 2 --emit-every 2
```

More wave-like:

```bash
python boundary_wave_particle_demo.py --ways 8 --emit-every 1
```

More hypnotic and dense:

```bash
python boundary_wave_particle_demo.py --ways 8 --emit-every 1 --alpha 0.003
```

## Notes

This is a conceptual reconstruction for learning and visualization. It is not a source-level recreation of the original Touhou implementation.

## License

This repository's source code is licensed under the MIT License.