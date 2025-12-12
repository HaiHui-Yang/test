# 粒子圣诞树示例

这是一个仅包含 3D 粒子圣诞树动画的最小示例项目，可直接运行查看效果或在无界面环境下导出 GIF。

## 运行
- 安装依赖：`pip install -r requirements.txt`
- 运行动画窗口：`python src/particle_tree.py`
  - 若在 IDE（如 PyCharm SciView）出现一片黑屏，请确保窗口弹出/允许外部窗口渲染；本代码已关闭 3D 动画的 `blit` 以避免空白画面。
- 无界面环境保存 GIF：`MPLBACKEND=Agg python -c "from src.particle_tree import animate_tree; animate_tree(save_path='tree.gif', frame_count=180, interval_ms=40, show=False)"`

## 说明
- 仅保留了动画所需的代码与依赖，其余示例与测试文件已移除。
- 依赖项：matplotlib、numpy、pillow（用于可选 GIF 导出）。
