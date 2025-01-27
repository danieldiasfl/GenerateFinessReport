import math
import os
import tkinter as tk
from PIL import Image, ImageFilter, ImageTk, ImageOps, ImageFont
from GetRankings import GetRankings

class Dashboards:    
    def __init__(self, rankings, week):
        self.week = week
        
        root = tk.Tk()
        root.title("Canva")

        root.geometry("1200x800")  # Tamanho da janela

        # Carregar a imagem do pódio de fundo


        # Criar um canvas para desenhar a tela
        self.canvas = tk.Canvas(root, width=1200, height=800)
        self.canvas.pack()
    
        self.create_dashboards(rankings)
        #createRanking(ranking, canvas)
        #create_group_ranking(ranking_group, canvas)
        #create_unmet(failed, canvas)
    
    def create_dashboards(self, rankings):
        self.create_ranking_individual(rankings.get_ranking_individual())
        self.create_ranking_group(rankings.get_ranking_group())
        self.create_ranking_accumulated(rankings.get_accumulated_individual())
        self.create_ranking_accumulated_group(rankings.get_accumulated_group())
        self.create_shame_wall(rankings.get_failed_individual())
        
        
    def create_ranking_individual (self, ranking):
        first_exercises = ranking[0]["exercises"]
        first_place = ([member['name'] for member in ranking if member['exercises'] == first_exercises])

        second_index = 0 + len(first_place)
        second_exercises = ranking[second_index]["exercises"]
        second_place = ([member['name'] for member in ranking if member['exercises'] == second_exercises])
        
        third_index = second_index + len(second_place)
        third_exercises = ranking[third_index]["exercises"]
        third_place = ([member['name'] for member in ranking if member['exercises'] == third_exercises])
        
        self.create_window_ranking_individual(first_exercises, first_place, second_exercises, second_place, third_exercises, third_place, self.canvas)
        self.create_window_ranking_destaque(first_exercises, first_place, self.canvas)
        
    def create_ranking_group(self, ranking):
        self.create_window_grupo_destaque(ranking[0][0], ranking[0][1], ranking[0][2], self.canvas)
            
    def create_ranking_accumulated (self, ranking):
        first_exercises = ranking[0][1]
        first_place = ([member[0] for member in ranking if member[1] == first_exercises])

        second_index = 0 + len(first_place)
        second_exercises = ranking[second_index][1]
        second_place = ([member[0] for member in ranking if member[1] == second_exercises])
        
        third_index = second_index + len(second_place)
        third_exercises = ranking[third_index][1]
        third_place = ([member[0] for member in ranking if member[1] == third_exercises])
        
        self.create_window_ranking_individual_accum(first_exercises, first_place, second_exercises, second_place, third_exercises, third_place, self.canvas)        
        
    def create_ranking_accumulated_group (self, ranking):
        print (ranking)
        first_exercises = ranking[0][1]
        print(first_exercises)
        first_place = ([member[0] for member in ranking if member[1] == first_exercises])

        second_index = 0 + len(first_place)
        second_exercises = ranking[second_index][1]
        second_place = ([member[0] for member in ranking if member[1] == second_exercises])
        
        #third_index = second_index + len(second_place)
        #third_exercises = ranking[third_index][1]
        #third_place = ([member[0] for member in ranking if member[1] == third_exercises])
        third_index = second_index 
        third_exercises = second_exercises
        third_place = second_place
        
        self.create_window_ranking_group_accum(first_exercises, first_place, second_exercises, second_place, third_exercises, third_place, self.canvas)        
           
    def create_shame_wall(self, shame_people):
        self.create_window_shame(shame_people)
    
    def create_window_ranking_individual (self, first_exercises, first_place, second_exercises, second_place, third_exercises, third_place, canvas):
        self.canvas.delete("all")
        podium_bg = self.load_image("pics/podio.jpg", size=(1200, 800))
        # Adicionar o fundo do pódio
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Ranking da semana", font=("arial.ttf", 61, "bold"), fill="gray")
        self.canvas.create_text(600, 80, text="Ranking da semana", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        

        member_images = []

        self.createImages(first_place, 550, 140, self.canvas, member_images, 0, 0, 0)
        self.canvas.create_text(600, 410, text=str(first_exercises) + " exercicios", font=("arial.ttf", 20, "bold"), fill="black")

        self.createImages(second_place, 280, 190, self.canvas, member_images, 0, 0, 0)  
        self.canvas.create_text(330, 480, text=str(second_exercises) + " exercicios", font=("arial.ttf", 20, "bold"), fill="black")
        
        self.canvas.create_text(880, 510, text=str(third_exercises) + " exercicios", font=("arial.ttf", 20, "bold"), fill="black")
        self.createImages(third_place, 815, 250, self.canvas, member_images, 0, 0, 0)

        self.save_canvas_as_image(self.canvas, str(self.week) + "/rankingIndividual.jpg")
        
    
    def create_window_ranking_individual_accum (self, first_exercises, first_place, second_exercises, second_place, third_exercises, third_place, canvas):
        self.canvas.delete("all")
        podium_bg = self.load_image("pics/podio.jpg", size=(1200, 800))
        # Adicionar o fundo do pódio
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Ranking Geral Individual", font=("arial.ttf", 61, "bold"), fill="gray")
        self.canvas.create_text(600, 80, text="Ranking Geral Individual", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        

        member_images = []

        self.createImages(first_place, 550, 140, self.canvas, member_images, 0, 0, 0)
        self.canvas.create_text(600, 410, text=str(first_exercises) + " pontos", font=("arial.ttf", 20, "bold"), fill="black")

        self.createImages(second_place, 280, 190, self.canvas, member_images, 0, 0, 0)  
        self.canvas.create_text(330, 480, text=str(second_exercises) + " pontos", font=("arial.ttf", 20, "bold"), fill="black")
        
        self.canvas.create_text(880, 510, text=str(third_exercises) + " pontos", font=("arial.ttf", 20, "bold"), fill="black")
        self.createImages(third_place, 815, 250, self.canvas, member_images, 0, 0, 0)

        self.save_canvas_as_image(self.canvas, str(self.week) + "/rankingIndividualAccum.jpg")
        
    def create_window_ranking_group_accum (self, first_exercises, first_place, second_exercises, second_place, third_exercises, third_place, canvas):
        self.canvas.delete("all")
        podium_bg = self.load_image("pics/podio.jpg", size=(1200, 800))
        # Adicionar o fundo do pódio
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Ranking geral grupos", font=("arial.ttf", 61, "bold"), fill="gray")
        self.canvas.create_text(600, 80, text="Ranking geral grupos", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        

        member_images = []

        self.createImages(first_place, 550, 140, self.canvas, member_images, 0, 0, 0)
        self.canvas.create_text(600, 410, text=str(first_exercises) + " pontos", font=("arial.ttf", 20, "bold"), fill="black")

        self.createImages(second_place, 280, 190, self.canvas, member_images, 0, 0, 0)  
        self.canvas.create_text(330, 480, text=str(second_exercises) + " pontos", font=("arial.ttf", 20, "bold"), fill="black")
        
        self.canvas.create_text(880, 510, text=str(third_exercises) + " pontos", font=("arial.ttf", 20, "bold"), fill="black")
        self.createImages(third_place, 815, 250, self.canvas, member_images, 0, 0, 0)

        self.save_canvas_as_image(self.canvas, str(self.week) + "/rankingGrupsAccum.jpg")
        
        
    def create_window_ranking_destaque (self, first_exercises, first_place, canvas):

        self.canvas.delete("all")
        # Adicionar o fundo do pódio
        podium_bg = self.load_image("pics/destaque.jpg", size=(1200, 800))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Destaque da semana", font=("arial.ttf", 61, "bold"), fill="light gray")
        self.canvas.create_text(600, 80, text="Destaque da semana", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        
        self.canvas.create_text(600, 150, text=str (first_exercises) + " exercícios", font=("Arial", 40))
        
        member_images = []
        self.createImages(first_place, 300, -220, self.canvas, member_images, 3, 300, 450)

        # Exibir a interface gráfica
        self.save_canvas_as_image(self.canvas, str(self.week) + "/Destaque.jpg")
        #root.mainloop()
        
    def create_window_grupo_destaque (self, first_group, first_exercises_person, first_exercises, canvas):
        self.canvas.delete("all")
        # Carregar a imagem do pódio de fundo
        podium_bg = self.load_image("pics/vencedor.jpg", size=(1200, 800))
        # Adicionar o fundo do pódio
        font = ImageFont.truetype("arial.ttf", 80)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Vencedor da Semana", font=("arial.ttf", 61, "bold"), fill="light gray")
        self.canvas.create_text(600, 80, text="Vencedor da Semana", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        self.canvas.create_text(600, 150, text=first_group, font=("Arial", 61, "bold"), fill="gold")
        self.canvas.create_text(600, 150, text=first_group, font=("Arial", 60, "bold"), fill="black")
        self.canvas.create_text(600, 150, text=first_group, font=("Arial", 59, "bold"), fill="white")
        
        
        self.canvas.create_text(600, 220, text=str(first_exercises) + " exercicios", font=("Arial", 40), fill="white")
        print (first_group)
        member_images = []
        self.createImages([first_group], 600, 350, self.canvas, member_images, 1, 400, 520)

        # Exibir a interface gráfica
        self.save_canvas_as_image(self.canvas, str(self.week) + "/rankingGroup.jpg")
        #root.mainloop()
        
    def create_window_shame(self, shame_people):
        print(shame_people)
        self.canvas.delete("all")
        # Adicionar o fundo do pódio
        podium_bg = self.load_image("pics/vergonha.jpg", size=(1200, 800))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Parede da vergonha", font=("arial.ttf", 61, "bold"), fill="light gray")
        self.canvas.create_text(600, 80, text="Parede da vergonha", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        
        #self.canvas.create_text(600, 150, text=str (shame_people) + " exercícios", font=("Arial", 40))
        
        shame_list = []
        for  value in shame_people:
            print (value)
            shame_list.append(value["name"]) 
    
        member_images = []
        self.createImages(shame_list, 300, -220, self.canvas, member_images, 3, 300, 450)

        # Exibir a interface gráfica
        self.save_canvas_as_image(self.canvas, str(self.week) + "/Mural_vergonha.jpg")
        #root.mainloop()
        
    # Função para carregar e exibir uma imagem
    def load_image(self, image_path, size=(100, 100)):
        img = Image.open(image_path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)

    def save_canvas_as_image(self, canvas, filename, dpi=300):
        # Força a atualização da interface gráfica antes de capturar
        self.canvas.update()
        
        # Salva o conteúdo do canvas em um arquivo PostScript
        ps_filename = "temp_canvas.ps"
        self.canvas.postscript(file=ps_filename, colormode="color")

        # Abre a imagem PostScript usando Pillow
        img = Image.open(ps_filename)

        # Remove espaços vazios ao redor do conteúdo
        #img = img.convert("RGB").crop(img.getbbox())
        width, height = img.size
        new_width = width * dpi // 72  # Ajuste a largura com base no DPI
        new_height = height * dpi // 72 
        img = img.resize((new_width, new_height), Image.LANCZOS)
        
        img = img.filter(ImageFilter.SMOOTH)
        # Redimensiona para aumentar a qualidade
        #img = ImageOps.scale(img, scale)

        # Salva no formato desejado
        img.save(filename, "PNG")
        print(f"Imagem salva como {filename}")

    def createImages(self, place_list, first_x, first_y, canvas, member_images, force_square, force_ratio, force_y):
        length = len(place_list)
        if length % 2 != 0: length = length - 1
        
        square = math.ceil( (math.sqrt( len(place_list) )) )
        if force_square != 0: square = force_square
        
        size_ratio = int (200/square)
        if force_ratio != 0: size_ratio = force_ratio
        
        x = first_x - len(place_list) /2 * (square - 1)
        y = first_y - len(place_list) /2 * square
        if force_y != 0: y = force_y
        
        i = 0
        
        for member in place_list:
            if (i == len(place_list) - 1 and i % square == 0 and i != 0):
                y = y + size_ratio
                x = first_x + size_ratio / 2
            elif (i % square == 0):
                y = y + size_ratio
                if force_y != 0: y = force_y
                x = first_x - len(place_list) /2 * (square - 1)
            else:
                x = x + size_ratio
                
            i = i + 1
            print (member)
            image = self.load_image("pics/" + member + ".jpg", size=(size_ratio, size_ratio))
            member_images.append(image)  # Armazenar a imagem na lista
            self.canvas.create_image(x, y, anchor=tk.CENTER, image=image)