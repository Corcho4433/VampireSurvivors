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
            if hasattr(item, upgrade_value.stat):
                base = getattr(item, upgrade_value.stat)

                match upgrade_value.type:
                    case self.MULTIPLY:
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
        return f"UpgradeObject - Description:{self.__description} - Values:{self.__values}"
