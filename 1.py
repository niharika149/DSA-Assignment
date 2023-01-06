def pair_sum(arr, n, given_num):
              count = 0
              for i in range(0,n):
                  for j in range(i+1,n):
                      if arr[i]+arr[j] == given_num:
                          count+=1
              print("Number of pairs whose sum is equal to given number :",count)

pair_sum([1,2,3,4,5],5,8)
