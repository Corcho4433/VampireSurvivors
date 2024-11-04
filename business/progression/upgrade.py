"""Defines a base upgrade for any weapon"""

from business.progression.interfaces import IUpgrade, IUpgradeValue, IInventoryItem


class UpgradeValue(IUpgradeValue):
    """One of the values held inside an upgrade"""

    def __init__(self, upgrade_type: str, stat: str, value: float):
        self.__type = upgrade_type
        self.__stat = stat
        self.__value = value

    @property
    def type(self):
        return self.__type

    @property
    def value(self):
        return self.__value

    @property
    def stat(self):
        return self.__stat

    def __eq__(self, other_value):
        return self.stat == other_value.stat and self.value == other_value.value and self.type == other_value.type #pylint: disable=C0301

class Upgrade(IUpgrade):
    """An upgrade for the weapon"""

    MULTIPLY = 1
    ADD = 2
    SUBTRACT = 3
    DIVIDE = 4
    POWER = 5

    def __init__(self, description: str, values: list[IUpgradeValue]):
        self.__values: list[IUpgradeValue] = values
        self.__description = description

    def apply(self, item: IInventoryItem):
        values = self.values

        for upgrade_value in values:
            if item.get_stat(upgrade_value.stat):
                base = item.get_stat(upgrade_value.stat)

                match upgrade_value.type:
                    case self.MULTIPLY:
                        #print(upgrade_value.stat, base, upgrade_value.value, upgrade_value.value * base)
                        item.change_stat(upgrade_value.stat, base * upgrade_value.value)
                    case self.ADD:
                        item.change_stat(upgrade_value.stat, base + upgrade_value.value)
                    case self.SUBTRACT:
                        item.change_stat(upgrade_value.stat, base - upgrade_value.value)
                    case self.DIVIDE:
                        item.change_stat(upgrade_value.stat, base / upgrade_value.value)
                    case self.POWER:
                        item.change_stat(upgrade_value.stat, base ** upgrade_value.value)

    @property
    def values(self) -> list[IUpgradeValue]:
        return self.__values

    @property
    def description(self):
        return self.__description

    def __str__(self):
        values_str = []
        for value in self.__values:
            values_str.append(f"stat:{value.stat}-value:{value.value}-type:{value.type}")

        return f"UpgradeObject - Description:{self.__description} - Values:{str(values_str)}"

    def __eq__(self, other):
        equal_desc = other.description == self.description
        equal_values = len(self.values) == len(other.values)

        if equal_values:
            for i in len(other.values):
                other_val = other.values[i]
                self_val = self.values[i]

                if self_val != other_val:
                    equal_values = False
                    break

        return equal_desc and equal_values
