from typing import Dict


class Trie(object):
    # a_ord = ord("a")

    class Node(object):
        def __init__(self, value: str = None) -> None:
            self.value = value
            self.children: Dict[str, Trie.Node] = {}
            self.is_endof_word = False

        def __repr__(self) -> str:
            return f"Node={self.value}|{self.is_endof_word}"

        def has_child(self, letter: str):
            if len(letter) != 1:
                raise ValueError("You should specify a letter.")

            return not (self.children.get(letter) is None)

        def add_child(self, letter):
            self.children[letter] = Trie.Node(letter)

        def get_child(self, letter: str):
            return self.children.get(letter)

        def remove_child(self, letter: str):
            if not self.has_child(letter):
                return None
            return self.children.pop(letter)

        @property
        def has_nochild(self):
            return len(self.children) == 0

    def __init__(self) -> None:
        self.root = Trie.Node(" ")

    def insert(self, word: str):
        current = self.root
        for letter in word:
            if not current.has_child(letter):
                current.add_child(letter)
            current = current.get_child(letter)

        current.is_endof_word = True

    def contains(self, word):
        current = self.root
        for letter in word:
            if not current.has_child(letter):
                return False
            current = current.get_child(letter)

        return current.is_endof_word

    def traverse_postorder(self, root="default"):
        if root == "default":
            root = self.root

        print(root)

        for child in root.children.values():
            self.traverse_postorder(child)

    def traverse_preorder(self, root="default"):
        if root == "default":
            root = self.root

        for child in root.children.values():
            self.traverse_preorder(child)

        print(root)

    def remove_word(self, word: str, root="default", index: int = 0):
        if root == "default":
            root = self.root

        if index == len(word):
            root.is_endof_word = False
            return

        child = root.get_child(word[index])
        if child is None:
            return

        self.remove_word(word, child, index + 1)

        if child.has_nochild and not child.is_endof_word:
            print(root)
            root.remove_child(child.value)

    def __auto_completion(self, word_prefix="None", words: list = None, root="default", curr_word: str = ""):
        if root == "default":
            root = self.root

        if words is None:
            words = []

        if root.value != self.root.value:
            curr_word += root.value

        if root.is_endof_word:
            words.append(word_prefix + curr_word)
            # print(words)

        if root.has_nochild:
            return

        for child in root.children.values():
            self.__auto_completion(word_prefix, words, child, curr_word)

    def auto_completion(self, word: str):

        last_root = self.get_lastroot_of(word)
        if last_root is None:
            return
        results = []
        self.__auto_completion(word_prefix=word[:-1], words=results, root=last_root)
        return results

    def get_lastroot_of(self, word: str):
        curr_root = self.root
        for letter in word:
            if not curr_root.has_child(letter):
                return
            curr_root = curr_root.get_child(letter)

        return curr_root


trie = Trie()
trie.insert("lay")
trie.insert("layer")
trie.insert("layered")
trie.insert("laid")
trie.insert("laider")
trie.insert("laidererdg")


print(trie.auto_completion(""))
# trie.remove_word("layer")
print("done")
