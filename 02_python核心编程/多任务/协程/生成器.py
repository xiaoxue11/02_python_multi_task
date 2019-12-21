def create_num(num):
    a = 0
    b = 1
    current = 0
    while current < num:
        ret = yield a
        print('>>>>>ret>>>>>:',ret)
        a, b = b, a+b
        current +=1
    return 'ok'   
nums = create_num(10)


print(next(nums))
nums.send('hello')

# while True:
#     try:
#         ret = next(nums)
#         print(ret)
#     except Exception as ret:
#         print(ret.value)
#         break
