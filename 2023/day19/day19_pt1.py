from collections import defaultdict

# input = 'sample.txt'
input = 'puzzle.txt'


workflows = {}


def evaluate_part(part, workflow_name):
  if workflow_name == 'A':
    return True
  if workflow_name == 'R':
    return False
  workflow = workflows[workflow_name]
  for rule in workflow:
    if rule == 'R':
      return False
    if rule == 'A':
      return True
    if ':' not in rule:
      return evaluate_part(part, rule)
    
    rule, destination = rule.split(':')
    if '>' in rule:
      rate, boundry = rule.split('>')
      if part[rate] > int(boundry):
        return evaluate_part(part, destination)
    if '<' in rule:
      rate, boundry = rule.split('<')
      if part[rate] < int(boundry):
        return evaluate_part(part, destination)
  return evaluate_part(part, destination)

  
def main():
  with open(input) as f:
    
    for workflow in f:
      if workflow == "\n":
        break
      name, rules = workflow.split('{')
      rules = rules.rstrip().replace('}', '').split(',')
      for rule in rules:
        workflows[name] = rules
    
    res_sum = 0  
    for part in f:
      ratings_value = part.replace('{','').replace('}','').split(',')
      part_ratings = {}
      for rv in ratings_value:
        rate, val = rv.split('=')
        part_ratings[rate] = int(val)
      
      if evaluate_part(part_ratings, 'in'):
        res_sum += sum(part_ratings.values())
    
    print(res_sum)
      
    
if __name__ == "__main__":
  main()
