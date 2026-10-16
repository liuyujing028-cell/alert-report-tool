# 告警统计工具

一个 Python 学习项目：读取 JSON 告警数据，统计级别和有效记录数量，生成处理提示，并保存报告。

## 功能

- 统计 critical、warning、info、unknown 四种告警级别。
- 将缺少级别或级别无法识别的字典记录归为 unknown。
- 将非字典记录计为无效记录，不参与级别统计。
- 检查文件不存在、JSON 格式错误和最外层不是列表的情况。
- 将统计结果保存到 report.json。

## 文件说明

- alert_report.py：统计程序。
- test_report.py：自动检查混合数据、空列表和全部无效记录。
- alerts.json：输入数据。
- report.json：运行后生成的报告。

## 运行方式

需要 Python 3，不需要安装第三方依赖。
在项目文件夹中运行：

```powershell
python alert_report.py
```

运行测试：

```powershell
python test_report.py
```

## 输入示例

将以下内容保存到 alerts.json：

```json
[
    {"severity": "critical"},
    {"severity": "urgent"},
    {},
    123,
    "warning"
]
```

预期结果：总数 5，有效记录 3，无效记录 2；
critical 为 1，unknown 为 2，其余级别为 0。

## 当前限制

- 目前仅按记录是否为字典判断其有效性。
- 处理提示基于固定规则，没有调用大模型。
- 输入和输出路径相对于运行命令时所在的文件夹。
- 保存报告时会覆盖同名文件。

## 项目说明

本项目是在 AI 辅助指导下完成的 Python 学习练习。
使用模拟告警数据，不代表真实生产系统的部署或验证。