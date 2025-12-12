import sys
from pathlib import Path

# 确保可以通过 `import src.xxx` 引入源码目录
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
