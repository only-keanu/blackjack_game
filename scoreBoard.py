scores = {

}
content =[]

def loadScores():
    scoreBoard = open('scores.dat','r')
    for line in scoreBoard:
        global scores
        content = line.split(',')
        scores[content[0]]=int(content[1])
    scoreBoard.close()
    return scores


def saveScores(scores):
    scoreBoard = scores
    scores = open('scores.dat','w')
    for k,v in scoreBoard.items():
        scores.write(str(k)+','+str(v)+'\n')
    scores.close()