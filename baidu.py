from aip import AipSpeech
import time
import wav2pcm
#import io
#import sys

#sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

APP_ID = '18240192'
API_KEY = 'l6olC3AktVQfKUksIh1Z8Dv3'
SECRET_KEY = '76sHQR5cUo9zigr1g7Ka4zkatNaGrNGT'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

pcm_file=wav2pcm.wav_to_pcm("D4_750.wav")

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#识别本地文件
start_time = time.time()
ret = client.asr(get_file_content('F:\\p project\\3.7\\D4_750.wav'), 'pcm', 16000, {'dev_pid': 1537,})
used_time = time.time() - start_time
print( "used time: {}s".format( round( time.time() - start_time, 2 ) ) )
print('ret:{}'.format(ret))