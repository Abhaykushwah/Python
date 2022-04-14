def Change(P,Q=30):
	P=P+Q
	Q=P-Q
	print (P,"#",Q)
	return(P) 
R=150
S=100
R=Change(R,S)
print (R,"#",S)
S=Change(S)
