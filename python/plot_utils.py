import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
from matplotlib.ticker import FormatStrFormatter



def create_kjonn_bar(df,column):
    """
    Creating bar plot
    
    """ 
    if(column == 'PERSON_ID'):
        #plt.title('Distribution of men and women who completed temporary wage subsidies in the period 2018-2020 ', size = 18)

        fig  = plt.bar(x=df['KJONN_ID'], height=df['Andel(%)'])
        plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
        plt.ylabel('Andel(%)')
        plt.figure(figsize=(10,10))
    elif(column == 'COUNT'):
        #plt.title(' Distribution of men and women who completed all measures in the period 2018-2020  ', size = 18)
        
        fig  = plt.bar(x=df['KJONN_ID'], height=df['Andel(%)'])
        plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
        plt.ylabel('Andel(%)')
    
    return fig


def create_flyke_bar(df,column):
    """
    Creating bar plot 
    """ 
    if(column == 'PERSON_ID'):
        graph =df.unstack('KJONN_ID').plot(kind='bar', stacked=False,figsize=(10,5))
        for p in graph.patches:
            graph.annotate((format((p.get_height()))), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=10,
                   xytext = (0, -12), 
                   textcoords = 'offset points')

        graph.axhline(50)
        #plt.title('Distribution of men and women in temporary wage subsidies by county in the period 2018 - 2020', size = 20)
        plt.ylabel('Andel(%)')
        plt.legend(bbox_to_anchor=(1.05, 1.03))


    elif(column == 'COUNT'):
        graph =df.unstack('KJONN_ID').plot(kind='bar', stacked=False,figsize=(10,5))
        for p in graph.patches:
            graph.annotate((format((p.get_height()))), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=10,
                   xytext = (0, -12), 
                   textcoords = 'offset points')

        graph.axhline(50)
        #plt.title('Distribution of men and women in all measures by county in the period 2018 - 2020', size = 20)
        plt.ylabel('Andel(%)')
        plt.legend(bbox_to_anchor=(1.05, 1.03))

    return graph


def create_flyke_bar(df,column):
    """
    Creating bar plot 
    """ 
    if(column == 'PERSON_ID'):
        graph =df.unstack('KJONN_ID').plot(kind='bar', stacked=False,figsize=(10,5))
        for p in graph.patches:
            graph.annotate((format((p.get_height()))), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=10,
                   xytext = (0, -12), 
                   textcoords = 'offset points')

        graph.axhline(50)
        #plt.title('Distribution of men and women in temporary wage subsidies by county in the period 2018 - 2020', size = 20)
        plt.ylabel('Andel(%)')
        plt.legend(bbox_to_anchor=(1.05, 1.03))


    elif(column == 'COUNT'):
        graph =df.unstack('KJONN_ID').plot(kind='bar', stacked=False,figsize=(10,5))
        for p in graph.patches:
            graph.annotate((format((p.get_height()))), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   size=10,
                   xytext = (0, -12), 
                   textcoords = 'offset points')

        graph.axhline(50)
        #plt.title('Distribution of men and women in all measures by county in the period 2018 - 2020', size = 20)
        plt.ylabel('Andel(%)')
        plt.legend(bbox_to_anchor=(1.05, 1.03))

    return graph


