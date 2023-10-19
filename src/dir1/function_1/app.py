from pkg.package_1.code import function_sample_1
def function_1():
    print("This is function 1 at app.py")
    # some delay
    print("calling function at app.py")
    function_2()
    function_3()


def function_2():
    print("This is function 2 at app.py")
    print("calling function 3 at app.py")
    function_3()


def function_3():
    print("This is function 3")
    print("calling function_sample_1 at package_1")
    function_sample_1()


def lambda_handler(event, context):
    print('start of lambda of function_1')
    function_1()
    return {
        "statusCode": 200,
        "body": "lambda function_1 completed"
    }
