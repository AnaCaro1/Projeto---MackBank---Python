import random

historico = []
conta = int
nome = ''
telefone = ''
email = ''
saldo = 0
limite = -1
senha = ''
action = int
cadastro_realizado = False
bloquear = False

#Validações

def validar(texto):
  if not texto:
    print('    Preenchimento obrigatório! Tente novamente.')

def valida_action(action,invalida,cadastro_realizado):
  while action < 0 or action > 7:
    action = int(input('SUA OPÇÃO: '))
    if action < 0 or action > 7:
      print('    Opção inválida! Tente novamente.')
    elif action == 1 and cadastro_realizado == True:
      print('\nVocê já possui um cadastro!\n')
    elif action > 1 and action <= 6 and cadastro_realizado != True:
      print('    É necessário um cadastro! Tente novamente.')
    else:
      invalida = True
  return(action,invalida)

def confirmar_conta(conta,nome):
  confirm_conta = int
  while not confirm_conta == conta:
    confirm_conta = int(input('    Digite o número da conta: '))
    if confirm_conta != conta:
      print('    Conta não encontrada! Tente novamente.')
  print(f'    Nome do Cliente: {nome}')

def confirmar_senha(senha, bloquear):
  confirm_senha = ''
  tentativa = 3
  while not confirm_senha == senha:
    confirm_senha = (input('    Confirme a senha da conta: '))
    if confirm_senha != senha:
      print(f'    Senha Incorreta. Tentativas restantes: {tentativa-1}')
      tentativa -= 1
    if tentativa < 0:
      bloquear = True

  return(bloquear)

#Cadastro
    
def cadastrar(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico):
  print('\nMACK BANK - CADASTRO DA CONTA\n')
  conta = random.randint(1,9999)
  print(f'    Número da conta: {conta}\n')
  
  while not nome:
    nome = input('    Digite o nome do cliente: ')
    validar(nome)
    
  while not telefone:
    telefone = input('    Digite o telefone do cliente: ')
    validar(telefone)

  while not email:  
    email = input('    Digite o e-mail do cliente: ')
    validar(email)
    
  while not saldo >= 1000:
    saldo = float(input('    Digite o saldo inicial da conta: '))
    if saldo < 1000:
      print('    O saldo inicial deve ser maior ou igual a R$ 1000,00')
      
  while not limite >= 0:  
    limite = float(input('    Digite o limite de crédito: '))
    if limite < 0:
      print('    O limite de crédito não pode ser negativo!')
    
  while not len(senha) >= 6:
    senha = input('    Digite a senha da conta: ')
    if len(senha) < 6:
      print('    A senha deve ter no mínimo 6 caracteres!')
    
  confirm_senha = ''
  while not confirm_senha == senha:
    confirm_senha = (input('    Confirme a senha da conta: '))
    if confirm_senha != senha:
      print('    As senhas não coincidem!')

  fim = input('\n CADASTRO FINALIZADO! Pressione uma tecla para voltar ao menu ')
  cadastro_realizado = True
  return main(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)

#Depósito

def depositar(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico):
  deposito = 0
  print('\nMACK BANK – DEPÓSITO DA CONTA\n')

  confirmar_conta(conta,nome)
  
  while deposito <= 0:
    deposito = float(input('    Digite o valor do Depósito:  '))
    if deposito <= 0:
      print('    O valor deve ser maior que zero!')
  saldo += deposito

  historico.append(f'    Depósito de R$ {deposito:.2f}')
  fim = input('\n DEPÓSITO REALIZADO COM SUCESSO! Pressione uma tecla para voltar ao menu ')

  return main(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)

#Saque

