class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        w = set(wordList)

        if endWord not in w:
            return 0

        dist = 0
        q = deque([beginWord])

        while q:
            dist += 1

            for _ in range(len(q)):
                curr = q.popleft()

                if curr == endWord:
                    return dist

                for i in range(len(curr)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        if j != curr[i]:
                            new = curr[:i] + j + curr[i + 1:]

                            if new in w:
                                q.append(new)
                                w.remove(new)

        return 0