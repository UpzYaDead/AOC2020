from typing import Dict, Set, List

RAW = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

#parse to a dict with as keys, the rule numbers
#as values, the options, which are either (sets of ) rules
# or 'a', 'b'

class Rules:
    def __init__(self, raw_input: str) -> None:
        self.input = raw_input
        self.all_combinations: Set[str] = set()
        self.rules: Dict[int, List[str]] = {}

    def parse(self) -> None:
        input = self.input.split("\n")
        for line in input:
            if not line:
                break
            rule_nmbr, rest = line.split(": ")
            rest = rest.split(" | ")
            if len(rest) > 1:
                temp = []
                for option in rest:
                    temp.append([str(x) for x in option.split()])
                self.rules[int(rule_nmbr)] = temp
            else:
                temp = []
                for rules in rest:
                    for x in rules.split():
                        if x.isdigit():
                            temp.append(str(x))
                        else:
                            temp.append(x[1])
                self.rules[int(rule_nmbr)] = temp
                # self.rules[int(rule_nmbr)] = [str(x) for rules in rest for x in rules.split()]

    def get_all_combinations(self, rule_nmr: int) -> str:
        print(f"input {rule_nmr} result {self.rules[rule_nmr][0]}")
        if self.rules[rule_nmr][0] == "a" or self.rules[rule_nmr][0] == "b":
            self.letters.append(self.rules[rule_nmr][0])
            return self.rules[rule_nmr][0]
        if isinstance(self.rules[rule_nmr], list):
            # do loop over lists
            for option in self.rules[rule_nmr]:
                for rule in option:
                    self.get_all_combinations(int(rule))
        else:
            for rule in self.rules[rule_nmr]:
                self.get_all_combinations((int(rule)))

    def solve(self):
        seen_before: Dict[int, str] = {}
        #we only need to solve for rule 0
        for rule in self.rules[0]: # 4, 1, 5
            print(f"\nfirst rule {rule}")
            self.letters = []
            letters = self.get_all_combinations(int(rule))
            print(self.letters)





rule = Rules(RAW)
rule.parse()
print(rule.rules)
print("\n-0-0-0\n")

rule.solve()
print(rule.all_combinations)


