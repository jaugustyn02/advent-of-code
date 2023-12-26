from collections import defaultdict
import math

# input = 'data/sample.txt'
input = 'data/puzzle.txt'


workflows = {}

class RatingBoundries:
    def __init__(self, min, max):
        self.min = min
        self.max = max


def part_combinations(part: dict[str:RatingBoundries]):
    return math.prod([part[rate].max - part[rate].min + 1 for rate in part])
    
    
def part_copy(part: dict[str:RatingBoundries]):
    return {rate: RatingBoundries(part[rate].min, part[rate].max) for rate in part}


def evaluate_part(part: dict[str:RatingBoundries], workflow_name: str):
    if workflow_name == 'A':
        return part_combinations(part)
    if workflow_name == 'R':
        return 0
    workflow = workflows[workflow_name]
    
    combine_combinations = 0
    for rule in workflow:
        if rule == 'R':
            return combine_combinations
        if rule == 'A':
            return combine_combinations + part_combinations(part)
        if ':' not in rule:
            return combine_combinations + evaluate_part(part, rule)
        
        rule, destination = rule.split(':')
        if '>' in rule:
            rate, boundry = rule.split('>')
            if part[rate].min > int(boundry):
                return combine_combinations + evaluate_part(part, destination)
            elif part[rate].max > int(boundry):
                new_part = part_copy(part)
                new_part[rate].min = int(boundry)+1
                part[rate].max = int(boundry)
                combine_combinations += evaluate_part(new_part, destination)
        if '<' in rule:
            rate, boundry = rule.split('<')
            if part[rate].max < int(boundry):
                return combine_combinations + evaluate_part(part, destination)
            elif part[rate].min < int(boundry):
                new_part = part_copy(part)
                new_part[rate].max = int(boundry)-1
                part[rate].min = int(boundry)
                combine_combinations += evaluate_part(new_part, destination)
    return combine_combinations

  
def main():
  with open(input) as f:
    
    for workflow in f:
      if workflow == "\n":
        break
      name, rules = workflow.split('{')
      rules = rules.rstrip().replace('}', '').split(',')
      for rule in rules:
        workflows[name] = rules
        
    part = {'x': RatingBoundries(1, 4000), 'm': RatingBoundries(1, 4000), 'a': RatingBoundries(1, 4000), 's': RatingBoundries(1, 4000)}
    print(evaluate_part(part, 'in'))
      
    
if __name__ == "__main__":
  main()
