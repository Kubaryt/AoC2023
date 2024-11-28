from script1 import Symbol, SymbolList


class NewSymbolList(SymbolList):
    def find_gears(self, symbolListslist: list) -> list[int]:
        valid_symbols = []
        if self.symbols == [] or self.symbols is None:
            return []
        connected_lists = []
        if self.line - 1 >= 0:
            connected_lists = symbolListslist[self.line -1].symbols
        try:
            connected_lists += symbolListslist[self.line +1].symbols
        except IndexError:
            pass

        connected_lists_symbol_type_symbols_indexes = []
        for symbol in connected_lists:
            if symbol.type == 'number':
                for index in symbol.index:
                    connected_lists_symbol_type_symbols_indexes.append(index)
        self_symbol_type_symbols_indexes = []
        for symbol in self.symbols:
            if symbol.type == 'number':
                for index in symbol.index:
                    self_symbol_type_symbols_indexes.append(index)
        for symbol in self.symbols:
            if symbol.type == 'number':
                continue
            for index in symbol.index:
                attached_symbols = []
                if index in connected_lists_symbol_type_symbols_indexes or index + 1 in connected_lists_symbol_type_symbols_indexes + self_symbol_type_symbols_indexes or index - 1 in connected_lists_symbol_type_symbols_indexes + self_symbol_type_symbols_indexes:
                    connected_to_local_list = list(filter(lambda x: index in x.index or index + 1 in x.index or index - 1 in x.index, connected_lists + self.symbols))
                    for _symbol in connected_to_local_list:
                        if _symbol.type == 'number':
                            attached_symbols.append(int(_symbol.chars))
                    if len(attached_symbols) >= 2:
                        valid_symbols.append(attached_symbols[0] * attached_symbols[1])
                        break
        return valid_symbols

def get_symbols(file_name: str) -> list[NewSymbolList] | None:
    symbol_lists_list = []
    with open(file_name, "r") as f:
        if f == "":
            return None
        i = 0
        for line in f:
            symbol_list = NewSymbolList()
            chars_found = {
                "dot" : 1,
                "number" : 0,
                "gears" : 0
            }
            j = 0
            line = line.strip()
            symbol_list.line = i
            new_symbol = Symbol()
            for char in line:
                if char == ".":
                    chars_found["dot"] = 1
                else:
                    if chars_found["dot"]:
                        if new_symbol is not None:
                            symbol_list.symbols.append(new_symbol)
                        new_symbol = Symbol()
                        chars_found["number"] = 0
                        chars_found["gears"] = 0
                    chars_found["dot"] = 0
                    if char in "0123456789":
                        if chars_found["symbol"] == 1:
                            symbol_list.symbols.append(new_symbol)
                            new_symbol = Symbol()
                        new_symbol.type = "number"
                        chars_found["number"] = 1
                        chars_found["gears"] = 0
                    elif char == "*":
                        if chars_found["number"] == 1:
                            symbol_list.symbols.append(new_symbol)
                            new_symbol = Symbol()
                        new_symbol.type = "gears"
                        chars_found["number"] = 0
                        chars_found["gears"] = 1
                    new_symbol.chars += char
                    new_symbol.index.append(j)
                j += 1
            if symbol_list.symbols[:1] != new_symbol:
                symbol_list.symbols.append(new_symbol)
            symbol_lists_list.append(symbol_list)
            i += 1
    return symbol_lists_list

def validate_symbols_list(symbol_lists_list: list[NewSymbolList]) -> list[list[int]]:
    valid_symbols_numbers = []
    for symbol_list in symbol_lists_list:
        valid_symbols_numbers += symbol_list.find_gears(symbol_lists_list)
    return valid_symbols_numbers


if __name__ == "__main__":
    _symbol_lists = get_symbols("input")
    _valid_symbols_numbers = validate_symbols_list(_symbol_lists)
    print(sum(_valid_symbols_numbers))