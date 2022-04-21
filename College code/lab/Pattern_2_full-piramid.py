'''
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''

r = int(input("Enter the number of row : "))
for i in range(1,r+1):
   print((r-i)*' '+i*'* ')
for i in range(r-1,0,-1):
   print((r-i)*' '+i*'* ')
