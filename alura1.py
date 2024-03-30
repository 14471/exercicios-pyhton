q_seguranca = int(input('Quantidade de pessoas na seegurança:'))
s_seguranca = int(input('Salario na segurança:'))

q_docente = int(input('Quantidade de pessoas na docente:'))
s_docente = int(input('Salario no corpo docente:'))

q_diretoria = int(input('Quantidade de pessoas na diretoria:'))
s_diretoria = int(input('Salario na diretoria:'))

q_total_empregados= q_seguranca+q_docente+q_diretoria
q_salario = s_diretoria+s_docente+s_seguranca
media_ponderada = (q_diretoria*s_diretoria+q_docente*s_docente+q_seguranca*s_seguranca)/(q_total_empregados)

print(f'A quantidade de pessoa, é {q_total_empregados}')
print(f'A media salarial, é:{media_ponderada}')