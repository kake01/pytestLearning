from src.roller_coaster import height_checker

def test_120cm未満():
    # 準備 & 実行
    actual_output = height_checker(119)
    # 検証
    assert actual_output == False

def test_120cm境界値():
    # 準備 & 実行
    actual_output = height_checker(120)
    # 検証
    assert actual_output == True

def test_170cm未満():
    # 準備 & 実行
    actual_output = height_checker(169)
    # 検証
    assert actual_output == True

def test_170cm():
    # 準備 & 実行
    actual_output = height_checker(170)
    # 検証
    assert actual_output == False