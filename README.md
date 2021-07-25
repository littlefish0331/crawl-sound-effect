# README

這個專案是為了 「Tbrain - Tomofun 狗音辨識 AI 百萬挑戰賽」。  
要收集其他公開的音效檔。

目前要爬取的網站，以及目標如下。  

- 檔案格式以 .wav 為主，否則就以 .mp3 做取代。  
- 音效長度不超過 5 分鐘。所以有做一層 filter 再 download。

| website - category | 0 Barking | 1 Howling | 2 Crying | 3 CO_Smoke | 4 GlassBreaking | 5 Other* | 6 Doorbell | 7 Bird | 8 Music_Instrument | 9 Laugh_Shout_Scream |
| ------------------ | --------- | --------- | -------- | ---------- | --------------- | -------- | ---------- | ------ | ------------------ | -------------------- |
| source 01          | ✔️        | ✔️        | ✔️       | ❌         | ✔️              | ✔️       | ✔️         | ✔️     | ❌                 | ✔️                   |
| source 01          | ✔️        | ✔️        | ❌       | ✔️         | ✔️              | ✔️       | ✔️         | ✔️     | ✔️                 | ✔️                   |

- Other*: Other, Vacuum, Blender, Electrics, Cat, Dishes

--

因為官方給的聲音，雖然 label 為 Music_Instrument，但可能需要用不同的關鍵字才能找到類似的音檔。  
而且每個網站要用的關鍵字也不進相同。

**query kwyqord:**

- source 01
  - Barking: dog bark, dog barking
  - Howling: dog howl, dog howling
  - Crying: dog cry, dog crying
  - CO_Smoke: -
  - GlassBreaking: glass crash, glass crashing
  - Other: vacuum, electric, mower, wave, electronic noise, noise
  - Doorbell: door bell, bell, doorbell, chime
  - Bird: bird
  - Music_Instrument: -
  - Laugh_Shout_Scream: laugh, laughs, shout, shouts, cheer, crowd, crowds
- source 02
  - Barking: dog bark, dog barking
  - Howling: dog howl, dog howling
  - Crying: -
  - CO_Smoke: smoke detector, fire+alarm beep, alarm beep, detector, detector beep
  - GlassBreaking: glass break, broken glass
  - Other: meow, cat voice, vacuum cleaner, vacuum, blender start, blender, NutriBullet, toy noise, electrical current, phone ring, telephone ring, dishes
  - Doorbell: doorbell, door ring
  - Bird: bird, bird chirping
  - Music_Instrument: warm pad, piano, soft piano, percussion
  - Laugh_Shout_Scream: laugh, laughter, shouting, scream, screaming

---

## 音效庫資料來源

