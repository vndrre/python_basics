def upc(num):
     if len(str(num)) < 11: 
         number = '%0*d' % (11, num)
 
     upc = [int(d) for d in str(num)]
     upc1 = upc[::2]
     upc2 = upc[1::2]
     m = (3*sum(upc1) + sum(upc2))%10
     if m == 0:
         upc3 = 0 
     else:
         upc3 = 10-m
 
     return upc3