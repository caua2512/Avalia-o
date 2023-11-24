import streamlit as st
import pandas as pd
from view import View
import time

class CadastroUI:
  def main():
     st.header("Cadastrar-se")
     CadastroUI.inserir()
  def inserir():
    nome = st.text_input("Informe seu nome")
    email = st.text_input("Informe seu e-mail")
    fone = st.text_input("Informe seu fone")
    senha = st.text_input("Informe sua senha")
    if st.button("Cadastre-se"):
      try:
        View.cliente_inserir(nome, email, fone, senha)
        st.success("Inserido com sucesso")
        time.sleep(2)
        st.rerun()
      except:
        st.error("nome, email, fone ou senha invalidos!")  
      #else:
      #  st.error("Email já cadastrado")
