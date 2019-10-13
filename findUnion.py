class UF:

    components = []

    def union(self, p, q):
        qFound = False
        pFound = False
        # print(p, q)

        if (self.connected(p, q)):
            # print("p and q are connected")
            return

        for layer in self.components:
            if q in layer:
                qLayer = layer
                qFound = True
                # print("q Finded")

        for layer in self.components:
            if p in layer:
                pFound = True
                if qFound == True:
                    self.components[self.components.index(layer)] = layer.union(qLayer)
                    self.components.remove(qLayer)

                    # layer.union(qLayer)
                    # print("p and q finded", layer)
                else:
                    layer.add(q)
                    # print("p finded", layer)
        
        if pFound == False:
            if qFound == True:
                qLayer.add(p)
            else:
                self.components.append(set((p, q)))
                # print("none is finded", set((p, q)))

    def getList(self):
        return self.components


    def connected (self, p, q):
        for layer in self.components:
            if (p in layer) & (q in layer):
                return True
        return False

def inputFromFile(filename):
    file_object = open(filename, "r")
    lines = str(file_object.read())
    file_object.close()

    lines = lines.split('\n')
    return [line.split(' ') for line in lines[1:]]

def main():
    lines = inputFromFile("input.txt")

    print(lines)

    uf = UF()

    for line in lines:
        uf.union(int(line[0]), int(line[1]))

    # print(uf.getList())
    # uf.union(9, 10)
    # print(uf.getList())
    # uf.union(10, 11)
    # print(uf.getList())
    # uf.union(11, 16)
    # print(uf.getList())
    # uf.union(124, 196)
    # print(uf.getList())
    # uf.union(10421, 1191266)
    # print(uf.getList())
    # uf.union(10421, 16)
    # print(uf.getList())

    print(uf.getList())

if __name__ == "__main__":
    main()