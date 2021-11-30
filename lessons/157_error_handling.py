# Error handling 
while True:
    try:
        age = int(input('what is your age?'))
        10/age
        print(age)
    except ValueError:
        print('enter a number')
    except ZeroDivisionError:
        print('cant be 0')
    else:
        break
    finally:
        print('done')