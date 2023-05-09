# Bibliotecas para tratamento de dados e importação de dados
from sklearn import tree
import csv
# Array de que armazena os dados
# x = Peso [100>x<200] e Textura [0 = aspera, 1 = lisa]
x = []
# y = Tipo da fruta Laranja [5] e Maçã [10]
y = []
# Adicionando dados nas Array
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      x.append([int(row[0]), int(row[1])])         
      y.append(int(row[2]))
# Arvore de decisão
clf = tree.DecisionTreeClassifier()
# Treinanado a IA
clf = clf.fit(x, y)
# Classificando o tipo de dado inportado
dado = clf.predict([[int(input('Peso: ')), int(input('Textura: '))]])
# Verificando dado para resposta
if dado[0] == 5:
  print('laranja')
else:
  print('maçã')