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
    context.alist.add(item, user=user)

@then('the item "{item}" is marked as added by {user}')
def step_impl(context, item, user):
    assert_that(context.alist.info(item).user, is_(equal_to(user)))

@then('the item "{item1}" is marked as added before than "{item2}"')
def step_impl(context, item1, item2):
    assert_that(context.alist.info(item1).time_added,
                is_(less_than(context.alist.info(item2).time_added)))

@given('we have a list created by {user} containing')
def step_impl(context, user):
    context.execute_steps('''
        Given we have an empty list created by {user}
    '''.format(**locals()))
    for row in context.table:
        item = row['item']
        context.execute_steps('when {user} adds "{item}" to the list'.format(**locals()))

@when('{user} types "{item}"')
def step_impl(context, user, item):
    if user in ['she', 'he']:
        user = None
    context.complete_suggestion = next(context.alist.complete(item))

@then('the suggestion is "{item}"')
def step_impl(context, item):
    assert_that(context.complete_suggestion, is_(item))

@when('{user} replaces "{old}" with "{new}"')
def step_impl(context, user, old, new):
    if user in ['she', 'he']:
        user = None
    context.alist.replace(old, new, user)

@then('the list is')
def step_impl(context):
    items = [row['item'] for row in context.table]
    assert_that(context.alist.get(), is_(equal_to(items)))

@then('the original of "{new}" is "{old}" and marked as added by {user}')
def step_impl(context, new, old, user):
    old_item = context.alist.info(new).original
    assert_that(old_item.value, is_(equal_to(old)))
    assert_that(old_item.user, is_(equal_to(user)))

@when('she removes "{item}"')
def step_impl(context, item):
    context.alist.remove(item)
