class MinStack:

    def __init__(self):
        
        self.value=[]
        self.min=None

    def push(self, x: int) -> None:
       
        if self.value==[]:
            self.min=x
            self.value.append(x)
        elif x<self.min:
            self.value.append(2*x-self.min)
            self.min=x
        else:
            self.value.append(x)
            
        

    def pop(self) -> None:
        if self.value[-1]<=self.min:
            self.min=2*(self.min)-self.value[-1]
        self.value.pop()
        

    def top(self) -> int:
        if self.value[-1]<=self.min:
            return(self.min)
        else:
            return self.value[-1]

    def getMin(self) -> int:
       
        return (self.min)
    



