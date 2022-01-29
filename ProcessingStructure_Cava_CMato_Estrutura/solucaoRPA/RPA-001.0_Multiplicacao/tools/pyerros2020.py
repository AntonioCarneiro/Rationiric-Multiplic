import sys
from decimal import Decimal, getcontext
from datetime import datetime, date, timedelta

import mysql.connector


# -----
# --
# -- pyerros2020
# -- Calcular a diferença em dias das medições existentes a partir de uma data inicial (yyyy-mm-dd) até NOW()
# -- RPA4All by Antonio Carneiro
# -- 06/01/22
# --
# -----


def pyerros2020(parm_cd_instrumento, parm_data_inicial):
    # Connect with MySQL Server
    cnx = mysql.connector.connect(user='root', password='Vitori@66',
                                  host='127.0.0.1',
                                  database='dbmultiplic')

    # Get two buffered cursors
    cur_down = cnx.cursor(buffered=True)
    cur_up = cnx.cursor(buffered=True)
    cur_count = cnx.cursor(buffered=True)
    number_of_records = 0

    # Open cursor
    cursor = cnx.cursor()

    # Query to get instruments
    query = ("SELECT data_medicao "
             " FROM dbMultiplic.tb_leitura_vc "
             " WHERE cd_instrumento = %s "
             "  AND data_medicao > %s "
             " ORDER BY data_medicao ASC;")

    # Query Count rows select
    query_count = ("SELECT count(*) "
                   "FROM dbMultiplic.tb_leitura_vc "
                   "WHERE cd_instrumento = %s "
                   "AND data_medicao > %s "
                   "AND valor > 0 "
                   "ORDER BY data_medicao ASC")

    # UPDATE and INSERT statements
    insert_error_2020 = "INSERT INTO TB_Temp_2020 (i_qtde_reg) VALUES ( %s )"

    # Truncate Table TB_Temp_2020
    truncate_2020 = "TRUNCATE TABLE TB_Temp_2020"

    # Parameters for cursor
    # p_cod_instrumento = "PICBMV2INA008"
    # p_data_inicial = "2020-07-01"
    p_cod_instrumento = parm_cd_instrumento
    p_data_inicial = parm_data_inicial

    # Limpa tabela de execuções anteriores
    cur_count.execute(truncate_2020)

    # Execute Cursor Contador de leituras
    cur_count.execute(query_count, (p_cod_instrumento, p_data_inicial))
    result = cur_count.fetchone()

    number_of_records = result[0]

    if number_of_records > 0:
        # Execute cursor
        cur_down.execute(query, (p_cod_instrumento, p_data_inicial))
        print("Numero de rows {}".format(number_of_records))

        getcontext().prec = 5

        data_inicial = ""
        data_final = ""
        daydiff = 0
        b_first = True
        dt_medicao_aux = ""
        date_format = "%Y-%m-%d"

        # Iterate through the result of cursor
        for (data_medicao) in cur_down:

            if b_first:
                dt_medicao_aux = data_medicao[0]
                b_first = False
            else:
                dt_medicao_aux = datetime.strptime(data_medicao[0], date_format).date()
                data_inicial = datetime.strptime(p_data_inicial, date_format).date()
                data_final = datetime.strptime(str(dt_medicao_aux), date_format).date()
                daydiff = abs((data_final - data_inicial).days)

            temp_2020 = (daydiff,)
            print("{}".format(daydiff))

            if daydiff > 0:
                cur_up.execute(insert_error_2020, temp_2020)

            # Commit the changes
            cnx.commit()

            dt_medicao_aux = data_medicao[0]

    # Close Mysql
    cursor.close()

    # Disconnect with MySQL Server
    cnx.close()


if __name__ == '__main__':
    pyerros2020(sys.argv[1], sys.argv[2])
    sys.exit(1)
