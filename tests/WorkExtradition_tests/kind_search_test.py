from unittest import TestCase, main

from tests.WorkExtradition_tests.Main_Class import MainClassTest
from tests.test_file.WorkExtradition.kind_search import test_ex
from wbxSearch import WorkExtradition

test_w_ex = WorkExtradition("../test_file/WorkExtradition/kind_search/read_file.csv")

result_default = [test_ex.womens_clothing.record_for_write_file(),
                  test_ex.electronics_menu.record_for_write_file()]

result_complete_match_false = [test_ex.womens_clothing.record_for_write_file(),
                               test_ex.test_clothing_men.record_for_write_file(),
                               test_ex.electronics_menu.record_for_write_file()]

result_contains_true = [
    test_ex.test_clothing_men.record_for_write_file(),
    test_ex.womens_clothing_discount.record_for_write_file(),
    test_ex.womens_clothing_menu.record_for_write_file(),
    test_ex.women.record_for_write_file(),
]

result_contains_true_complete_match_false = [
    test_ex.womens_clothing_discount.record_for_write_file(),
    test_ex.womens_clothing_menu.record_for_write_file(),
    test_ex.women.record_for_write_file(),
]

result_multi_param_default = [test_ex.womens_clothing.record_for_write_file(),
                              test_ex.electronics_menu.record_for_write_file(),
                              test_ex.womens_clothing_discount.record_for_write_file(),
                              ]

result_multi_param_complete_match_false = [test_ex.womens_clothing.record_for_write_file(),
                                           test_ex.test_clothing_men.record_for_write_file(),
                                           test_ex.electronics_menu.record_for_write_file(),
                                           test_ex.womens_clothing_discount.record_for_write_file()]

result_multi_param_contains_true = [
    test_ex.test_clothing_men.record_for_write_file(),
    test_ex.womens_clothing_menu.record_for_write_file(),
    test_ex.women.record_for_write_file(),
]

result_multi_param_contains_true_complete_match_false = [
    test_ex.womens_clothing_menu.record_for_write_file(),
    test_ex.women.record_for_write_file(),
]


class KindSearchTest(TestCase, MainClassTest):
    """вообще kind встречал только с значением common, но в тесте придумаю новые значения"""

    def test_multi_file_default(self):
        pass

    def test_multi_file_complete_match_false(self):
        pass

    def test_multi_file_contains_true(self):
        pass

    def test_multi_file_contains_true_complete_match_false(self):
        pass

    def test_multi_and_param_file_default(self):
        pass

    def test_multi_file_and_param_complete_match_false(self):
        pass

    def test_multi_file_and_param_contains_true(self):
        pass

    def test_multi_file_and_param_contains_true_complete_match_false(self):
        pass

    def test_default(self):
        res_list = [x.record_for_write_file() for x in test_w_ex.kind_search("common")]
        self.assertEqual(res_list.sort(), result_default.sort())

    def test_complete_match_false(self):
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.kind_search("common", complete_match=False)]
        self.assertEqual(res_list.sort(), result_complete_match_false.sort())

    def test_contains_true(self):
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.kind_search("common", contains=True)]
        self.assertEqual(res_list.sort(), result_contains_true.sort())

    def test_contains_true_complete_match_false(self):
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.kind_search("common", contains=True, complete_match=False)]
        self.assertEqual(res_list.sort(), result_contains_true_complete_match_false.sort())

    def test_multi_param_default(self):
        """проверка поиска по полному совпадению kind"""
        res_list = [x.record_for_write_file() for x in test_w_ex.kind_search(["common", "mamon"])]
        self.assertEqual(res_list.sort(), result_multi_param_default.sort())

    def test_multi_param_complete_match_false(self):
        """проверка поиска по не полному совпадению kind"""
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.kind_search(["common", "mon"], complete_match=False)]
        self.assertEqual(res_list.sort(), result_multi_param_complete_match_false.sort())

    def test_multi_param_contains_true(self):
        """проверка поиска по полному совпадению kind, где есть полное совпадение записи не включаются в
        результат """
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.kind_search(["common", "mamon"], contains=True)]
        self.assertEqual(res_list.sort(), result_multi_param_contains_true.sort())

    def test_multi_param_contains_true_complete_match_false(self):
        """проверка поиска по частичному совпадению kind, где есть частичное совпадение записи не включаются в
        результат """
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.kind_search(["common", "mamon"], contains=True, complete_match=False)]
        self.assertEqual(res_list.sort(), result_multi_param_contains_true_complete_match_false.sort())


if __name__ == '__main__':
    main()
