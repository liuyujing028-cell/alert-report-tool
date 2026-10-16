import json
def count_records(records):
    return len(records)


def summarize_alerts(records):
    counts = {
        "critical": 0,
        "warning": 0,
        "info": 0,
        "unknown": 0,
    }

    for record in records:
        if not isinstance(record, dict):
          continue
        severity = record.get("severity", "unknown")

        if severity not in ["critical", "warning", "info"]:
            severity = "unknown"

        counts[severity] += 1

    return counts

def count_invalid(records):
    invalid_count = 0

    for record in records:
        if not isinstance(record, dict):
            invalid_count += 1

    return invalid_count

def build_report(records):
    total = count_records(records)
    invalid = count_invalid(records)

    return {
        "total": total,
        "valid": total - invalid,
        "invalid": invalid,
        "counts": summarize_alerts(records),
    }

def get_message(result):
    if result["counts"]["critical"] > 0:
        return "需要优先处理"
    elif result["counts"]["warning"] > 0:
        return "需要关注"
    else:
        return "暂无紧急或警告告警"

def load_records(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)

def print_report(result):
    print(f"共收到 {result['total']} 条告警")
    print(f"有效记录：{result['valid']} 条")
    for severity, number in result["counts"].items():
        print(f"{severity}：{number} 条")

    print(f"处理提示：{result['message']}")
    print(f"无效记录：{result['invalid']} 条")
    classified_count = sum(result["counts"].values())
    checked_total = classified_count + result["invalid"]

    if checked_total == result["total"]:
        print("统计核对通过")
    else:
        print("统计数量不一致")

def save_report(report, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=4)

def main():
    try:
        alerts = load_records("alerts.json")
    except FileNotFoundError:
        print("找不到 alerts.json，请检查文件位置")
    except json.JSONDecodeError:
        print("JSON 格式有误，请检查逗号、引号和括号")
    else:
        if not isinstance(alerts, list):
            print("数据格式错误：最外层必须是列表")
            return
        result = build_report(alerts)
        result["message"] = get_message(result)
        print_report(result)
        save_report(result, "report.json")

if __name__ == "__main__":
    main()