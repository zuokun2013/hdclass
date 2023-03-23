
ffmpeg split audio
  ffmpeg -i  '.\04-4 慧灯禅修12 轮回痛苦4.mp3' -f segment -segment_time 2700 -c copy output2_%03d.mp3


  curl https://api.openai.com/v1/audio/transcriptions   -H "Authorization: Bearer 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"   -H "Content-Type: multipart/form-data"   -F model="whisper-1" -F response_format="vtt"  -F file="@c:\\tmp\\output2_000.mp3"

  curl https://api.openai.com/v1/audio/transcriptions   -H "Authorization: Bearer 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"   -H "Content-Type: multipart/form-data"   -F model="whisper-1"   -F file="@c:\\tmp\\output2_000.mp3"

New-PSDrive -Name "j" -PSProvider FileSystem -Root "\\192.168.1.222\sambashare\data" -Persist

  whisper --language Chinese --task transcribe --model base 'j:\金密钥\课程视频\慧灯禅修课\慧灯禅修课第四册\04-1 慧灯禅修课31 加行的修法-曼荼罗1.mp4'

  whisper --language Chinese --task transcribe --model base 'j:\金密钥\课程视频\慧灯禅修课\慧灯禅修课第三册\02-3 慧灯禅修课4 人身难得3.mp4'