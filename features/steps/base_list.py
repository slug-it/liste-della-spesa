from behave import *
from hamcrest import *

from lista_della_spesa import ListaDellaSpesa

@given('we have an empty list')
def step_impl(context):
    context.alist = ListaDellaSpesa()

@given('we have an empty list created by {user}')
def step_impl(context, user):
    context.alist = ListaDellaSpesa(user)

@when('we add "{item}" to the list')
def step_impl(context, item):
    context.alist.add(item)

@then('the list contains "{item}"')
def step_impl(context, item):
    assert_that(context.alist.get(), contains(item))

@then('the list contains {count:d} item')
def step_impl(context, count):
    assert_that(context.alist.get(), has_length(1))

@then('the list contains "{item1}" and "{item2}" in this order')
def step_impl(context, item1, item2):
    assert_that(context.alist.get(), is_(equal_to([item1, item2])))

@when('{user} adds "{item}" to the list')
def step_impl(context, user, item):
    context.alist.add(item)

@then('the item "{item}" is marked as added by {user}')
def step_impl(context, item, user):
    assert_that(context.alist.info(item).creator, is_(equal_to(user)))

@then('the item "{item1}" is marked as added before than "{item2}"')
def step_impl(context, item1, item2):
    assert_that(context.alist.info(item1).time_added,
                is_(less_than(context.alist.info(item2).time_added)))

@given('we have a list created by {user} containing "{item}"')
def step_impl(context, user, item):
    context.execute_steps('''
        Given we have an empty list created by {user}
        when {user} adds "{item}" to the list
    '''.format(**locals()))

@when('she types "{item}"')
def step_impl(context, item):
    context.complete_suggestion = context.alist.complete(item)

@then('the suggestion is "{item}"')
def step_impl(context, item):
    assert_that(context.complete_suggestion, is_(item))


