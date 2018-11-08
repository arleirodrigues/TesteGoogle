from behave import given,when,then
import time

@given(u'Acesso a pagina')
def step_impl(context):
    context.app.pagina('https://www.google.com.br')
    time.sleep(3)


@when(u'Faco uma pesquisa')
def step_impl(context):
    context.app.escreve('lst-ib','scrum org psm I','id').submit()
    time.sleep(3)
    pass

@then(u'Obtenho o resulato da pesquisa')
def step_impl(context):
    pass