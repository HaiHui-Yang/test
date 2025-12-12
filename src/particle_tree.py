"""3D 粒子圣诞树动画。

运行后会打开一个 Matplotlib 3D 窗口：
- 树由随机粒子构成，并随时间轻微左右摇摆。
- 视角会缓慢绕 Z 轴旋转，顶端星星闪烁。
"""
from __future__ import annotations

import math
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter


@dataclass
class ParticleCloud:
    """封装粒子坐标和表现参数。"""

    positions: np.ndarray  # 形状：(N, 3)
    colors: np.ndarray     # 形状：(N, 4) RGBA
    sizes: np.ndarray      # 点大小


def _generate_tree_body(num_particles: int = 1400) -> ParticleCloud:
    """生成树身粒子，分布在圆锥体内。"""
    heights = np.random.uniform(0.0, 1.0, num_particles)
    angles = np.random.uniform(0.0, 2 * math.pi, num_particles)
    radii = (1.0 - heights) * np.random.uniform(0.15, 0.4, num_particles)

    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    z = heights * 1.4

    greens = np.clip(np.random.normal(0.4, 0.12, num_particles), 0, 0.7)
    colors = np.stack([
        0.05 + greens * 0.2,
        0.25 + greens,
        0.1 + greens * 0.2,
        np.full(num_particles, 0.9),
    ], axis=1)

    sizes = np.random.uniform(6, 18, num_particles)
    positions = np.stack([x, y, z], axis=1)
    return ParticleCloud(positions=positions, colors=colors, sizes=sizes)


def _generate_trunk(num_particles: int = 200) -> ParticleCloud:
    """生成树干粒子，位于底部小圆柱体。"""
    z = np.random.uniform(-0.25, 0.05, num_particles)
    angles = np.random.uniform(0.0, 2 * math.pi, num_particles)
    radii = np.random.uniform(0.05, 0.1, num_particles)

    x = radii * np.cos(angles)
    y = radii * np.sin(angles)

    colors = np.stack([
        np.full(num_particles, 0.35),
        np.full(num_particles, 0.18),
        np.full(num_particles, 0.08),
        np.full(num_particles, 1.0),
    ], axis=1)
    sizes = np.random.uniform(12, 22, num_particles)
    positions = np.stack([x, y, z], axis=1)
    return ParticleCloud(positions=positions, colors=colors, sizes=sizes)


def _generate_star(num_rays: int = 80) -> ParticleCloud:
    """生成顶部星星粒子，分布在小球体表面。"""
    phi = np.random.uniform(0.0, math.pi, num_rays)
    theta = np.random.uniform(0.0, 2 * math.pi, num_rays)
    r = np.random.uniform(0.02, 0.08, num_rays)

    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = 1.4 + r * np.cos(phi) + 0.04

    base_color = np.array([1.0, 0.9, 0.35, 1.0])
    flicker = np.random.uniform(0.85, 1.05, (num_rays, 1))
    colors = np.clip(base_color * flicker, 0.0, 1.0)

    sizes = np.random.uniform(35, 60, num_rays)
    positions = np.stack([x, y, z], axis=1)
    return ParticleCloud(positions=positions, colors=colors, sizes=sizes)


def _compose_clouds(*clouds: ParticleCloud) -> ParticleCloud:
    positions = np.concatenate([c.positions for c in clouds], axis=0)
    colors = np.concatenate([c.colors for c in clouds], axis=0)
    sizes = np.concatenate([c.sizes for c in clouds], axis=0)
    return ParticleCloud(positions=positions, colors=colors, sizes=sizes)


def _rotate(points: np.ndarray, angle: float, tilt: float) -> np.ndarray:
    """绕 Z 轴旋转并增加轻微倾斜。"""
    cos_a, sin_a = math.cos(angle), math.sin(angle)
    rot_z = np.array([[cos_a, -sin_a, 0], [sin_a, cos_a, 0], [0, 0, 1]])

    tilt_y = np.array(
        [[math.cos(tilt), 0, math.sin(tilt)], [0, 1, 0], [-math.sin(tilt), 0, math.cos(tilt)]]
    )
    return points @ rot_z.T @ tilt_y.T


def animate_tree(
    frame_count: int = 360,
    interval_ms: int = 50,
    *,
    save_path: str | None = None,
    show: bool = True,
) -> FuncAnimation:
    """创建并播放 3D 粒子圣诞树动画。

    参数：
    - frame_count: 动画帧数。
    - interval_ms: 帧间隔，单位毫秒。
    - save_path: 若提供，则保存为 GIF 文件（需安装 Pillow）。
    - show: 是否弹出窗口播放动画。
    """

    plt.style.use("dark_background")

    body = _generate_tree_body()
    trunk = _generate_trunk()
    star = _generate_star()
    cloud = _compose_clouds(body, trunk, star)

    fig = plt.figure(figsize=(7, 8))
    ax = fig.add_subplot(111, projection="3d")
    ax.axis("off")
    ax.set_xlim(-0.8, 0.8)
    ax.set_ylim(-0.8, 0.8)
    ax.set_zlim(-0.3, 1.6)

    scat = ax.scatter(
        cloud.positions[:, 0],
        cloud.positions[:, 1],
        cloud.positions[:, 2],
        c=cloud.colors,
        s=cloud.sizes,
    )

    def _update(frame: int):
        angle = frame * math.pi / 180
        tilt = 0.08 * math.sin(frame / 15)
        rotated = _rotate(cloud.positions, angle, tilt)

        # 星星闪烁：周期性调整前半部分粒子的透明度
        alpha_wave = 0.75 + 0.25 * np.sin(frame / 7)
        colors = cloud.colors.copy()
        star_slice = -len(star.positions)
        colors[star_slice:, 3] = np.clip(alpha_wave, 0.5, 1.0)

        scat._offsets3d = (rotated[:, 0], rotated[:, 1], rotated[:, 2])
        scat.set_facecolors(colors)
        scat.set_sizes(cloud.sizes * (0.9 + 0.2 * np.sin(frame / 20 + cloud.positions[:, 2])))
        ax.view_init(elev=15 + 3 * math.sin(frame / 40), azim=angle * 180 / math.pi)
        return scat,

    anim = FuncAnimation(fig, _update, frames=frame_count, interval=interval_ms, blit=True)
    plt.tight_layout()

    if save_path:
        fps = max(1, int(1000 / interval_ms))
        anim.save(save_path, writer=PillowWriter(fps=fps))

    if show:
        plt.show()
    else:
        plt.close(fig)

    return anim


if __name__ == "__main__":
    animate_tree()