def create_sub_plot(df,column):
    """
    Prep dataframe for subplot for counties and age groups  
    Input: - dataframe
           - column : specific column(counties and age groups)  
    Returns : sub plot 
    
    """
    
    df = df.reset_index()
    # Renaming the columns                       
    df.columns._data[2] = 'Alle_tiltak'
    df.columns._data[3] = 'Arbeidstrening'
    df.columns._data[4] = 'Midlertidig_lønnstilskudd '
    #df

    lst_column = df[column].unique()
    #print(lst_column)
    labels = []

    labels.append('Alle_tiltak')
    labels.append('Arbeidstrening')
    labels.append('Midlertidig_lønnstilskudd')
    men_list = [];
    kvinne_list = [];

    for i in lst_column:
        listts = df.values.tolist()
        list_kjonn_column =[a[2:] for a in listts]
        
    for i in range(0, len(list_kjonn_column)):
        if i % 2:
            kvinne_list.append(list_kjonn_column[i])
        else :
            men_list.append(list_kjonn_column[i])

    #print(listts)

    #print('menn list:',men_list)
    #print('@@@@@@@@')
    #print('kvinner list:',kvinne_list)
    
    #creating subplot
    x = np.arange(len(labels))
    #print(x)
    width = 0.3
    if(column == 'flyke_new'):
        fig,axs = plt.subplots(4,3, figsize=(15,15),sharex=True, sharey=True)
        #fig.suptitle("Andel av  kvinner og menn som har fullført alle tiltak,midl. lønnstilskudd og arbeidstrening  etter fylke i perioden 2018-2020", fontsize = 20)

        index = 0
        for i in range(0,4):
            for j in range(0,3):
                if(i == 3 and j == 2):
                    axs.flat[-1].set_visible(False)
                else:
                    #print(index)
                    menn_bar =axs[i,j].bar(x-width/2, men_list[index], width, label='Menn')
                    kvinner_bar =axs[i,j].bar(x+width/2, kvinne_list[index], width, label='Kvinner')
                    axs[i,j].set_title(lst_column[index])
                    axs[i,j].bar_label(menn_bar, padding=2)
                    axs[i,j].bar_label(kvinner_bar, padding=2)
                    axs[i,j].axhline(50)
                    axs[i,j].legend()
                    #print(men_flyke_list[index], '   ---  ', kvinne_flyke_list[index],'----' , lst_flyke[index])
                    index = index + 1 
    elif(column == 'alder_gruppen'):
        fig,axs = plt.subplots(2,2, figsize=(15,10),sharex=True, sharey=True)
        #fig.suptitle("Proportion of women and men who have completed all measures, temporary wage subsidy and work training by county in the period 2018-2020", fontsize = 20)

        index = 0
        
        for i in range(0,2):
            for j in range(0,2):
                #print(index)
                menn_bar =axs[i,j].bar(x-width/2, men_list[index], width, label='Menn')
                kvinner_bar =axs[i,j].bar(x+width/2, kvinne_list[index], width, label='Kvinner')
                axs[i,j].set_title(lst_column[index])
                axs[i,j].bar_label(menn_bar, padding=2)
                axs[i,j].bar_label(kvinner_bar, padding=2)
                axs[i,j].axhline(50)
                axs[i,j].legend()
                #print(men_flyke_list[index], '   ---  ', kvinne_flyke_list[index],'----' , lst_flyke[index])
                index = index + 1 
  
    plt.xticks([0,1,2], labels, fontsize=18)
    # Add some text for labels, title and custom x-axis tick labels, etc.
    
    fig.tight_layout()

