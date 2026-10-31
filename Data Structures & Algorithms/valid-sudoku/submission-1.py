class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(len(board)):
            if not self.cond_1(i,board):
                # continue
            # else:
              return False

            if not self.cond_2(i,board):
                # continue
            #     print(i)
            # else:
              return False

        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                if not self.cond_3(i,j,board):
                #     continue
                # else:
                  return False
        return True

    def cond_1(self,n,board):
        arr = board[n]
        return self.validity(arr)

    def cond_2(self,n,board):
        arr = []
        for i in range(len(board)):
            arr.append(board[i][n])
        # print(arr)
        return self.validity(arr)

    def cond_3(self,n,m,board):
        arr = []
        for i in range(n,n+3):
            for j in range(m, m+3):
                arr.append(board[i][j])
        # print(arr)
        return self.validity(arr)

    def count_dots(self,arr):
        c = 0
        for i in arr:
            if i == ".":
                c += 1
        return c

    def validity(self,arr):
        c = self.count_dots(arr)
        a = set(arr)
        if c>0:
            if c+len(a) != 10:
                return False
        else:
            if len(a) != 9:
                return False
        return True