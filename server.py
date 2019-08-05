import socket
import wave
import pyaudio

def audio(frames):
	chunk = 1024  # Record in chunks of 1024 samples
	sample_format = pyaudio.paInt16  # 16 bits per sample
	channels = 2
	fs = 44100  # Record at 44100 samples per second
	seconds = 3
	filename = "output.wav"
	print ("Saving data as wav file")
	wf = wave.open(filename, 'wb')
	wf.setnchannels(channels)
	wf.setsampwidth(2)
	wf.setframerate(fs)
	wf.writeframes(b''.join(frames))
	wf.close()
	print ("wav file saved")
def send():
	frames=[]
	HOST='192.168.14.147' #localhost
	PORT=50008

	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM ) #create an INET, STREAMing socket
	s.bind((HOST,PORT)) #bind to that port
	s.listen(1) #listen for user input and accept 1 connection at a time.

	conn, addr = s.accept()

	print ("The connection has been set up")
	while True:
		data=conn.recv(10024)
		print (data)
		if b'end' in data:
			print ("end of file")
			break
		frames.append(data)
	print (frames)
	s.close()
	audio(frames)
send()