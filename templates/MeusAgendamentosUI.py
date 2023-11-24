import streamlit as st
import pandas as pd
from view import View
import time
import datetime

class MeusAgendamentosUI:
  def main():
    st.header("Meus agendamentos")
    MeusAgendamentosUI.listar()

  def listar():
    data_inicial = st.text_input("informe a data incial em formato: dd/mm/aaaa")
    data_final = st.text_input("informe a data final em formato: dd/mm/aaaa")
    cliente = st.session_state["cliente_id"]

    if st.button("Listar"):
        agendas = View.listar_meus_horarios(data_inicial,data_final, cliente)
    
        if len(agendas) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in agendas: dic.append(obj.to_json())            
            df = pd.DataFrame(dic)
            st.dataframe(df)    
