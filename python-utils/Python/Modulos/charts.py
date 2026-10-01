import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def line_chart(X, y, theme='base', title='Titulo del gráfico', eje_x = 'Variable X', eje_y = 'Variable Y', line_color=None, multi_line=False, tags=False ,colors=None,save=False, path=None):
    
    fig, ax = plt.subplots(figsize=(12, 5))
    
    if theme == 'dark':
        fig.patch.set_facecolor('#21252b') 
        ax.set_facecolor('#282c34') 

        font_color='white'

    else:
        font_color='black'

    plt.title(title, color=font_color, weight=1000, fontsize=15)

    plt.xlabel(eje_x, color=font_color, fontsize=13)
    plt.ylabel(eje_y, color=font_color, fontsize=13)

    plt.xticks(fontsize=10, color=font_color, weight=500)
    plt.yticks(fontsize=10, color=font_color, weight=500)

    if multi_line == True:
        for i in range(len(y)):
            plt.plot(X[0], y[i], marker='o', color=colors[i])

            if tags==True:
                for j, label in enumerate(y[i]):
                    plt.annotate(label, (x[0][j] + 0, y[i][j]), color=font_color)

            
    else:
        plt.plot(X, y, marker='o', color=line_color)

        if tags==True:
            for i, label in enumerate(y):
                plt.annotate(label, (x[i] + 0, y[i] ), color=font_color)

        
    plt.grid(linewidth=0.2)

    if save:
        plt.savefig(path)
    else:
        plt.show()


if __name__ == '__main__':
    pass