from unittest import TestCase, main

from tests.test_file.WorkExtradition.search_preset_id import test_ex
from wbxSearch import WorkExtradition

test_w_ex = WorkExtradition("../test_file/WorkExtradition/search_preset_id/read_file.csv")

result_default_search_preset_id = [test_ex.womens_clothing.record_for_write_file(),
                                   test_ex.womens_clothing_discount.record_for_write_file()]

result_complete_match_false_search_preset_id = [test_ex.womens_clothing.record_for_write_file(),
                                                test_ex.womens_clothing_discount.record_for_write_file(),
                                                test_ex.womens_clothing_menu.record_for_write_file()]

result_contains_true_search_preset_id = [
                                  test_ex.test_clothing_men.record_for_write_file(),
                                  test_ex.womens_clothing_menu.record_for_write_file(),
                                  test_ex.women.record_for_write_file(),
                                  test_ex.electronics_menu.record_for_write_file()
                                  ]

result_contains_true_complete_match_false_search_preset_id = [
    test_ex.test_clothing_men.record_for_write_file(),
    test_ex.women.record_for_write_file(),
    test_ex.electronics_menu.record_for_write_file()
]


class SearchPresetIDTest(TestCase):

    def test_default_search_preset_id(self):
        """проверка поиска по полному совпадению preset_id"""
        res_list = [x.record_for_write_file() for x in test_w_ex.search_preset_id("1001")]
        self.assertEqual(res_list.sort(), result_default_search_preset_id.sort())

    def test_complete_match_false_search_preset_id(self):
        """проверка поиска по не полному совпадению preset_id"""
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.search_preset_id("1001", complete_match=False)]
        self.assertEqual(res_list.sort(), result_complete_match_false_search_preset_id.sort())

    def test_contains_true_search_preset_id(self):
        """проверка поиска по полному совпадению preset_id, где есть полное совпадение записи не включаются в
        результат """
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.search_preset_id("1001", contains=True)]
        self.assertEqual(res_list.sort(), result_contains_true_search_preset_id.sort())

    def test_contains_true_complete_match_false_search_preset_id(self):
        """проверка поиска по частичному совпадению preset_id, где есть частичное совпадение записи не включаются в
        результат """
        res_list = [x.record_for_write_file() for x in
                    test_w_ex.search_preset_id("1001", contains=True, complete_match=False)]
        self.assertEqual(res_list.sort(), result_contains_true_complete_match_false_search_preset_id.sort())


if __name__ == '__main__':
    main()
