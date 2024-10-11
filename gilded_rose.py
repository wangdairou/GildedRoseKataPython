# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_passes(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Sulfuras never changes
            elif item.name.startswith("Conjured"):
                self.update_conjured_item(item)
            else:
                self.update_normal_item(item)

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

            item.quality = max(0, min(item.quality, 50))

    def update_normal_item(self, item):
        item.quality -= 1
        if item.sell_in <= 0:
            item.quality -= 1

    def update_aged_brie(self, item):
        item.quality += 1
        if item.sell_in <= 0:
            item.quality += 1

    def update_backstage_passes(self, item):
        if item.sell_in > 10:
            item.quality += 1
        elif item.sell_in > 5:
            item.quality += 2
        elif item.sell_in > 0:
            item.quality += 3
        else:
            item.quality = 0

    def update_conjured_item(self, item):
        item.quality -= 2
        if item.sell_in <= 0:
            item.quality -= 2