#Projeto Hackathon Mackenzie2022
#Bibliotecas
import streamlit as st
import pandas as pd
  
# Título
st.title("Cálculo CCE - Dólar")

# Descrição do Projeto
st.header("A finalidade deste projeto é calcular o lucro baseado na redução da emissão de gases nocivos às condições globais.")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Insira abaixo as informações necessárias para o cálculo.")

#Coluna Informativa relacionada ao ganho de créditos relacionados à emissão reduzida.
col1, col2 = st.columns(2)
col1.write("Carbono")
col2.write("1 Crédito por Tonelada")

col3, col5 = st.columns(2)
col1.write("Metano")
col2.write("21 Créditos por Tonelada")

col5, col6 = st.columns(2)
col1.write("Hexafluoreto de Enxofre")
col2.write("23900 Créditos por Tonelada")

# Selecionar o gás.
option = st.selectbox(
    'Qual gás nocivo deseja reduzir?',
    ('CO2 (Carbono)', 'CH4 (Gás Metano)', 'SF6 (Hexafluoreto de Enxofre)'))

#Coleção dos dados relacionados à quantidade reduzida.
number = st.number_input('insira o valor em Toneladas')

#Botão que aciona o cálculo de proporção de ganho pela quantia reduzida da emissão.
if st.button('Consultar'):
  if option == 'CO2 (Carbono)':
    
 
if option == 'CH4 (Gás Metano)':

  
if option == 'SF6 (Hexafluoreto de Enxofre)':


  
#Proporção crédito de carbono/dólar


