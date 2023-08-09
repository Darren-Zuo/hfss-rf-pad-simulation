# Check out https://github.com/openai/whisper for the installation and usage instruction of the package
import whisper
import datetime

model = whisper.load_model('small')
# define whisper options:
other_whisper_options = {'language': 'English'}
task = 'transcribe'
result = model.transcribe('HFSS rf pad.mp4', task=task, verbose=True, **other_whisper_options)

# result['text']
save_target = 'HFSS rf pad.srt'
with open(save_target, 'w') as file:
    for indx, segment in enumerate(result['segments']):
        file.write(str(indx + 1) + '\n')
        file.write(str(datetime.timedelta(seconds=segment['start'])) + ' --> ' + str(datetime.timedelta(seconds=segment['end'])) + '\n')
        file.write(segment['text'].strip() + '\n')
        file.write('\n')