import os
import re


class ParseFile:
    def __init__(self, filename, week):
        self.week = week
        self.create_directory_if_not_exists(self.week)
        self.result = self.parse_fitness_file(filename)

    def create_directory_if_not_exists(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Diretório '{directory}' criado com sucesso.")
        else:
            print(f"O diretório '{directory}' já existe.")
            
    def parse_fitness_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
        return self.parse_fitness_goals(data)
    
    def get_result(self):
        return self.result


    def parse_fitness_goals(self, data):
        groups = {}
        current_group = None
        
        for line in data.split('\n'):
            line = line.strip()
            
            if not line:
                continue
            
            # Identify group names
            if not line.startswith("-") and not line.startswith("Meta") and not line.startswith("Feito"):
                current_group = line.replace("*", "")
                groups[current_group] = {"members": [], "meta": 0, "total": 0}
            
            # Parse member data
            elif line.startswith("-"):
                match = re.match(r"- ([^\d]+) (\d+)/(\S+)", line)
                if match:
                    name, exercises, goal = match.groups()

                    exercises = int(exercises) if exercises.isdigit() else 0
                    goal =      int(goal)      if goal.isdigit()      else 0
                    if goal == 0:
                        exercises = 0
                        
                    groups[current_group]["members"].append({
                        "name": name.strip(),
                        "exercises": exercises,
                        "goal": goal
                    })
            
            # Parse group meta
            elif line.startswith("Meta"):
                match = re.match(r"Meta:\s*(\d+)", line)
                if "/" in line:
                    match = re.match(r"Meta:\s*\d+/(\d+)", line)
                
                
                if match:
                    meta = match.group(1)
                    groups[current_group]["meta"] = int(meta) if meta.isdigit() else 0
            
            # Parse group total
            elif line.startswith("Feito"):
                match = re.match(r"Feito: (\d+)", line)
                if match:
                    total = match.group(1)
                    groups[current_group]["total"] = int(total)
        
        return groups