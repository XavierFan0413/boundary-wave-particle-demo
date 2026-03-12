import math
from dataclasses import dataclass

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button
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

        self.fig = plt.figure(figsize=(10, 11))

        self.ax = self.fig.add_axes([0.10, 0.43, 0.80, 0.50])
        self.ax.set_aspect("equal")
        self.ax.set_xlim(-self.view_radius, self.view_radius)
        self.ax.set_ylim(-self.view_radius, self.view_radius)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_title(
            "Boundary between Wave and Particle — interactive demo\n"
            "space: pause/resume    r: reset    s: save snapshot    q: quit",
            fontsize=12,
            pad=10,
        )

        self.spawn_ring = plt.Circle(
            (0, 0),
            self.spawn_radius,
            fill=False,
            linestyle="--",
            linewidth=1.0,
            alpha=0.35,
        )
        self.ax.add_patch(self.spawn_ring)

        self.scatter = self.ax.scatter([], [], s=self.point_size)

        self.info_ax = self.fig.add_axes([0.10, 0.34, 0.80, 0.07])
        self.info_ax.axis("off")
        self.info = self.info_ax.text(
            0.01,
            0.95,
            "",
            va="top",
            ha="left",
            fontsize=10.5,
            family="monospace",
            bbox=dict(boxstyle="round", facecolor="white", alpha=0.85),
        )

        self._build_controls()
        self.fig.canvas.mpl_connect("key_press_event", self.on_key)

    def _build_controls(self):
        ax_ways = self.fig.add_axes([0.12, 0.25, 0.60, 0.025])
        ax_alpha = self.fig.add_axes([0.12, 0.21, 0.60, 0.025])
        ax_emit = self.fig.add_axes([0.12, 0.17, 0.60, 0.025])
        ax_speed = self.fig.add_axes([0.12, 0.13, 0.60, 0.025])
        ax_spawn = self.fig.add_axes([0.12, 0.09, 0.60, 0.025])

        ax_pause = self.fig.add_axes([0.78, 0.21, 0.12, 0.045])
        ax_reset = self.fig.add_axes([0.78, 0.15, 0.12, 0.045])
        ax_save = self.fig.add_axes([0.78, 0.09, 0.12, 0.045])

        self.slider_ways = Slider(
            ax_ways, "ways", 1, 12, valinit=self.ways, valstep=1
        )
        self.slider_alpha = Slider(
            ax_alpha, "alpha", 0.0002, 0.0080, valinit=self.alpha, valfmt="%.4f"
        )
        self.slider_emit = Slider(
            ax_emit, "emit", 1, 8, valinit=self.emit_every, valstep=1
        )
        self.slider_speed = Slider(
            ax_speed, "speed", 0.005, 0.10, valinit=self.bullet_speed, valfmt="%.3f"
        )
        self.slider_spawn = Slider(
            ax_spawn, "spawn", 0.05, 1.20, valinit=self.spawn_radius, valfmt="%.3f"
        )

        self.button_pause = Button(ax_pause, "Pause")
        self.button_reset = Button(ax_reset, "Reset")
        self.button_save = Button(ax_save, "Save")

        self.slider_ways.on_changed(self.on_slider_change)
        self.slider_alpha.on_changed(self.on_slider_change)
        self.slider_emit.on_changed(self.on_slider_change)
        self.slider_speed.on_changed(self.on_slider_change)
        self.slider_spawn.on_changed(self.on_slider_change)

        self.button_pause.on_clicked(self.on_pause_clicked)
        self.button_reset.on_clicked(self.on_reset_clicked)
        self.button_save.on_clicked(self.on_save_clicked)

    def apply_slider_values(self):
        self.ways = int(self.slider_ways.val)
        self.alpha = float(self.slider_alpha.val)
        self.emit_every = int(self.slider_emit.val)
        self.bullet_speed = float(self.slider_speed.val)
        self.spawn_radius = float(self.slider_spawn.val)
        self.spawn_ring.set_radius(self.spawn_radius)

    def on_slider_change(self, _):
        self.apply_slider_values()
        self.reset()

    def on_pause_clicked(self, _):
        self.paused = not self.paused
        if self.paused:
            self.button_pause.label.set_text("Resume")
        else:
            self.button_pause.label.set_text("Pause")

    def on_reset_clicked(self, _):
        self.reset()

    def on_save_clicked(self, _):
        path = f"boundary_wave_particle_snapshot_f{self.frame}.png"
        self.fig.savefig(path, dpi=180, bbox_inches="tight")
        print(f"Saved snapshot to {path}")

    def reset(self):
        self.frame = 0
        self.phase = 0.0
        self.bullets = []

    def on_key(self, event):
        if event.key == " ":
            self.on_pause_clicked(None)
        elif event.key == "r":
            self.reset()
        elif event.key == "s":
            self.on_save_clicked(None)
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
        self.spawn_ring.set_radius(self.spawn_radius)

        if not self.bullets:
            self.scatter.set_offsets(np.empty((0, 2)))
            self.scatter.set_facecolors(np.empty((0, 4)))
            ang_vel = self.frame * self.alpha
            self.info.set_text(
                f"frame={self.frame}   bullets=0   ways={self.ways}   alpha={self.alpha:.6f}\n"
                f"emit={self.emit_every}   speed={self.bullet_speed:.4f}   "
                f"spawn={self.spawn_radius:.3f}   omega≈{ang_vel:.4f}"
            )
            return self.scatter, self.info, self.spawn_ring

        xy = np.array([(b.x, b.y) for b in self.bullets], dtype=float)
        ages = np.array([b.age for b in self.bullets], dtype=float)

        age_norm = np.clip(1.0 - ages / self.max_age, 0.0, 1.0)
        rgba = np.zeros((len(self.bullets), 4), dtype=float)
        rgba[:, 0] = 0.85
        rgba[:, 1] = 0.55 + 0.20 * age_norm
        rgba[:, 2] = 0.95
        rgba[:, 3] = 0.15 + 0.85 * age_norm

        self.scatter.set_offsets(xy)
        self.scatter.set_facecolors(rgba)
        self.scatter.set_edgecolors("none")

        ang_vel = self.frame * self.alpha
        self.info.set_text(
            f"frame={self.frame}   bullets={len(self.bullets)}   ways={self.ways}   alpha={self.alpha:.6f}\n"
            f"emit={self.emit_every}   speed={self.bullet_speed:.4f}   "
            f"spawn={self.spawn_radius:.3f}   omega≈{ang_vel:.4f}"
        )
        return self.scatter, self.info, self.spawn_ring

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


def main():
    demo = BoundaryWaveParticleDemo()
    demo.run()


if __name__ == "__main__":
    main()