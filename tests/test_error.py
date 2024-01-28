import pytest
from src.hit_raise import my_raise, MyError

def test_my_raise():
    with pytest.raises(MyError) as e:
        my_raise()
        
    # エラーメッセージを検証
    assert str(e.value) == 'MyErrorが発生'