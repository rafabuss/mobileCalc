from behave import given, when, then

operator = ''
result = ''

@given('I want to do a "{OPERATION}" ')
def do_operation(OPERATION):
    global operator
    operator = OPERATION

@when('I perform the operation between "{FIRST_NUM}" and "{SECOND_NUM}"')
def calculation(context, FIRST_NUM, SECOND_NUM):
    global result
    result = context.app.main_page.do_calculation(operator,FIRST_NUM,SECOND_NUM)

@then('the result must be "{EXPECTED_RESULT}"')
def verify_result(EXPECTED_RESULT):
    if result == EXPECTED_RESULT:
        print ('Resultado correto! ' + result)
    else:
        print ('Resultado incorreto! A expectativa era ' + EXPECTED_RESULT + ', mas o resultado foi ' + result)
