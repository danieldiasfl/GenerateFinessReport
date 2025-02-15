
import csv
from collections import defaultdict
import glob

class GetRankings:
    def __init__(self, parsed_results, week):
        self.results = parsed_results
        self.week = week
        self.ranking_individual = self.calculate_ranking_individual()
        self.ranking_group = self.calculate_ranking_group()
        self.failed_individual = self.calculate_unmet_goals()
        self.carregados = self.calculate_carregados()
        #self.failed_group = get_unmetGroup_goals(result)  
    
    def calculate_ranking_individual(self):
        all_members = [
            member for group in self.results.values() for member in group['members']
        ]
        sorted_members = sorted(all_members, key=lambda x: x['exercises'], reverse=True)
        sorted_members_name = sorted(all_members, key=lambda x: x['name'], reverse=False)
        
        #write output to file
        with open( str(self.week) + "/out_individual" + ".csv", "w", newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Name", "Exercises", "Goal"])
            for member in sorted_members_name:
                csv_writer.writerow([member["name"], member["exercises"], member["goal"]])
            
        return sorted_members
    
    def get_ranking_individual(self):
        return self.ranking_individual
    
    def get_accumulated_individual(self):

        exercise_totals = defaultdict(int)
        for weekNumber in range(1, int(self.week) + 1):
            try:
                with open(f'{weekNumber}/out_individual.csv', 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    next(reader)  # Pular cabeçalho
                    
                    for row in reader:
                        name, exercises, goal = row
                        exercise_totals[name] += int(exercises)
            
            except FileNotFoundError:
                print(f"Arquivo '{weekNumber}' não encontrado. Pulando...")
            except Exception as e:
                print(f"Erro ao processar '{weekNumber}': {e}")

        result = sorted(exercise_totals.items(), key=lambda x: x[1], reverse=True)
        return result

    def calculate_ranking_group(self):
        all_groups =  [
                (
                    name,
                    data["total"] / sum(1 for member in data["members"] if member["goal"] > 0),
                    data["total"],
                    data["meta"]
                )
                for name, data in self.results.items()
            ]
        sorted_group = sorted(all_groups, key=lambda x: x[1], reverse=True)
        sorted_group_name = sorted(all_groups, key=lambda x: x[0], reverse=False)

        #write output to file
        with open(self.week + "/out_group"  + ".csv", "w", newline='') as csvfile:  
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Group", "Total_pessoa", "Total", "Meta"])
            for group in sorted_group:
                csv_writer.writerow(group)
                
        return sorted_group
                
    def get_ranking_group(self):
        return self.ranking_group
    
    def get_accumulated_group(self):
        group_scores = {}

        for weekNumber in range(1, int(self.week) + 1):
            with open(str (weekNumber) + '/out_group' + '.csv', 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader)  # Pular o cabeçalho

                i = 0
                for row in reader:
                    group_name = row[0]
                    total_value = float(row[1])
                    points_week = 0
                    
                    if (i == 0):
                        points_week = 3
                    elif (total_value > 3):
                        points_week = 1
                    # Somar os valores para cada grupo
                    if group_name in group_scores:
                        group_scores[group_name] += points_week
                    else:
                        group_scores[group_name] = points_week
                    
                    i = i + 1

        # Ordenar os grupos pelo total acumulado em ordem decrescente
        points = sorted(group_scores.items(), key=lambda x: x[1], reverse=True)
        print (points)
        # Atribuir pontos de acordo com as regras
  
        return points

    def calculate_unmet_goals(self):
        unmet = [member for group in self.results.values() for member in group["members"] if member["exercises"] < member["goal"]]
        with open(str(self.week) + "/out_unmet" +  ".csv", "w", newline='') as csvfile:   
            csv_writer = csv.writer(csvfile) 
            csv_writer.writerow(["Unmet Goals"])
            for member in unmet:
                csv_writer.writerow([member["name"], member["exercises"], member["goal"]])
        return unmet
    
    def get_failed_individual(self):
        return self.failed_individual

    def get_unmetGroup_goals(groups):

        with open("out_unmetGroup" + args.filename + ".csv", "w", newline='') as csvfile:   
            csv_writer = csv.writer(csvfile) 
            csv_writer.writerow([])
            csv_writer.writerow(["Unmet Group Goals"])
            for group in get_unmetGroup_goals(result):
                csv_writer.writerow(group)
        return ((name, data["total"], data["meta"]) for name, data in groups.items() if data["total"] < data["meta"])

    def calculate_carregados(self):
        print (self.results.values())
        carregados = [
            member for group in self.results.values() 
            for member in group["members"] 
            if member["exercises"] < 3 and member["goal"] != 0 
        ]
        return carregados
        
    def get_carregados(self):
        return self.carregados