def create_sankey_midlønn(df):
    """Preparing data(temporary wage measure) for Sankey diagram"""
   
    my_dict = {}
    my_dict.clear()
    my_dict_overall_percentages  =  {}
    my_dict_overall_percentages.clear()
    count_temp = 0
    for T in df:
        #print(T)
        count = 0
        flag = False
        #if(count_temp == 500):
            #break
        for elem in T:
            #print('----',elem)
            count = count + 1
            index = 0
                #if(isinstance(elem, int) == True):
                #print('----------------',T)
                #break
            if(isinstance(elem, int) == False):
                #print(isinstance(elem,object))
                #print('-',elem,'-')
                #print(elem.strip())
            
                #print(elem.to_dict())
            
                #print('----->>>>>>',elem['TILTAKSKODE'])
                try:
                    llst= list(elem['TILTAK_NAVN'])
                    #print(llst)
                    if(len(llst) == 1 ):
                        break 
                    if 'Midlertidig_lønnstilskudd' in llst :
                        #print('----->>>>>>',llst)
                        index=llst.index("Midlertidig_lønnstilskudd")
                        #print(index)
                        if(len(llst) == 2):
                            if(llst[0] == "Midlertidig_lønnstilskudd" and llst[1] == "Midlertidig_lønnstilskudd"):
                                break
                            elif (llst[index + 1]  == "Midlertidig_lønnstilskudd"):
                                break
                            else:
                                my_dict[llst[index+1]] = my_dict.setdefault(llst[index+1],0) + 1
                                #print('2=====', my_dict)
                        elif(len(llst) > 2):
                            #print('-------')
                                if(llst[index+1]== "Midlertidig_lønnstilskudd"):
                                    index = index + 2
                                else:
                                    index = index + 1
                                my_dict[llst[index]] = my_dict.setdefault(llst[index],0) + 1
                                count_temp = count_temp+1
                                #print('3====',my_dict)
                except:
                    #print("Oops!")
                    #print(llst)
                    if(index+1 < len(llst)):
                        my_dict[llst[index+1]] = my_dict.setdefault(llst[index+1],0) + 1
                        #print('excp====',my_dict)
    
    #print(my_dict)   
    my_dict["Midlertidig_lønnstilskudd"]  = 0  


    # finding total percentage
    values = my_dict.values()

    count = 0 
    total = sum(values)
    for key in my_dict:
        
        #print(my_dict[key])
        percentage = (my_dict[key] / total) * 100
        #print(percentage)
        if(percentage < 5):
            count = count + my_dict[key]
        else:
            my_dict_overall_percentages[key] = percentage
    my_dict_overall_percentages["Midlertidig_lønnstilskudd"]  = 0  

    my_dict_overall_percentages['ANDRE TILTAK'] = (count / total) * 100
    #print(my_dict_overall_percentages['ANDRE TILTAK'])


    return my_dict_overall_percentages
    #print (my_dict_overall_percentages)


def draw_sankey_midlønn(my_dict_1,my_dict_2,my_dict_3):
    """Draw up a Sankey diagram"""

    dict_list_1 = sorted(my_dict_1.keys())

    source_1=[]
    target_1=[]
    value_1=[]

    source_1.clear()
    target_1.clear()
    value_1.clear()

    idx=0
    for ind in dict_list_1:
        #print(ind)
    
        index=dict_list_1.index("Midlertidig_lønnstilskudd")
        target_1.append(index)
        source_1.append(idx)
        value_1.append(my_dict_1[ind])
        idx = idx + 1

    
    trace1 = go.Sankey(arrangement = "snap",valueformat = ".0f",domain={
       'x': [0, 0.45],
            'y': [0.55, 1],
    },

    node = dict( 
           pad = 15 ,
          thickness = 20,
          line = dict(color = "green", width = 0.5),
         label = dict_list_1, color = "blue"
     
    ),
    link = dict(label = dict_list_1,
          
          # indices correspond to labels
      
        source = source_1, 
          target = target_1,
          value = value_1
    ))
    
        
    data_1 = [trace1]

    layout =  go.Layout(height =700,
        font = dict(
          size = 10
        ),title_text="TMeasures that users have had before the temporary wage subsidy in the period 2018-2020 ", font_size=10)


    fig_1 = go.Figure(data=data_1, layout=layout)

    fig_1.show()
 
    dict_list_2 = sorted(my_dict_2.keys())

    source_2=[]
    target_2=[]
    value_2=[]

    source_2.clear()
    target_2.clear()
    value_2.clear()

    idx=0
    for ind in dict_list_2:
        #print(ind)
    
        index=dict_list_2.index("Midlertidig_lønnstilskudd")
        target_2.append(index)
        source_2.append(idx)
        value_2.append(my_dict_2[ind])
        idx = idx + 1

    
    trace2 = go.Sankey(arrangement = "snap",valueformat = ".0f",domain={
       'x': [0, 0.45],
            'y': [0.55, 1],
    },

    node = dict( 
           pad = 15 ,
          thickness = 20,
          line = dict(color = "green", width = 0.5),
         label = dict_list_2, color = "blue"
     
    ),
    link = dict(label = dict_list_2,
          
          # indices correspond to labels
      
        source = source_2, 
          target = target_2,
          value = value_2,
    ))
    
    dict_list_3= sorted(my_dict_3.keys())

    source_3=[]
    target_3=[]
    value_3=[]

    source_3.clear()
    target_3.clear()
    value_3.clear()

    idx=0
    for ind in dict_list_3:
        #print(ind)
    
        index=dict_list_3.index("Midlertidig_lønnstilskudd")
        target_3.append(index)
        source_3.append(idx)
        value_3.append(my_dict_3[ind])
        idx = idx + 1

    
    trace3 = go.Sankey(arrangement = "snap",valueformat = ".0f",domain={
            'x': [0.55, 1],
            'y': [0, 0.45],
        },

    node = dict( 
           pad = 15 ,
          thickness = 20,
          line = dict(color = "green", width = 0.5),
         label = dict_list_3, color = "red"
     
    ),
    link = dict(label = dict_list_3,
          
          # indices correspond to labels
      
        source = source_3, 
          target = target_3,
          value = value_3
    ))
    
    
    data = [trace2,trace3]

    layout =  go.Layout(height = 700,
        font = dict(
          size = 10
        ),title_text="Measures that men and women have had prior to temporary wage subsidies in the period 2018-2020 ", font_size=10)

    fig = go.Figure(data=data, layout=layout)

    fig.show()


