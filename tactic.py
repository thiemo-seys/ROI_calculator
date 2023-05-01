from enum import Enum

from condition import Condition

class Action(Enum):
    buy = "buy"
    sell = "sell"


class Tactic:
    def __init__(self, action: Action, conditions: list[Condition]):
        self.action = action
        self.conditions = conditions

    def conditions_fulfilled(self):
        all(condition.fulfilled() for condition in self.conditions)

    def execute(self):
        if self.conditions_fulfilled(): self.action.execute()

