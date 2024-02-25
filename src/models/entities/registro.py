from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
class Registro():

    def __init__(self,  id_paciente, id_medico, result_no_tb,   result_normal, resul_tb,):
       
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.result_tb = resul_tb
        self.result_no_tb = result_no_tb
        self.result_normal = result_normal


    def to_JSON(self):
        return {
            
            'id_paciente': self.id_paciente,
            'id_medico': self.id_medico,
            'result_no_tb': self.result_no_tb,
            'result_tb': self.result_tb,
             'result_normal': self.result_normal,
        }
