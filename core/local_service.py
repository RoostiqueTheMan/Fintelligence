from Fintelligence.core.budget_counter import BudgetCounter
from datetime import datetime


class LocalServie:
    """Class for local using budget counter."""

    def __init__(self, start_date: str, end_date: str):
        """Initializing method.

        Args:
            start_date: accounting period start
            end_date: accounting period end
        """
        self.__start_date = start_date
        self.__end_date = end_date
        self.__budget_counter = BudgetCounter(
            start_date=start_date,
            end_date=end_date
        )

    def budget(self, value: float) -> None:
        """Correct budget.

        Returns: None
        """
        self.__budget_counter.correct_budget(value=value)

    def write_transactions(self, record: str) -> None:
        """Write all transactions in txt file.

        Returns: None
        """
        with open(f'/home/sigma-st-6/roostique/side/fintelligence/Fintelligence/transactions/{self.__budget_counter._BudgetCounter__start_date}.txt', 'a') as file:
            record = f'{record}\n'
            file.write(record)

    def start_counter(self) -> None:
        """Get expense or income and print current daily budget.

        Returns: None
        """
        value = 0
        while value != 'stop':
            value = input('Введите сумму: ')
            self.budget(value=float(value))
            self.write_transactions(record=value)
            print(f'Сумма на день составляет: {self.__budget_counter.daily_budget}')
            print(f'Бюджет на остаток рассчетного периода составляет: {self.__budget_counter.budget}')

    def continue_counter(self, file_name: str) -> None:
        """Continue get expense or income and print current daily budget.

        Returns: None
        """
        with open(f'/home/sigma-st-6/roostique/side/fintelligence/Fintelligence/transactions/{file_name}.txt', 'r') as file:
            string = file.read().split('\n')
            for value in range(len(string)):
                self.budget(value=float(value))
                current_budget = self.__budget_counter.budget
                self.__budget_counter = BudgetCounter(
                    end_date=self.__end_date,
                    start_date=datetime.now().date().strftime('%d.%m.%Y')
                )
                self.budget(value=float(current_budget))
        self.start_counter()


local_service = LocalServie(
    start_date='06.10.2023',
    end_date='25.10.2023'
)
# local_service.start_counter()
local_service.continue_counter(file_name='06.10.2023')
