from unittest import TestCase, main

from tests.test_file.WorkExtradition.active_search import test_ex
from wbxSearch import WorkExtradition

test_w_ex = WorkExtradition("../test_file/WorkExtradition/active_search/read_file.csv")

result_true_active_search = [
    test_ex.womens_clothing.record_for_write_file(),
    test_ex.womens_clothing_discount.record_for_write_file(),
    test_ex.womens_clothing_menu.record_for_write_file(),
    test_ex.women.record_for_write_file(),
]

result_false_active_search = [
    test_ex.test_clothing_men.record_for_write_file(),
    test_ex.electronics_menu.record_for_write_file()
]


class ActiveSearchTest(TestCase):

    def test_true_active_search(self):
        """проверка поиска где столбец active = yes"""
        res_list = [x.record_for_write_file() for x in test_w_ex.active_search()]
        self.assertEqual(res_list, result_true_active_search)

    def test_false_active_search(self):
        """проверка поиска где столбец active = no"""
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.active_search(False)]
        self.assertEqual(res_list, result_false_active_search)


if __name__ == '__main__':
    main()
