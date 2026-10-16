# 项目结构说明

## 当前落地结构

```text
vscode-git-demo/
├─ README.md                         项目介绍
├─ CHANGELOG.md                      变更记录
├─ .github/                          Issue 与 PR 模板
├─ docs/
│  ├─ README.md                      文档入口
│  ├─ guides/                        结构、使用、需求输入说明
│  ├─ iterations/                    版本计划
│  ├─ versions/                      交付档案
│  ├─ ui/v0.2.0/                     设计材料
│  ├─ acceptance/v0.2.0/             验收材料
│  └─ templates/                     可复用文档模板
└─ Instrument_tool/Instrument_tool/  现有可执行业务目录
   ├─ InstrumentTool.py             主入口与菜单
   ├─ imports.py                    页面导入与显示管理
   ├─ lib.py                        公共方法、窗口及通信
   ├─ *.py                          仪表、车控、QNX 等页面
   ├─ cli/*_data.py                  业务命令与数据映射
   ├─ resources/                    ADB、scrcpy 等工具
   └─ FactoryApk/                   平台相关安装资源
```

本轮只优化文档和迭代资料的组织，不移动业务文件。现有代码存在相对路径和直接模块导入，直接迁移目录可能影响启动。

## 修改定位

| 需求 | 首先查看 | 验证重点 |
| --- | --- | --- |
| 主导航或模块切换 | InstrumentTool.py、imports.py | 所有已有页面可访问 |
| 页面 UI | 对应业务 .py，如 charge.py | 布局、缩放、原有回调 |
| 新增车辆属性操作 | cli/ 对应 *_data.py 与页面 | 属性映射、目标设备、实际结果 |
| 公共通信与资源路径 | lib.py 与实际调用位置 | 现有调用兼容性 |
| 版本与交付范围 | docs/iterations、docs/versions、CHANGELOG.md | 范围和证据一致 |

## 后续代码结构演进原则

新增 UI 通用组件可在业务目录内按需建立独立模块；新增通信封装应先替换一个调用点并验证，再推广。未来如需 ui/services/transports 等分层，应作为单独重构任务，先列出入口、导入、资源路径和打包影响。本轮未实施该迁移。

不要创建 V0.1、V0.2 等整套源码副本；版本源码通过 Git 标签保留。虚拟环境、运行日志和本地设置不放入版本档案目录。