def create_sankey_arbtren(df):
    """Preparing data(work training measure) for Sankey diagram"""
   
    my_dict = {}
    my_dict.clear()
    my_dict_overall_percentages ={}
    my_dict_overall_percentages.clear()

    count_temp = 0


    
    for T in df:
    #print(T)
        flag = False
        #if(count_temp == 20):
            #break
        for elem in T:
            #print('----',elem)
            index = 0
                #if(isinstance(elem, int) == True):
                #print('----------------',T)
                #break

            if(isinstance(elem, int) == False):


                #print(isinstance(elem,object))
                #print('-',elem,'-')
                #print(elem.strip())
            
                #print(elem.to_dict())
            
                #print('----->>>>>>',elem['TILTAKSKODE'])
                try:
                    llst= list(elem['TILTAK_NAVN'])
                    #print(llst)
                    if(llst[0] == "Arbeidstrening" ):
                        break
                    if(len(llst) == 1 ):
                        break 
                    if 'Arbeidstrening' in llst :
                        index=llst.index("Arbeidstrening")
                        #print('----->>>>>>',llst, index)


                        #print(index)
                        if(len(llst) == 2):
                            if(llst[0] == "Arbeidstrening" and llst[1] == "Arbeidstrening"):
                                break
                            else:
                                my_dict[llst[index-1]] = my_dict.setdefault(llst[index-1],0) + 1
                                #print('===222==' ,my_dict)
                        elif(len(llst) > 2):   
                                if(llst[index+1] == "Arbeidstrening"):
                                    index = index - 2
                                else:
                                    index = index - 1
                                my_dict[llst[index]] = my_dict.setdefault(llst[index],0) + 1
                            
                                #print('==33===',my_dict)
                                count_temp = count_temp +1 


                except:
                    #print("Oops!")
                    #print(llst)
                    if(index+1 <= len(llst)):
                        my_dict[llst[index-1]] = my_dict.setdefault(llst[index-1],0) + 1
                        #print('===== excep ==',my_dict)



    my_dict["Arbeidstrening"]  = 0
    #print(my_dict)


    # finding total percentage
    values = my_dict.values()

    count = 0 
    total = sum(values) 
    #print(total)
    for key in my_dict:
        
        #print(my_dict[key])
        percentage = (my_dict[key] / total) * 100
        #print(percentage)
        if(percentage < 5):
            count = count + my_dict[key]
        else:
            my_dict_overall_percentages[key] = percentage
    my_dict_overall_percentages["Arbeidstrening"]  = 0  

    my_dict_overall_percentages['ANDRE TILTAK'] = (count / total) * 100

    #print(my_dict)

    return my_dict_overall_percentages
    #print (my_dict_overall_percentages)



