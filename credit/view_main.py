from .services import get_username

def hello_user(requests):
    context = {
        'name': get_username()
    }
    return render(requests, 'hello_user.html', context)
# Si así lo deseamos poder enviar parametros a nuestra petición.

def hello_user(requests):
    params = { 'order': 'desc' }

    context = {
        'name': get_username(params)
    }
    return render(requests, 'hello_user.html', context)
