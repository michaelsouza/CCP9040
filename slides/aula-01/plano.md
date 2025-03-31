Plano de Aula: Introdução à Programação Científica com Python (Baseado no Capítulo 1)
Objetivo Geral: Introduzir os conceitos fundamentais de programação utilizando Python como uma ferramenta para cálculos científicos, com base no Capítulo 1 do livro "A Primer on Scientific Programming with Python".
Duração Sugerida: 2-3 horas (ajustável dependendo do nível dos alunos e da profundidade desejada).
Público-Alvo: Iniciantes em programação, estudantes de ciências e engenharia.
Recursos: Computadores com Python 2.7 (recomendado pelo autor para os capítulos iniciais) e preferencialmente IPython instalado. Acesso à página web do livro para download de exemplos.
Estrutura da Aula:
1. Introdução (15 minutos)
•
Boas-vindas e apresentação dos objetivos da aula: aprender os primeiros passos na programação científica com Python.
•
Discussão sobre a importância do aprendizado prático em programação.
•
Breve introdução ao livro "A Primer on Scientific Programming with Python" e sua abordagem.
•
Mencionar a recomendação do autor para usar Python 2.7 para os capítulos iniciais, e a discussão sobre Python 2 vs 3.
2. Python como uma Calculadora (20 minutos)
•
Demonstrar o uso do interpretador Python no modo interativo para realizar operações aritméticas básicas (+, -, *, /, **).
•
Exemplos de como digitar expressões e obter resultados imediatos.
•
Introdução ao conceito de ordem de operações.
•
Exercício prático: Resolver pequenos problemas matemáticos utilizando o interpretador Python como calculadora (por exemplo, Exercício 1.1).
3. Programas e Programação (25 minutos)
•
O que são programas de computador e para que servem.
•
A diferença entre escrever e executar um programa.
•
Ferramentas para escrever programas:
◦
Editores de texto simples (Gedit, Emacs, Vim).
◦
Ambientes de Desenvolvimento Integrado (IDEs) com editores de texto (mencionar Spyder brevemente, referindo à Seção H.1).
◦
IPython Notebooks (mencionar brevemente, referindo à Seção H.1.9). A escolha depende do acesso ao Python.
•
Escrevendo e executando o primeiro programa Python:
◦
Criando um arquivo .py com um editor de texto.
◦
A função print para exibir resultados na tela.
◦
Executando programas a partir da linha de comando (python nome_do_programa.py) e no IPython (run nome_do_programa.py). Referenciar a Seção H.2 para outras formas de execução.
◦
Exercício prático: Escrever e executar o programa "Hello, World!" (Exercício 1.2).
4. Elementos Fundamentais da Linguagem (35 minutos)
•
Atenção ao digitar o texto do programa: Sensibilidade a maiúsculas e minúsculas.
•
Verificando o resultado: A importância de testar a correção dos programas.
•
Utilizando variáveis:
◦
Atribuição de valores a variáveis (=).
◦
Como usar variáveis em cálculos.
•
Nomes de variáveis:
◦
Convenções de nomenclatura (letras minúsculas, palavras separadas por underscores).
◦
Nomes descritivos para melhor legibilidade.
•
Palavras reservadas em Python: Mencionar que certas palavras têm significado especial e não podem ser usadas como nomes de variáveis.
•
Comentários:
◦
A importância de adicionar comentários para explicar o código (#).
◦
Ignorados durante a execução.
◦
Exemplo de programa com comentários.
•
Formatação de texto e números:
◦
Utilizando a função print com formatação (e.g., %f, %g).
◦
Quebras de linha em comandos longos com a barra invertida \.
◦
A importância do uso adequado de espaços em branco para legibilidade (ao redor de =, +, -, sem espaços ao redor de *, /, **; espaço após print é essencial). O termo "whitespace".
5. Exemplos e Conceitos Adicionais (30 minutos)
•
Divisão Inteira (Potencial Erro): Demonstrar o comportamento da divisão entre inteiros no Python 2.x (e.g., 9/5 resultando em 1) e como obter a divisão de ponto flutuante (e.g., 9.0/5 ou float(9)/5). Mencionar o arquivo c2f_v1.py.
•
Computação Interativa:
◦
Executando programas no IPython e a facilidade de explorar resultados anteriores usando _, __, ___ ou _iX.
◦
O comando run no IPython.
◦
O prompt >>> usado em outros materiais para sessões interativas.
•
Computação Simbólica (Breve Introdução):
◦
Mencionar o pacote sympy para computação simbólica.
◦
Exemplos básicos de diferenciação e integração simbólica (referir à Seção 1.7).
◦
Resolução de equações e séries de Taylor (referir à Seção 1.7).
•
Exemplo: Trajetória de uma Bola: Discutir brevemente o exemplo da trajetória de uma bola (Seção 1.8.2) e como as fórmulas matemáticas podem ser traduzidas para código Python (e.g., variáveis initial_velocity, acceleration_of_gravity, TIME, VerticalPositionOfBall).
6. Convenções de Tipografia e Estilo (10 minutos)
•
Explicar as convenções de tipografia usadas no livro para distinguir entre snippets de código e programas completos (linha vertical à esquerda).
•
Mostrar exemplos de como sessões interativas (>>>) e a saída de programas (texto simples) são formatadas.
•
Mencionar brevemente o Guia de Estilo para Código Python (PEP8).
7. Exercícios e Próximos Passos (15 minutos)
•
Revisar alguns dos exercícios propostos no final do Capítulo 1 (Seção 1.9), como:
◦
Derivar e computar uma fórmula (Exercício 1.3).
◦
Converter unidades de comprimento (Exercício 1.4).
◦
Calcular a massa de substâncias (Exercício 1.5).
◦
Calcular o crescimento de dinheiro em um banco (Exercício 1.6).
◦
Identificar e corrigir erros em programas (Exercício 1.7, 1.9, 1.14, 1.16, 1.17).
◦
Avaliar uma função Gaussiana (Exercício 1.10).
•
Incentivar os alunos a praticarem resolvendo os exercícios para consolidar o aprendizado.
•
Breve introdução ao conteúdo do próximo capítulo (Loops e Listas).
•
Indicar a página web do livro (http://hplgit.github.com/scipro-primer) onde todos os exemplos de programas estão disponíveis para download.
Avaliação: Observação da participação dos alunos durante a aula e a resolução dos exercícios práticos.
Este plano de aula visa cobrir os principais tópicos do Capítulo 1, fornecendo uma base sólida para os conceitos de programação científica com Python, conforme apresentado no livro. A ênfase na prática e nos exemplos do livro é crucial para o aprendizado eficaz.