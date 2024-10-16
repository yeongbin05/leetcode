class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # 현재 문자가 자식 노드에 없으면 새 노드를 추가
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # 단어의 끝을 표시
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            # 현재 문자가 자식 노드에 없다면 False 반환
            if char not in node.children:
                return False
            node = node.children[char]
        # 끝까지 탐색한 후, 단어의 끝이 표시된 노드인지 확인
        return node.is_end_of_word 
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            # 현재 문자가 자식 노드에 없다면 False 반환
            if char not in node.children:
                return False
            node = node.children[char]
        # prefix의 모든 문자가 트라이에 존재하면 True 반환
        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
