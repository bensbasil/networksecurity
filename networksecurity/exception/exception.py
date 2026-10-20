import sys

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(str(error_message))

        _, _, exc_tb = error_detail.exc_info()

        if exc_tb is not None:
            self.file_name = exc_tb.tb_frame.f_code.co_filename
            self.lineno = exc_tb.tb_lineno
        else:
            self.file_name = None
            self.lineno = None

        self.error_message = error_message

    def __str__(self):
        return (
            f"Error occurred in Python script [{self.file_name}] "
            f"at line [{self.lineno}]: {self.error_message}"
        )
    