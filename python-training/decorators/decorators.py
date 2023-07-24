#how to create decorators in python

# from datetime import datetime
#
# def log_datetime(func):
#     '''date and time of a function'''
#
#     def wrapper():
#         func()
#         print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
#         print(f'{"-" * 30}')
#
#     return wrapper
#
#
# @log_datetime
# def daily_backup():
#     print("Daily back up job ")
#
# daily_backup()


#How to add arguments to decorators in python

def my_decorator():
    def wrapper(*args,**kwargs)

