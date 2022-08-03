from unittest import TestCase, main

from tests.test_file.WorkExtradition.search_query_search import test_ex
from wbxSearch import WorkExtradition

test_w_ex = WorkExtradition("../test_file/WorkExtradition/search_query_search/read_file.csv")
result_default_search_query_search = [test_ex.womens_clothing.record_for_write_file()]

result_complete_match_false_search_query_search = [test_ex.womens_clothing.record_for_write_file(),
                                                   test_ex.womens_clothing_discount.record_for_write_file(),
                                                   test_ex.womens_clothing_menu.record_for_write_file(),
                                                   ]

result_contains_true_search_query_search = [test_ex.womens_clothing.record_for_write_file(),
                                            test_ex.test_clothing_men.record_for_write_file(),
                                            test_ex.womens_clothing_discount.record_for_write_file(),
                                            test_ex.womens_clothing_menu.record_for_write_file(),
                                            test_ex.women.record_for_write_file()
                                            ]

result_contains_true_complete_match_false_search_query_search = [
    test_ex.test_clothing_men.record_for_write_file(),
    test_ex.women.record_for_write_file(),
    test_ex.electronics_menu.record_for_write_file()
]


class SearchQuerySearchTest(TestCase):

    def test_default_search_query_search(self):
        """проверка поиска по полному совпадению query_search"""
        res_list = [x.record_for_write_file() for x in test_w_ex.search_query_search("(женская одежда)")]
        self.assertEqual(res_list, result_default_search_query_search)

    def test_complete_match_false_search_query_search(self):
        """проверка поиска по не полному совпадению query_search"""
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.search_query_search("женская одежда", complete_match=False)]
        self.assertEqual(res_list, result_complete_match_false_search_query_search)

    def test_contains_true_search_query_search(self):
        """проверка поиска по полному совпадению query_search, где есть полное совпадение записи не включаются в
        результат """
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.search_query_search("(электроника меню)", contains=True)]
        self.assertEqual(res_list, result_contains_true_search_query_search)

    def test_contains_true_complete_match_false_search_query_search(self):
        """проверка поиска по частичному совпадению query_search, где есть частичное совпадение записи не включаются в
        результат """
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.search_query_search("женская одежда", contains=True, complete_match=False)]
        self.assertEqual(res_list, result_contains_true_complete_match_false_search_query_search)


if __name__ == '__main__':
    main()
