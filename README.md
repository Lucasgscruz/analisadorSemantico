# Analisador Sintático
Projeto apresentado ao curso de Ciência da Computação, da
Universidade Federal de São João del Rei, como requisito parcial
para obtenção da nota final da disciplina de Compiladores.

Este projeto consiste na implementação do analisador semântico e
gerador de código  Assembly de um compilador para a linguagem "C".

## Execução
Para executar o compilador, basta inserir na pasta "entrada" o arquivo com
o código fonte que deseja compilar, acessar a pasta raiz do projeto
através de um terminal linux e digitar o seguinte comando:

        python ./compilador.py ./entrada/<nome_do_arquivo_fonte.c>

caso queira executar o arquivo padrão "helloWorld.c" basta digitar o comando:

        make

## Saída
Como saída o compilador retorna uma mensagem informando se as análises léxica,
sintática e semântica foram executadas com êxito, ou se houve algum erro durante a
compilação. Caso algum erro tenha sido detectado, o mesmo é exibido
na tela do terminal juntamente com sua respectiva localização no código-fote(linha/coluna).
Após a compilação, na pasta raiz é criado um arquvio "executavel" contendo o código Assembly
que foi gerado a partir do código-fonte.

### Desenvolvido por:
![](https://github.com/Lucasgscruz.png?size=100)
Lucas Cruz ([github](https://github.com/lucasgscruz))
