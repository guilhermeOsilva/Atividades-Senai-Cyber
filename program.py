import Config_CriarExcel as cexcel

qtdTempoMonitoramentoDados = int(input("Insira o tempo desejo para monitoramento (Em segundos)"))

cexcel.monitorarMemoriaDoComputador(qtdTempoMonitoramentoDados)
print(f"\nTotal de registros coletados: {len(cexcel.dadosMonitoramento)}")
cexcel.criarExcelParaMonitoramentoDoComputador()