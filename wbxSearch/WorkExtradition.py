from wbxSearch import WorkCSV, Extradition


class WorkExtradition:
    def __init__(self, path_read_file: str, path_write_file: str = ""):
        self.csv = WorkCSV(file_name=path_read_file)
        self._data_csv = self.csv.read_csv()
        self.path_write_file = path_write_file
        self._list_ex = [Extradition(x) for x in self._data_csv]

        """в этот лист записываются результаты поиска выдач, потом из этого листа
        # формируем этот файл, либо удалям эти выдачи из листа list_ex"""
        self._new_list_ex = []

        if self.path_write_file:
            self._new_csv = WorkCSV(file_name=path_write_file)

    def param_search(self, param: str,
                     value_param: str,
                     complete_match: bool = True,
                     contains: bool = True) -> list:
        """
        ищем записи по параметру в выдачах
        :param param: наименование параметра по которому ищем(всего их 10, список в шапке класса Extradition)
        :param value_param: значение параметра по которому ищем
        :param complete_match: полное совпадение
        :param contains: наоборот ищем выдачи где нет kind
        :return: list с подходящими выдачами
        """
        if complete_match and contains:
            result_list = [x for x in self._list_ex if value_param == x.get_param(param)]
        elif complete_match is False and contains:
            result_list = [x for x in self._list_ex if value_param in x.get_param(param)]
        elif complete_match and contains is False:
            result_list = [x for x in self._list_ex if value_param != x.get_param(param)]
        elif complete_match is False and contains is False:
            result_list = [x for x in self._list_ex if value_param not in x.get_param(param)]
        else:
            raise "Не правильно выставлены условия"

        self._new_list_ex += result_list
        return result_list

    def search_query_search(self, search_query: str, complete_match: bool = True, contains: bool = True) -> list:
        """
        ищем записи по 1 столбцу в выдачах
        :param search_query: наименование search_query по которому ищем
        :param complete_match: полное совпадение
        :param contains: наоборот ищем выдачи где нет search_query
        :return: list с подходящими выдачами
        """
        return self.param_search("search_query", search_query, complete_match, contains)

    def search_preset_id(self, preset_id: str, complete_match: bool = True, contains: bool = True) -> list:
        """
        ищем записи по 2 столбцу в выдачах
        :param preset_id: наименование preset_id по которому ищем
        :param complete_match: полное совпадение
        :param contains: наоборот ищем выдачи где нет preset_id
        :return: list с подходящими выдачами
        """
        return self.param_search("preset_id", preset_id, complete_match, contains)

    def active_search(self, active: bool = True) -> list:
        """ищем записи по 3 столбцу в выдачах, это поле актив, оно бывает двух видов yes и no,
        по умолчанию ищем yes"""
        result_list = [x for x in self._list_ex if x.get_active() is active]
        self._new_list_ex += result_list
        return result_list

    def kind_search(self, kind: str, complete_match: bool = True, contains: bool = True) -> list:
        """
        ищем записи по 4 столбцу в выдачах
        :param kind: наименование kind по которому ищем
        :param complete_match: полное совпадение
        :param contains: наоборот ищем выдачи где нет kind
        :return: list с подходящими выдачами
        """
        return self.param_search("kind", kind, complete_match, contains)

    def parent_search(self, parent: str, complete_match: bool = True, contains: bool = True) -> list:
        """
        ищем записи по 5 столбцу в выдачах
        :param parent: наименование parent по которому ищем
        :param complete_match: полное совпадение
        :param contains: наоборот ищем выдачи где нет kind
        :return: list с подходящими выдачами
        """
        return self.param_search("parent", parent, complete_match, contains)

    def get_new_list_ex(self):
        return self._new_list_ex

    def write_file(self) -> bool:
        """записываем результат в файл у которого путь path_write_file"""
        if self.path_write_file == "":
            raise "Не указан path_write_file"
        if not self._new_list_ex:
            self._new_csv.write_csv([])
            return True

        new_data_csv = [x.record_for_write_file() for x in self._new_list_ex]
        self._new_csv.write_csv(new_data_csv)
        return True
