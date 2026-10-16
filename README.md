# 仪表测试小工具

面向汽车仪表、车控及 QNX 调试的 Python/Tkinter 桌面工具。

当前产品基线为 **V0.1：已可稳定交付**。后续迭代以 UI 升级和功能新增为主。

## 文档入口

- [版本路线图](docs/ROADMAP.md)
- [GitHub 迭代与仓库规范](docs/GITHUB_WORKFLOW.md)
- [版本档案索引](docs/versions/README.md)
- [V0.1 基线档案](docs/versions/v0.1.0.md)
- [V0.2 迭代计划](docs/iterations/v0.2.0.md)
- [版本变更记录](CHANGELOG.md)

## 源码位置

入口：`Instrument_tool/Instrument_tool/InstrumentTool.py`。
业务页面位于同目录；`cli/` 保存业务命令和数据映射；`resources/` 保存外部工具资源。

## 源码启动

Windows 环境，使用已配置项目依赖的 Python，从业务目录启动：

```powershell
cd Instrument_tool/Instrument_tool
python InstrumentTool.py
```

当前使用 Tkinter 和 pyserial；具体依赖版本、已验证 Python 版本和交付包以发布记录为准，尚需在首次 Release 中补齐。根目录现有 requirements.txt 为本地未跟踪文件，本次未将其作为已验证依赖清单提交。

设备调试需要适配的 ADB/串口连接和对应设备环境。设备操作的验收记录按版本保存。
