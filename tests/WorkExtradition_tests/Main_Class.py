from abc import ABC, abstractmethod


class MainClassTest(ABC):
    @abstractmethod
    def test_default(self):
        """Проверка поиска по полному совпадению значению параметра
        - один параметр один файл"""
        pass

    @abstractmethod
    def test_complete_match_false(self):
        """Проверка поиска по не полному совпадению значению параметра
        - один параметр один файл"""
        pass

    @abstractmethod
    def test_contains_true(self):
        """Проверка поиска по полному совпадению значению параметра, где есть полное совпадение записи,
         эти записи не включаются в результат
        - один параметр один файл"""
        pass

    @abstractmethod
    def test_contains_true_complete_match_false(self):
        """Проверка поиска по частичному совпадению значения параметра, где есть частичное совпадение записи
        не включаются в результат
        - один параметр один файл"""
        pass

    @abstractmethod
    def test_multi_param_default(self):
        """Проверка поиска по полному совпадению значению параметра
        - два параметра один файл"""
        pass

    @abstractmethod
    def test_multi_param_complete_match_false(self):
        """Проверка поиска по не полному совпадению значению параметра
        - два параметра один файл"""
        pass

    @abstractmethod
    def test_multi_param_contains_true(self):
        """Проверка поиска по полному совпадению значению параметра, где есть полное совпадение записи,
         эти записи не включаются в результат
        - два параметра один файл"""
        pass

    @abstractmethod
    def test_multi_param_contains_true_complete_match_false(self):
        """Проверка поиска по частичному совпадению значения параметра, где есть частичное совпадение записи
        не включаются в результат
        - два параметра один файл"""
        pass

    @abstractmethod
    def test_multi_file_default(self):
        """Проверка поиска по полному совпадению значению параметра
        - один параметр два файла"""
        pass

    @abstractmethod
    def test_multi_file_complete_match_false(self):
        """Проверка поиска по не полному совпадению значению параметра
         - один параметр два файла"""
        pass

    @abstractmethod
    def test_multi_file_contains_true(self):
        """Проверка поиска по полному совпадению значению параметра, где есть полное совпадение записи,
         эти записи не включаются в результат
        - один параметр два файла"""
        pass

    @abstractmethod
    def test_multi_file_contains_true_complete_match_false(self):
        """Проверка поиска по частичному совпадению значения параметра, где есть частичное совпадение записи
        не включаются в результат
        - один параметр два файла"""
        pass

    @abstractmethod
    def test_multi_and_param_file_default(self):
        """Проверка поиска по полному совпадению значению параметра
        - два параметра два файла"""
        pass

    @abstractmethod
    def test_multi_file_and_param_complete_match_false(self):
        """Проверка поиска по не полному совпадению значению параметра
         - два параметра два файла"""
        pass

    @abstractmethod
    def test_multi_file_and_param_contains_true(self):
        """Проверка поиска по полному совпадению значению параметра, где есть полное совпадение записи,
         эти записи не включаются в результат
        - два параметра два файла"""
        pass

    @abstractmethod
    def test_multi_file_and_param_contains_true_complete_match_false(self):
        """Проверка поиска по частичному совпадению значения параметра, где есть частичное совпадение записи
        не включаются в результат
        - два параметра два файла"""
        pass

