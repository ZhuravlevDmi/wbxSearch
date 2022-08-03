from unittest import TestCase, main

from tests.test_file.WorkExtradition.kind_search import test_ex
from wbxSearch import WorkExtradition

test_w_ex = WorkExtradition("../test_file/WorkExtradition/kind_search/read_file.csv")

result_default_kind_search = [test_ex.womens_clothing.record_for_write_file(),
                              test_ex.electronics_menu.record_for_write_file()]

result_complete_match_false_kind_search = [test_ex.womens_clothing.record_for_write_file(),
                                           test_ex.test_clothing_men.record_for_write_file(),
                                           test_ex.electronics_menu.record_for_write_file()]

result_contains_true_kind_search = [
    test_ex.test_clothing_men.record_for_write_file(),
    test_ex.womens_clothing_discount.record_for_write_file(),
    test_ex.womens_clothing_menu.record_for_write_file(),
    test_ex.women.record_for_write_file(),
]

result_contains_true_complete_match_false_kind_search = [
    test_ex.womens_clothing_discount.record_for_write_file(),
    test_ex.womens_clothing_menu.record_for_write_file(),
    test_ex.women.record_for_write_file(),
]


class KindSearchTest(TestCase):
    """вообще kind встречал только с значением common, но в тесте придумаю новые значения"""

    def test_default_kind_search(self):
        """проверка поиска по полному совпадению kind"""
        res_list = [x.record_for_write_file() for x in test_w_ex.kind_search("common")]
        self.assertEqual(res_list, result_default_kind_search)

    def test_complete_match_false_kind_search(self):
        """проверка поиска по не полному совпадению kind"""
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.kind_search("common", complete_match=False)]
        self.assertEqual(res_list, result_complete_match_false_kind_search)

    def test_contains_true_kind_search(self):
        """проверка поиска по полному совпадению kind, где есть полное совпадение записи не включаются в
        результат """
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.kind_search("common", contains=True)]
        self.assertEqual(res_list, result_contains_true_kind_search)

    def test_contains_true_complete_match_false_kind_search(self):
        """проверка поиска по частичному совпадению kind, где есть частичное совпадение записи не включаются в
        результат """
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.kind_search("common", contains=True, complete_match=False)]
        self.assertEqual(res_list, result_contains_true_complete_match_false_kind_search)


if __name__ == '__main__':
    main()
