Funcionamento operação CRUD:

#1 uma requisicao HTTP com um memtodo - GET, POST, PUT, DELETE - eh feita
#2 requisicao passa pelo urls.py do project que passa pelo urls.py de my_app
#3 em urls.py de my_app ha uma indicacao de qual class na view chamar, conforme
a url
#4 em views.py ha classes <minhaClasseList> e <minhaClasseDetail> que possuem os
metodos para tratar requisicoes GET, POST, PUT, DELETE