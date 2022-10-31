import datetime
import whisper


model = whisper.load_model("small")

# run model
print("startedAt: {}".format(datetime.datetime.now()))
result = model.transcribe("eo_channeltalk.wav")
print("endedAt: {}".format(datetime.datetime.now()))

# print full result
# print(result['text'])

# print segments
for item in result['segments']:
    print("[{:8.4f}s] {}".format(item['start'], item['text']))
