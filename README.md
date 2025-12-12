# Codex Cloud 示例项目

这是一个用于测试 Codex Cloud 的最小 Python 项目示例。

## 3D 粒子圣诞树演示
- 安装依赖：`pip install -r requirements.txt`
- 运行动画窗口：`python src/particle_tree.py`
- 无界面环境下保存 GIF：`MPLBACKEND=Agg python -c "from src.particle_tree import animate_tree; animate_tree(frame_count=180, interval_ms=40, save_path='tree.gif', show=False)"`
- 动画效果：3D 粒子树随时间轻微摇曳并缓慢旋转，顶部星星闪烁。
