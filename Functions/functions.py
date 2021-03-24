import pandas as pd
from datetime import datetime

## Funcao para carregar o arquivo de dados de tempo disponível para anuncios
def read_inv(file_inv):
    #file_inv = '../Data/tvaberta_inventory_availability.csv(1).csv'
    dateparser_inv = lambda x: datetime.strptime(x, '%d/%m/%Y')
    sep_inv = ';'
    parsedates_inv = ['date']
    df_inv = pd.read_csv(file_inv,
                         sep=sep_inv,
                         parse_dates=parsedates_inv,
                         date_parser=dateparser_inv)
    df_inv['weekday'] = df_inv.date.dt.dayofweek
    # acrescentando colunas do outro conjunto de dados de audiencia media e prevista para realizar mesclagem dos conjuntos
    # valores sao inicializados com -1, caso alguma requisicao retorne com -1 em audiencia prevista significa que a data do registro correspondeu apenas à este conjunto df_inv.
    df_inv['average_audience'] = -1
    df_inv['predicted_audience'] = -1
    return df_inv


## Funcao para carregar o arquivo de dados de media historica de anuncios
def read_pro(file_pro):
    #file_pro = '../Data/tvaberta_program_audience(1).csv'
    dateparser_pro = lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%fZ")
    sep_pro = ','
    parsedates_pro = ['program_start_time']
    indexcol_pro = 'program_start_time'
    df_pro = pd.read_csv(file_pro,
                         sep=sep_pro,
                         parse_dates=parsedates_pro,
                         date_parser=dateparser_pro)
    df_pro['exhibition_date'] = pd.to_datetime(df_pro['exhibition_date'], format='%Y-%m-%d')
    df_pro = df_pro.rename(columns={"exhibition_date": "date"})
    df_pro['weekday'] = df_pro.date.dt.dayofweek  
    # inicializando audiencia prevista em -1
    df_pro['predicted_audience'] = -1
    # valores de tempo estimado inicializados com -1, caso alguma requisicao retorne com -1 em tempo estimado significa que a data do registro correspondeu apenas à este conjunto df_pro.
    df_pro['available_time'] = -1
    del df_pro['program_start_time']
    return df_pro

## Calculo da mediana que recebe como parametro um pandas dataframe, uma coluna alvo de calculo e uma janela temporal de calculo.
def median_window(df,target,window):
    if len(df[target])>0:
        # o calculo da mediana se da pelo valor na posicao central do conjunto ordenado portanto as linhas do dataframe sao ordenadas com base na coluna alvo, com complexidade n*log(2)*n em qualquer caso de ordenacao. Dado que o pandas utiliza o algoritmo merge sort na funcao .sort_values
        df.sort_values(by=[target])
        # captura-se o primeiro valor da coluna alvo do daframe
        fill = df[target].values[0]
        # se o tamanho do dataframe for par, deve-se calcular a mediana atraves da media do valor central e o proximo elemento, dentro da janela de calculo
        if window % 2 == 0:
            s1 = int(window / 2)
            s2 = int(window / 2) + 1
            # para otimizacão do calculo da mediana sao utilizados 2 vetores com a coluna de valores deslocados pelo tamanho da janela de calculo, que no caso deste exercicio tem tamanho 4. Portanto a mediana, de janela 4, para qualquer registro dentro do dataframe ordenado sera a media aritmetica entre o 2o e 3o valor anterior à este registro.
            laux1 = df[target].shift(s1,fill_value=fill)
            laux2 = df[target].shift(s2,fill_value=fill)
            return ((laux1 + laux2) / 2)
        else:
            s1 = int(window/2) + 1
            return df[target].shift(s1,fill_value=fill)

# Função para varrer o dataframe com os registros de audiencia e calcular a mediana para cada registro pertencente a uma localizacao, codigo de programa e dia da semana distinto.
def df_predicted_audience(df):
    # obtendo lista de localizacoes distintas de transmissao
    l_signal = df.signal.unique()
    # iteracao para cada localizacao
    for v_signal in l_signal:
        # filtrando o dataframe para a localizacao da iteracao
        df_aux = df.loc[df['signal'] == v_signal]
        # obtendo lista de programas distintos dentro do dataframe filtrado
        l_program_code = df_aux.program_code.unique()
        # iterando sobre cada programa
        for v_program in l_program_code:
            # filtrando o dataframe a localizacao e codigo de programa da iteracao
            df_aux = df.loc[(df['signal'] == v_signal) & (df['program_code'] == v_program)]
            # obtendo lista de dias da semana disponiveis dentro do dataframe filtrado
            l_weekdays = df_aux.weekday.unique()
            for v_day in l_weekdays:
                # obtendo um dataframe auxiliar com todos os registros da localizacao, codigo de programa e dia da semana filtrados
                df_aux = df.loc[(df['weekday'] == v_day) & (df['signal'] == v_signal) & (
                            df['program_code'] == v_program)]
                #df_aux.sort_values(by=['average_audience'])
                # acionando a funcao para o calculo da audiencia estimada por meio da mediana, dentro do dataframe auxiliar
                df_aux['predicted_audience'] = median_window(df_aux,'average_audience',4)
                # gravando os valores de audiencia estimada correspondentes aos indices dos registros filtrados no dataframe resultante.
                df.predicted_audience.loc[df_aux.index] = df_aux['predicted_audience'].values
    return df