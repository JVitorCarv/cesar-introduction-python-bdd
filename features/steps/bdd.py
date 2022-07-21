from behave import *
from src.adder import *
from src.multiplier import *


# use_step_matcher("re")


@given("the first number is {op1}")
def step_first_num(context, op1):
    """
    :type context: behave.runner.Context
    """
    context.op1 = int(op1)


@step("the second number is {op2}")
def step_second_num(context, op2):
    """
    :type context: behave.runner.Context
    """
    context.op2 = int(op2)


@when("I sum the two numbers")
def step_add_two_numbers(context):
    """
    :type context: behave.runner.Context
    """
    context.result = Adder().sum(context.op1, context.op2)


@then("the result must be {result}")
def step_result_7(context, result):
    """
    :type context: behave.runner.Context
    """
    assert context.result == int(result)


@when("I multiply the two numbers")
def step_multiply_two_numbers(context):
    """
    :type context: behave.runner.Context
    """
    context.result = Multiplier().mult(context.op1, context.op2)