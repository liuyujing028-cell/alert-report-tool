from alert_report import build_report


def test_mixed_records():
    records = [
        {"severity": "critical"},
        {},
        123,
    ]

    result = build_report(records)

    assert result["total"] == 3
    assert result["valid"] == 2
    assert result["invalid"] == 1
    assert result["counts"] == {
        "critical": 1,
        "warning": 0,
        "info": 0,
        "unknown": 1,
    }


def test_empty_records():
    result = build_report([])
    assert result["total"] == 0
    assert result["valid"] == 0
    assert result["invalid"] == 0

def test_invalid_records():
    result = build_report([123, "warning", None])

    assert result["total"] == 3
    assert result["valid"] == 0
    assert result["invalid"] == 3
    assert sum(result["counts"].values()) == 0

test_mixed_records()
test_empty_records()
test_invalid_records()
print("全部测试通过")