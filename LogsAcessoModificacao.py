import datetime

def captura_log_acesso(db_acessos, usuario):
    def decorator(funcao):
        def wrapper(*args):
            data = datetime.datetime.now()
            funcao(*args)
            db_acessos.append((usuario, f'{data.day}/{data.month}/{data.year}', f'{data.hour}:{data.minute}:{data.second}'))
        return wrapper
    return decorator