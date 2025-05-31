import serial
import serial.tools.list_ports

class SerialClass:
    def __init__(self, port_name, baud_rate, timeout):
        self.ser = serial.Serial(port=port_name, baudrate=baud_rate, timeout=timeout)


    def get_serial_print(self):
        return self.ser.readline().decode('utf-8').strip()


    @staticmethod
    def get_ports():
        return list(serial.tools.list_ports.comports())