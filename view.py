
from models.cliente import Cliente, NCliente
from models.servico import Servico, NServico
from models.agenda import Agenda, NAgenda
import datetime

class View:
  def cliente_inserir(nome, email, fone, senha):
    if nome == " ": raise ValueError("coloque o nome")
    if email == "": raise ValueError("coloque o email")
    if fone == " ": raise ValueError("coloque o fone") 
    if senha == " ": raise ValueError("coloque a senha")
    for senhazinha in View.cliente_listar():
      if senhazinha.get_email() == email: raise ValueError("E-mail repetido")
    #if email == cliente.get_email(): raise ValueError("email já cadastrado") 
    cliente = Cliente(0, nome, email, fone, senha)
    NCliente.inserir(cliente)

  def cliente_listar():
    return NCliente.listar()
  
  def cliente_listar_id(id):
    return NCliente.listar_id(id)

  def cliente_atualizar(id, nome, email, fone, senha):
    if nome == "": raise ValueError("coloque o nome")
    if email == "": raise ValueError("coloque o email")
    if fone == "": raise ValueError("coloque o fone") 
    if senha == "": raise ValueError("coloque a senha")
    for senhazinha in View.cliente_listar():
      if senhazinha.get_email() == email: raise ValueError("E-mail repetido")
    #for email in View.cliente_listar:
    #  if email == cliente.get_email(): raise ValueError("email já cadastrado")
    cliente = Cliente(id, nome, email, fone, senha)
    NCliente.atualizar(cliente)
    
  def cliente_excluir(id):
    cliente = Cliente(id, "", "", "", "")
    NCliente.excluir(cliente)    

  def cliente_admin():
    for cliente in View.cliente_listar():
      if cliente.get_nome() == "admin": return
    View.cliente_inserir("admin", "admin", "0000", "admin")  

  #Avaliação
  #def cliente_login(email, senha):
  #  for cliente in View.cliente_listar():
  #    if cliente.get_email() == email and cliente.get_senha() == senha:
  #      return True
  #  return False

  def cliente_login(email, senha):
    for cliente in View.cliente_listar():
      if cliente.get_email() == email and cliente.get_senha() == senha:
        return cliente
    return None

  def servico_listar():
    return NServico.listar()

  def servico_listar_id(id):
    return NServico.listar_id(id)

  def servico_inserir(descricao, valor, duracao):
    if descricao == "": raise ValueError("coloque a descrição")
    if valor < 0: raise ValueError("Valor inválido")
    if duracao <= 0: raise ValueError("Duração inválida")
    NServico.inserir(Servico(0, descricao, valor, duracao))

  def servico_atualizar(id, descricao, valor, duracao):
    if descricao == "": raise ValueError("coloque a descrição")
    if valor < 0: raise ValueError("Valor inválido")
    if duracao <= 0: raise ValueError("Duração inválida")
    NServico.atualizar(Servico(id, descricao, valor, duracao))

  def servico_excluir(id):
    NServico.excluir(Servico(id, "", 0, 10))

  def servico_reajustar(percentual):
    for servico in View.servico_listar():    
      NServico.atualizar(Servico(servico.get_id(), servico.get_descricao(), servico.get_valor() * (1 + percentual/100), servico.get_duracao()))

  def agenda_listar():
    return NAgenda.listar()

  def agenda_listarhoje():
    r = []
    hoje = datetime.datetime.today()
    for horario in View.agenda_listar():
      if horario.get_confirmado() == False and horario.get_data().date() == hoje.date():
        r.append(horario)
    return r    

  def agenda_inserir(data, confirmado, id_cliente, id_servico):
    hj = datetime.datetime.today()
    if data < hj: raise ValueError("data no passado")
    NAgenda.inserir(Agenda(0, data, confirmado, id_cliente, id_servico))

  def agenda_atualizar(id, data, confirmado, id_cliente, id_servico):
    hj = datetime.datetime.today()
    if data < hj: raise ValueError("data no passado")
    NAgenda.atualizar(Agenda(id, data, confirmado, id_cliente, id_servico))

  def agenda_excluir(id):
    NAgenda.excluir(Agenda(id, "", "", 0, 0))

  def agenda_abrir_agenda(data, hinicio, hfim, intervalo):
    data_inicio = datetime.datetime.strptime(f"{data} {hinicio}", "%d/%m/%Y %H:%M")
    data_fim = datetime.datetime.strptime(f"{data} {hfim}", "%d/%m/%Y %H:%M")
    delta = datetime.timedelta(minutes = intervalo) 
    aux = data_inicio
    data_atual = datetime.datetime.today()
    if data_atual.date() < data_atual.date():
      raise ValueError("a data inicial não pode ser anterior a data de hoje")    
    if intervalo <= 0:
      raise ValueError("o Intervalo entre os horarios não pode ser negativo")      
    while aux <= data_fim :
      NAgenda.inserir(Agenda(0, aux, False, 0, 0))
      aux = aux + delta
  def editar_perfil(id, nome, email, fone, senha):
    NCliente.atualizar(Cliente(id, nome, email, fone, senha))
  def horarios_da_semana():
    horarios_disponiveis = []
    hoje = datetime.datetime.today()
    semana = hoje + datetime.timedelta(days=7)
    for agenda in View.agenda_listar():
      if hoje.date() <= agenda.get_data().date() <= semana.date() and agenda.get_confirmado() == False:
        horarios_disponiveis.append(agenda)

    return horarios_disponiveis
  def listar_meus_horarios(datainicio,datafim, cliente_IDZIN):
    data_inicial = datetime.datetime.strptime(f"{datainicio}", "%d/%m/%Y")
    data_final = datetime.datetime.strptime(f"{datafim}", "%d/%m/%Y")
    periodo_solicitado = []
    for horarizinho in View.agenda_listar():
      if horarizinho.get_id_cliente() == cliente_IDZIN:
        if data_inicial <= horarizinho.get_data() <= data_final:
          periodo_solicitado.append(horarizinho)
    return periodo_solicitado
  
  def listar_n_confirmados():
    n_confirmado = []
    for agenda in View.agenda_listar():
      if agenda.get_confirmado() == False:
        n_confirmado.append(agenda)
    return n_confirmado


