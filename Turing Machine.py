import ast

machine = input()

dic = ast.literal_eval(machine)

print(dic['aceita'])


list_input = []
list_out = []

numb_inputs = int(input())

for i in range(numb_inputs):
    input = list(input())
    list_input.append(input)

# Percorrendo a lista de entradas
for inputs in list_input:

    # Resetando o cabeçote da fita para o inicio da entrada
    tape_head = inputs[0]

    # Variável que verifica se pode computar a fita
    tape_integrity = True

    # Resetando o estado inicial
    current_state = dic['inicial']

    # Loop que verifica se existe alguma função de transição para o estado atual da máquina de turing
    while(tape_integrity):
        # Percorrendo as funções de transição
        for transitions in dic['delta']:
            # Verificando se o estado atual da máquita de turing é igual ao estado atual da função de transição
            if(current_state == transitions[0]):
                # Verificando se o cabeçote da fita é igual a variávei de leitura da função de transição
                if(tape_head == transitions[2]):
                    # Atualizando o estado atual da máquina de turing proposto de função delta 
                    current_state = transitions[1]
                    # Verifica se a função pede para o cabeçote parar
                    if(transitions[4] == 'P'):
                        tape_integrity = False



#print(list_entry[0])
#list_entry[0][0] = '0'
#print(list_entry[0])
