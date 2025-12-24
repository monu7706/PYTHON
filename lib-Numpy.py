#Numpy         Numpy data ko store karne ke liye hota hai but PANDAS Data ko manipulate karta hai 
#  kaise data ko proper way me enhance karte hai,ye pandas karta hai
# Numpy is like a list
#   Numpy is faster than list
#   and have advanced mathematical operation 
#   Homogeneous hai 
# reshape kr shape kr sakte hai ,iteration kr sakte hai join kr sakte hai and bahut kuch
# technical term me locality of reference numpy letters ko sequence me rekhta hai[5,6,7]
# aur list [5,6,8,7] kahi bhi rekhta hai isliye list se fast work karta hai numpy


# import numpy as np
# lst1 = np.array(4)            #0D ARRAY
# lst = np.array([4,9,6,7])     #1D ARRAY
# lst2 = np.array([[5,7,9,8],[1,6,8,7]])     #2D ARRAY
# print(lst2.ndim)
# print(lst.ndim)
# print(lst1.ndim)
# lst3 = np.array([4,9,6,7],ndmin=8)
# print(lst3)
# stk = [4,9,6,7]
# print(stk)


# import numpy as np
# lst = np.array([4,9,6,7])
# print(lst[1] +  lst[2])  # 15    # indexing like list
# print(lst[1:3])                # slicing means piece of sequence  where 3 stop position hamesha 1
#                                 # bdha kr dena hai

# lst = np.array([[4,9,6,7],[2,5,6,7]], ndmin=2)  # to know shape of matrix use .shape (2,4) ka matrix hai
# print(lst.shape)

# yes, we can reshaping

# import numpy as np
# lst = np.array([5,6,4,7,1,2,3,8])
# print(lst)
# newLst = lst.reshape(4,2)
# print(newLst)