# Codex Cloud 示例项目

这是一个用于测试 Codex Cloud 的最小 Python 项目示例。

## 3D 粒子圣诞树演示
- 安装依赖：`pip install -r requirements.txt`
- 运行动画窗口：`python src/particle_tree.py`
- 无界面环境下保存 GIF：`MPLBACKEND=Agg python -c "from src.particle_tree import animate_tree; animate_tree(frame_count=180, interval_ms=40, save_path='tree.gif', show=False)"`
- 动画效果：3D 粒子树随时间轻微摇曳并缓慢旋转，顶部星星闪烁。

## 在 PyCharm 中运行小提示
- **创建解释器**：在 PyCharm 右下角选择「Python Interpreter」→「Add Interpreter」→ 选择现有虚拟环境或新建，指向本项目（推荐 `.venv`）。
- **安装依赖**：在终端（或 PyCharm 的 Terminal）执行 `pip install -r requirements.txt`。
- **运行动画**：右键 `src/particle_tree.py` 选择「Run 'particle_tree'」，如需无界面导出 GIF 可在「Run/Debug Configurations」里设置环境变量 `MPLBACKEND=Agg`，并在 Parameters 里添加 `--` 后附加自定义参数（例如通过 `save_path` 指定输出）。
- **运行测试**：右键 `tests` 目录选择「Run 'pytest in tests'」，或在 Terminal 运行 `pytest`。
