from datetime import datetime


class BudgetCounter:
    """Class for monthly budget counting"""

    def __init__(self, start_date: str, end_date: str):
        """Initializing method.

        Args:
            start_date: start of accounting period date(day:month:year)
            end_date: end of accounting period date(day:month:year)

        """
        self.__start_date = start_date
        self.__end_date = end_date
        self.__budget = 0

    @staticmethod
    def date_(date_: str) -> datetime:
        """Returns date.

        Returns: str
        """
        return datetime.strptime(date_, '%d.%m.%Y')

    @property
    def budget(self) -> float:
        """Count budget for accounting period.

        Returns: float budget
        """
        return self.__budget

    def correct_budget(self, value: float):
        """Count current budget in view of current expense or income.

        Args:
            value: current expense or income

        Returns: float
        """
        self.__budget += value

    @property
    def accounting_period(self) -> int:
        """Count days in accounting period.

        Returns: int days count
        """
        start_date = self.date_(date_=self.__start_date)
        end_date = self.date_(date_=self.__end_date)
        return int(str(end_date - start_date).split(' ')[0]) + 1

    @property
    def daily_budget(self) -> float:
        """Returns daily budget.

        Returns: float
        """
        return self.budget / self.accounting_period
