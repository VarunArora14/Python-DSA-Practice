# https://stackoverflow.com/questions/40182944/whats-the-difference-between-raise-try-and-assert
a=  [1]

assert 1 in a, "1 not in a[]"
print("passed")

'''
Try-except-exception-finally
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')
'''