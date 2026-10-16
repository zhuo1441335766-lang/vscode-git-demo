# 本地使用说明

## 目录与启动

当前本地仓库：`E:\git_github_vscode\vscode-git-demo`。

从内层业务目录启动，确保相对资源路径正确：

```powershell
Set-Location E:\git_github_vscode\vscode-git-demo\Instrument_tool\Instrument_tool
$env:PATH = "$PWD\resources;" + $env:PATH
& ..\..\.venv\Scripts\python.exe InstrumentTool.py
```

示例使用当前本地 .venv；其他电脑应使用已配置依赖的 Python 路径。不要照搬本机绝对路径。Tkinter 属于 Python 图形环境，pyserial 为已识别依赖；准确依赖版本须按交付环境确认。

## 设备连接

1. Android 设备连接数据线，开启调试并允许授权；网络调试则使用实际设备地址连接。
2. 从业务目录执行 ` .\resources\adb.exe devices -l`，确认目标状态为 device。
3. 工具中选择仪表侧、车控、QNX 侧或其他模块。
4. QNX 使用对应串口连接；遵循工具中的连接提示，确认端口与台架匹配。

现有命令有未显式指定序列号的调用，多台 ADB 设备可能导致目标不明确。执行前确认目标连接环境。首次验证可先读取版本，再验证截图和日志，涉及属性写入的操作在对应台架上执行并记录结果。

## 常见定位

| 现象 | 检查方式 |
| --- | --- |
| 没有显示窗口 | 用 python.exe 在终端启动，读取异常；检查是否已有窗口 |
| 找不到资源 | 确认当前目录为内层 Instrument_tool |
| adb 命令找不到 | 确认 resources 存在且已加入本次进程 PATH |
| 无设备或 unauthorized | 检查数据线、设备端授权与调试配置 |
| QNX 无法连接 | 检查串口、占用情况和对应连接方式 |

问题反馈附工具版本/提交、复现步骤和相关错误输出。设备未连接时的界面检查不能替代实机验收。
