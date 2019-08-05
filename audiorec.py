import pyaudio
import wave
import socket

def record():
	chunk = 1024  # Record in chunks of 1024 samples
	sample_format = pyaudio.paInt16  # 16 bits per sample
	channels = 2
	fs = 44100  # Record at 44100 samples per second
	seconds = 10
	filename = "output.wav"

	p = pyaudio.PyAudio()  # Create an interface to PortAudio

	print('Recording')

	stream = p.open(format=sample_format,
					channels=channels,
					rate=fs,
					frames_per_buffer=chunk,
					input=True)

	frames = []  # Initialize array to store frames

	# Store data in chunks for 3 seconds
	for i in range(0, int(fs / chunk * seconds)):
		data = stream.read(chunk)
		frames.append(data)

	# Stop and close the stream 
	stream.stop_stream()
	stream.close()
	# Terminate the PortAudio interface
	p.terminate()

	print('Finished recording')
	# Save the recorded data as a WAV file
	print (p.get_sample_size(sample_format))
	return frames

def send():
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM ) #create an INET, STREAMing socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host ="192.168.14.147"
	port =50008
	s.connect((host,port))
	frames=record()
	print (frames[0])
	for frame in frames:
		s.sendall(frame)
	s.sendall(b'end')
	s.close()
send()