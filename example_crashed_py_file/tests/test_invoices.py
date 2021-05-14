import unittest

from example_crashed_py_file.invoices import InvoicesRepo


class InvoiceRepoTestCase(unittest.TestCase):

    def test_get_invoices(self):
        resp = InvoicesRepo().get_with_term_today()
        self.assertEqual(resp, ['invoice1.pdf'])
