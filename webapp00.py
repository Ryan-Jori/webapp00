#Projeto Hackathon Mackenzie2022
#Bibliotecas
import streamlit as st
import pandas as ps
  
# Título
st.title("Cálculo CCE - Dólar")

# Descrição do Projeto
st.header("A finalidade deste projeto é calcular o lucro baseado na redução da emissão de gases nocivos às condições globais.")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Insira abaixo as informações necessárias para o cálculo.")

# Selecionar o gás
option = st.selectbox(
    'Qual gás nocivo deseja reduzir?',
    ('CO2 (Carbono)', 'CH4 (Gás Metano)', 'SF6 (Hexafluoreto de Enxofre)'))

#Proporção gás/crédito de carbono
if option == 'CO2 (Carbono)':
  st.write('Uma tonelada deemissão de carbono reduzida equivale a 1 Crédito de carbono')
 
if option == 'CH4 (Gás Metano)':
  st.write('Uma tonelada deemissão de carbono reduzida equivale a 21 Créditos de carbono')
  
if option == 'SF6 (Hexafluoreto de Enxofre)':
  st.write('Uma tonelada deemissão de carbono reduzida equivale a 23900 Créditos de carbono')
  
#Proporção crédito de carbono/dólar


