convidados = ['angelica', 'bruna', 'daiane']
print(f'Oi {convidados[0].title()}, você está convidado(a) para jantar aqui em casa hoje.')
print(f'Oi {convidados[1].title()}, você está convidado(a) para jantar aqui em casa hoje.')
print(f'Oi {convidados[2].title()}, você está convidado(a) para jantar aqui em casa hoje.')

print(f"\nOi pessoal a {convidados[2].title()} não vai poder vir, vou substitui-la por outra pessoa.\n")

convidados[2] = 'djulia'
print(f"Agora sim {convidados[0].title()}, tudo certo para o jantar hoje à noite.")
print(f"Agora sim {convidados[1].title()}, tudo certo para o jantar hoje à noite.")
print(f"Agora sim {convidados[2].title()}, tudo certo para o jantar hoje à noite.")

print("\nOi pessoal consegui uma mesa maior, poderei convidar mais 3 pessoas.\n")

convidados.insert(0, 'abigail')
convidados.insert(2, 'carol')
convidados.append('fernanda')

print(f"Oficializado {convidados[0].title()}, jantar hoje lá em casa.")
print(f"Oficializado {convidados[1].title()}, jantar hoje lá em casa.")
print(f"Oficializado {convidados[2].title()}, jantar hoje lá em casa.")
print(f"Oficializado {convidados[3].title()}, jantar hoje lá em casa.")
print(f"Oficializado {convidados[4].title()}, jantar hoje lá em casa.")
print(f"Oficializado {convidados[5].title()}, jantar hoje lá em casa.")

print(f"\nO Numero de convidados é '{len(convidados)}' convidados.")

print("\nMil desculpas pessoal, mas, a mesa não chegara a tempo, só poderei convidar duas pessoas.\n")

removed_convidados = convidados.pop(0)
print(f"Desculpe {removed_convidados.title()} por não poder te convidar.")
removed_convidados = convidados.pop(4)
print(f"Desculpe {removed_convidados.title()} por não poder te convidar.")
removed_convidados = convidados.pop(2)
print(f"Desculpe {removed_convidados.title()} por não poder te convidar.")
print(convidados)
removed_convidados = convidados.pop(1)
print(f"Desculpe {removed_convidados.title()} por não poder te convidar.\n")

print(f"Oi {convidados[0].title()}, você ainda está convidada para o jantar hoje á noite la em casa.")
print(f"Oi {convidados[1].title()}, você ainda está convidada para o jantar hoje á noite la em casa.\n")

del convidados[1]
del convidados[0]
print(convidados)
