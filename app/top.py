import re
import pickle

from app.blockChain import blockChain
from app.db_exception import *



class top:
    def __init__(self) -> None:
        self.bc_list = []
        fp = open('app/chain_data/data','rb')
        self.bc_list = pickle.load(fp)
        self.bc = blockChain(name="BCDB")
    
    def __dup(self, name):
        for i in self.bc_list:
            if(re.search(str(name),str(i))):
                return True
        return False 
    
    def list_add(self, name, blochain=0) -> bool:

        if self.__dup(name):
            print("Duplicate chain name")
            return False
        else:
            tar = blochain or blockChain(name)
            self.bc_list.append(tar)
            return True
        
    def showDB(self) -> str:
        return str(["" + str(i) for i in self.bc_list])

    def delete(self, name):
        for i in range(len(self.bc_list)-1,-1,-1):
            if str(self.bc_list[i]) == name:
                del self.bc_list[i]
                return True

        print("cant find the database to delete")
        return False
    
    def use(self, name):
        for i in self.bc_list:
            if name == str(i):
                if i.valid_chain():
                    print('inspection passed')
                    self.bc = i
                    print('access successfully')
                    return True
                else: return False
        return False
    

        
        
    
    def strg(self):
        fp = open('app/chain_data/data','wb')
        pickle.dump(self.bc_list,fp)
        fp.close()
        
    def __str__(self):
        pri = ""
        for i in self.bc_list:
            pri += str(i)
            pri += '\n'
            pri += i.printAll() 
        return pri

