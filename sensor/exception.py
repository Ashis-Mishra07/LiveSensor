import sys
import os 


def error_message_detail(error_message, error_detail: sys):
    _, _, exc_tb = sys.exc_info()
    if exc_tb is not None:
        filename = exc_tb.tb_frame.f_code.co_filename
        lineno = exc_tb.tb_lineno
        return f"error occured and the file name is [{filename}] and the linenumber is [{lineno}]and error is [{error_message}]"
    else:
        return f"error occured and error is [{error_message}]"



class SensorException(Exception):
    
    def __init__(self,error_message,error_detail:sys):

        super().__init__(error_message)


     
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return  self.error_message