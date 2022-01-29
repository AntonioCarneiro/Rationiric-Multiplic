import decimal
import sys
from decimal import Decimal, getcontext
from datetime import datetime, date, timedelta

import mysql.connector


def desvpadrao(parm_cd_instrumento, parm_data_inicial):
    # Connect with MySQL Server
    cnx = mysql.connector.connect(user='root', password='Vitori@66',
                                  host='127.0.0.1',
                                  database='dbmultiplic')

    # Get two buffered cursors
    cur_down = cnx.cursor(buffered=True)
    cur_up = cnx.cursor(buffered=True)
    cur_marc = cnx.cursor(buffered=True)
    cur_count = cnx.cursor(buffered=True)
    rows_count = 0

    # Open cursor
    cursor = cnx.cursor()

    # Query to get instruments
    query = ("SELECT IF(TRUNCATE(valor, 5) > 0, TRUNCATE(valor, 5) , 0), id_instrumento"
             " FROM dbMultiplic.tb_leitura_vc "
             " WHERE cd_instrumento = %s "
             "  AND data_medicao > %s "
             "  AND valor > 0 "
             " ORDER BY data_medicao ASC;")

    # Query Somatoria das Marcações
    query_marcacoes = ("SELECT TRUNCATE(sum(valor), 5)"
                       " FROM dbMultiplic.tb_leitura_vc"
                       " WHERE cd_instrumento = %s"
                       " AND data_medicao > %s"
                       " AND valor > 0 "
                       "ORDER BY data_medicao ASC;")

    # Query Count rows select
    query_count = ("SELECT count(valor) "
                   "FROM dbMultiplic.tb_leitura_vc "
                   "WHERE cd_instrumento = %s "
                   "AND data_medicao > %s "
                   "AND valor > 0 "
                   "ORDER BY data_medicao ASC")

    # UPDATE and INSERT statements for the old and new salary
    update_desv_padrao = (
        "UPDATE tb_leitura_vc SET desv_padrao = %s WHERE id_instrumento = %s;")

    # Parameters for cursor
    # p_cod_instrumento = "PICBMV2INA008"
    # p_data_inicial = "2020-07-01"
    p_cod_instrumento = parm_cd_instrumento
    p_data_inicial = parm_data_inicial
    s_devpadrao = 'OK'

    # Execute Cursor Contador de leituras
    cur_count.execute(query_count, (p_cod_instrumento, p_data_inicial))
    result = cur_count.fetchone()

    number_of_records = result[0]
    rows_count = number_of_records

    if number_of_records > 0:
        # Execute cursor
        cur_down.execute(query, (p_cod_instrumento, p_data_inicial))

        # Execute Cursor Marcacoes Somatoria
        cur_marc.execute(query_marcacoes, (p_cod_instrumento, p_data_inicial))

        getcontext().prec = 5

        # Iterate through the result of cursor
        for (valor) in cur_count:
            rows_count = float('.'.join(str(elem) for elem in valor))

        # Iterate through the result of cursor
        for (valor) in cur_marc:
            sum_leituras = float('.'.join(str(elem) for elem in valor))

        somatorio = 0.0
        desv_padrao = 0.0
        mediadif = 0.0
        elevado = 0.0

        # Iterate through the result of cursor
        for (valor, id_instrumento) in cur_down:
            # Update the new STATUS of desvio padrão
            media_leitura = (sum_leituras / rows_count)
            mediadif = valor - media_leitura
            elevado = mediadif ** 2
            somatorio = somatorio + elevado

        desv_padrao = ((somatorio / rows_count) ** (1 / 2))

        limite_baixo = (media_leitura - (3 * desv_padrao))
        limite_alto = (media_leitura + (3 * desv_padrao))

        cur_down.execute(query, (p_cod_instrumento, p_data_inicial))
        for (valor, id_instrumento) in cur_down:
            s_desvpadrao = "OK"

            if valor < limite_baixo:
                s_desvpadrao = "NOK"

            if valor > limite_alto:
                s_desvpadrao = "NOK"

            cur_up.execute(update_desv_padrao, (s_desvpadrao, id_instrumento))

            # Commit the changes
            cnx.commit()

    # Close Mysql
    cursor.close()

    # Disconnect with MySQL Server
    cnx.close()


if __name__ == '__main__':
    desvpadrao(sys.argv[1], sys.argv[2])
    sys.exit(1)
