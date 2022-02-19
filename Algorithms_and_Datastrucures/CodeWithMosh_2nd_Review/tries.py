from typing import Union


class RadixNode:
    def __init__(self, letter: str = None):
        self.children: dict[str, RadixNode] = {}
        self._letter = letter
        self.is_last_letter = False

    def has_letter(self, letter: str):
        return self.children.get(letter) is not None

    def add_letters(self, letters: str):
        for letter in letters:
            self.children.update(
                {letter: RadixNode(letter)}
            )

    def get_child(self, letter: str):
        return self.children.get(letter)

    def delete_child(self, child: Union[str, 'RadixNode']):
        letter = ""
        if isinstance(child, RadixNode):
            letter = child.letter
        elif isinstance(child, str):
            letter = child
        else:
            raise TypeError
        return self.children.pop(letter)

    @property
    def letter(self):
        return self._letter

    @property
    def has_children(self):
        return len(self.children) != 0

    def __repr__(self):
        return f'RN<{self._letter}>'

    def __eq__(self, other):
        if isinstance(other, str):
            return self._letter == other
        elif isinstance(other, RadixNode):
            return self._letter == other.letter
        else:
            raise TypeError('A RadixNode can only be equal to a letter or another RedixNode')


class RadixTree:
    def __init__(self):
        self._base = RadixNode()

    def add_word(self, word: str):
        current = self._base
        for letter in word:
            if not current.has_letter(letter):
                current.add_letters(letter)
            current = current.get_child(letter)
        current.is_last_letter = True

    def has_word(self, word: str):
        current = self._base
        for letter in word:
            if not current.has_letter(letter):
                return False
            current = current.get_child(letter)
        return current.is_last_letter

    def delete_word(self, word: str):
        path = []
        current = self._base
        for letter in word:
            if not current.has_letter(letter):
                return False
            path.append(current)
            current = current.get_child(letter)
        path.append(current)

        if not current.is_last_letter:
            return False

        current.is_last_letter = False

        for i in range(len(path) - 1, 0, -1):
            node = path[i]
            parent = path[i - 1]
            if (not node.is_last_letter) and (not node.has_children):
                parent.delete_child(node)
        return True


tree = RadixTree()
tree.add_word('add')
tree.add_word('address')
# tree.add_word('addrenaline')

print(tree.has_word('add'))
print(tree.has_word('address'))
print(tree.has_word('addrenaline'))
print(tree.has_word('ad'))
print(tree.has_word('somt'))
print(tree.has_word('anohter'))

print(tree.delete_word('adds'))
print(tree.delete_word('address'))
print(tree.delete_word('address'))
print(tree.delete_word('address'))
