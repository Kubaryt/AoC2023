class Symbol:
    chars = str
    index = list[int]
    type = str

    def __init__(self):
        self.chars = ""
        self.index = []
        self.type = "undefined"

    def __str__(self):
        return f"{self.chars} | {self.index} | {self.type}"

class SymbolList:
    line = int
    symbols = list[Symbol]

    def __init__(self):
        self.symbols = []

    def __str__(self):
        return f"{self.line} | {len(self.symbols)}"

    def validate_symbols(self, symbolListslist: list) -> list[int]:
        valid_symbols = []
        if self.symbols == [] or self.symbols is None:
            return []
        connected_lists = []
        print(str(self.line) + "current")
        if self.line - 1 >= 0:
            connected_lists = symbolListslist[self.line -1].symbols
            print(symbolListslist[self.line -1].line)
            for symbol in symbolListslist[self.line -1].symbols:
                print(symbol)
        try:
            connected_lists += symbolListslist[self.line +1].symbols
            print(symbolListslist[self.line + 1].line)
            for symbol in symbolListslist[self.line + 1].symbols:
                print(symbol)
        except IndexError:
            pass

        connected_lists_symbol_type_symbols_indexes = []
        for symbol in connected_lists:
            if symbol.type == 'symbol':
                for index in symbol.index:
                    connected_lists_symbol_type_symbols_indexes.append(index)
        self_symbol_type_symbols_indexes = []
        for symbol in self.symbols:
            if symbol.type == 'symbol':
                for index in symbol.index:
                    self_symbol_type_symbols_indexes.append(index)
        for symbol in self.symbols:
            if symbol.type == 'symbol':
                continue
            for index in symbol.index:
                if index in connected_lists_symbol_type_symbols_indexes or index + 1 in connected_lists_symbol_type_symbols_indexes + self_symbol_type_symbols_indexes or index - 1 in connected_lists_symbol_type_symbols_indexes + self_symbol_type_symbols_indexes:
                    valid_symbols.append(int(symbol.chars))
                    break
        return valid_symbols

def get_symbols(file_name: str) -> list[SymbolList] | None:
    symbol_lists_list = []
    new_symbol = None
    with open(file_name, "r") as f:
        if f == "":
            return None
        i = 0
        for line in f:
            symbol_list = SymbolList()
            chars_found = {
                "dot" : 1,
                "number" : 0,
                "symbol" : 0
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
                        chars_found["symbol"] = 0
                    chars_found["dot"] = 0
                    if char not in "0123456789":
                        if chars_found["number"] == 1:
                            symbol_list.symbols.append(new_symbol)
                            new_symbol = Symbol()
                        new_symbol.type = "symbol"
                        chars_found["number"] = 0
                        chars_found["symbol"] = 1
                    else:
                        if chars_found["symbol"] == 1:
                            symbol_list.symbols.append(new_symbol)
                            new_symbol = Symbol()
                        new_symbol.type = "number"
                        chars_found["number"] = 1
                        chars_found["symbol"] = 0
                    new_symbol.chars += char
                    new_symbol.index.append(j)
                j += 1
            if symbol_list.symbols[:1] != new_symbol:
                symbol_list.symbols.append(new_symbol)
            symbol_lists_list.append(symbol_list)
            i += 1
    return symbol_lists_list


def validate_symbols_list(symbol_lists_list: list[SymbolList]) -> list[list[int]]:
    valid_symbols_numbers = []
    for symbol_list in symbol_lists_list:
        valid_symbols_numbers += symbol_list.validate_symbols(symbol_lists_list)
    return valid_symbols_numbers


if __name__ == "__main__":
    _symbol_lists = get_symbols("input")
    _valid_symbols_numbers = validate_symbols_list(_symbol_lists)
    print(sum(_valid_symbols_numbers))
