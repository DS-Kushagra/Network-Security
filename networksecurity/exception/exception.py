import sys

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        try:
            exc_type, exc_value, exc_tb = error_details.exc_info()
            if exc_tb:
                lineno = exc_tb.tb_lineno
                file_name = exc_tb.tb_frame.f_code.co_filename
            else:
                lineno = "Unknown"
                file_name = "Unknown"

            self.error_message = (
                f"Error occurred in python script {file_name} in line number {lineno} "
                f"with error message: {error_message}"
            )
        except Exception as internal_exception:
            self.error_message = f"Error initializing exception: {internal_exception}"

        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message
