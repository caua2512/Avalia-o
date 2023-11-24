import streamlit as st
import pandas as pd
from view import View
import time

class AgendaHorarioUI:
  def main():
    st.header("Agendar um Horario")
    AgendaHorarioUI.listar()
    AgendaHorarioUI.Agendar()
  def listar():
    agendas = View.horarios_da_semana()
    if len(agendas) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      dic = []
      for obj in agendas: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)
  def Agendar():
      cliente = st.session_state["cliente_id"]
      agenda_H = View.horarios_da_semana()
      agenda = st.selectbox("escolher um horario", agenda_H)
      confirmado = False
      serviço = st.selectbox("Escolher um serviço", View.servico_listar())
      if st.button("Marcar horario"):
        View.agenda_atualizar(agenda.get_id(),agenda.get_data(),confirmado,cliente,serviço.get_id())
        st.success("Agendamento realizado com sucesso")
