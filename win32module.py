import win32com.client


speak = win32com.client.Dispatch("SAPI.SpVoice")

text = "congratulations"
speak.Speak(text)

names = ["charan", "cherry", "rahul", "virat"]

for name in names:
    speak.Speak(f"shoutout to {name}")
