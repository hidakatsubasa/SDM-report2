#!/usr/bin/python3

import re
                
def calc(A,B):
        ai=str(A)
        bi=str(B)
        # 修正: 小数を許容せず、先頭から末尾まで数字のみのパターンかチェック
        if ai.isdigit() and bi.isdigit():
                # 修正: 整数のみであるためfloatをintに変更
                a=int(ai)
                b=int(bi)

                # 修正: 範囲チェックの仕様を変更 (1から999まで)
                if 1 <= a <= 999 and 1 <= b <= 999:
                        return a * b
            
        # 条件を満たさない場合は -1 を返す
        return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
