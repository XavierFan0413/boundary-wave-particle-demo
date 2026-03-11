import argparse
import math
from dataclasses import dataclass

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


@dataclass
class Bullet:
    x: float
    y: float
    vx: float
    vy: float
    age: int = 0


class BoundaryWaveParticleDemo:
    def __init__(
        self,
        ways: int = 5,
        alpha: float = math.pi / 1600,
        emit_every: int = 2,
        spawn_radius: float = 0.25,
        bullet_speed: float = 0.035,
        view_radius: float = 8.0,
        max_age: int = 260,
        point_size: float = 14.0,
        interval_ms: int = 30,
    ):
        self.ways = ways
        self.alpha = alpha
        self.emit_every = emit_every
        self.spawn_radius = spawn_radius
        self.bullet_speed = bullet_speed
        self.view_radius = view_radius
        self.max_age = max_age
        self.point_size = point_size
        self.interval_ms = interval_ms

        self.frame = 0
        self.phase = 0.0
        self.bullets = []
        self.paused = False

        self.fig, self.ax = plt.subplots(figsize=(7, 7))
        self.ax.set_aspect("equal")
        self.ax.set_xlim(-self.view_radius, self.view_radius)
        self.ax.set_ylim(-self.view_radius, self.view_radius)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_title(
            "Boundary between Wave and Particle — conceptual Python reconstruction\n"
            "space: pause/resume   r: reset   s: save snapshot   q: quit",
            fontsize=11,
        )

        spawn_ring = plt.Circle(
            (0, 0),
            self.spawn_radius,
            fill=False,
            linestyle="--",
            linewidth=1.0,
            alpha=0.35,
        )
        self.ax.add_patch(spawn_ring)

        self.scatter = self.ax.scatter([], [], s=self.point_size)
        self.info = self.ax.text(
            0.02,
            0.98,
            "",
            transform=self.ax.transAxes,
            va="top",
            ha="left",
            fontsize=10,
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.75),
        )

        self.fig.canvas.mpl_connect("key_press_event", self.on_key)

    def reset(self):
        self.frame = 0
        self.phase = 0.0
        self.bullets = []

    def on_key(self, event):
        if event.key == " ":
            self.paused = not self.paused
        elif event.key == "r":
            self.reset()
        elif event.key == "s":
            path = f"boundary_wave_particle_snapshot_f{self.frame}.png"
            self.fig.savefig(path, dpi=180, bbox_inches="tight")
            print(f"Saved snapshot to {path}")
        elif event.key == "q":
            plt.close(self.fig)

    def emit(self):
        for i in range(self.ways):
            theta = self.phase + i * 2.0 * math.pi / self.ways
            x = self.spawn_radius * math.cos(theta)
            y = self.spawn_radius * math.sin(theta)
            vx = self.bullet_speed * math.cos(theta)
            vy = self.bullet_speed * math.sin(theta)
            self.bullets.append(Bullet(x=x, y=y, vx=vx, vy=vy))

    def step(self):
        self.phase += self.frame * self.alpha

        if self.frame % self.emit_every == 0:
            self.emit()

        new_bullets = []
        limit = self.view_radius + 0.5
        for b in self.bullets:
            b.x += b.vx
            b.y += b.vy
            b.age += 1
            if abs(b.x) <= limit and abs(b.y) <= limit and b.age <= self.max_age:
                new_bullets.append(b)
        self.bullets = new_bullets
        self.frame += 1

    def draw(self):
        if not self.bullets:
            self.scatter.set_offsets(np.empty((0, 2)))
            self.scatter.set_facecolors(np.empty((0, 4)))
            return self.scatter, self.info

        xy = np.array([(b.x, b.y) for b in self.bullets], dtype=float)
        ages = np.array([b.age for b in self.bullets], dtype=float)

        age_norm = np.clip(1.0 - ages / self.max_age, 0.0, 1.0)
        rgba = np.zeros((len(self.bullets), 4), dtype=float)
        rgba[:, 0] = 0.1 + 0.9 * age_norm
        rgba[:, 1] = 0.2 + 0.6 * age_norm
        rgba[:, 2] = 0.9
        rgba[:, 3] = 0.08 + 0.92 * age_norm

        self.scatter.set_offsets(xy)
        self.scatter.set_facecolors(rgba)
        self.scatter.set_edgecolors("none")

        ang_vel = self.frame * self.alpha
        self.info.set_text(
            f"frame = {self.frame}\n"
            f"bullets = {len(self.bullets)}\n"
            f"ways = {self.ways}\n"
            f"alpha = {self.alpha:.6f} rad/frame²\n"
            f"instant angular speed ≈ {ang_vel:.4f} rad/frame"
        )
        return self.scatter, self.info

    def update(self, _):
        if not self.paused:
            self.step()
        return self.draw()

    def run(self):
        self.anim = FuncAnimation(
            self.fig,
            self.update,
            interval=self.interval_ms,
            blit=False,
            cache_frame_data=False,
        )
        plt.show()


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Conceptual Python reconstruction of Touhou's 'Boundary between Wave and Particle'."
    )
    p.add_argument("--ways", type=int, default=5, help="number of simultaneous radial streams")
    p.add_argument("--alpha", type=float, default=math.pi / 1600, help="angular acceleration term")
    p.add_argument("--emit-every", type=int, default=2, help="emit bullets every N frames")
    p.add_argument("--spawn-radius", type=float, default=0.25, help="radius of the emission ring")
    p.add_argument("--bullet-speed", type=float, default=0.035, help="radial bullet speed")
    p.add_argument("--view-radius", type=float, default=8.0, help="plot window half-width")
    p.add_argument("--max-age", type=int, default=260, help="maximum bullet lifetime in frames")
    p.add_argument("--point-size", type=float, default=14.0, help="marker size for bullets")
    p.add_argument("--interval-ms", type=int, default=30, help="animation frame interval in milliseconds")
    return p


def main():
    args = build_parser().parse_args()
    demo = BoundaryWaveParticleDemo(
        ways=args.ways,
        alpha=args.alpha,
        emit_every=args.emit_every,
        spawn_radius=args.spawn_radius,
        bullet_speed=args.bullet_speed,
        view_radius=args.view_radius,
        max_age=args.max_age,
        point_size=args.point_size,
        interval_ms=args.interval_ms,
    )
    demo.run()


if __name__ == "__main__":
    main()