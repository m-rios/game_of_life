def glider(pos):
    pos[0][2].alive = True
    pos[1][0].alive = True
    pos[1][2].alive = True
    pos[2][1].alive = True
    pos[2][2].alive = True

def test(pos):
    pos[0][36].alive = True
    pos[1][36].alive = True
    pos[1][37].alive = True
    pos[2][36].alive = True
    pos[2][38].alive = True    

def gosper_glider_gun(pos):
    pos[5][1].alive = True
    pos[6][1].alive = True
    pos[5][2].alive = True
    pos[6][2].alive = True
    
    pos[5][11].alive = True
    pos[6][11].alive = True
    pos[7][11].alive = True
    pos[4][12].alive = True
    pos[8][12].alive = True
    pos[3][13].alive = True
    pos[9][13].alive = True
    pos[3][14].alive = True
    pos[9][14].alive = True
    pos[6][15].alive = True
    pos[4][16].alive = True
    pos[8][16].alive = True
    pos[5][17].alive = True
    pos[6][17].alive = True
    pos[7][17].alive = True
    pos[6][18].alive = True

    pos[3][21].alive = True
    pos[4][21].alive = True
    pos[5][21].alive = True
    pos[3][22].alive = True
    pos[4][22].alive = True
    pos[5][22].alive = True
    pos[2][23].alive = True
    pos[6][23].alive = True

    pos[1][25].alive = True
    pos[2][25].alive = True
    pos[6][25].alive = True
    pos[7][25].alive = True

    pos[3][35].alive = True
    pos[4][35].alive = True
    pos[3][36].alive = True
    pos[4][36].alive = True