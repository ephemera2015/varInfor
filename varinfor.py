#!/usr/bin/python
#-*-coding:utf-8-*-
import math
def log2(x):
    return math.log(x,2)
    
def entropy(p):
    x=(-t*log2(t) for t in p if t!=0)
    return reduce(lambda m,n:m+n,x,0.0)

def conditionalEntropy(p_x,p_y,p_xy):
    a=b=0.0
    for i,px in enumerate(p_x):
        for j,py in enumerate(p_y):
            pxy=p_xy[i][j]
            if pxy!=0:
                a-=pxy*log2(pxy/px)
                b-=pxy*log2(pxy/py)
    return a,b

def distance(p_x,p_y,p_xy):
    a,b=conditionalEntropy(p_x,p_y,p_xy)
    #print a+b
    return a+b

def normalDistance(p_x,p_y,p_xy):
    #print entropy((y for x in p_xy for y in x))
    return distance(p_x,p_y,p_xy)/entropy((y for x in p_xy for y in x))
    


def similarity(p_x,p_y,p_xy):
    #print normalDistance(p_x,p_y,p_xy)
    return 1.0-normalDistance(p_x,p_y,p_xy)
    
def similarity_seq(x,y):
    _px={}
    _py={}
    _pxy={}
    cnt=0.0
    while True:
        try:
            v=x.next()
            if _px.has_key(v):
                _px[v]+=1
            else:
                _px[v]=1
            w=y.next()
            if _py.has_key(w):
                _py[w]+=1
            else:
                _py[w]=1
            if _pxy.has_key((v,w)):
                _pxy[(v,w)]+=1
            else:
                _pxy[(v,w)]=1
            cnt+=1
        except :
            break
    px=tuple(a/cnt for a in _px.values())
    py=tuple(b/cnt for b in _py.values())
    pxy=[]
    for a in _px.keys():
        t=[]
        for b in _py.keys():
            if _pxy.has_key((a,b)):
                t.append(_pxy[(a,b)]/cnt)
            else:
                t.append(0)
        pxy.append(t)
    print px,py,pxy    
    '''
    _px={}
    _py={}
    _pxy={}

    _px={}
    for i,v in enumerate(x):
        s=_px.setdefault(v,set())
        s.add(i)
    _py={}
    for i,v in enumerate(y):
        s=_py.setdefault(v,set())
        s.add(i)
    px=tuple((len(a)/n for a in _px.values()))
    py=tuple((len(b)/n for b in _py.values()))
    pxy=[]
    for a in _px.values():
        pxy.append(tuple((len(a&b)/n for b in _py.values())))
    #print px,py,pxy'''
    return similarity(px,py,pxy)
            
if __name__=='__main__':         
    x=(1,1,2,2,1,1,1,2,1,1,2,2,1,1,2,2)*1000000
    y=(3,3,4,4,3,3,4,4,3,3,4,4,3,3,4,4)*1000000   
    print similarity_seq(x,y)



