import serial
import pyvesc

def main():
    print("Hello World!")

    fsesc = serial.Serial('COM3')
    print(fsesc.name)



if __name__ == "__main__":
    main()

