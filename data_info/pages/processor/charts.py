import seaborn as sns
import matplotlib.pyplot as plt
def display_outliers(df,x_col,y_col,z_col,color):
    
    fig,axes = plt.subplots(1,3,figsize=(12,5))

    fig.suptitle("Graphical representation of outliers")

    sns.boxplot(data=df,ax=axes[0],x=x_col, color=color)

    sns.histplot(data=df,x=x_col, kde=True,ax=axes[1],color=color)

    sns.scatterplot(data=df,x=x_col,y=y_col,hue=z_col,ax=axes[2],color=color)
    
    
    return fig
    
    
