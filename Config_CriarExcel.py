import psutil
import pandas as pd
import time

dadosMonitoramento = []

def monitorarMemoriaDoComputador(qtdTempoMonitoramentoDados):
    print(f"Iniciando monitoramento por segundos...")
    

    registros = []
    
    for i in range(qtdTempoMonitoramentoDados):
        percentualCpu = psutil.cpu_percent(interval=1)
        memoria = psutil.virtual_memory()
        rede = psutil.net_io_counters()
        
        registro = {
            'timestamp': time.strftime('%H:%M:%S'),
            'cpu_percent': percentualCpu,
            'mem_total': memoria.total,
            'mem_usada': memoria.used,
            'mem_livre': memoria.free,
            'mem_percent': memoria.percent,
            'bytes_enviados': rede.bytes_sent,
            'bytes_recebidos': rede.bytes_recv
        }
        
        registros.append(registro)
        dadosMonitoramento.append(registro)
        
        print(f"[{time.strftime('%H:%M:%S')}] CPU: {percentualCpu:.1f}% | "
              f"RAM: {memoria.percent:.1f}% | Net RX: {rede.bytes_recv/1024:.1f}KB")
    
    ExibirMonitoramento(registros[-1]) 

def ExibirMonitoramento(ultimo_registro):
    print("\n=== ÚLTIMO REGISTRO ===")
    print(f"CPU: {ultimo_registro['cpu_percent']:.1f}%")
    print(f"Memória Total: {ultimo_registro['mem_total'] / (1024**3):.1f} GB")
    print(f"Memória Usada: {ultimo_registro['mem_usada'] / (1024**3):.1f} GB")
    print(f"Memória %: {ultimo_registro['mem_percent']:.1f}%")
    print(f"Bytes Enviados: {ultimo_registro['bytes_enviados'] / (1024**2):.1f} MB")
    print(f"Bytes Recebidos: {ultimo_registro['bytes_recebidos'] / (1024**2):.1f} MB")

def criarExcelParaMonitoramentoDoComputador():
    if dadosMonitoramento:
        df = pd.DataFrame(dadosMonitoramento)
        df.to_excel('monitoramento_sistema.xlsx', index=False)
        print("Dados salvos em 'monitoramento_sistema.xlsx'")
    else:
        print("Nenhum dado para salvar")

