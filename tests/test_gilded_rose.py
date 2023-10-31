from hamcrest import assert_that, is_
from src.gilded_rose import Item, GildedRose

class TestGildedRose:
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        assert_that(items[0].quality, is_(0))
