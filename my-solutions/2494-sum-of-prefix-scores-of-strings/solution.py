class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Solution(object):
    def sumPrefixScores(self, words):
        root = TrieNode()

        # Trie에 단어와 그 접두사를 삽입하고 카운트 증가
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                node.count += 1

        # 각 단어의 접두사 점수를 계산
        result = []
        for word in words:
            node = root
            score = 0
            for char in word:
                node = node.children[char]
                score += node.count
            result.append(score)
        
        return result
