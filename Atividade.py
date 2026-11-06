import tkinter as tk

def digitar(caracter):
    visor.insert(tk.END, caracter)
    
def digitar_del():
    visor.delete(0, tk.END)
    
def digitar_igual():
    visor.delete(0, tk.END)
    
def limpar():
    visor.delete(0, tk.END)

janela = tk.Tk()
janela.title("Primeiros botões")


# O visor ocupa três colunas da primeira linha
visor = tk.Entry(janela, width=24, justify="right")
visor.grid(row=0, column=0, columnspan=3, padx=5, pady=5)



botao_c = tk.Button(janela, text="C", width=8, height=3, command=limpar)
botao_c.grid(row=1, column=0, padx=2, pady=2)

botao_del = tk.Button(janela, text="⌫", width=8, height=3, command=limpar)
botao_del.grid(row=1, column=1, padx=2, pady=2)

botao_mais = tk.Button(janela, text="", width=8, height=3, command=limpar)
botao_mais.grid(row=1, column=2, padx=2, pady=2)

botao_vezes = tk.Button(janela, text="x", width=8, height=3, command=limpar)
botao_vezes.grid(row=1, column=3, padx=2, pady=2)


botao_9 = tk.Button(janela, text="9", width=8, height=3, command=lambda:digitar("/"))
botao_9.grid(row=2, column=0, padx=2, pady=2)

botao_8 = tk.Button(janela, text="8", width=8, height=3, command=lambda:digitar("/"))
botao_8.grid(row=2, column=1, padx=2, pady=2)

botao_7 = tk.Button(janela, text="7", width=8, height=3, command=lambda:digitar("/"))
botao_7.grid(row=2, column=2, padx=2, pady=2)

botao_menos = tk.Button(janela, text="-", width=8, height=3, command=lambda:digitar("/"))
botao_menos.grid(row=2, column=3, padx=2, pady=2)


botao_6 = tk.Button(janela, text="6", width=8, height=3, command=lambda:digitar("/"))
botao_6.grid(row=3, column=0, padx=2, pady=2)

botao_5 = tk.Button(janela, text="5", width=8, height=3, command=lambda:digitar("/"))
botao_5.grid(row=3, column=1, padx=2, pady=2)

botao_4 = tk.Button(janela, text="4", width=8, height=3, command=lambda:digitar("/"))
botao_4.grid(row=3, column=2, padx=2, pady=2)

botao_mais = tk.Button(janela, text="+", width=8, height=3, command=lambda:digitar("/"))
botao_mais.grid(row=3, column=3, padx=2, pady=2)



botao_3 = tk.Button(janela, text="3", width=8, height=3, command=lambda:digitar("/"))
botao_3.grid(row=4, column=0, padx=2, pady=2)

botao_2 = tk.Button(janela, text="2", width=8, height=3, command=lambda:digitar("/"))
botao_2.grid(row=4, column=1, padx=2, pady=2)

botao_1 = tk.Button(janela, text="1", width=8, height=3, command=lambda:digitar("/"))
botao_1.grid(row=4, column=2, padx=1, pady=1)

botao_igual = tk.Button(janela, text="=", width=9, height=7, command=digitar_igual)
botao_igual.grid(row=4, column=3, rowspan=2, padx=2, pady=2)




botao_0= tk.Button(janela, text="0", width=16, height=3, command=lambda:digitar("/"))
botao_0.grid(row=5, column=0, columnspan=2, padx=2, pady=2)

botao_ponto = tk.Button(janela, text=".", width=8, height=3, command=lambda:digitar("/"))
botao_ponto.grid(row=5, column=2, padx=2, pady=2)

janela.mainloop()