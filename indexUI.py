from templates.ManterClienteUI import ManterClienteUI
from templates.ManterServicoUI import ManterServicoUI
from templates.ManterAgendaUI import ManterAgendaUI
from templates.AbrirAgendaUI import AbrirAgendaUI
from templates.loginUI import LoginUI
from templates.agendahojeui import AgendaHojeUI
from templates.serviçoreajusteUI import ServicoReajusteUI
from templates.abrircontaUI import AbrirContaUI
from templates.editar_perfilUI import EditarPerfil
from templates.AgendaHorarioUI import AgendaHorarioUI
from templates.MeusAgendamentosUI import MeusAgendamentosUI
from templates.ConfirmaAgendamentoUI import ConfirmarUI
from view import View

import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta",])
    if op == "Login": LoginUI.main()
    if op == "Abrir Conta": AbrirContaUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Agenda", "Manter Clientes", "Manter Serviços", "Abrir Agenda do Dia", "Reajustar Preço", "Editar Perfil", "confirmar agendamentos"])
    if op == "Manter Agenda": ManterAgendaUI.main()
    if op == "Manter Clientes": ManterClienteUI.main()
    if op == "Manter Serviços": ManterServicoUI.main()
    if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
    if op == "Reajustar Preço": ServicoReajusteUI.main()
    if op == "confirmar agendamentos": ConfirmarUI.main()
    if op == "Editar Perfil": EditarPerfil.main()


  def menu_cliente():
    op = st.sidebar.selectbox("Menu", ["Agenda de Hoje", "Editar Perfil", "Agenda Horario","Meus Agendamentos"])
    if op == "Agenda de Hoje": AgendaHojeUI.main()
    if op == "Agenda Horario": AgendaHorarioUI.main()
    if op == "Meus Agendamentos": MeusAgendamentosUI.main()
    if op == "Editar Perfil": EditarPerfil.main()
  
  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["cliente_id"]
      del st.session_state["cliente_nome"]
      st.rerun()

  def sidebar():
    if "cliente_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
      if st.session_state["cliente_nome"] == "admin": IndexUI.menu_admin()
      else: IndexUI.menu_cliente()
      IndexUI.btn_logout()  

  def main():
    View.cliente_admin()
    IndexUI.sidebar()

IndexUI.main()


