# README

更新時間: 2021-07-25

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

- [範例聲音觀察](./範例聲音觀察.md)
- [query keyword](./query-keyword.md)

--

**音效庫資料來源:**

- source 01: [BBC Rewind - Sound Effects](https://sound-effects.bbcrewind.co.uk/)
- source 02: [Download Free Sound Effects & Royalty Free Music | ZapSplat](https://www.zapsplat.com/)

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

---

## TO DO LIST

- [Other Sound Effect Libraries](./Other-Sound-Effect-Libraries.md)
