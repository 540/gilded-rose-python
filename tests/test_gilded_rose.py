from hamcrest import assert_that, is_
from src.gilded_rose import Item, GildedRose


class TestGildedRose:
    def test_the_quality_of_an_item_degrades_by_one_per_day(self):
        item = [Item("Elixir of the Mongoose", 5, 7)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        assert_that(item[0].quality, is_(6))

    def test_the_quality_of_an_item_can_never_be_negative(self):
        item = [Item("Elixir of the Mongoose", 5, 0)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        assert_that(item[0].quality, is_(0))

    def test_the_quality_of_an_item_degrades_twice_as_fast_once_the_sell_by_date_has_passed(
        self,
    ):
        item = [Item("Elixir of the Mongoose", 0, 10)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        assert_that(item[0].quality, is_(8))

    def test_the_quality_of_aged_brie_increases_by_one_per_day(self):
        item = [Item("Aged Brie", 5, 10)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        assert_that(item[0].quality, is_(11))

    def test_the_quality_of_aged_brie_increases_twice_as_fast_once_the_sell_by_date_has_passed(
        self,
    ):
        item = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        assert_that(item[0].quality, is_(12))

    def test_the_quality_of_an_item_is_never_more_than_50(self):
        item = [Item("Aged Brie", 5, 50)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        assert_that(item[0].quality, is_(50))

    def test_the_quality_of_sulfuras_never_changes(self):
        item = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        assert_that(item[0].quality, is_(80))

    def test_the_sell_in_date_of_sulfuras_never_changes(self):
        item = [Item("Sulfuras, Hand of Ragnaros", 5, 80)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        assert_that(item[0].sell_in, is_(5))

    def test_the_quality_of_backstage_passes_increases_by_one_per_day(self):
        item = [Item("Backstage passes to a TAFKAL80ETC concert", 20, 10)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        assert_that(item[0].quality, is_(11))

    def test_the_quality_of_backstage_passes_increases_by_two_per_day_when_there_are_10_days_or_less(self):
        item = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        assert_that(item[0].quality, is_(12))

    def test_the_quality_of_backstage_passes_increases_by_three_per_day_when_there_are_5_days_or_less(self):
        item = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        assert_that(item[0].quality, is_(13))

    def test_the_quality_of_backstage_passes_drops_to_zero_after_the_concert(self):
        item = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(item)

        gilded_rose.update_quality()

        assert_that(item[0].quality, is_(0))
