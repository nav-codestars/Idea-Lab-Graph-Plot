import serial
import serial.tools.list_ports
import threading
import queue

class SerialClass:
    def __init__(self, port_name, baud_rate, timeout):
        self.ser = None
        self.thread = None
        self.running = False
        self.data_queue = queue.Queue()
        try:
            self.ser = serial.Serial(port=port_name, baudrate=baud_rate, timeout=timeout)
            self.running = True
            self.thread = threading.Thread(target=self._read_serial, daemon=True)
            self.thread.start()
        except serial.SerialException as e: 
            print(f"Serial port error during initialization: {e}")
        except Exception as e:
            print(e)

    def _read_serial(self):
        buffer = ""
        while self.running and self.ser and self.ser.is_open:
            try:
                chunk = self.ser.read(self.ser.in_waiting or 1).decode('utf-8', errors='ignore')
                buffer += chunk
                while '\n' in buffer:
                    line, buffer = buffer.split('\n', 1)
                    line = line.strip()
                    if line:
                        self.data_queue.put(line)
            except Exception as e:
                print(f"Serial read error: {e}")
                break

    def get_serial_print(self):
        try:
            return self.data_queue.get_nowait()
        except queue.Empty:
            return None

    def close_serial(self):
        self.running = False
        if self.ser and self.ser.is_open:
            self.ser.close()

    @staticmethod
    def get_ports():
        return list(serial.tools.list_ports.comports())




