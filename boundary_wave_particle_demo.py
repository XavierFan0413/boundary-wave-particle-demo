"""Compatibility entry point.

Canonical Python implementation lives at:
python/boundary_wave_particle_demo.py
"""

def main():
    # Lazy import keeps this wrapper lightweight for tooling/import inspection.
    from python.boundary_wave_particle_demo import main as run_main

    run_main()


if __name__ == "__main__":
    main()
