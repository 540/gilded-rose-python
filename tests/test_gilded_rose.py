from hamcrest import assert_that, is_
from src.gilded_rose import Item, GildedRose


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()

    assert_that(items[0].name, is_(3))
