import csv
import pandas as pd
import io

# -----
# --
# -- gerarcsvleitura.py
# -- Read a file .csv check the column name and write a new file .csv
# -- RPA4All by Antonio Carneiro
# -- 17/01/22
# --
# -----

layout_saida = ['id_instrumento', 'Código do Instrumento', 'Tipo de Instrumento', 'Data de Medição', 'Hora de medição',
                'Situação da Medição', 'Valor', 'Tipo de Coleta', 'Justificativa de não Medição', 'Número de OS',
                'Condição Adversa',
                'Observação', 'Unidade de Medida (U)', 'Leitura Manual (m)', 'Unidade de Medida (Y)',
                'Unidade de Medida (W)',
                'Unidade de Medida (AA)', 'Unidade de Medida (AC)', 'Leitura (m)', 'Leitura', 'Cota (Z)',
                'Leitura do Sensor Ultrassônico ',
                'Unidade de Medida (AE)', 'Unidade de Medida (ALL)', 'desv_padrao']

s_linOut = ''

fleituras = open('2022_01_15_INOUT_CadastroXLSX.csv', encoding='UTF8')

csv_reader = csv.reader(fleituras)

for line in csv_reader:
    print(line)

fleituras.close()

fieldnames = ['id_instrumento', 'cd_instrumento', 'tp_instrumento', 'stp_instrumento', 'dt_medicao', 'hr_medicao',
               'sit_medicao',
               'valor', 'tp_coleta', 'just_n_medicao', 'numero_OS', 'cond_adversa', 'obs', 'unid_medida_u',
               'unid_medida_y',
               'leitura_m', 'unid_medida_w', 'unid_medida_aa', 'unid_medida_ac', 'cd_instrumento_1', 'tp_instrumento_1',
               'stp_instrumento_1', 'dt_medicao_1', 'hr_medicao_1', 'sit_medicao_1', 'valor_1', 'tp_coleta_1',
               'just_n_medicao_1',
               'numero_OS_1', 'cond_adversa_1', 'obs_1', 'unid_medida_u_1', 'lei_manual_m', 'unid_medida_y_1',
               'unid_medida_w_1',
               'unid_medida_aa_1', 'unid_medida_ac_1', 'cd_instrumento_1_1', 'tp_instrumento_1_1',
               'stp_instrumento_1_1', 'dt_medicao_1_1',
               'hr_medicao_1_1', 'sit_medicao_1_1', 'valor_1_1', 'tp_coleta_1_1', 'just_n_medicao_1_1', 'numero_OS_1_1',
               'cond_adversa_1_1',
               'obs_1_1', 'unid_medida_u_1_1', 'unid_medida_y_1_1', 'leitura', 'unid_medida_w_1_1', 'leitua_sensor_u1',
               'cd_instrumento_1_1_1',
               'tp_instrumento_1_1_1', 'stp_instrumento_1_1_1', 'dt_medicao_1_1_1', 'hr_medicao_1_1_1',
               'sit_medicao_1_1_1', 'valor_1_1_1',
               'tp_coleta_1_1_1', 'just_n_medicao_1_1_1', 'numero_OS_1_1_1', 'cond_adversa_1_1_1', 'obs_1_1_1',
               'unid_medida_u_1_1_1',
               'lei_manual_m_1', 'unid_medida_w_1_1_1', 'unid_medida_aa_1_1', 'unid_medida_ac_1_1',
               'cd_instrumento_1_1_1_1', 'tp_instrumento_1_1_1_1',
               'stp_instrumento_1_1_1_1', 'dt_medicao_1_1_1_1', 'hr_medicao_1_1_1_1', 'sit_medicao_1_1_1_1',
               'valor_1_1_1_1', 'tp_coleta_1_1_1_1',
               'just_n_medicao_1_1_1_1', 'numero_OS_1_1_1_1', 'cond_adversa_1_1_1_1', 'obs_1_1_1_1',
               'unid_medida_u_1_1_1_1', 'unid_medida_y_1_1_1',
               'unid_medida_w_1_1_1_1', 'unid_medida_aa_1_1_1', 'cota_z', 'cd_instrumento_1_1_1_1_1',
               'tp_instrumento_1_1_1_1_1', 'stp_instrumento_1_1_1_1_1',
               'dt_medicao_1_1_1_1_1', 'hr_medicao_1_1_1_1_1', 'sit_medicao_1_1_1_1_1', 'valor_1_1_1_1_1',
               'tp_coleta_1_1_1_1_1',
               'just_n_medicao_1_1_1_1_1', 'numero_OS_1_1_1_1_1', 'cond_adversa_1_1_1_1_1', 'obs_1_1_1_1_1',
               'unid_medida_u_1_1_1_1_1',
               'unid_medida_w_1_1_1_1_1', 'leitura_sensor_u1_1', 'cd_instrumento_1_1_1_1_1_1',
               'tp_instrumento_1_1_1_1_1_1', 'stp_instrumento_1_1_1_1_1_1', 'dt_medicao_1_1_1_1_1_1',
               'hr_medicao_1_1_1_1_1_1', 'sit_medicao_1_1_1_1_1_1', 'valor_1_1_1_1_1_1', 'tp_coleta_1_1_1_1_1_1',
               'just_n_medicao_1_1_1_1_1_1',
               'unid_medida', 'numero_OS_1_1_1_1_1_1', 'cond_adversa_1_1_1_1_1_1', 'obs_1_1_1_1_1_1',
               'lei_manual_m_1_1', 'unid_medida_y_1_1_1_1',
               'unid_medida_aa_1_1_1_1', 'unid_medida_ac_1_1_1', 'cd_instrumento_1_1_1_1_1_1_1',
               'tp_instrumento_1_1_1_1_1_1_1', 'stp_instrumento_1_1_1_1_1_1_1',
               'dt_medicao_1_1_1_1_1_1_1', 'hr_medicao_1_1_1_1_1_1_1', 'sit_medicao_1_1_1_1_1_1_1',
               'Valor_1_1_1_1_1_1_1', 'tp_coleta_1_1_1_1_1_1_1',
               'just_n_medicao_1_1_1_1_1_1_1', 'unid_medida_1', 'numero_OS_1_1_1_1_1_1_1', 'cond_adversa_1_1_1_1_1_1_1',
               'obs_1_1_1_1_1_1_1',
               'lei_manual_m_1_1_1', 'unid_medida_y_1_1_1_1_1', 'unid_medida_aa_1_1_1_1_1', 'unid_medida_ac_1_1_1_1',
               'unid_medida_aec',
               'cota_z_1', 'cd_instrumento_1_1_1_1_1_1_1_1', 'tp_instrumento_1_1_1_1_1_1_1_1',
               'stp_instrumento_1_1_1_1_1_1_1_1',
               'dt_medicao_1_1_1_1_1_1_1_1', 'hr_medicao_1_1_1_1_1_1_1_1', 'sit_medicao_1_1_1_1_1_1_1_1',
               'valor_1_1_1_1_1_1_1_1',
               'tp_coleta_1_1_1_1_1_1_1_1', 'just_n_medicao_1_1_1_1_1_1_1_1', 'unid_medida_1_1',
               'numero_OS_1_1_1_1_1_1_1_1', 'cond_adversa_1_1_1_1_1_1_1_1',
               'obs_1_1_1_1_1_1_1_1', 'lei_manual_m_1_1_1_1', 'unid_medida_y_1_1_1_1_1_1', 'unid_medida_aa_1_1_1_1_1_1',
               'unid_medida_ac_1_1_1_1_1',
               'cd_instrumento_1_1_1_1_1_1_1_1_1', 'tp_instrumento_1_1_1_1_1_1_1_1_1',
               'stp_instrumento_1_1_1_1_1_1_1_1_1', 'dt_medicao_1_1_1_1_1_1_1_1_1',
               'hr_medicao_1_1_1_1_1_1_1_1_1', 'sit_medicao_1_1_1_1_1_1_1_1_1', 'valor_1_1_1_1_1_1_1_1_1',
               'tp_coleta_1_1_1_1_1_1_1_1_1',
               'just_n_medicao_1_1_1_1_1_1_1_1_1', 'unid_medida_1_1_1', 'numero_OS_1_1_1_1_1_1_1_1_1',
               'cond_adversa_1_1_1_1_1_1_1_1_1',
               'obs_1_1_1_1_1_1_1_1_1', 'lei_manual_m_1_1_1_1_1', 'unid_medida_y_1_1_1_1_1_1_1',
               'unid_medida_aa_1_1_1_1_1_1_1',
               'unid_medida_ac_1_1_1_1_1_1', 'cd_instrumento_1_1_1_1_1_1_1_1_1_1', 'tp_instrumento_1_1_1_1_1_1_1_1_1_1',
               'stp_instrumento_1_1_1_1_1_1_1_1_1_1',
               'dt_medicao_1_1_1_1_1_1_1_1_1_1', 'hr_medicao_1_1_1_1_1_1_1_1_1_1', 'sit_medicao_1_1_1_1_1_1_1_1_1_1',
               'valor_1_1_1_1_1_1_1_1_1_1',
               'tp_coleta_1_1_1_1_1_1_1_1_1_1', 'just_n_medicao_1_1_1_1_1_1_1_1_1_1', 'unid_medida_1_1_1_1',
               'numero_OS_1_1_1_1_1_1_1_1_1_1',
               'cond_adversa_1_1_1_1_1_1_1_1_1_1', 'obs_1_1_1_1_1_1_1_1_1_1', 'lei_manual_m_1_1_1_1_1_1',
               'unid_medida_y_1_1_1_1_1_1_1_1',
               'unid_medida_aa_1_1_1_1_1_1_1_1', 'unid_medida_ac_1_1_1_1_1_1_1', 'cd_instrumento_1_1_1_1_1_1_1_1_1_1_1',
               'tp_instrumento_1_1_1_1_1_1_1_1_1_1_1', 'stp_instrumento_1_1_1_1_1_1_1_1_1_1_1',
               'dt_medicao_1_1_1_1_1_1_1_1_1_1_1', 'hr_medicao_1_1_1_1_1_1_1_1_1_1_1',
               'sit_medicao_1_1_1_1_1_1_1_1_1_1_1', 'valor_1_1_1_1_1_1_1_1_1_1_1', 'tp_coleta_1_1_1_1_1_1_1_1_1_1_1',
               'just_n_medicao_1_1_1_1_1_1_1_1_1_1_1',
               'numero_OS_1_1_1_1_1_1_1_1_1_1_1', 'cond_adversa_1_1_1_1_1_1_1_1_1_1_1', 'obs_1_1_1_1_1_1_1_1_1_1_1',
               'desv_padrao']


