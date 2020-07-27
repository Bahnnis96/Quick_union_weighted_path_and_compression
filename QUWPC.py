class QUWPC:
    #initialize our lis id
    id=[]
    sz=[]
    count=0
    #the uf method return a list from 0 to N-1
    def uf(self,N):
        self.id=list(range(N))
        self.sz=list(range(N))
        for i in range(0,N):
            self.id[i]=i
            self.sz[i]=1
            
     #the root method fetch for the root of the point in a tree of points 
    def root(self,i):
        while i!=self.id[i]:
            self.id[i]=self.id[self.id[i]]
            i=self.id[i]
        return i
    
       #this method check if two points are connected or not
    def find(self,p,q):
        return self.root(p)==self.root(q)
    
    #the method union merge two trees by implementing one movement only it tries to searchj for the root and merge them into one tree
    def union(self,p,q):
        i=0
        j=0
        i=self.root(p)
        j=self.root(q)
        if i==j:
            return
        if self.sz[i]>self.sz[j]:
            self.id[j]=i
            self.sz[j]+=self.sz[i]
        else:
            self.id[i]=j
            self.sz[i]+=self.sz[j]
