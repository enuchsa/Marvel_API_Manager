Bem vindo a minha tentativa de reproduzir um API

O intuíto desse projeto era criar uma API que consumisse uma API externa que fornece dados de heróis
Abaixo deixarei uma descrição de como baixar e rodar a API

* Passo 1 - Baixe ou clone o projeto, crie ou entre no seu ambiente virtual (estou usando o venv) abra o terminal e rode o comando `pip install -r requirements.txt` para instalar os módulos necessários
* Passo 2 - Rode o comando `py manage.py migrate` para que os models sejam criados no banco (estou usando o sqlite) mas caso você use o postgres ou outro banco será necessário ir no arquivo "settings.py" na pasta manager_heroes e ir em "DATABASES" lá será possível fazer a configuração de conexão de acordo com seu banco.
* Passo 3 - Rode o comando `py manage.py runserver` para iniciar a API

Aqui está o link com todos os endpoints pedidos [Marvel API.postman_collection.json](https://github.com/enuchsa/Marvel_API_Manager/files/14058678/Marvel.API.postman_collection.json)

Os endpoints de requitar listas ou um heróis não tem autenticação, já os demais tem, então será necessário primeiro ir nas rotas de autenticação.

obs: gostaria só de relatar que tive muitos problemas com internet e tempo esses dias, então só consegui fazer até este ponto, sei que falta os extras e algumas coisas bem necessárias mas me atnetei a fazer o essencial e ao sistema funcionar como pedido
