from os import abort
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Definiremos algumas funções que facilitaram os calculos
#Função que calcula o coeficiente angular da reta
def reta(xc,yc,xp,yp):
    #coeficiente angular
    m = (yp-yc)/(xp-xc)
    if(m == 0):
        print("O coeficiente angular não pode ser 0, insira os dados corretamente!")
        abort

    #cortaY da reta
    n = -1 * (m * xc - yc)
    return m; 

#ponto_camera = [x,y,z]
#ponto_projecao = [x,y,z]
#ponto_interseccao = [x,y,z]

print("Para conseguirmos encontrar o ponto no espaço em que dois feixes de luz se cruzam precisamos de duas câmeras posicionadas, para isso: ")

print("Insira os valores do ponto da câmera 1:")
xc1 = float(input("Valor de x da câmera 1: "))
yc1 = float(input("Valor de y da câmera 1: "))
zc1 = float(input("Valor de z da câmera 1: "))

print("Insira os valores do ponto da projeção da câmera 1:")
xp1 = int(input("Valor de x da projeção da câmera 1: "))
yp1 = float(input("Valor de y da projeção da câmera 1: "))
zp1 = float(input("Valor de z da projeção da câmera 1: "))


print("Agora, insira os valores do ponto da câmera 2:")
xc2 = float(input("Valor de x da câmera 2: "))
yc2 = float(input("Valor de y da câmera 2: "))
zc2 = float(input("Valor de z da câmera 2: "))

print("Insira os valores do ponto da projeção da câmera 2:")
xp2 = float(input("Valor de x da projeção da câmera 2: "))
yp2 = float(input("Valor de y da projeção da câmera 2: "))
zp2 = float(input("Valor de z da projeção da câmera 2: "))


print("Certo! Como estamos falando de um ponto no plano xyz, precisamos que você escolha em quais dois planos deseja fazer o cálculo da intersecção")
print("Para plano XY digite:       1")
print("Para plano XZ digite:       2")
print("Para plano ZY digite:       3")
print("E caso queira sair, digite: 4")
opcao_escolhida = int(input('Escolha uma opção: '))
2

if opcao_escolhida == 1:
    print("O plano escolhido foi o XY")
    m1 = reta(xc1,yc1,xp1,yp1)
    print("O coeficiente angular da reta 1 é, m=", m1)
    
    m2 = reta(xc2,yc2,xp2,yp2)
    print("O coeficiente angular da reta 2 é, m=", m2)

#X e Y do ponto de intersecção
    xi = (-(m2* xc2) + yc2 + (m1 + xc1) - yc1)/ (m1 - m2)
    yi = (m1*xi) - (m1*xc1) + yc1

    print("Com essas informações, concluimos que o X do ponto de cruzamento é :", xi ," e o Y é: ", yi)

 
elif opcao_escolhida == 2:
    print("O plano escolhido foi o XZ")
    m1 = reta(xc1,zc1,xp1,zp1)
    print("O coeficiente angular da reta 1 é, m=", m1)
    
    m2 = reta(xc2,zc2,xp2,zp2)
    print("O coeficiente angular da reta 2 é, m=", m2)

#X e Y do ponto de intersecção
    xi = (-(m2* xc2) + zc2 + (m1 + xc1) - zc1)/ (m1 - m2)
    yi = (m1*xi) - (m1*xc1) + zc1 #neste plano o Z tem funcão de Y

    print("Com essas informações, concluimos que o X do ponto de cruzamento é :"+ xi + " e o Y é: "+ yi)
 
elif opcao_escolhida == 3:
    print("O plano escolhido foi o ZY")
    m1 = reta(zc1,yc1,zp1,yp1)
    print("O coeficiente angular da reta 1 é, m=", m1)
    
    m2 = reta(zc2,yc2,zp2,yp2)
    print("O coeficiente angular da reta 2 é, m=", m2)

#X e Y do ponto de intersecção
    xi = (-(m2* zc2) + yc2 + (m1 + zc1) - yc1)/ (m1 - m2)#neste plano o Z tem função de X
    yi = (m1*xi) - (m1*zc1) + yc1

    print("Com essas informações, concluimos que o X do ponto de cruzamento é :", xi  ," e o Y é: ", yi)

elif opcao_escolhida == 4:
    print("Sair")
    exit
 
else:
    print("Por favor, selecione uma opção válida")


#Construindoo gráfico
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(projection = '3d')  #gráfico 3d vazio

ax.scatter(xc1, yc1, zc1, c='red', label='Câmera 1') #ponto - Câmera 1
ax.scatter(xp1, yp1, zp1, c='orange', label='Projeção da Câmera 1') #ponto - Projeção da Câmera 1
ax.scatter(xc2, yc2, zc2, c='blue', label='Câmera 2') #ponto - Câmera 2
ax.scatter(xp2, yp2, zp2, c='skyblue', label='Projeção da Câmera 2') #ponto - Projeção da Câmera 2

x1 = np.linspace(xc1, xp1)
y1 = np.linspace(yc1, yp1)
z1 = np.linspace(zc1, zp1)
ax.plot(x1, y1, z1, color = 'k') #linha Câmera-Projeção 1

x2 = np.linspace(xc2, xp2)
y2 = np.linspace(yc2, yp2)
z2 = np.linspace(zc2, zp2)
ax.plot(x2, y2, z2, color = 'k') #linha Câmera-Projeção 2

ax.legend() #quadro com as legendas
ax.set_xlim(0, 5) #limite do eixo x
ax.set_ylim(0, 5) #limite do eixo y
ax.set_zlim(0, 5) #limite do eixo z
ax.set_xlabel('X') #Nome do eixo x
ax.set_ylabel('Y') #Nome do eixo y
ax.set_zlabel('Z') #Nome do eixo z

plt.show()  #mostra o gráfico



