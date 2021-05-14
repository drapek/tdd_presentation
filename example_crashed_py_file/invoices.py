from example_crashed_py_file.repo_client import GetRepo  # this will make an error


class InvoicesRepo:
    invoices = []

    def __init__(self):
        repo = GetRepo()
        self.invoices = repo.invoices()

    def get_with_term_today(self):
        return self.invoices
