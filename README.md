# Selenium Testing
# TABLA DE CONTENIDOS
- [Tecnologias](#tecnologias)
- [TestSuit_1](#testsuit_1)
- [TestSuit_2](#testsuit_2)
- [Resultados](#resultados)
  
    
   
 


# Descripcion

> Son unos casos de pruebas probando funcionalidades especificas que estan descritas en la carpeta Requeriments, el website a utilizar es https://academybugs.com/find-bugs/ es una pagina educativa ya que contiene bugs por lo cual es mas interesante para ver si las funciones estan bien desarrolladas o no. <!-- toc -->

## Tecnologias
* Librerias: Selenium, Request, unittest, time
* driver: Chromedriver(importante componente para poder utilizar selenium)

## TestSuit_1
>Leer los requirements https://github.com/DMAlmeyda/TestingConSelenium/blob/65fa8f69306d8652f45f4d42d6d8959ab9cd06e0/Requirements/Requisitos_TestSuit01.pdf

Esta divido en dos test, en uno se testea el boton comprar en donde debe aparecer una pantalla confirmando que la compra fue exitosa

https://github.com/DMAlmeyda/TestingConSelenium/blob/65fa8f69306d8652f45f4d42d6d8959ab9cd06e0/TestSuit_1/TestCase01_test.py#L20-L24

En el segundo confirmamos que los productos esten siendo visualizados en el ViewCart

https://github.com/DMAlmeyda/TestingConSelenium/blob/65fa8f69306d8652f45f4d42d6d8959ab9cd06e0/TestSuit_1/TestCase01_test.py#L26-L43

Codigo completo

https://github.com/DMAlmeyda/TestingConSelenium/blob/65fa8f69306d8652f45f4d42d6d8959ab9cd06e0/TestSuit_1/TestCase01_test.py#L2-L50


## TestSuit_2

>Leer los requeriments https://github.com/DMAlmeyda/TestingConSelenium/blob/65fa8f69306d8652f45f4d42d6d8959ab9cd06e0/Requirements/Requisitos_TestSuit02.pdf

Se testea especificamente que los enlaces respondan entonces extraemos los enlaces atravez del dev tools de chrome y verificamos con la libreria request que su estado sea optimo.

En algunos casos se hizo una prueba especial porque el sistema anterior dicho no se adaptaba adecuadamente.

Codigo Completo

https://github.com/DMAlmeyda/TestingConSelenium/blob/65fa8f69306d8652f45f4d42d6d8959ab9cd06e0/TestSuit_2/TestCase02_test.py#L2-L80

## Resultados

* TestSuit_01 Todas las pruebas se ejecutaron como se esperaba.

Evidencia 
  
  
  ![TestCase01](https://user-images.githubusercontent.com/108648799/208528214-22f19b13-e835-4439-bf5b-e47ddf65e3eb.PNG)

* TestSuit_02 No paso con exito se encontro desperfectos en dos partes

Evidencia
  
  
  ![TestCase02](https://user-images.githubusercontent.com/108648799/208528466-10a5c753-bae3-4d80-a527-87bc4de0f813.PNG)






