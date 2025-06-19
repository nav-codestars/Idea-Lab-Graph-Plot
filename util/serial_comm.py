import serial
import serial.tools.list_ports

class SerialClass:
    def __init__(self, port_name, baud_rate, timeout):
        try:
            self.ser = serial.Serial(port=port_name, baudrate=baud_rate, timeout=timeout)
        except serial.SerialException as e: 
            print(f"Serial port error during initialization: {e}")
            self.ser = None
        return self.ser

    def get_serial_print(self):
        if self.ser is None or not self.ser.is_open:
            print("Serial port not open or not initialized.")
            return None
        try:
            return self.ser.readline().decode('utf-8').strip()
        except serial.SerialException as e:
            print(f"Serial read error: {e}")
            return None

    def close_serial(self):
        self.ser.close() if self.ser and self.ser.is_open else None

    @staticmethod
    def get_ports():
        return list(serial.tools.list_ports.comports())




