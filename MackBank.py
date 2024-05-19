import random

conta = int
nome = ''
telefone = ''
email = ''
saldo_inicial = 0
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
  while action < 0 or action > 6:
    action = int(input('SUA OPÇÃO: '))
    if action < 0 or action > 6:
      print('    Opção inválida! Tente novamente.')
    elif action == 1 and cadastro_realizado == True:
      print('\nVocê já possui um cadastro!\n')
    elif action > 1 and action < 5 and cadastro_realizado != True:
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
    
def cadastrar(conta,nome,telefone,email,saldo_inicial,limite,senha,cadastro_realizado,bloquear):
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
    
  while not saldo_inicial >= 1000:
    saldo_inicial = float(input('    Digite o saldo inicial da conta: '))
    if saldo_inicial < 1000:
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
  return main(conta,nome,telefone,email,saldo_inicial,limite,senha,cadastro_realizado,bloquear)

#Depósito

def depositar(conta,nome,telefone,email,saldo_inicial,limite,senha,cadastro_realizado,bloquear):
  deposito = 0
  print('\nMACK BANK – DEPÓSITO DA CONTA\n')

  confirmar_conta(conta,nome)
  
  while deposito <= 0:
    deposito = float(input('    Digite o valor do Depósito:  '))
    if deposito <= 0:
      print('    O valor deve ser maior que zero!')
  saldo_inicial += deposito

  print(f'\n    Depósito realizado com sucesso!\n')

  return main(conta,nome,telefone,email,saldo_inicial,limite,senha,cadastro_realizado,bloquear)

#Saque

def sacar(conta,nome,telefone,email,saldo_inicial,limite,senha,cadastro_realizado,bloquear):
  saque = 0
  print('\nMACK BANK – SAQUE DA CONTA\n')

  confirmar_conta(conta,nome)
  bloquear = confirmar_senha(senha, bloquear)
  
  while saque <= 0 or saque > saldo_inicial:
    saque = float (input('    Digite o valor do Saque: '))
    if saque < 0:
      print('    O valor do saque deve ser maior que zero!')
    elif saque > saldo_inicial:     
      if saque <= (saldo_inicial + limite):
        print('    Você está usando seu Limite de Crédito!')
        saque -= saldo_inicial
        saldo_inicial = 0
        limite -= saque
        break
      else:
        print('    Saldo insuficiente!')
    else:
      saldo_inicial = saldo_inicial - saque
      
  print('    Saque realizado com sucesso!')
  return main(conta,nome,telefone,email,saldo_inicial,limite,senha,cadastro_realizado,bloquear)

#Menu

def main(conta,nome,telefone,email,saldo_inicial,limite,senha,cadastro_realizado,bloquear):
  action = -1
  invalida = False
  print('\nMACK BANK – ESCOLHA UMA OPÇÃO\n')
  print('    1 – CADASTRAR CONTA CORRENTE')
  print('    2 – DEPOSITAR')
  print('    3 – SACAR')
  print('    4 – CONSULTAR SALDO')
  print('    5 – CONSULTAR EXTRATO')
  print('    6 – FINALIZAR\n')

  while invalida == False:
    action = -1
    action,invalida = valida_action(action,invalida,cadastro_realizado)
    
  if invalida:
    if action == 1 and cadastro_realizado != True:
      cadastrar(conta,nome,telefone,email,saldo_inicial,limite,senha,cadastro_realizado,bloquear)
    elif action == 2:
      depositar(conta,nome,telefone,email,saldo_inicial,limite,senha,cadastro_realizado,bloquear)
    elif action == 3 and not bloquear:
      sacar(conta,nome,telefone,email,saldo_inicial,limite,senha,cadastro_realizado,bloquear)
    elif action == 4 and not bloquear:
      print()
    elif action == 5 and not bloquear:
      print()
    
main(conta,nome,telefone,email,saldo_inicial,limite,senha,cadastro_realizado,bloquear)
