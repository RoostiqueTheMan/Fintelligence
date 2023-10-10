from datetime import datetime


class BudgetCounter:
    """Class for monthly budget counting"""

    def __init__(self, income: float, date: str, planned_spending: float = 0):
        """Initializing method.

        Args:
            income: current budget
            date: end of accounting period date(day:month:year)
            planned_spending: planned spending

        """
        self.__income = income
        self.__date = date
        self.__planned_spending = planned_spending
        self.__budget = self.income - self.planned_spending

    @property
    def income(self) -> float:
        """Returns income.

        Returns: float
        """
        return self.__income

    @property
    def date(self) -> datetime:
        """Returns date.

        Returns: str
        """
        return datetime.strptime(self.__date, '%d:%m:%Y')

    @property
    def planned_spending(self) -> float:
        """Returns planned spending.

        Returns: float
        """
        return self.__planned_spending

    @property
    def budget(self) -> float:
        """Count budget for accounting period.

        Returns: float budget
        """
        return self.__budget

    def correct_budget(self, *args) -> float:
        """Count current budget in view of current expense or income.

        Args:
            args: current expense or income

        Returns: float
        """
        for arg in args:
            self.__budget += arg

    @property
    def accounting_period(self) -> int:
        """Count days in accounting period.

        Returns: int days count
        """
        return int((str(self.date - datetime.now())).split(' ')[0]) + 1

    @property
    def daily_budget(self) -> float:
        """Returns daily budget.

        Returns: float
        """
        return self.budget / self.accounting_period
