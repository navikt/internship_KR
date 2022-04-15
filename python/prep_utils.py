import pandas as pandas
import numpy as np

def fetch_sql_file(query_script, con):
    """
    Run sql query against DWH
    Input:
    query_script - sql script
    con - (string) connection string

    returns: dataframe
    """
    query = open(query_script, 'r' )
    #print(query)  
    df_ = pandas.read_sql(query.read().format(), con=con)
    return df_

def map_tiltak_navn(df):
    """
    Prep dataframe by mapping tiltak navn to TILTAKKODE column 
    Input: - datafarme                   
    Returns: prepped pandas dataframe with new column (TILTAK_NAVN)
    """

    if "TILTAKSKODE" in df.columns:
        # add column "tiltak navn"

        df['TILTAK_NAVN'] = df['TILTAKSKODE'].map(tiltak_navn)
        return df

def replace_kjonn_id(df):
    """
    Prep dataframe by replacing kjonn_id  
    Input: - datafarme                   
    Returns: prepped pandas dataframe
    """
    # replacing tiltak kode and  kjonn_id 
    df['TILTAKSKODE'] = df['TILTAKSKODE'].replace ('AMOE','ENKELAMO')
    df['KJONN_ID'] = df['KJONN_ID'].replace([9,10],['kvinner','Menn'])


    return df

#grouping and finding percentage 

def find_kjonn_percentage(df,column):
    """
    Prep dataframe by using groupby function and finding percentage
    Input: - datafarme  
             column : grouping dataframe by specific column
    Returns: prepped pandas dataframe
    """ 

    # groupby function
    grp_df = df.groupby(['KJONN_ID']).agg({column: 'count'})
    # add column "andel"
    grp_df['Andel(%)'] = np.round(100.* grp_df[column] / grp_df[column].sum(),1)
    grp_df = grp_df.reset_index()
    return grp_df


def fetch_flykenummer_map_flyke_navn(df):
    """
    Prep dataframe by extracting first 2 digits from counties column and mapping to fylker

    Input: - datafarme 
    Returns: prepped pandas dataframe
    """

    df['PERSON_GEOGRAFI_KOMMUNENR'] = df['PERSON_GEOGRAFI_KOMMUNENR'].fillna(0)
    df['Flyke'] = [str(x)[0:2] for x in df['PERSON_GEOGRAFI_KOMMUNENR']]

    df['Flyke'] = df['Flyke'].astype(float).round(1)
    if 'Flyke' in df.columns:
        df['flyke_new'] = df['Flyke'].map(flyker_2020)
        
        #Drop unnecessary counties

        df.drop(df[ df['flyke_new'] == 'Annet bosted'].index,inplace=True)
        df.drop(df[ df['flyke_new'] == 'Svalbard'].index,inplace=True)

        return df


def flyke_percentage_alletiltak(df,column1,column2):
    """
    Prep dataframe by using groupby function and finding percentage for counties with all measures
    Input: - datafarme 
             column 1: grouping dataframe by specific column
             column 2: aggregating by specific column
    Returns: grouped and aggregrated pandas dataframe
    """ 


    grp_df = df.groupby([column1,'KJONN_ID']).agg({column2: 'count'})
    andel_grp_df = grp_df.groupby(level=[0]).apply(lambda x:100 * x / x.sum()).round(1)
    return andel_grp_df




def flyke_percentage_arbtren_midlønn(df,column1,column2):
    """
    Prep dataframe by using groupby function and finding percentage for counties with worktraining and temporary wages measures 
    Input: - datafarme 
            column 1: grouping dataframe by specific column
            column 2: aggregating by specific column
    Returns: grouped and aggregrated pandas dataframe
    """
    grp_df =df.groupby([column1,'KJONN_ID']).agg({column2:'nunique'})
    andel_df = grp_df.groupby(level=[0]).apply(lambda x:100 * x / x.sum()).round(1)
    return andel_df






