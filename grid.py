class Grid:
    
    def __init__(self, puzzle = 81*'.'):
        """
            Constructeur par défaut
            Arguments :
                - puzzle : chaine de 81 caractères
            Tests :
            >>> Grid().puzzle == 81*'.', Grid(81*'2').puzzle == 81*'2'
            (True, True)
            >>> Grid().full, Grid(81*'2').full
            (False, True)
        """
        self.puzzle = puzzle
        self.full = '.' not in self.puzzle
        
    def loadFromFile(num):
        """
            Charger un puzzle dans le fichier grids.sud
            Argument :
                - num : numéro du puzzle à charger
            Tests :
            >>> Grid.loadFromFile(0).puzzle[:10]
            '4.....8.5.'
        """
        grids = open('./data/grids.sud')
        line = grids.readlines()
        return Grid(line[num]) 
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
        
