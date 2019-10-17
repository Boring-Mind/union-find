class UF:
    """Contains unions and can add items to union or check connectivity"""

    components = []

    def union(self, p: int, q: int):
        """Creates union between p and q. Creates p or q, if necessary"""

        q_found = False
        p_found = False

        if self.connected(p, q):
            return

        for layer in self.components:
            if q in layer:
                q_layer = layer
                q_found = True

        for layer in self.components:
            if p in layer:
                p_found = True
                if q_found is True:
                    self.components[self.components.index(layer)] = layer.union(q_layer)
                    self.components.remove(q_layer)
                else:
                    layer.add(q)
        if p_found is False:
            if q_found is True:
                q_layer.add(p)
            else:
                self.components.append(set((p, q)))

    def print_list(self):
        """Prints components list without formatting"""

        print(self.components)

    def connected(self, p: int, q: int) -> bool:
        """Checks, whether p and q are in one union or not"""

        for layer in self.components:
            if (p in layer) & (q in layer):
                return True
        return False


def input_from_file(filename: str) -> [str]:
    """Reads given file and initialize components list"""

    file_object = open(filename, "r")
    lines = str(file_object.read())
    file_object.close()

    lines = lines.split('\n')
    return [line.split(' ') for line in lines]


def main():
    """Initializes program and run it"""

    lines = input_from_file("input.txt")

    print(lines)

    uf = UF()

    for line in lines:
        uf.union(int(line[0]), int(line[1]))

    uf.print_list()


if __name__ == "__main__":
    main()
