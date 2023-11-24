import streamlit as st
import pandas as pd
from view import View
import time

class ConfirmarUI:
  def main():
    st.header("Horarios não confirmados")
    ConfirmarUI.Confirmar()

  def Confirmar():
    agendas = View.listar_n_confirmados()
    if len(agendas) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      dic = []
      for obj in agendas: dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)

    Horario_n_confirmados = View.listar_n_confirmados()
    n_conf = st.selectbox("Escolhar horario para Confirmar", Horario_n_confirmados)
    if st.button("confirmar"):
      View.agenda_atualizar(n_conf.get_id(),n_conf.get_data(), True, n_conf.get_id_cliente(),n_conf.get_id_servico())
      time.sleep(2)
      st.rerun()
