# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEquals("fixme", items[0].name)

    def test_aged_brie(self):
        items = [Item("Aged Brie", -1, 5)]  # Aged Brie at max quality, past sell-by date
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)  # Quality should still be 50

    def test_conjured_item(self):
        items = [Item("Conjured Cookie", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_quality_never_negative(self):
        items = [Item("Negative", -1, -1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(gilded_rose.items[0].quality, 0)

if __name__ == '__main__':
    unittest.main()