def leituraglobal():
    with open('2022_01_15_INOUT_CadastroXLSX.csv', encoding='UTF8') as fleituras:
        csv_reader = csv.DictReader(fleituras, fieldnames)

        next(csv_reader)
        for line in csv_reader:
            print(line[0])
            for lay_saida in range(25):
                for lay_in in range(202):
                    print(" Id Instrumento {}".format(line['id_instrumento']))

                    if line['id_instrumento'].startswith(layout_saida[lay_saida]):
                        if len(line['cd_instrumento']) == 0:
                            s_linOut = s_linOut
                            print(f" Linha {line['id_instrumento']} is {line['cd_instrumento']} Teste")
                            exit()
    fleituras.close()


def leitura():
    fleituras = open('2022_01_15_INOUT_CadastroXLSX.csv', encoding='UTF8')
    csv_reader = csv.reader(fleituras)

    for line in csv_reader:
        print(line[0])
        for lay_saida in range(25):
            for lay_in in range(202):
                print(" Id Instrumento {}".format(line[0]))

                if line[0].startswith(layout_saida[lay_saida]):
                   if len(line[0]) == 0:
                      s_linOut = s_linOut
                      print(f" Linha {line[0]} is {line[0]} Teste")
                      exit()

fleituras.close()


leitura()