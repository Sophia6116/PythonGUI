
import tkinter as tk

# Função para digitar no visor
def digitar(caracter):
    visor.insert(tk.END, caracter)

# Função para apagar o último caractere
def digitar_del():
    texto = visor.get()

    if texto != "":
        visor.delete(len(texto) - 1, tk.END)

# Função para limpar o visor
def limpar():
    visor.delete(0, tk.END)

# Função para calcular
def digitar_igual():
    conta = visor.get()

    if "+" in conta:
        numeros = conta.split("+")
        n1 = float(numeros[0])
        n2 = float(numeros[1])
        resultado = n1 + n2

    elif "-" in conta:
        numeros = conta.split("-")
        n1 = float(numeros[0])
        n2 = float(numeros[1])
        resultado = n1 - n2

    elif "*" in conta:
        numeros = conta.split("*")
        n1 = float(numeros[0])
        n2 = float(numeros[1])
        resultado = n1 * n2

    elif "/" in conta:
        numeros = conta.split("/")
        n1 = float(numeros[0])
        n2 = float(numeros[1])
        resultado = n1 / n2

    visor.delete(0, tk.END)
    visor.insert(0, resultado)


# Cria a janela
janela = tk.Tk()
janela.title("Calculadora")

# Visor
visor = tk.Entry(janela, width=24, justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Botões da primeira linha
botao_c = tk.Button(janela, text="C", width=8, height=3, command=limpar)
botao_c.grid(row=1, column=0, padx=1, pady=1)

botao_del = tk.Button(janela, text="⌫", width=8, height=3, command=digitar_del)
botao_del.grid(row=1, column=1, padx=1, pady=1)

botao_dividir = tk.Button(janela, text="/", width=8, height=3,command=lambda: digitar("/"))
botao_dividir.grid(row=1, column=2, padx=1, pady=1)

botao_vezes = tk.Button(janela, text="x", width=8, height=3,command=lambda: digitar("*"))
botao_vezes.grid(row=1, column=3, padx=1, pady=1)

# Botões dos números
botao_9 = tk.Button(janela, text="9", width=8, height=3,command=lambda: digitar("9"))
botao_9.grid(row=2, column=0, padx=1, pady=1)

botao_8 = tk.Button(janela, text="8", width=8, height=3,command=lambda: digitar("8"))
botao_8.grid(row=2, column=1, padx=1, pady=1)

botao_7 = tk.Button(janela, text="7", width=8, height=3,command=lambda: digitar("7"))
botao_7.grid(row=2, column=2, padx=1, pady=1)

botao_menos = tk.Button(janela, text="-", width=8, height=3,command=lambda: digitar("-"))
botao_menos.grid(row=2, column=3, padx=1, pady=1)

botao_6 = tk.Button(janela, text="6", width=8, height=3,command=lambda: digitar("6"))
botao_6.grid(row=3, column=0, padx=1, pady=1)

botao_5 = tk.Button(janela, text="5", width=8, height=3,command=lambda: digitar("5"))
botao_5.grid(row=3, column=1, padx=1, pady=1)

botao_4 = tk.Button(janela, text="4", width=8, height=3,command=lambda: digitar("4"))
botao_4.grid(row=3, column=2, padx=1, pady=1)

botao_mais = tk.Button(janela, text="+", width=8, height=3,command=lambda: digitar("+"))
botao_mais.grid(row=3, column=3, padx=1, pady=1)

botao_3 = tk.Button(janela, text="3", width=8, height=3,command=lambda: digitar("3"))
botao_3.grid(row=4, column=0, padx=1, pady=1)

botao_2 = tk.Button(janela, text="2", width=8, height=3,command=lambda: digitar("2"))
botao_2.grid(row=4, column=1, padx=1, pady=1)

botao_1 = tk.Button(janela, text="1", width=8, height=3,command=lambda: digitar("1"))
botao_1.grid(row=4, column=2, padx=1, pady=1)

botao_igual = tk.Button(janela, text="=", width=8, height=7,command=digitar_igual)
botao_igual.grid(row=4, column=3, rowspan=2, padx=1, pady=1)

botao_0 = tk.Button(janela, text="0", width=16, height=3,command=lambda: digitar("0"))
botao_0.grid(row=5, column=0, columnspan=2, padx=1, pady=1)

botao_ponto = tk.Button(janela, text=".", width=8, height=3,command=lambda: digitar("."))
botao_ponto.grid(row=5, column=2, padx=1, pady=1)

janela.mainloop()
