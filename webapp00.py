# myFirstStreamlitApp.py
  
#import the library
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Cálculo CCE - Dólar")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Cabeçalho")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("Sub Cabeçalho")

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

# Selecionar o gás
option = st.selectbox(
    'Qual gás nocivo deseja reduzir?',
    ('CO2(Carbono)', 'CH4(Gás Metano)', 'SF6 (Hexafluoreto de Enxofre)'))

st.write('Você selecionou ', option)

#Proporção gás/crédito de carbono
if option == 'CO2 (Carbono)'
  st.write('Uma tonelada deemissão de carbono reduzida equivale a 1 Crédito de carbono')
 
if option == 'CH4 (Gás Metano)'
  st.write('Uma tonelada deemissão de carbono reduzida equivale a 21 Créditos de carbono')
  
if option == 'SF6 (Hexafluoreto de Enxofre)'
  st.write('Uma tonelada deemissão de carbono reduzida equivale a 23900 Créditos de carbono')

#Proporção crédito de carbono/dólar


