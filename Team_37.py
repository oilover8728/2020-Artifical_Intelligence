import STcpClient
import random
'''
    輪到此程式移動棋子
    board : 棋盤狀態(list of list), board[i][j] = i row, j column 棋盤狀態(i, j 從 0 開始)
            0 = 空、1 = 黑、2 = 白、-1 = 四個角落
    is_black : True 表示本程式是黑子、False 表示為白子

    return Step
    Step : single touple, Step = (r, c)
            r, c 表示要下棋子的座標位置 (row, column) (zero-base)
'''
def GetStep(board, is_black):
    if is_black:
        max=0
        for i in range(8):
            for j in range(8):
                if board[i][j]==0:
                    count=0
                    for k in range(1, 7):
                        if i-k>=0 and j-k>=0:
                            if board[i-k][j-k]==2:
                                continue
                            if board[i-k][j-k]==1:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if i-k>=0:
                            if board[i-k][j]==2:
                                continue
                            if board[i-k][j]==1:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if i-k>=0 and j+k<8:
                            if board[i-k][j+k]==2:
                                continue
                            if board[i-k][j+k]==1:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if j-k>=0:
                            if board[i][j-k]==2:
                                continue
                            if board[i][j-k]==1:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if j+k<8:
                            if board[i][j+k]==2:
                                continue
                            if board[i][j+k]==1:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if i+k<8 and j-k>=0:
                            if board[i+k][j-k]==2:
                                continue
                            if board[i+k][j-k]==1:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if i+k<8:
                            if board[i+k][j]==2:
                                continue
                            if board[i+k][j]==1:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if i+k<8 and j+k<8:
                            if board[i+k][j+k]==2:
                                continue
                            if board[i+k][j+k]==1:
                                count+=(k-1)
                                break
                            else:
                                break
                    if count>max:
                        max=count
                        x=i
                        y=j
        if max==0:
            min=8
            pos=[]
            for i in range(1, 6):
                for j in range(1, 6):
                    if board[i][j]==0:
                        count=0
                        if i-1>=0 and j-1>=0:
                            if board[i-1][j-1]==2:
                                count+=1
                        if i-1>=0:
                            if board[i-1][j]==2:
                                count+=1
                        if i-1>=0 and j+1<8:
                            if board[i-1][j+1]==2:
                                count+=1
                        if j-1>=0:
                            if board[i][j-1]==2:
                                count+=1
                        if j+1<8:
                            if board[i][j+1]==2:
                                count+=1
                        if i+1<8 and j-1>=0:
                            if board[i+1][j-1]==2:
                                count+=1
                        if i+1<8:
                            if board[i+1][j]==2:
                                count+=1
                        if i+1<8 and j+1<8:
                            if board[i+1][j+1]==2:
                                count+=1
                        if count==min:
                            pos.append((i, j))
                        elif count<min:
                            for k in range(len(pos)):
                                p=pos.pop()
                            pos.append((i, j))
                            min=count
            a=random.randint(0, len(pos)-1)
            x=pos[a][0]
            y=pos[a][1]
    if is_black==False:
        max=0
        for i in range(8):
            for j in range(8):
                if board[i][j]==0:
                    count=0
                    for k in range(1, 7):
                        if i-k>=0 and j-k>=0:
                            if board[i-k][j-k]==1:
                                continue
                            if board[i-k][j-k]==2:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if i-k>=0:
                            if board[i-k][j]==1:
                                continue
                            if board[i-k][j]==2:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if i-k>=0 and j+k<8:
                            if board[i-k][j+k]==1:
                                continue
                            if board[i-k][j+k]==2:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if j-k>=0:
                            if board[i][j-k]==1:
                                continue
                            if board[i][j-k]==2:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if j+k<8:
                            if board[i][j+k]==1:
                                continue
                            if board[i][j+k]==2:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if i+k<8 and j-k>=0:
                            if board[i+k][j-k]==1:
                                continue
                            if board[i+k][j-k]==2:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if i+k<8:
                            if board[i+k][j]==1:
                                continue
                            if board[i+k][j]==2:
                                count+=(k-1)
                                break
                            else:
                                break
                    for k in range(1, 7):
                        if i+k<8 and j+k<8:
                            if board[i+k][j+k]==1:
                                continue
                            if board[i+k][j+k]==2:
                                count+=(k-1)
                                break
                            else:
                                break
                    if count>max:
                        max=count
                        x=i
                        y=j
        if max==0:
            min=8
            pos=[]
            for i in range(1, 6):
                for j in range(1, 6):
                    if board[i][j]==0:
                        count=0
                        if i-1>=0 and j-1>=0:
                            if board[i-1][j-1]==1:
                                count+=1
                        if i-1>=0:
                            if board[i-1][j]==1:
                                count+=1
                        if i-1>=0 and j+1<8:
                            if board[i-1][j+1]==1:
                                count+=1
                        if j-1>=0:
                            if board[i][j-1]==1:
                                count+=1
                        if j+1<8:
                            if board[i][j+1]==1:
                                count+=1
                        if i+1<8 and j-1>=0:
                            if board[i+1][j-1]==1:
                                count+=1
                        if i+1<8:
                            if board[i+1][j]==1:
                                count+=1
                        if i+1<8 and j+1<8:
                            if board[i+1][j+1]==1:
                                count+=1
                        if count==min:
                            pos.append((i, j))
                        elif count<min:
                            for k in range(len(pos)):
                                p=pos.pop()
                            pos.append((i, j))
                            min=count
            a=random.randint(0, len(pos)-1)
            x=pos[a][0]
            y=pos[a][1]
    return (x,y)
while(True):
    (stop_program, id_package, board, is_black) = STcpClient.GetBoard()
    if(stop_program):
        break
    Step = GetStep(board, is_black)
    STcpClient.SendStep(id_package, Step)