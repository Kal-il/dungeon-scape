Dungeon Escape
==============

Dungeon Escape é um jogo simples feito com PgZero em Python. O objetivo do jogador é atravessar o mapa e alcançar o ponto final sem ser pego pelos inimigos.

Requisitos
----------
- Python 3.8 ou superior
- PgZero instalado (pip install pgzero)

Estrutura do Projeto
--------------------
/dungeon_escape/
├── intro.py                # Arquivo principal do jogo
├── images/                 # Pasta com sprites (herói, inimigos, fundo, etc.)
│   ├── bg.png
│   ├── drawKnife1.png
│   ├── hero_walk1.png
│   ├── hero_walk2.png
│   ├── hero_walk1_copia.png
│   ├── hero_walk2_copia.png
│   ├── enemy_idle1.png
│   ├── enemy_walk1.png
│   ├── enemy_walk2.png
│   ├── enemy_idle1_copia.png
│   ├── enemy_walk1_copia.png
│   ├── enemy_walk2_copia.png
│   └── victory.png
├── sounds/
│   ├── theme.ogg
│   ├── footstep00.ogg
│   └── drawKnife1.ogg

Como Jogar
----------
- Use as teclas de seta para mover o personagem.
- Evite os inimigos. Se colidir com um deles, o jogo volta ao menu.
- Alcance o ponto final (ícone da faca) para vencer.
- Ao vencer, uma tela de vitória será exibida com opção de voltar ao menu.

Controles
---------
- Setas direcionais: mover
- Mouse: clicar em botões do menu

Créditos
--------
Sprites e sons foram criados ou adaptados para fins de demonstração. O jogo foi desenvolvido como um projeto de exemplo com PgZero.

