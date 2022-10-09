import pyaudio
import wave
import whisper
class whip():
    def __init__(self,chunk=1024,sample_format = pyaudio.paInt16, channels = 2,fs = 44100,seconds = 3,filename ="output.wav",model_type="base"):
        self.chunk=chunk,
        self.sample_format=sample_format
        self.channels=channels
        self.fs=fs
        self.filename=filename
        self.model_type=model_type
        self.seconds=seconds

    def record(self):  # Record in chunks of 1024 samples
    
        p = pyaudio.PyAudio() 

        print('Recording')
        self.chunk=self.chunk[0]
        stream = p.open(format=self.sample_format,
                        channels=self.channels,
                        rate=self.fs,
                        frames_per_buffer=self.chunk,
                        input=True)

        frames = []  # Initialize array to store frames

        # Store data in chunks for 3 seconds
        for i in range(0, int(self.fs / self.chunk * self.seconds)):
            data = stream.read(self.chunk)
            frames.append(data)

        # Stop and close the stream 
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        p.terminate()

        print('Finished recording')

        # Save the recorded data as a WAV file
        wf = wave.open(self.filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(frames))
        wf.close()

    def mod_whisper(self):
        model=whisper.load_model(self.model_type)
        result=model.transcribe(self.filename)
        print(result)
obj=whip(seconds=10,model_type="small")
obj.record()
obj.mod_whisper()