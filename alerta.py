from datetime import datetime

def alerta (nivel, base, etapa):
    
        dataAtual = str(datetime.now())
        
        if nivel == 1:
            title = 'ATENÇÃO: Alerta Baixo'
        elif nivel == 2:
            title = 'ATENÇÃO: Alerta Médio'
        elif nivel  == 3:
            title = 'ATENÇÃO: Alerta Alto'
        else:
            print("Nivel",nivel,"não disponível!")
        
        from plyer import notification
        notification.notify(
            title = title,
            message = f'Falha no carregamento da base {base} na etapa {etapa}. {dataAtual}',
            app_icon = None,
            timeout = 10
        )
        
alerta (nivel = 2,
    base = 'CLIENTES',
    etapa = 'EXTRAÇÃO')

    
