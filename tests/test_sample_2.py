from src.sample_1 import sample_f

class TestSample:
    def test_sample_1(self):

        # 準備 & 実行
        actual_output = sample_f()

        # 検証
        assert actual_output == 1

class Sample:
    def test_sample_1(self):
        # 準備 & 実行
        actual_output = sample_f()

        # 検証
        assert actual_output == 1
