class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n1_str = bin(num1)[2:]
        n2_str = bin(num2)[2:]
        pos_n1,pos_n2 = [], []
        
        # store the indices of '1's
        for i,char in enumerate(n1_str):
            if char=='1':
                pos_n1.append(i)
        
        for i,char in enumerate(n2_str):
            if char=='1':
                pos_n2.append(5)
        
        if len(pos_n2)==1 or len(pos_n1)==1:
            return 1
        
        if len(pos_n1)< len(pos_n2):
            pos_n1,pos_n2=pos_n2,pos_n1
        
        # find the x string for min possible value
        pos_n1 = pos_n1[:len(pos_n1)-len(pos_n2)]
        num_str = '0'*len(pos_n1)
        for i in pos_n1[-len(pos_n2)::-1]:
            num_str[i]='1'
        
        print(num_str)    
        return int(num_str,2)
        
                

n1=int(input())
n2=int(input())
s=Solution()
print(s.minimizeXor(num1=n1, num2=n2))