def draw_sankey_arbtren(my_dict_1,my_dict_2,my_dict_3):
    
    """Draw up a Sankey diagram"""


    dict_list_1 = sorted(my_dict_overall.keys())

    source_1=[]
    target_1=[]
    value_1=[]

    source_1.clear()
    target_1.clear()
    value_1.clear()

    idx=0
    for ind in dict_list_1:
        #print(ind)
    
        index=dict_list_1.index("Arbeidstrening")
        #print(index)
        source_1.append(index)
        target_1.append(idx)
        value_1.append(my_dict_overall[ind])
        idx = idx + 1

    
    trace1 = go.Sankey(arrangement = "snap",valueformat = ".0f",domain={
       'x': [0, 0.45],
            'y': [0.55, 1],
    },

    node = dict( 
           pad = 15 ,
          thickness = 20,
          line = dict(color = "green", width = 0.5),
         label = dict_list_1, color = "blue"
     
    ),
    link = dict(label = dict_list_1,
          
          # indices correspond to labels
      
        source = source_1, 
          target = target_1,
          value = value_1
    ))
    
        
    data_1 = [trace1]

    layout =  go.Layout(height =850,
        font = dict(
          size = 10
        ),title_text="Measures that users have had after work training in the period 2018-2020", font_size=10)


    fig_1 = go.Figure(data=data_1, layout=layout)

    fig_1.show()
 
    
 
    dict_list_2 = sorted(my_dict_man.keys())

    source_2=[]
    target_2=[]
    value_2=[]

    source_2.clear()
    target_2.clear()
    value_2.clear()

    idx=0
    for ind in dict_list_2:
        #print(ind)
    
        index=dict_list_2.index("Arbeidstrening")
        source_2.append(index)
        target_2.append(idx)
        value_2.append(my_dict_man[ind])
        idx = idx + 1

    
    trace2 = go.Sankey(arrangement = "snap",valueformat = ".0f",domain={
       'x': [0, 0.45],
            'y': [0.55, 1],
    },

    node = dict( 
           pad = 15 ,
          thickness = 20,
          line = dict(color = "green", width = 0.5),
         label = dict_list_2, color = "blue"
     
    ),
    link = dict(label = dict_list_2,
          
          # indices correspond to labels
      
        source = source_2, 
          target = target_2,
          value = value_2,
    ))
    
    dict_list_3= sorted(my_dict_kvinner.keys())

    source_3=[]
    target_3=[]
    value_3=[]

    source_3.clear()
    target_3.clear()
    value_3.clear()

    idx=0
    for ind in dict_list_3:
        #print(ind)
    
        index=dict_list_3.index("Arbeidstrening")
        source_3.append(index)
        target_3.append(idx)
        value_3.append(my_dict_kvinner[ind])
        idx = idx + 1

    
    trace3 = go.Sankey(arrangement = "snap",valueformat = ".0f",domain={
            'x': [0.55, 1],
            'y': [0, 0.45],
        },

    node = dict( 
           pad = 15 ,
          thickness = 20,
          line = dict(color = "green", width = 0.5),
         label = dict_list_3, color = "red"
     
    ),
    link = dict(label = dict_list_3,
          
          # indices correspond to labels
      
        source = source_3, 
          target = target_3,
          value = value_3
    ))
    
    
    data = [trace2,trace3]

    layout =  go.Layout(height = 850,
        font = dict(
          size = 10
        ),title_text="Measures that men and women have had after work training in the period 2018-2020 ", font_size=10)

    fig = go.Figure(data=data, layout=layout)

    fig.show()



