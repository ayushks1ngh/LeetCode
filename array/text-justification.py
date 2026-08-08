class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0
        n = len(words)
        
        while i < n:
            line = []
            letters = 0

            while i < n and letters + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                letters += len(words[i])
                i += 1
            
            if i == n or len(line) == 1:
                s = " ".join(line)
                s += " " * (maxWidth - len(s))
                res.append(s)
            else:
                total_spaces = maxWidth - letters
                gaps = len(line) - 1
                even_space = total_spaces // gaps
                extra_space = total_spaces % gaps
                s = ""

                for j in range(gaps):
                    s += line[j]
                    s += " " * even_space
                    if j < extra_space:
                        s += " "
                
                s += line[-1]
                res.append(s)
        return res