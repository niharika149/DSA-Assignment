def TowerOfHanoi(n , tower1, tower2, tower3):
              if n == 1:
                  print("Move disk 1 from rod",tower1,"to rod",tower2)
                  return
              TowerOfHanoi(n-1, tower1, tower3, tower2)
              print("Move disk",n,"from rod",tower1,"to rod",tower2)
              TowerOfHanoi(n-1, tower3, tower2, tower1)
          
TowerOfHanoi(3,'P','Q','R')