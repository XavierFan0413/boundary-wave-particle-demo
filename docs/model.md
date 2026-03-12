# Shared Simulation Model

This project visualizes how a wave-like pattern can emerge from discrete particles.

The repository has two implementations:

- Python desktop demo (`python/boundary_wave_particle_demo.py`)
- Web browser demo (`web/index.html`)

They do not share runtime code. They do share a conceptual simulation model, defined here.

## 1. Scope

This document is the conceptual source of truth for:

- core simulation state
- simulation parameters
- per-frame update rules
- emission rules
- which concepts must remain aligned across implementations

## 2. Core State

At simulation level, both implementations track:

- `frame`: integer simulation step counter
- `phase`: angular phase used for emission direction
- `bullets`: list of particles
  - each bullet has `(x, y)` position
  - each bullet has `(vx, vy)` velocity
  - each bullet has `age` in frames

## 3. Core Parameters

Shared conceptual parameters:

- `ways`: number of streams emitted per emission event
- `alpha`: phase growth factor controlling angular twist over time
- `emit_every`: emit cadence in frames
- `bullet_speed`: speed magnitude at spawn
- `spawn_radius`: radius of emission ring
- `lifetime`: maximum bullet age before removal

Implementation naming:

| Concept | Python name | Web name |
| --- | --- | --- |
| streams count | `ways` | `ways` |
| phase growth factor | `alpha` | `alpha` (derived from slider via cubic mapping) |
| emit cadence | `emit_every` | `emitEvery` |
| speed | `bullet_speed` | `bulletSpeed` |
| spawn ring | `spawn_radius` | `spawnRadius` |
| bullet lifetime | `max_age` | `lifetime` |

## 4. Emission Rule

When emission is triggered, emit `ways` bullets at evenly spaced angles:

- `theta_i = phase + i * (2*pi / ways)` for `i in [0, ways-1]`
- spawn position:
  - `x = center_x + spawn_radius * cos(theta_i)`
  - `y = center_y + spawn_radius * sin(theta_i)`
- initial velocity:
  - `vx = bullet_speed * cos(theta_i)`
  - `vy = bullet_speed * sin(theta_i)`
- `age = 0`

In Python, center is world origin `(0, 0)`.
In Web, center is screen-based `(cx, cy)`.

## 5. Frame Update Rule

Per simulation frame:

1. Update phase:
   - `phase = phase + frame * alpha`
2. If `frame % emit_every == 0`, run emission.
3. For each bullet:
   - `x = x + vx`
   - `y = y + vy`
   - `age = age + 1`
4. Remove bullets that violate lifetime or view bounds.
5. Increment frame:
   - `frame = frame + 1`

Important: the order above is part of the conceptual contract.

## 6. Simulation vs Rendering

Simulation concerns:

- state transitions in Sections 2-5
- parameter semantics
- bullet lifecycle rules

Rendering concerns:

- camera/view coordinate mapping
- color, glow, alpha curves, point size
- UI widgets and labels
- interaction affordances (keyboard, touch, play mode)

Rendering may differ by implementation as long as simulation semantics remain recognizable.

## 7. Alignment Contract

Must stay conceptually aligned:

- particle-based emission from a rotating phase
- same emission topology (`ways` evenly distributed angles)
- same phase progression form (`phase += frame * alpha`)
- same bullet kinematics (constant velocity after spawn)
- age-based lifetime culling

Allowed to differ:

- units and coordinate systems (world units vs pixels)
- parameter ranges and UI mapping
- visual styling and effects
- additional non-core gameplay/UI features (for example, web play mode collisions)
- viewport culling margins

## 8. Lightweight Parity Checklist

When changing one implementation, sanity-check the other with:

1. Low `alpha` + low `ways` should produce slowly twisting radial streams.
2. Increasing `ways` should increase simultaneous stream count.
3. Increasing `emit_every` should reduce bullet density.
4. Increasing `bullet_speed` should expand the pattern faster.
5. Increasing lifetime should leave more historical trails on screen.

Exact frame-by-frame identity is not required. Qualitative behavior should remain aligned.
