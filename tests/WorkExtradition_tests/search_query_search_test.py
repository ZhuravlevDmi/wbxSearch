from unittest import TestCase, main

from tests.test_file.WorkExtradition.search_query_search import test_ex
from wbxSearch import WorkExtradition

test_w_ex = WorkExtradition("../test_file/WorkExtradition/search_query_search/read_file.csv")

test_w_ex_two = WorkExtradition(["../test_file/WorkExtradition/search_query_search/read_file2.csv",
                                 "../test_file/WorkExtradition/search_query_search/read_file.csv"])
result_default = [test_ex.womens_clothing.record_for_write_file()]

result_complete_match_false = [test_ex.womens_clothing.record_for_write_file(),
                               test_ex.womens_clothing_discount.record_for_write_file(),
                               test_ex.womens_clothing_menu.record_for_write_file(),
                               ]

result_contains_true = [test_ex.womens_clothing.record_for_write_file(),
                        test_ex.test_clothing_men.record_for_write_file(),
                        test_ex.womens_clothing_discount.record_for_write_file(),
                        test_ex.womens_clothing_menu.record_for_write_file(),
                        test_ex.women.record_for_write_file()
                        ]

result_contains_true_complete_match_false = [
    test_ex.test_clothing_men.record_for_write_file(),
    test_ex.women.record_for_write_file(),
    test_ex.electronics_menu.record_for_write_file()
]

result_multi_file_and_param_default = [test_ex.womens_clothing.record_for_write_file(),
                                       test_ex.tourist_tent.record_for_write_file()]


class SearchQuerySearchTest(TestCase):

    def test_default(self):
        """проверка поиска по полному совпадению query_search"""
        res_list = [x.record_for_write_file() for x in test_w_ex.search_query_search("(женская одежда)")]
        self.assertEqual(res_list.sort(), result_default.sort())

    def test_complete_match_false(self):
        """проверка поиска по не полному совпадению query_search"""
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.search_query_search("женская одежда", complete_match=False)]
        self.assertEqual(res_list.sort(), result_complete_match_false.sort())

    def test_contains_true(self):
        """проверка поиска по полному совпадению query_search, где есть полное совпадение записи не включаются в
        результат """
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.search_query_search("(электроника меню)", contains=True)]
        self.assertEqual(res_list.sort(), result_contains_true.sort())

    def test_contains_true_complete_match_false(self):
        """проверка поиска по частичному совпадению query_search, где есть частичное совпадение записи не включаются в
        результат """
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.search_query_search("женская одежда", contains=True, complete_match=False)]
        self.assertEqual(res_list.sort(), result_contains_true_complete_match_false.sort())

    def test_multi_file_and_param_default(self):
        """проверка поиска по полному совпадению query_search"""
        res_list = [x.record_for_write_file() for x in test_w_ex_two.search_query_search(["(женская одежда)",
                                                                                          "(палатка туристическая)"])]
        self.assertEqual(res_list.sort(), result_multi_file_and_param_default.sort())


if __name__ == '__main__':
    main()
