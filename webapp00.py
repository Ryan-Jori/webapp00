#Projeto Hackathon Mackenzie2022
#Bibliotecas
import streamlit as st

# Título
st.title("Cálculo CCE - Dólar")

# Descrição do Projeto
st.header("A finalidade deste projeto é calcular o lucro baseado na redução da emissão de gases nocivos às condições globais, doando parte deste para Organizações Não Governamentais.")


# Use st.write("") para adicionar um texto ao seu Web app
st.write("Um crédito de carbono equivale a R$175,00")

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

# Use st.write("") para adicionar um texto ao seu Web app
st.write("Insira abaixo as informações necessárias para o cálculo.")

# Selecionar o gás.
option = st.selectbox(
    'Qual gás nocivo deseja reduzir?',
    ('CO2 (Carbono)', 'CH4 (Gás Metano)', 'SF6 (Hexafluoreto de Enxofre)'))

#Coleção dos dados relacionados à quantidade reduzida.
number = st.number_input('insira o valor em Toneladas')

#Botão que aciona o cálculo de proporção de ganho pela quantia reduzida da emissão.
if st.button('Consultar'):
  if option == 'CO2 (Carbono)':
    st.write(number, "toneladas conferem", number, "créditos")  
    
    
  if option == 'CH4 (Gás Metano)':
    st.write(number, "toneladas conferem", number*21, "créditos")
    number = 21*number
    
  if option == 'SF6 (Hexafluoreto de Enxofre)':
    st.write(number, "toneladas conferem", number*23900, "créditos")
    number = 23900*number
   
 # Tabela representando a proporção e distribuição do ganho por tonelada de gás reduzido.
  st.write("Valor Doado: ")
  st.write("R$", (number/100)*10, " (10%)")
    
  st.write("Lucro da Empresa: ")
  st.write("R$", (number/100)*70, " (70%)")
   
  st.write("Parcela do Serviço contratado: ")
  st.write("R$", (number/100)*20, " (20%)")


