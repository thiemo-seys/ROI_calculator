import pytest

from decorators import require_keywords

class TestDecorators:
    def test_require_keywords(self):
        @require_keywords("a", "b")
        def func(**kwargs):
            return kwargs["a"] + kwargs["b"]

        # assert func with all required keyword arguments does not throw ValueError
        assert func(a=1, b=2) == 3
        assert func(a=1, b=2, c=3) == 3

        # assert func with all required keyword arguments does not throw ValueError
        with pytest.raises(ValueError, match=r"^Missing required keyword argument: '\w+'$"):
            func()
            func(1)
            func(1, 2)
            func(1, 2, 3)
            func(a=1)
            func(b=123)
