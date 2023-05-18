
import numpy as np;
import matplotlib.pyplot as plt;

nome_colunas = np.array(['A','B','C','D'])
valores_colunas = np.array([3,8,1,10])


plt.style.use('Solarize_Light2')
plt.bar(nome_colunas,valores_colunas , color = 'blue')

plt.ylabel("Sua Legenda do Eixo Y")
plt.xlabel("Sua Legenda do Eixo X")
plt.title(" O Título do seu Gráfico ")
plt.show()