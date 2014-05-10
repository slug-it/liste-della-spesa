from behave import *
from lista_della_spesa import ListaDellaSpesa

@given('we have an empty list')
def step_impl(context):
    context.alist = ListaDellaSpesa()

@when('we add "{item}" to the list')
def step_impl(context, item):
    context.alist.add(item)

@then('the list contains "{item}"')
def step_impl(context, item):
    assert item in context.alist.get()
