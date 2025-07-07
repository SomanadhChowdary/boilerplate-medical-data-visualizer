import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
def check_weight(x):
    if x>25:
        return 1
    else:
        return 0
df['overweight'] = (df['weight']/((df['height']/100)*(df['height']/100))).apply(check_weight)

# 3
df['cholesterol']=np.where(df['cholesterol']==1,0,1)
df['gluc']=np.where(df['gluc']==1,0,1)

# 4
def draw_cat_plot():
    df = pd.read_csv('medical_examination.csv')

# 2
    def check_weight(x):
        if x>25:
            return 1
        else:
            return 0
    df['overweight'] = (df['weight']/((df['height']/100)*(df['height']/100))).apply(check_weight)

# 3
    df['cholesterol']=np.where(df['cholesterol']==1,0,1)
    df['gluc']=np.where(df['gluc']==1,0,1)
    # 5
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # 6
    df_cat=df_cat.value_counts(['cardio','variable','value']).reset_index(name='total')
    

    # 7


    category_order=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    # 8
    fig = sns.catplot(x='variable',y='total',hue='value',col='cardio',data=df_cat,kind='bar',order=category_order).fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    df = pd.read_csv('medical_examination.csv')

# 2
    def check_weight(x):
        if x>25:
            return 1
        else:
            return 0
    df['overweight'] = (df['weight']/((df['height']/100)*(df['height']/100))).apply(check_weight)

# 3
    df['cholesterol']=np.where(df['cholesterol']==1,0,1)
    df['gluc']=np.where(df['gluc']==1,0,1)
    # 11
    df_heat = df[(df['ap_lo']<=df['ap_hi'])&(df['height']>=df['height'].quantile(0.025))&(df['height']<=df['height'].quantile(0.975))&(df['weight']>=df['weight'].quantile(0.025))&(df['weight']<=df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr().round(1)
    corr_values=np.round(corr.values,1)
    # 13
    mask = np.triu(np.ones_like(corr,dtype=bool))

    

    # 14
    fig, ax = plt.subplots(figsize=(12,10))

    # 15
    sns.heatmap(corr,mask=mask,annot=corr_values,fmt=".1f",center=0,square=True,linewidths=.5,cbar_kws={"shrink":0.5})


    # 16
    fig.savefig('heatmap.png')
    return fig