def sacar(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico):
  saque = 0
  print('\nMACK BANK – SAQUE DA CONTA\n')

  confirmar_conta(conta,nome)
  bloquear = confirmar_senha(senha, bloquear)
  
  while saque <= 0 or saque > saldo:
    saque = float (input('    Digite o valor do Saque: '))
    if saque < 0:
      print('    O valor do saque deve ser maior que zero!')
    elif saque > saldo:     
      if saque <= (saldo + limite):
        print('    Você está usando seu Limite de Crédito!')
        historico.append(f'    Saque de R$ {saque:.2f}')
        saque -= saldo
        saldo = 0
        limite -= saque
        saldo -= saque
        break
      else:
        print('    Saldo insuficiente!')
    else:
      historico.append(f'    Saque de R$ {saque:.2f}')
      saldo = saldo - saque
      break

  fim = input('\n SAQUE REALIZADO COM SUCESSO! Pressione uma tecla para voltar ao menu ')
  return main(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)

#Consulta do Saldo

def consultar_saldo(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico):
  print('\nMACK BANK – CONSULTA DO SALDO\n')

  confirmar_conta(conta,nome)
  bloquear = confirmar_senha(senha, bloquear)

  print(f'    Saldo em conta: R$ {saldo:.2f}')
  print(f'    Limite de Crédito da conta: R$ {limite:.2f}')

  fim = input('\nPressione uma tecla para voltar ao menu ')
  return main(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)
  
#Consulta do Extrato

def consultar_extrato(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico):
  print('\nMACK BANK – EXTRATO DA CONTA\n')

  confirmar_conta(conta,nome)
  bloquear = confirmar_senha(senha, bloquear)
  
  print(f'    Limite de Crédito da conta: R$ {limite:.2f}')
  print('\n    ÚLTIMAS OPERAÇÕES:\n')

  for item in historico:
    print(item)
    
  print(f'    Saldo em conta: R$ {saldo:.2f}')
  if saldo < 0:
    print('    Atenção ao seu saldo!')
  

  fim = input('\nPressione uma tecla para voltar ao menu ')
  return main(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)

#Redefinir Senha

def redefinir_senha(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico):
  print('\nMACK BANK – REDEFINIR SENHA DA CONTA\n')
  
  confirmar_conta(conta,nome)
  bloquear = confirmar_senha(senha, bloquear)
  nova_senha = ''

  while not len(nova_senha) >= 6 or senha == nova_senha:
    nova_senha = input('    Digite a nova senha da conta: ')
    if len(nova_senha) < 6:
      print('    A senha deve ter no mínimo 6 caracteres!')
    elif senha == nova_senha:
      print('    A senha não pode ser igual a anterior! Tente novamente.')

  confirm_senha = ''
  while not confirm_senha == nova_senha:
    confirm_senha = (input('    Confirme a nova senha da conta: '))
    if confirm_senha != nova_senha:
      print('    As senhas não coincidem!')

  senha = nova_senha
  fim = input('\nSENHA REDEFINIDA COM SUCESSO! Pressione uma tecla para voltar ao menu ')
  return main(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)

#Finalização

def finalizar(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico):
  print('\nMACK BANK – SOBRE\n')
  print('Este programa foi desenvolvido por:\n     Ana Carolina Pereira Banhos dos Santos - 10434541\n      Rafaella Cruciti Rangon - RA')

#Menu

def main(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico):
  action = -1
  invalida = False
  print('\nMACK BANK – ESCOLHA UMA OPÇÃO\n')
  print('    1 – CADASTRAR CONTA CORRENTE')
  print('    2 – DEPOSITAR')
  print('    3 – SACAR')
  print('    4 – CONSULTAR SALDO')
  print('    5 – CONSULTAR EXTRATO')
  print('    6 – REDEFINIR SENHA')
  print('    7 - FINALIZAR\n')

  while invalida == False:
    action = -1
    action,invalida = valida_action(action,invalida,cadastro_realizado)
    
  if invalida:
    if action == 1 and cadastro_realizado != True:
      cadastrar(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)
    elif action == 2:
      depositar(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)
    elif action == 3 and not bloquear:
      sacar(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)
    elif action == 4 and not bloquear:
      consultar_saldo(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)
    elif action == 5 and not bloquear:
      consultar_extrato(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)
    elif action == 6 and not bloquear:
      redefinir_senha(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)
    elif action == 7 and not bloquear:
      finalizar(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)
  
main(conta,nome,telefone,email,saldo,limite,senha,cadastro_realizado,bloquear,historico)
