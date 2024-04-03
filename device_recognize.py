import soundcard as sc

mics = sc.all_microphones(include_loopback=True)
# print(mics)

for i in range(len(mics)):
    try:
        print(f"{i}: {mics[i].name}")
    except Exception as e:
        print(e)