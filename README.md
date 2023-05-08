# 2048
Game: 2048<br>
A practice with object oriented programming<br>
w Pygame<br><br>

How to play?<br>
1. Rules:<br>
	- Win condition:
		- The objective of the 2048 game is to combine tiles with the same number on a 4x4 grid to create a tile with the number 2048.<br>
		- After you get 2048, the game can go on until you run out of blocks to move
    - Keep accumulating points to see how high you can it to.<br>
		
2. Game dynamics:<br>
  - 2048 is a sliding tile puzzle game.<br>
	- The game begins with two randomly placed tiles with the numbers 2 or 4..<br>
    - It randomly spawns blocks worth 2 points 90% of the time.<br>
    - It randomly spawns blocks worth 4 points 10% of the time.<br>
	- Players can slide the tiles in four directions: up, down, left, and right.<br>
    - When two tiles with the same number touch while sliding, they merge into a single tile with their combined value.<br>
      - For example, two tiles with the number 2 will merge into a tile with the number 4, and two tiles with the number 4 will merge into a tile with the number 8.<br>
    - If there are no tiles in the direction of the arrowkey, the tile goes all the way to the edge/wall of the given direction.<br>
    - After each move, a new tile with the number 2 or 4 will randomly appear on an empty cell.<br>
  - Players must strategically move the tiles to create combinations, aiming to reach the 2048 tile without filling up the entire grid.<br>
  - If there are no possible moves left and the grid is full, the game ends in a loss.<br>

3. Legal moves/Button controls:<br>
	- Once in game:<br>
		- Up Arrow: Slide all the tiles up.<br>
    - Down Arrow: Slide all the tiles down.<br>
    - Left Arrow: Slide all the tiles left.<br>
    - Right Arrow: Slide all the tiles right.<br>
	- Clicking on X(window close) - exits game<br><br>

Game Start:<br>
![image](https://user-images.githubusercontent.com/98131995/236724967-73991017-cdbd-430f-b1d2-6853d015d3bc.png)<br><br>

Mid Game:<br>
![image](https://user-images.githubusercontent.com/98131995/236725022-d99e4e81-85c1-4c81-8b90-2dbaf4fb5d14.png)<br><br>

WIN:<br>
![image](https://user-images.githubusercontent.com/98131995/236728737-e64839de-90ca-4339-8bc2-4fba40e4819d.png)<br><br>

Lose:<br>
![image](https://user-images.githubusercontent.com/98131995/236725070-7a460c54-e255-48f5-9e9f-fc48c6b52b7e.png)<br><br>

Sample Game:<br>
![2048](https://user-images.githubusercontent.com/98131995/236748883-b2bea3f5-591b-4b9f-8f8e-f3d492a1795f.gif)<br><br>
