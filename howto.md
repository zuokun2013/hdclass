
ffmpeg split audio
  ffmpeg -i  '.\04-4 慧灯禅修12 轮回痛苦4.mp3' -f segment -segment_time 2700 -c copy output2_%03d.mp3


  curl https://api.openai.com/v1/audio/transcriptions   -H "Authorization: Bearer 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"   -H "Content-Type: multipart/form-data"   -F model="whisper-1" -F response_format="vtt"  -F file="@c:\\tmp\\output2_000.mp3"

  curl https://api.openai.com/v1/audio/transcriptions   -H "Authorization: Bearer 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"   -H "Content-Type: multipart/form-data"   -F model="whisper-1"   -F file="@c:\\tmp\\output2_000.mp3"

New-PSDrive -Name "j" -PSProvider FileSystem -Root "\\192.168.1.222\sambashare\data" -Persist

  whisper --language Chinese --task transcribe --model base 'j:\金密钥\课程视频\慧灯禅修课\慧灯禅修课第四册\04-1 慧灯禅修课31 加行的修法-曼荼罗1.mp4'

  whisper --language Chinese --task transcribe --model base 'j:\金密钥\课程视频\慧灯禅修课\慧灯禅修课第三册\02-3 慧灯禅修课4 人身难得3.mp4'

  whisper --language Chinese --task transcribe --model medium '/Volumes/easyshare-12t/金密钥/课程音频/慧灯禅修课/慧灯禅修课第三册/04-4 慧灯禅修课12 轮回痛苦4.mp3'

  whisper --language Chinese --task transcribe --model base '/mnt/easystore-12t/金密钥/课程视频/慧灯禅修课/慧灯禅修课第三册/05-5 慧灯禅修课17 因果不虚5.mp4'

  nohup whisper --language Chinese --task transcribe --model small '/mnt/easystore-12t/金密钥/课程视频/慧灯禅修课/慧灯禅修课第三册/05-5 慧灯禅修课17 因果不虚5.mp4' > 因果不虚5.txt &

ssh zuokun@192.168.1.223

for FILE in /mnt/easystore-12t/金密钥/课程视频/慧灯禅修课/慧灯禅修课第三册/*; do 
  echo $FILE; 
  whisper --language Chinese --task transcribe --model small "$FILE" >> hdcx3慧灯禅修课第三册.txt
done

for FILE in /mnt/easystore-12t/金密钥/课程视频/慧灯禅修课/慧灯禅修课第三册/*; do 
  echo $FILE; 
  filename=$(basename -- "$FILE")
  echo $filename
  nameonly="${filename%.*}"
  echo $nameonly 
  echo "$nameonly" | tr ' ' _
done

  whisper --help
usage: whisper [-h] [--model MODEL] [--model_dir MODEL_DIR] [--device DEVICE] [--output_dir OUTPUT_DIR] [--output_format {txt,vtt,srt,tsv,json,all}] [--verbose VERBOSE] [--task {transcribe,translate}]
               [--language {af,am,ar,as,az,ba,be,bg,bn,bo,br,bs,ca,cs,cy,da,de,el,en,es,et,eu,fa,fi,fo,fr,gl,gu,ha,haw,he,hi,hr,ht,hu,hy,id,is,it,ja,jw,ka,kk,km,kn,ko,la,lb,ln,lo,lt,lv,mg,mi,mk,ml,mn,mr,ms,mt,my,ne,nl,nn,no,oc,pa,pl,ps,pt,ro,ru,sa,sd,si,sk,sl,sn,so,sq,sr,su,sv,sw,ta,te,tg,th,tk,tl,tr,tt,uk,ur,uz,vi,yi,yo,yue,zh,Afrikaans,Albanian,Amharic,Arabic,Armenian,Assamese,Azerbaijani,Bashkir,Basque,Belarusian,Bengali,Bosnian,Breton,Bulgarian,Burmese,Cantonese,Castilian,Catalan,Chinese,Croatian,Czech,Danish,Dutch,English,Estonian,Faroese,Finnish,Flemish,French,Galician,Georgian,German,Greek,Gujarati,Haitian,Haitian Creole,Hausa,Hawaiian,Hebrew,Hindi,Hungarian,Icelandic,Indonesian,Italian,Japanese,Javanese,Kannada,Kazakh,Khmer,Korean,Lao,Latin,Latvian,Letzeburgesch,Lingala,Lithuanian,Luxembourgish,Macedonian,Malagasy,Malay,Malayalam,Maltese,Mandarin,Maori,Marathi,Moldavian,Moldovan,Mongolian,Myanmar,Nepali,Norwegian,Nynorsk,Occitan,Panjabi,Pashto,Persian,Polish,Portuguese,Punjabi,Pushto,Romanian,Russian,Sanskrit,Serbian,Shona,Sindhi,Sinhala,Sinhalese,Slovak,Slovenian,Somali,Spanish,Sundanese,Swahili,Swedish,Tagalog,Tajik,Tamil,Tatar,Telugu,Thai,Tibetan,Turkish,Turkmen,Ukrainian,Urdu,Uzbek,Valencian,Vietnamese,Welsh,Yiddish,Yoruba}]
               [--temperature TEMPERATURE] [--best_of BEST_OF] [--beam_size BEAM_SIZE] [--patience PATIENCE] [--length_penalty LENGTH_PENALTY] [--suppress_tokens SUPPRESS_TOKENS] [--initial_prompt INITIAL_PROMPT]
               [--condition_on_previous_text CONDITION_ON_PREVIOUS_TEXT] [--fp16 FP16] [--temperature_increment_on_fallback TEMPERATURE_INCREMENT_ON_FALLBACK] [--compression_ratio_threshold COMPRESSION_RATIO_THRESHOLD]
               [--logprob_threshold LOGPROB_THRESHOLD] [--no_speech_threshold NO_SPEECH_THRESHOLD] [--word_timestamps WORD_TIMESTAMPS] [--prepend_punctuations PREPEND_PUNCTUATIONS] [--append_punctuations APPEND_PUNCTUATIONS]
               [--highlight_words HIGHLIGHT_WORDS] [--max_line_width MAX_LINE_WIDTH] [--max_line_count MAX_LINE_COUNT] [--max_words_per_line MAX_WORDS_PER_LINE] [--threads THREADS]
               audio [audio ...]
whisper: error: argument -h/--help: ignored explicit argument 'elp'
zuokun@m710q:~$