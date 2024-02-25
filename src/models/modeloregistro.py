from database.db import get_connection
from .entities.registro import Registro


class ModeloRegistro():

    @classmethod
    def get_registros(self):

        try:
            connection = get_connection()
            registros = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM registros")

                resultset = cursor.fetchall()

                for row in resultset:
                    registro = Registro(row[0], row[1], row[2], row[4], row[3], row[5])
                    registros.append(registro.to_JSON())

            connection.close()
            return registros
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_registro(self, id_paciente):
        try:
            connection = get_connection()
            registros = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM registros WHERE id_paciente = %s", (id_paciente,))

                resultset = cursor.fetchall()

                for row in resultset:
                    registro = Registro(row[1], row[2], round(float(row[3]) * 100, 2), round(float(row[5]) * 100, 2), round(float(row[4]) * 100, 2))
                    registros.append(registro.to_JSON())

            connection.close()

            print(registros)
            return registros
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_registro(self, registro):

        print(registro.id_paciente)
        print(registro.id_medico)
        print("no tb", registro.result_no_tb)
        print(" tb", registro.result_tb)
        print("normal", registro.result_normal)

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO registros ( id_paciente, id_medico, result_no_tb, result_tb, result_normal)
                            VALUES ( %s, %s, %s ,%s, %s)""", (registro.id_paciente, registro.id_medico, registro.result_no_tb, registro.result_tb, registro.result_normal))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
