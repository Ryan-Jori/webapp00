#Projeto Hackathon Mackenzie2022
#EcoDoa

#Bibliotecas
import streamlit as st
from PIL import Image

#Separação de Abas
tab1, tab2, tab3, tab4 = st.tabs(["Início", "Sobre Nós", "Informações", "Amostra"])

with st.sidebar:
    cola, colb, colc = st.columns([1,6,1])
    with cola:
        st.write("")
    
    with colb:
        st.image('https://media.discordapp.net/attachments/1021891230868717588/1022296227645239306/ecodoalogo-removebg-preview.png', width=200)

    with colc:
        st.write("")
        
add_selectbox = st.sidebar.selectbox(
    "Contate-nos via:",
    ("Email", "Telefone")
)

#------------------------------------------------------------------------ Primeira Aba
with tab1:
    st.write("aaaaa")
    

#------------------------------------------------------------------------ Primeira Aba
with tab2:
    # Título
    cola, colb, colc = st.columns([4,6,2])

    with cola:
        st.write("")
    
    with colb:
        st.title('Eco Doa')

    with colc:
        st.write("")
        
    st.write("Nosso web aplicativo “EcoDoa” visa como pricipal objetivo a solução de dois problemas através da redução de CO2 e outros gases estufa liberados na atmosfera durante o processo produtivo de grandes empresas. A ideia base do projeto consiste em medir a redução da emissão de gás na atmosfera e após isso converter a quantidade em créditos (que virão dos fundos nacionais e internacionais), calcular a porcentagem que será destinada tanto para doação quanto para as empresas, assim incentivando a redução dos gases causadores do aquecimento  global por parte das grandes empresas, destinando parte desses créditos para instituições e projetos de caridade e também ajudando na preservação do ecossistema. ")
    st.image('https://img.freepik.com/premium-vector/ecological-stop-co2-emissions-sign-white-background-vector-illustration_100456-6232.jpg?w=740', width=100)
    
#------------------------------------------------------------------------ Segunda Aba
with tab3:
    # Use st.write("") para adicionar um texto ao seu Web app
    st.header('Créditos de Carbono')
    st.write('Crédito de carbono é um conceito surgido no fim dos anos 90, visando reduzir a emissão de gáses que intensificam o efeito estufa e combater o grande problema das mudanças climáticas. A ideia surgiu no Protocolo de Kyoto, dizendo que cada tonelada de carbono ou outros gases reduzida por um país, uma certificação é emitida pelo MDL (Mecanismo de Desenvolvimento Limpo).')
    st.write('Sendo assim, quanto mais reduzida é a emissão de carbono de um país, mais crédito se obtem. Atualmente, pode-se utilizar esta certificação como moeda com outros países que não tenham atingido sua meta anual estipulada. Existem diversas estratégias  para a redução destes compostos extremamente nocivos ao ambiente, tais como :')
    st.write('- Redução dos níveis de desmatamento')
    st.write('- Utilização de fontes de energia alternativas e mais limpas')
    st.write('- Incentivo para que empresas adotem um método de produção e consumo mais ecológico')
    st.write('O Brasil, por exemplo, consta entre os maiores emissores destes gases, provenientes do corte excessivo de arvores e desmatamento desenfreado. Nosso país consta como o 4º na lista das nações que mais poluem o ambiente desta forma, com 5% do total mundial desde o século 19.')
    
    st.header('Seu valor comercial')
    st.write('Em maio deste ano, o preço por crédito alcançou os 53 euros, equivalentes a 336 reais por tonelada, exibindo uma valorização exorbirtante de 260% desde os ultimos 3 anos.  O aumento vem sendo esponencial apenas por um fator : Oferta e Demanda')
    st.write ('A pressão pela redução destes gases acaba tornando necessária a possibilidade de comprar créditos de outras empresas para compensar seu débito, porém, o que acontece é que a demanda pela compra de tal crédito é muito maior que sua oferta, inflando assim seu preço.')
    
    st.write("Abaixo está informada uma tabela referenciando a quantidade de créditos obtidos pela redução da emissão de alguns gases específicos, note que seu perigo ambiental aumenta seu peso em créditos.")

    #Coluna Informativa relacionada ao ganho de créditos relacionados à emissão reduzida.
    col1, col2 = st.columns(2)
    col1.write("Carbono")
    col2.write("1 Crédito por Tonelada")

    col3, col4 = st.columns(2)
    col1.write("Metano")
    col2.write("21 Créditos por Tonelada")

    col5, col6 = st.columns(2)
    col1.write("Hexafluoreto de Enxofre")
    col2.write("23900 Créditos por Tonelada")
    
#------------------------------------------------------------------------ Terceira Aba
with tab4:
    
    st.title("Calculadora")
    
    # Use st.write("") para adicionar um texto ao seu Web app
    st.write("Insira abaixo as informações necessárias para o cálculo.")

    # Selecionar o gás.
    option = st.selectbox(
        'Qual gás nocivo deseja reduzir?',
        ('CO2 (Carbono)', 'CH4 (Gás Metano)', 'SF6 (Hexafluoreto de Enxofre)'))

    #Coleção dos dados relacionados à quantidade reduzida.
    number = st.number_input('insira o valor em Toneladas')
    
    values = st.slider('Valor a ser doado (Em porcentagem)', 5, 80, 45)

    #Botão que aciona o cálculo de proporção de ganho pela quantia reduzida da emissão.
    
    if st.button('Consultar'):
        
        #Coleta a informação dada dentro da caixa de seleção e exibe de acordo com o peso de cada gás em relação aos créditos condizentes
        if option == 'CO2 (Carbono)':
            st.write(number, "toneladas conferem", number, "créditos")  
            st.write(number, "créditos conferemR$", number*175)  

        if option == 'CH4 (Gás Metano)':
            st.write(number, "toneladas conferem", number*21, "créditos")
            number = 21*number
            st.write(number, "créditos conferemR$", number*175)  
            
        if option == 'SF6 (Hexafluoreto de Enxofre)':
            st.write(number, "toneladas conferem", number*23900, "créditos")
            number = 23900*number
            st.write(number, "créditos conferem R$", number*175)  

     # Tabela representando a proporção e distribuição do ganho por tonelada de gás reduzido.
        
        st.subheader("Valor Doado: ")
        st.write("R$", ((number*175)/100)*values, " (", values," %)")
        st.write("")

        st.subheader("Lucro da Empresa: ")
        st.write("R$", ((number*175)/100)*80-values, " (", 80 - values, "%)")
        st.write("")

        st.subheader("Parcela do Serviço contratado: ")
        st.write("R$", ((number*175)/100)*20, " (", 20, "%)")
        st.write("") 


