import tkinter as tk

def verificar_palindromo():
    palavra = entrada.get()

    # Verificar se a caixa de entrada não está vazia e não contém apenas espaços
    if palavra.strip():
        palavra_sem_espacos = palavra.replace(" ", "").lower()
        palavra_invertida = palavra_sem_espacos[::-1]

        if palavra_sem_espacos == palavra_invertida:
            resultado.config(text="Uau, '{}' é um palíndromo!".format(palavra))
            resultado.config(fg="green")  # Texto em verde para indicar sucesso
        else:
            resultado.config(text="Ops, '{}' não é um palíndromo.".format(palavra))
            resultado.config(fg="red")  # Texto em vermelho para indicar falha
    else:
        resultado.config(text="Por favor, digite uma palavra válida.")
        resultado.config(fg="black")  # Reiniciar cor para o padrão

# Criar a janela principal
janela = tk.Tk()
janela.title("Verificador de Palíndromos")

# Adicionar uma mensagem inicial
mensagem_inicial = tk.Label(janela, text="Bem-vindo! Digite uma palavra para verificar se é um palíndromo.")
mensagem_inicial.pack(pady=10)

# Criar e posicionar widgets (caixa de entrada, botão e rótulo de resultado)
tk.Label(janela, text="Digite uma palavra:").pack(pady=5)
entrada = tk.Entry(janela, width=30)
entrada.pack(pady=5)
tk.Button(janela, text="Verificar", command=verificar_palindromo).pack(pady=10)
resultado = tk.Label(janela, text="", font=("Helvetica", 12, "bold"))
resultado.pack(pady=10)

# Iniciar o loop da interface gráfica
janela.mainloop()


