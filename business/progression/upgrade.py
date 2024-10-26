"""Defines a base upgrade for any weapon"""

from business.progression.interfaces import IUpgrade, IUpgradeValue, IInventoryItem

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
                        setattr(item, upgrade_value.stat, base * upgrade_value.value)
                    case self.ADD:
                        setattr(item, upgrade_value.stat, base + upgrade_value.value)
                    case self.SUBTRACT:
                        setattr(item, upgrade_value.stat, base - upgrade_value.value)
                    case self.DIVIDE:
                        setattr(item, upgrade_value.stat, base / upgrade_value.value)
                    case self.POWER:
                        setattr(item, upgrade_value.stat, base ** upgrade_value.value)


    @property
    def values(self) -> list[IUpgradeValue]:
        return self.__values

    @property
    def description(self):
        return self.__description
