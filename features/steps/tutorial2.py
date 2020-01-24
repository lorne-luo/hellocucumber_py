from behave import *


def belending(input):
    mapping = {
        "Red Tree Frog": "mush",
        "iPhone": "toxic waste",
        "Galaxy Nexus": "toxic waste",
    }
    return mapping.get(input, None)


@given(u'I put {input} in a blender,')
def step_impl(context, input):
    context.input = input


@when(u'I switch the blender on')
def step_impl(context):
    context.on = True


@then(u'it should transform into {other_thing}')
def step_impl(context, other_thing):
    output = belending(context.input) if context.on else None
    assert output == other_thing