- source 01: [BBC Rewind - Sound Effects](https://sound-effects.bbcrewind.co.uk/)
- source 02: [Download Free Sound Effects & Royalty Free Music | ZapSplat](https://www.zapsplat.com/)

--

以下是沒時間爬取的音效庫來源，有時間可以再研究XD

- source 03: [Freesound - sound search](https://freesound.org/search/?q=dog)
- source 04: [Download Sound Effects | Soundsnap Sound Effects Library](https://www.soundsnap.com/)
- source 05: [Free audio samples, drum loops & kits, vocals, royalty free music](https://sampleswap.org/)
- source 06: [Free Sound Effects, Royalty Free Sound Effects, Nature Sounds](https://www.partnersinrhyme.com/pir/PIRsfx.shtml)
- source 07: [GameSounds.xyz - Royalty free or public domain game music and sounds](https://gamesounds.xyz/)
- source 08: [Free SFX](https://www.freesfx.co.uk/Default.aspx)
- source 09: [Sound Effects +](https://www.soundeffectsplus.com/search.php)
- source 10: [Free Sound Effects - SoundGator](http://www.soundgator.com/)
- source 11: [FindSounds - Browse for sounds](https://www.findsounds.com/)
- source 12: [Free Loops Samples Sounds Wavs Beats Download](https://www.looperman.com/loops?type=wav)
- source 13: [get-sounds.com - Sound Effects](http://www.get-sounds.com/index.php)
- source 14: [創作者工作坊](https://business.facebook.com/creatorstudio/home)
- source 15: [Dog Barking Multiple Sound Effect | Dog Sounds | Orange Free Sounds](https://orangefreesounds.com/dog-barking-multiple-sound-effect/)
- source 16: [Download Free Sound Effects](https://www.mediacollege.com/downloads/sound-effects/)
- source 17: [Community Audio : Free Community : Free Download, Borrow and Streaming : Internet Archive](https://archive.org/details/opensource_audio)
- source 18: [Download Free Sound Effects & Royalty Free Music // SoundsCrate](https://sfx.productioncrate.com/)
- source 19: [Free Music Archive](https://freemusicarchive.org/home)
- source 20: [Free Sound Clips | SoundBible.com](https://soundbible.com/)
- source 21: [Download Free Sound Effects for Videos | Mixkit](https://mixkit.co/free-sound-effects/)
- source 22: [Royalty free music and sound effects | Epidemic Sound](https://www.epidemicsound.com/)
- source 23: [Free SFX](https://freesfx.co.uk/)
- source 24: [Royalty Free Sound Effects Sounds Download FX Stock Audio](https://www.videvo.net/royalty-free-sound-effects/)
- source 25: [Download Royalty Free Sound Effects - Envato Elements](https://elements.envato.com/sound-effects)
- source 26: [頻道資訊主頁 - YouTube Studio](https://studio.youtube.com/channel/UCjrRAbxYmp9CSacu9dRywFQ)

---

## 關於範例的聲音

以下是對各個範例聲音檔案的一些觀察

| Remark             | Label | Count | Range                       | Description                               | Comment                                                                                                                                                                                                              |
| ------------------ | ----- | ----- | --------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Barking            | 0     | 200   | 00001-00200                 | 狗狗的吠叫聲                              | 狗叫, 吉娃娃的啾啾狗叫, 黃金獵犬的汪汪叫, 看門狗的吠叫, 有些有警示嚕的聲音, 屋嗚                                                                                                                                     |
| Howling            | 1     | 200   | 00201-00400 - 00393 + 00577 | 狗狗的嚎叫聲                              | 凹嗚~, 嗚~, 拉比較長, 有哭腔, 或是喔咿的呻吟, 嚎叫, 哭嚎, 通常會大聲到小聲                                                                                                                                           |
| Crying             | 2     | 200   | 00401-00600 - 00577 + 00393 | 狗狗的哭泣聲                              | 哭泣, 委屈, 類似狗叫，但是沒有, 嗚咿~, 大多偏小聲, 可能前面會咿很久，但最後尾音都會下墜且變小聲                                                                                                                      |
| CO_Smoke           | 3     | 200   | 00601-00800                 | 家中⼀氧化碳/煙霧警報器的聲⾳             | 高頻的警報聲, 短促的逼逼聲, 有些類似倒車後退快撞到東西的聲音, 咿~ 咿~ , 鬧鐘逼逼聲, 聽起來都很刺耳，或是讓人緊張不舒服, 有些會有電子提示聲                                                                           |
| GlassBreaking      | 4     | 199   | 00801-01000 - 00909         | 家中玻璃破碎的聲⾳                        | 比起 Dishes 有更多的玻璃碰撞聲, smash glass, crash glass, 摔玻璃                                                                                                                                                     |
| (Other)Other       | 5     | 1     | 00909                       | 家中非其他 9 類的聲⾳                     | 鈴聲+火花劈哩啪啦的聲音                                                                                                                                                                                              |
| (Other)Vacuum      | 5     | 90    | 01001-01090                 | 家中非其他 9 類的聲⾳: 真空、吸塵器       | 吸塵器, 有風洞聲, 吸走東西的感覺, 固定音調，咿~, 啟動時像引擎發動, 割草機(?), 路上吹垃圾的機器, 吹風機, 發動機的聲音, 割草機的聲音, 音高不一定、大小聲不一定                                                         |
| (Other)Blender     | 5     | 10    | 01091-01100                 | 家中非其他 9 類的聲⾳: 攪拌機             | 有空洞感的旋轉聲, 攪拌東西的旋轉卡住聲, 嘎的一聲                                                                                                                                                                     |
| (Other)Electrics   | 5     | 10    | 01101-01110                 | 家中非其他 9 類的聲⾳: 電子雜音           | 無特色的電子怪聲, 電波聲音, 電子雜音, 電話鈴聲, **某個旋轉的電子設備(電鑽頭), 電子嗡嗡聲, 除了電話鈴聲與電鑽頭外，總之就是雜音很重的聲音**                                                                           |
| (Other)Cat         | 5     | 30    | 01111-01140                 | 家中非其他 9 類的聲⾳: 貓叫               | 喵, 喵凹, 凹喵, 喵壓, 壓阿屋, 喵阿, 挖凹, 卡到毛球的凹屋咕嚕聲, 凹, 屋凹, 壓, 大多拉長，不知道在公三小的喵喵叫                                                                                                       |
| (Other)Dishes      | 5     | 60    | 01141-01200                 | 家中非其他 9 類的聲⾳: 洗、擺放盤子等操作 | **收/整理 盤子的聲音, 把盤子放到桌上的聲音, 盤子重疊時的聲音, 瓷器碰撞聲**, 金屬杯碰撞的聲音, 到東西到盤子上的聲音(麥片), 些微水聲在洗盤子                                                                           |
| Doorbell           | 6     | 100   | 01201-01300                 | 家中⾨鈴聲                                | **壓的鈴聲(不舒服), 叮~ 咚~(長短皆有), 電子音的叮~ 咚~, 燈等~, 電子音的燈等~, 噹~, 叮~, 咚~**, 學校鐘聲, 人聲在問what's up, 鈴聲可能被按多次，然後不規律, 咿喔咿喔, **醫院的燈等掛號聲**, 叫號碼的聲音, 玩具的音樂聲 |
| Bird               | 7     | 100   | 01301-01400                 | ⿃類的叫聲                                | **高音單調**, **啾啾啾, 啾~ 啾~ 啾~, 啾!啾!啾!**, 像吹口哨, 小鳥打架, 尖銳的音頻, 可能只會叫一下，但是聲音很高, **大多很短、急促、重複，再唱歌的才很長**                                                             |
| Music_Instrument   | 8     | 100   | 01401-01500                 | ⾳樂聲以及樂器聲                          | **鋼琴曲子, 鋼琴練習, 鋼琴彈錯, 鋼琴琴按下去的重音感, 鋼琴重複按鍵練習, 著名曲子**, 音樂盒, 混卓的音樂, 鬧鐘的音樂, 管樂器, 中斷的音樂, 音響放出的音樂, **音響的混濁音質聲, 音響的爆音, 數位音樂的音質粗糙**, 打擊樂 |
| Laugh_Shout_Scream | 9     | 100   | 01501-01600                 | ⼈類的笑聲、⼤叫聲以及尖叫聲              | 質疑的"阿"~, 撞到東西的"阿"~, 笑, 大笑, 鬼叫, 鬼吼, 對話, 看球隊進球的大叫, 看球隊沒進球的大叫, 懊悔的吼叫, 大叫(長), 大叫(短), 尖叫, 呵呵呵, 電視聲, **人聲重疊**, 歡呼, 哭泣, 怒吼, **都是英文的人聲**             |

---

## 資料夾結構

一個類別一個資料夾，音效檔案的名稱標記來源與序號，  
如s01-001.mp3，代表來源01的第一個音效檔案。

```{txt}
/crawl_voice
├─code
│ ├─check_folder_structure.ipynb
│ ├─crawler_source01.ipynb
│ └─func4crawl
└─data
  ├─category_0
  │ └─soo-xxxx.wav/soo-xxxx.mp3: 音效檔
  ├─category_1
  ├─...
  ├─category_9
  └─metadata
    ├─category_00.json
    └─category_00.csv
```

---

## END
