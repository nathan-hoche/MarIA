# About this Project
This project is an implementation of a genetic algorithm for platformer game. The goal is to make a program that can learn to play a platformer game.

# How to launch a sample:

1. Execute the following line:
```sh
python3 main.py [map.txt] [nbStartingGene] [nbPopulation] [nbGeneration]
```
2. Be happy!!! :)

> Sometime, the program can not find a solution. In this case, you can try to increase the number of generation or remove useless moves. Or just restart the program.

# How to do your own simulation:
1. Moves
- Add your own moves in the file `actions.json`

2. Map
- Create your own map in the folder `maps`
- You can use config.json to know what to put in your map
- Put a `P` for the player anf a `E` for the goal