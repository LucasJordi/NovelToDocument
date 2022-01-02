# Scrap de Novels para documentos
Esse código possibilita capturar todos os capítulos de uma novel pré-definida e transformar em documentos separados ( Ainda apenas em txt).

### OBS:
Sites suportados:

* [NovelFull](https://novelfull.com/)
* [WuxiaWorld](https://www.wuxiaworld.com/)
* [Nano Mashin Online](https://www.nanomashin.online/)



## Primeiros passos:


### WebDriver


Para poder utilizar o script é preciso ter o aequivo chromedriver com a respectiva versão do Chrome da sua máquina. Como saber qual a versão do seu Chrome? No Chrome, em opções acessar "Ajuda" > "Sobre o Google Chrome".

Após descobrir a sua versão, acessar a respectiva versão em [ChromeWebDriver](https://chromedriver.storage.googleapis.com/index.html) e extrair o arquivo "chromedriver" na pasta raiz do projeto.



### Instalando dependências:


```
# Usar o comando:
pip install -r requirements.txt 
```


## Utilizando a ferramenta


Dentro do Script usar:
```
# Exemplo: Dentro de novelfull.py
getChapters(LINK DA NOVEL)

# Terminal:
python novelfull.py
```
