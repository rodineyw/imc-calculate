import tkinter as tk
from tkinter import ttk, messagebox

class CalculadoraIMC:
 def __init__(self, root):
  self.root = root
  self.root.title("Calculadora de IMC")
  self.root.geometry("250x550")
  self.root.resizable(False, False)
  self.root.configure(bg="#f0f0f0")
  
  
  # Estilo para os componentes
  self.style = ttk.Style()
  self.style.configure("Tframe", background="#f0f0f0")
  self.style.configure("TLabel", background="#f1f1f1", font=("Segoe UI", 10))
  self.style.configure("Tbutton", font=("Segoe UI", 10, "bold"))
  self.style.configure("TEntry", font=("Segoe UI", 10))
  
  # Criação dos widgets
  self.criar_widgets()
  
 def criar_widgets(self):
  # Frame Principal
  main_frame = ttk.Frame(self.root)
  main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
  
  # Titulo
  lbl_titulo = ttk.Label(main_frame, text="Calculadora de IMC", font=("Segoe UI", 16, "bold"))
  
  lbl_titulo.grid(row=0, column=0, columnspan=2, pady=10)
  
  # Entrda de peso
  lbl_peso = ttk.Label(main_frame, text="Peso (Kg):")
  lbl_peso.grid(row=1, column=0, pady=5, sticky=tk.W)
  self.entrada_peso = ttk.Entry(main_frame)
  self.entrada_peso.grid(row=2, column=0, pady=5, ipady=5, sticky=tk.EW)
  
  # Entrada de altura
  lbl_altura = ttk.Label(main_frame, text="Altura (cm):")
  lbl_altura.grid(row=3, column=0, pady=5, sticky=tk.W)
  self.entrada_altura = ttk.Entry(main_frame)
  self.entrada_altura.grid(row=4, column=0, pady=5, ipady=5, sticky=tk.EW)
  
  # Botão de calculo
  btn_calcular = ttk.Button(main_frame, text="Calcular IMC", command=self.calcular_imc)
  btn_calcular.grid(row=5, column=0, pady=5, ipady=10, sticky=tk.EW)
  
  # Resultados
  self.lbl_resultado = ttk.Label(main_frame, text="Seu IMC: ", font=("Segoe UI", 12, "bold"))
  self.lbl_resultado.grid(row=6, column=0, pady=5)
  self.lbl_classificacao = ttk.Label(main_frame, text="Classificaão: ", font=("Segoe UI", 12, "bold"))
  self.lbl_classificacao.grid(row=7, column=0, pady=5)
  
  # tabela de classificação
  frame_tabela = ttk.Frame(main_frame)
  
  frame_tabela.grid(row=8, column=0, pady=20, sticky=tk.EW)
  
  ttk.Label(frame_tabela, text="Classificação", font=("Segoe UI", 9, "bold")).grid(row=0, column=0, pady=5)
  ttk.Label(frame_tabela, text="IMC", font=("Segoe UI", 9, "bold")).grid(row=0, column=1, pady=5)
  
  classificacoes = [
   ("Abaixo do peso", "< 18.5"),
   ("Peso normal", "18.5 - 24.9"),
   ("Sobrepeso", "25 - 29.9"),
   ("Obesidade Grau I", "30 - 34.9"),
   ("Obesidade Grau II", "35 - 39.9"),
   ("Obesidade Grau III", ">= 40")
  ]
  for i, (classif, imc) in enumerate(classificacoes, start=1):
   ttk.Label(frame_tabela, text=classif).grid(row=i, column=0, sticky=tk.W, padx=5)
   ttk.Label(frame_tabela, text=imc).grid(row=i, column=1, sticky=tk.E, padx=5)
   
 def calcular_imc(self):
  try:
   peso = float(self.entrada_peso.get().replace(",", "."))
   altura = float(self.entrada_altura.get().replace(",", ".")) /100 # Converte cm para metros
   if peso <= 0 or altura <= 0:
    raise ValueError("Valores devem ser psoitivos.")
   
   imc = peso / (altura ** 2)
   classificacao = self.classificar_imc(imc)
   
   self.lbl_resultado.config(text=f"Seu IMC: {imc:1f}", foreground=self.cor_classificacao(imc))
   self.lbl_classificacao.config(text=f"Classificação: {classificacao}")
   
  except ValueError:
   messagebox.showerror("Erro", "Por favor, insira valores númericos válidos.")
   
 def classificar_imc(self, imc):
  if imc < 18.5:
   return "Abaixo do peso"
  elif 18.5 <= imc < 25:
   return "Peso normal"
  elif 25 <= imc < 30:
   return "Sobrepeso"
  elif 30 <= imc <35:
   return "Obesidade Grau I"
  elif 35 <= imc < 40:
   return "Obesidade Grau II"
  else:
   return "Obesidade Grau III"
  
 def cor_classificacao(self, imc):
  if imc < 18.5:
   return "#2196f3"
  elif 18.5 <= imc < 25:
   return "#4caf50"
  elif 25 <= imc < 30:
   return "#ffc107"
  else:
   return "#f44336"
  
if __name__ == "__main__":
 root = tk.Tk()
 app = CalculadoraIMC(root)
 root.mainloop()