import sys
from matplotlib import pyplot
from time import sleep
import Tkinter
import datetime
import time
import RPi.GPIO as GPIO

trigger_pin = 18
echo_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

def send_trigger_pulse():
    GPIO.output(trigger_pin, True)
    time.sleep(0.0001)
    GPIO.output(trigger_pin, False)

def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(echo_pin) != value and count > 0:
        count = count - 1

def get_distance():
    send_trigger_pulse()
    wait_for_echo(True, 10000)
    start = time.time()
    wait_for_echo(False, 10000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len / 0.000058
    return (distance_cm)

def saat_tombol_mulai():
    while True:
        if flag.get():
            sleep(0.0001)
            outf = open("data_jarak.txt", "ab")
            outf.write("%f\n" % get_distance())
            print get_distance()
            pData.append(float(get_distance()))
            pyplot.ylim([0, 100])
            del pData[0]
            l1.set_xdata([i for i in xrange(25)])
            l1.set_ydata(pData)  # update data
            pyplot.title("INTERFACE DATA JARAK HC-SR04")
            pyplot.xlabel("Waktu (s)")
            pyplot.ylabel("Jarak (cm)")
            #pyplot.savefig('grafik_jarak.png',format='png')
            pyplot.draw()  # update plot
            top.update()
        else:
            flag.set(True)
            break


def saat_tombol_pause():
    flag.set(False)


def saat_tombol_keluar():
    print "Keluar"
    saat_tombol_pause()
    pyplot.close(fig)
    top.quit()
    top.destroy()
    print "Selesai"
    sys.exit()

# Judul GUI Tkinter 
top = Tkinter.Tk()
top.title("GUI Python Kontrol")

# Membuat flag agar dapat bekerja dengan while loop
flag = Tkinter.BooleanVar(top)
flag.set(True)

pyplot.ion()
pData = [0.0] * 25
fig = pyplot.figure()
ax1 = pyplot.axes()
l1, = pyplot.plot(pData)
pyplot.ylim([0, 100])

# GUI Mulai terhubung dengan fungsi saat tombol mulai
tombol_mulai = Tkinter.Button(top,
                             text="Mulai",
                             command=saat_tombol_mulai)
tombol_mulai.grid(column=1, row=2)

# GUI Pause terhubung dengan fungsi saat tombol pause
tombol_pause = Tkinter.Button(top,
                             text="Pause",
                             command=saat_tombol_pause)
tombol_pause.grid(column=2, row=2)

# GUI Keluar terhubung dengan fungsi saat tombol keluar
tombol_keluar = Tkinter.Button(top,
                            text="Keluar",
                            command=saat_tombol_keluar)
tombol_keluar.grid(column=3, row=2)

top.mainloop()

