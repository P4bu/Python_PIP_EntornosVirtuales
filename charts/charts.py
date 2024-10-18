# Crear venv para instalar dependencia y ejecutar README
import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A','B','C']
    values = [100,200,140]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('.pie.jpg')
    plt.close()