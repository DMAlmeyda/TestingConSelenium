# Testing con selenium utilizando el patron POM(Page Object Model)
# TABLA DE CONTENIDOS
- [Tecnologias](#tecnologias)
- [Dependencias](#dependencias)
- [Estrategias](#estrategias)
- [POM](#pom)
- [TestSuit01](#testSuit01)
- [TestSuit02](#testSuit02)
- [Resultados](#resultados)  
 
  
    
   
 


# Descripcion

> Estos son unas pruebas automatizadas a un demo website para comprobar su correcto funcionamiento. 

>En este caso las pruebas estan orientadas a la compra de un producto, y comprobar el correcto funcionamiento de los enlaces para compartir el producto en redes sociales

>TestSuit01 requirements https://github.com/DMAlmeyda/TestingConSelenium/blob/93672699b5cede3e9b75094a483b8fabfa6025c3/Requirements/Requisitos_TestSuit01.pdf

>TestSuit02 requirements https://github.com/DMAlmeyda/TestingConSelenium/blob/93672699b5cede3e9b75094a483b8fabfa6025c3/Requirements/Requisitos_TestSuit02.pdf
 
>El sitio web que se utilizara para las pruebas es el siguiente https://academybugs.com/find-bugs/ (es un sitio interesante ya que contiene muchos bugs asi se debe tener mayor atencion)

<!-- toc -->

## Tecnologias
* Selenium
* request(libreria)
* html report(libreria)
* IDE: Pycharm



## Estrategias

* En este caso se utilizara el patron POM para lograr un testing mas facil de mantener en el tiempo y mas legible, pero ademas se prestara atencion a los localizadores buscando cuidadosamente cual elegir para que los tests se mantenga en el tiempo.

* Tambien en uno de los test deberemos comprobar si los links para compartir un producto funcionan correctamente asi que se comprobaremos que el codigo de estado http/s sea de 200

* Abajo se ve una imagen de un arbol representando los localizadores mas importantes(los frutos bajos)

![selenium-locators-apple-tree-diagram-dashed-fixed](https://user-images.githubusercontent.com/108648799/216841593-d6a4b27b-1396-4d5a-a3eb-a7ea90e6d0ba.png)

> Para mas informacion visitar www.quality-stream.com/selenium-webdriver-localizadores-estrategias-de-localizacion/



## POM
* El POM esta dividido en tres clases, una es la base con todas las funciones mas recurrentes de selenium y la otras contendran los metodos y atributos del sitio web a testear

* La clase base
https://github.com/DMAlmeyda/TestingConSelenium/blob/93672699b5cede3e9b75094a483b8fabfa6025c3/pom/Base.py#L1-L49

* las clases que contienen los atributos y metodos de la pagina hederan los metodos y atributos de la clase base

* La clase btn_viewCart 
https://github.com/DMAlmeyda/TestingConSelenium/blob/93672699b5cede3e9b75094a483b8fabfa6025c3/pom/btn_viewCart.py#L2-L33

* La clase share_links 
https://github.com/DMAlmeyda/TestingConSelenium/blob/93672699b5cede3e9b75094a483b8fabfa6025c3/pom/share_links.py#L2-L85

## TestSuit01

* Se testea el sitio web respetando los requerimentos especificados.
https://github.com/DMAlmeyda/TestingConSelenium/blob/93672699b5cede3e9b75094a483b8fabfa6025c3/testsuit_1/TestCase01_test.py#L2-L46

## TestSuit02
https://github.com/DMAlmeyda/TestingConSelenium/blob/93672699b5cede3e9b75094a483b8fabfa6025c3/testsuit_2/TestCase01_test.py#L1-L66


## Resultados

> No todas las pruebas pasaron

> Link del reporte generado https://raw.githack.com/DMAlmeyda/TestingConSelenium/master/report.html








