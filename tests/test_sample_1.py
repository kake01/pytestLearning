from src.sample_1 import convert

def test_sample_1():

    # 準備 & 実行
    actual_output = convert()

    # 検証
    assert actual_output == 1