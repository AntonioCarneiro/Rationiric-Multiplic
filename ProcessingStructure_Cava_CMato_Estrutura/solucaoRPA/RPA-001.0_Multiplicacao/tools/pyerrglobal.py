import sys
from decimal import Decimal, getcontext
from datetime import datetime, date, timedelta

import mysql.connector


# -----
# --
# -- pyerrglobal
# -- Calcular a diferença em dias das medições existentes de um instrumento até NOW()
# -- BC IT SERVICE by Antonio Carneiro
# -- 06/01/22
# --
# -----


def pyerrglobal(parm_cd_instrumento):
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
             "  FROM dbMultiplic.tb_leitura_vc "
             " WHERE cd_instrumento = %s "
             "   AND valor > 0 "
             " ORDER BY data_medicao ASC;")

    # Query Count rows select
    query_count = ("SELECT count(*) "
                   "  FROM dbMultiplic.tb_leitura_vc "
                   " WHERE cd_instrumento = %s "
                   "   AND valor > 0 "
                   " ORDER BY data_medicao ASC")

    # UPDATE and INSERT statements
    insert_error_2020 = "INSERT INTO TB_Temp_spv2 (i_qtde_reg) VALUES ( %s )"

    # Truncate Table TB_Temp_2020
    truncate_2020 = "TRUNCATE TABLE TB_Temp_spv2"

    # Parameters for cursor
    # p_cod_instrumento = "PICBMV2INA008"
    # p_data_inicial = parm_dt_inicial
    p_cod_instrumento = (parm_cd_instrumento, )

    # Limpar tabela de execuções anteriores
    cur_count.execute(truncate_2020)

    # Execute Cursor Contador de leituras
    cur_count.execute(query_count, p_cod_instrumento)
    result = cur_count.fetchone()

    number_of_records = result[0]

    if number_of_records > 0:
        # Execute cursor
        cur_down.execute(query, p_cod_instrumento)
        # print("Numero de rows {}".format(number_of_records))

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
                dt_medicao_aux = datetime.strptime(data_medicao[0], date_format).date()
                b_first = False
            else:
                data_inicial = datetime.strptime(str(dt_medicao_aux), date_format).date()
                data_final = datetime.strptime(data_medicao[0], date_format).date()

                # Retornar a diferença em dias de duas datas
                daydiff = abs((data_final - data_inicial).days)

            temp_2020 = (daydiff,)
            # print("{}".format(daydiff))

            if daydiff > 0:
                cur_up.execute(insert_error_2020, temp_2020)

            # Commit the changes
            cnx.commit()

            dt_medicao_aux = datetime.strptime(data_medicao[0], date_format).date()

    # Close Mysql
    cursor.close()

    # Disconnect with MySQL Server
    cnx.close()


if __name__ == '__main__':
    pyerrglobal(str(sys.argv[1]))
    sys.exit(1)
