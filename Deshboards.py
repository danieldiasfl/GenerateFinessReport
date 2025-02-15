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
        #self.create_ranking_individual(rankings.get_ranking_individual())
        #self.create_ranking_group(rankings.get_ranking_group())
        #self.create_ranking_accumulated(rankings.get_accumulated_individual())
        self.create_ranking_accumulated_group(rankings.get_accumulated_group())
        #self.create_shame_wall(rankings.get_failed_individual())
        #self.create_carregados(rankings.get_carregados())
        #self.create_specialthanks()
        

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
        first_exercises = ranking[0][1]
        first_place = ([member[0] for member in ranking if member[1] == first_exercises])

        second_index = 0 + len(first_place)
        second_exercises = ranking[second_index][1]
        second_place = ([member[0] for member in ranking if member[1] == second_exercises])
        
        third_index = second_index + len(second_place)
        print (third_index)
        third_exercises = ranking[third_index][1]
        print (third_exercises)
        third_place = ([member[0] for member in ranking if member[1] == third_exercises])
        print (third_place)
        self.create_window_ranking_group_accum(first_exercises, first_place, second_exercises, second_place, third_exercises, third_place, self.canvas)        
           
    def create_shame_wall(self, shame_people):
        self.create_window_shame(shame_people)
    
    def create_carregados(self, carregados):
        self.create_window_carregados(carregados)
        
    def create_specialthanks (self):
        self.canvas.delete("all")
        podium_bg = self.load_image("pics/agradecimento.jpg", size=(1200, 800))
        # Adicionar o fundo do pódio
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Agradecimento Especial", font=("arial.ttf", 60, "bold"), fill="gray")
        self.canvas.create_text(598, 79, text="Agradecimento Especial", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        

        member_images = []
        thanked1 = ["Junebilos"]
        thanked = ["Le", "Jands", "Jun", "Alec" ]
        thanked2 = [ "Naomi", "Nelso" ]
        self.createImages(thanked1, 600, 600, 200, self.canvas, member_images, 0, 0, 0, 0)
        self.createImages(thanked2, 600, 460, 200, self.canvas, member_images, 0, 0, 0, 75)
        self.createImages(thanked, 600, 280, 200, self.canvas, member_images, 0, 0, 0, 0)
        self.canvas.create_text(600, 520, text="Por carregarem o Junebilos essa semana", font=("arial.ttf", 20, "bold"), fill="black")
        
        self.save_canvas_as_image(self.canvas, str(self.week) + "/thanks.jpg")
        
    def create_window_ranking_individual (self, first_exercises, first_place, second_exercises, second_place, third_exercises, third_place, canvas):
        self.canvas.delete("all")
        podium_bg = self.load_image("pics/podio.jpg", size=(1200, 800))
        # Adicionar o fundo do pódio
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Ranking da semana", font=("arial.ttf", 60, "bold"), fill="gray")
        self.canvas.create_text(598, 79, text="Ranking da semana", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        

        member_images = []

        self.createImages(first_place, 600, 280, 200, self.canvas, member_images, 0, 0, 0, 0)
        self.canvas.create_text(600, 410, text=str(first_exercises) + " exercicios", font=("arial.ttf", 20, "bold"), fill="black")

        self.createImages(second_place, 330, 350, 200, self.canvas, member_images, 0, 0, 0, 0)  
        self.canvas.create_text(330, 480, text=str(second_exercises) + " exercicios", font=("arial.ttf", 20, "bold"), fill="black")
        
        self.canvas.create_text(880, 510, text=str(third_exercises) + " exercicios", font=("arial.ttf", 20, "bold"), fill="black")
        self.createImages(third_place, 880, 380, 200, self.canvas, member_images, 0, 0, 0, 0)

        self.save_canvas_as_image(self.canvas, str(self.week) + "/rankingIndividual.jpg")
        
        
    def create_window_ranking_individual_accum (self, first_exercises, first_place, second_exercises, second_place, third_exercises, third_place, canvas):
        self.canvas.delete("all")
        podium_bg = self.load_image("pics/podio.jpg", size=(1200, 800))
        # Adicionar o fundo do pódio
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Ranking Geral Individual", font=("arial.ttf", 60, "bold"), fill="gray")
        self.canvas.create_text(598, 79, text="Ranking Geral Individual", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)

        member_images = []

        self.createImages(first_place, 600, 280, 200, self.canvas, member_images, 0, 0, 0, 0)
        self.canvas.create_text(600, 410, text=str(first_exercises) + " pontos", font=("arial.ttf", 20, "bold"), fill="black")

        self.createImages(second_place, 330, 350, 200, self.canvas, member_images, 0, 0, 0, 0)  
        self.canvas.create_text(330, 480, text=str(second_exercises) + " pontos", font=("arial.ttf", 20, "bold"), fill="black")
        
        self.canvas.create_text(880, 510, text=str(third_exercises) + " pontos", font=("arial.ttf", 20, "bold"), fill="black")
        self.createImages(third_place, 880, 380, 200, self.canvas, member_images, 0, 0, 0, 0)

        self.save_canvas_as_image(self.canvas, str(self.week) + "/rankingIndividualAccum.jpg")
        
    def create_window_ranking_group_accum (self, first_exercises, first_place, second_exercises, second_place, third_exercises, third_place, canvas):
        self.canvas.delete("all")
        podium_bg = self.load_image("pics/podio.jpg", size=(1200, 800))
        # Adicionar o fundo do pódio
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Ranking geral grupos", font=("arial.ttf", 60, "bold"), fill="gray")
        self.canvas.create_text(598, 79, text="Ranking geral grupos", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        

        member_images = []

        self.createImages(first_place, 600, 280, 200, self.canvas, member_images, 0, 0, 0, 0)
        self.canvas.create_text(600, 410, text=str(first_exercises) + " pontos", font=("arial.ttf", 20, "bold"), fill="black")

        self.createImages(second_place, 330, 350, 200, self.canvas, member_images, 0, 0, 0, 0)  
        self.canvas.create_text(330, 480, text=str(second_exercises) + " pontos", font=("arial.ttf", 20, "bold"), fill="black")
        
        self.canvas.create_text(880, 510, text=str(third_exercises) + " pontos", font=("arial.ttf", 20, "bold"), fill="black")
        self.createImages(third_place, 880, 380, 200, self.canvas, member_images, 0, 0, 0, 0)

        self.save_canvas_as_image(self.canvas, str(self.week) + "/rankingGrupsAccum.jpg")
        
        
    def create_window_ranking_destaque (self, first_exercises, first_place, canvas):

        self.canvas.delete("all")
        # Adicionar o fundo do pódio
        podium_bg = self.load_image("pics/destaque.jpg", size=(1200, 800))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Destaque da semana", font=("arial.ttf", 60, "bold"), fill="light gray")
        self.canvas.create_text(598, 79, text="Destaque da semana", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        
        self.canvas.create_text(600, 150, text=str (first_exercises) + " exercícios", font=("Arial", 40))
        
        member_images = []
        member_size = 300 
        if len (first_place) > 8: member_size = 75
        elif len (first_place) > 4: member_size = 150
        self.createImages(first_place, 600, 600, 200, self.canvas, member_images, len(first_place), 0, 450, member_size)

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
        self.canvas.create_text(600, 80, text="Vencedor da Semana", font=("arial.ttf", 60, "bold"), fill="light gray")
        self.canvas.create_text(598, 79, text="Vencedor da Semana", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        self.canvas.create_text(600, 150, text=first_group, font=("Arial", 60, "bold"), fill="gold")
        self.canvas.create_text(598, 149, text=first_group, font=("Arial", 60, "bold"), fill="black")
        self.canvas.create_text(596, 148, text=first_group, font=("Arial", 60, "bold"), fill="white")
        
        
        self.canvas.create_text(600, 220, text=str(first_exercises) + " exercicios", font=("Arial", 40), fill="white")
        member_images = []
        self.createImages([first_group], 600, 500, 500, self.canvas, member_images, 1, 0, 0, 0)

        # Exibir a interface gráfica
        self.save_canvas_as_image(self.canvas, str(self.week) + "/rankingGroup.jpg")
        #root.mainloop()
        
    def create_window_shame(self, shame_people):
        self.canvas.delete("all")
        # Adicionar o fundo do pódio
        podium_bg = self.load_image("pics/vergonha.jpg", size=(1200, 800))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Parede da vergonha", font=("arial.ttf", 60, "bold"), fill="light gray")
        self.canvas.create_text(598, 79, text="Parede da vergonha", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        
        self.canvas.create_text(600, 150, text="Não cumpriram a meta", font=("Arial", 30), fill="white")
        
        shame_list = []
        for  value in shame_people:
            shame_list.append(value["name"]) 
    
        member_images = []
        self.createImages(shame_list, 250, 350, 300, self.canvas, member_images, 2, 0, 0, 0)

        # Exibir a interface gráfica
        self.save_canvas_as_image(self.canvas, str(self.week) + "/Mural_vergonha.jpg")
        #root.mainloop()
        
    def create_window_carregados(self, carregados):
        self.canvas.delete("all")
        podium_bg = self.load_image("pics/carregado.jpg", size=(1200, 800))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=podium_bg)
        self.canvas.create_text(600, 80, text="Carregados da semana", font=("arial.ttf", 60, "bold"), fill="dark grey")
        self.canvas.create_text(598, 79, text="Carregados da semana", font=("arial.ttf", 60, "bold"), fill="white")
        self.canvas.create_line(100, 115, 1100, 115, fill="white", width=2)
        
        self.canvas.create_text(600, 140, text="Dava pra fazer 3+ né?", font=("arial.ttf", 30, "bold"), fill="white")
        #self.canvas.create_text(600, 150, text=str (shame_people) + " exercícios", font=("Arial", 40))
        shame_list = []
        for  value in carregados:
            shame_list.append(value["name"]) 
    
        member_images = []
        self.createImages(shame_list, 680, 300, 200, self.canvas, member_images, 0, 0, 0, 0)
        #self.createImages(shame_list, 680, 350, 300, self.canvas, member_images, 0, 0, 0, 0)
        
        # Exibir a interface gráfica
        self.save_canvas_as_image(self.canvas, str(self.week) + "/carregados.jpg")
        
    # Função para carregar e exibir uma imagem
    def load_image(self, image_path, size=(100, 100)):
        img = Image.open(image_path)
        img = img.resize(size)
        return ImageTk.PhotoImage(img)

    def save_canvas_as_image(self, canvas, filename, dpi=300):
        # Força atualização da interface gráfica
        self.canvas.update()

        # Salva o conteúdo do canvas como PostScript com tamanho real
        ps_filename = "temp_canvas.ps"
        self.canvas.postscript(
            file=ps_filename, colormode="color",
            height=canvas.winfo_height(), width=canvas.winfo_width(),
            pagewidth=str(canvas.winfo_width())+"p",
            pageheight=str(canvas.winfo_height())+"p"
        )

        # Abre a imagem PostScript com Pillow
        img = Image.open(ps_filename).convert("RGB")

        # Ajusta a resolução corretamente para DPI alto
        width, height = img.size
        new_width = int(width * dpi / 72)  # Corrige com base no DPI
        new_height = int(height * dpi / 72)
        img = img.resize((new_width, new_height), Image.LANCZOS)

        # Aplica um filtro para suavizar a imagem
        img = img.filter(ImageFilter.SMOOTH_MORE)

        # Salva no formato desejado
        img.save(filename, "PNG", dpi=(dpi, dpi))
        print(f"Imagem salva com qualidade alta em {filename}")
    
    def createImages(self, place_list, center_x, center_y, ratio, canvas, member_images, force_square, force_x, force_y, force_ratio):
        length = len(place_list)

        square = math.ceil( (math.sqrt( length )) )
        if force_square != 0: square = force_square
        
        size_ratio = int (ratio/square)
        if force_ratio != 0: size_ratio = force_ratio
        
        x = center_x - 1/2 * (square - 1) * size_ratio
        y = center_y - 1/2 * (square - 1) * size_ratio
        if force_y != 0: y = force_y
        if force_x != 0: x = force_x
        initial_x = x
        inital_y = y
        
        i = 0
        
        for member in place_list:
            if (i == 0):
                x = initial_x
                y = inital_y
                
            elif (i == length - 1 and i % square == 0):
                y = y + size_ratio
                x = initial_x
                
            elif (i % square == 0):
                y = y + size_ratio
                x = initial_x
                
            else:
                x = x + size_ratio
                
            i = i + 1
            image = self.load_image("pics/" + member + ".jpg", size=(size_ratio, size_ratio))
            member_images.append(image)  # Armazenar a imagem na lista
            self.canvas.create_image(x, y, anchor=tk.CENTER, image=image)