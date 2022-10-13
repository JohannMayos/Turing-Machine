import ast

machine = input()

dic = ast.literal_eval(machine)


list_input = []
list_out = []

numb_inputs = int(input())

for i in range(numb_inputs):
    i = list(input())
    list_input.append(i)

# Percorrendo a lista de entradas
for inputs in list_input:

    i = 0
    # Resetando o cabeçote da fita para o inicio da entrada
    tape_head = inputs[i]

    # Variável que verifica se pode computar a fita
    tape_integrity = True

    # Resetando o estado inicial
    current_state = dic['inicial']

    # Loop que verifica se existe alguma função de transição para o estado atual da máquina de turing
    while tape_integrity:
        tape_integrity = False

        # Percorrendo as funções de transição
        for transitions in dic['delta']:
            # Verificando se o estado atual da máquita de turing é igual ao estado atual da função de transição
            if current_state == transitions[0]:
                # Verificando se o cabeçote da fita é igual a variávei de leitura da função de transição
                if tape_head == str(transitions[2]):
                    # Atualizando o estado atual da máquina de turing proposto de função delta 
                    current_state = transitions[1]
                    tape_integrity = True

                    # Escrevendo o valor que deve ser escrito em cima do valor lido pelo cabeçote da fita
                    if tape_head != 'b':
                        inputs[i] = str(transitions[3])
                    
                    # 
                    if transitions[4] == 'D':
                        i = i + 1
                        if len(inputs) <= i:
                            tape_head = 'b'
                        else:
                            tape_head = inputs[i]

                    elif transitions[4] == 'E':
                        i = i - 1
                        if 0 >= i:
                            tape_head = 'b'
                        else:
                            tape_head = inputs[i]

                    # Verifica se a função pede para o cabeçote parar
                    elif transitions[4] == 'P':
                        tape_integrity = False

                        if dic['aceita'] == current_state:
                            for i in inputs:
                                print(i, end='')

                            print(" ACEITA")

                        if dic['rejeita'] == current_state:
                            for i in inputs:
                                print(i, end='')

                            print(" REJEITA")
