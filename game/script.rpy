# 游戏的脚本可置于此文件中。
# このファイルにゲームのスクリプトを記述できます。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
# このゲームで使用するキャラクターを宣言します。colorパラメーターでキャラクター名に色をつけられます。

define n = Character(None, kind=nvl)
define aa_flash = Fade(0.05, 0.0, 0.12, color="#ffffff")


# 游戏在此开始。
# ゲームはここから始まります。
label splashscreen:
    jump start
label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。
    # 背景を表示します。デフォルトではプレースホルダー画像が表示されますが、
    # 画像ディレクトリにファイル（bg room.png または bg room.jpg）を追加することでも表示できます。
    $ quick_menu = True
    scene bg_kaiwa
    with fade
    pause 0.5
    play music "<silence 0.2>"
    queue music "intro.mp3"
    # 此处显示各行对话。
    # ここに各行の台詞を記述します。
    n "{cps=30}食堂で二人が座っている。{/cps}"
    n "{cps=30}「今日の飯、{/cps}"
    extend "{cps=30}悪くなかっただろ？」 {/cps}"
    extend "{cps=30}大沢ぴいは、親友のコノハに問いかけた。{/cps}"
    
    window hide
    # 等待玩家第二次点击（用于查看背景）
    # プレイヤーの2回目のクリックを待ちます（背景を確認するため）
    pause
    # 玩家点击后恢复对话框并继续下一句
    # クリック後にダイアログを再表示して次の台詞に進みます
    window show

    n "{cps=30}......{/cps}"

    nvl clear
    
    n "{cps=30}大沢ぴいは居心地わるかった，{/cps}"
    extend"{cps=30}向かいのコノハはおそらく察している。{/cps}"
    n "{cps=30}コノハは動揺していた，{/cps}"
    extend "{cps=30}向かいの大沢ぴいもおそらく気づいている。{/cps}"
    n "{cps=30}ふたりとも、オトナなんだから。{/cps}"

    nvl clear

    window hide
    scene bg_shokudou
    with fade
    n "{cps=30}「まあな」 {/cps}"
    extend "{cps=30}コノハはそっけなく、しかし苛立ちを隠さずに答えた。{/cps}"
    extend "{cps=30}首の斜め上にある顔を、指でつついた。{/cps}"
    nvl clear
    n "{cps=30}「親知らず、飯食うのは大丈夫なの？」 {/cps}"
    n "{cps=30}大沢ぴいは他人を気遣うのが好きだ。{/cps}"
    n "{cps=30}「......こっち、腫れてるように見えるのか？」{/cps}"
    extend "{cps=30} コノハは指をわざと力を込めて突いた。{/cps}"
    n "{cps=30}コノハは今日は他人の気遣いを拒むのだ。{/cps}"
    n "{cps=30}「ないな。」{/cps}"
    n "{cps=30}「......」{/cps}"
    n "{cps=30}「............」{/cps}"
    stop music fadeout 3.0
    n "{cps=30}雰囲気が冷たくなった。{/cps}"
    n "{cps=30}二人は沈黙したまま、食事を続けた。{/cps}"

    nvl clear
    n "{cps=30}食事が終わった。{/cps}"
    n "{cps=30}皿が持ち上げられた。{/cps}" 
    n "{cps=30}十秒後、{/cps}"
    stop music fadeout 1.0
    play sound "放尿.wav"
    extend "{cps=30}二つの皿がざぶんと洗い場に落ちた。{/cps}"
    
    window hide
    scene black
    with fade

    # 清除 NVL 缓冲，下一句将作为全新一页显示
    # NVLバッファをクリアし、次の台詞を新しいページとして表示します
    nvl clear
    centered "{cps=10}{size=40}私、見てしまいました。{/size}{/cps}"

    play music "悪夢への彷徨.mp3"
    window hide
    scene bg_exit
    with fade
    n "{cps=30}大沢ぴいが食堂のホールを曲がると、冴えない身なりのインターナショナル学生さん（インセイ？）が、{/cps}"
    extend "{cps=30}通路の洗面台に腰をかがめて突っ伏しているのが目に入った。 {/cps}"

    scene bg_sink with fade

    nvl clear
    n "{cps=30}インセイは、{/cps}"
    extend "{cps=30}まるで水を飲むかのように、{/cps}"
    extend "{cps=30}蛇口から出る水を口に含んでいた。{/cps}"
    
    n "{cps=30}大沢ぴいは反対側の蛇口へ歩み寄り、ハンドルをひねる。{/cps}"
    extend "{cps=30}壊れることのない日常、その断片を使わせてもらおうとしたのだ......{/cps}"
    
    window hide
    scene black
    with fade
    centered "{cps=10}{size=40}だが、{/size}{/cps}"
    stop music fadeout 1.0
    extend "{cps=5}{size=30}水は{/size}{size=20}出な{/size}{size=10}かった{/size}{/cps}"
    
    play music "audio/シュレディンガー.mp3"
    nvl clear
    window hide
    scene bg_sink with fade
    with fade

    n "{cps=30}もう一方の蛇口に目を向け、{/cps}"
    extend "{cps=30}先ほどのチャイナ男の{color=#f00}殘留思念{/color}があった。{/cps}"
    scene black with aa_flash
    centered "{cps=0}{size=30}{color=#f00}「オレは忙しいんだ、デートなんだ。」{/color}{/cps}"
    scene bg_sink with aa_flash
    nvl clear
    n "{cps=30}と。{/cps}"
    n ""

    n "{cps=30}でも、さっき見えたばかりなのに！{/cps}"
    extend "{cps=30}わずか五秒前、その男が{/cps}"
    extend "{cps=10}日常的な水で{/cps}"
    extend "{cps=30}濡れた手で、跳ねた髪を撫でつけたのに！！{/cps}"

    # 在这里也想清除之前的 NVL 内容、单独显示下一句时，再调用 nvl clear
    # ここでも以前のNVL内容をクリアして次の台詞を単独表示したい場合、nvl clearを再度呼び出します
    nvl clear
    window hide
    scene black
    with fade
    centered "{cps=30}{size=30}NICHIJOUという名のメインストーリーに疲れ果てた大沢ぴいは{/size}{/cps}"
    centered "{cps=30}{size=30}そろそろ「次へ」のボタンを押してしまいたいと願うんだ{/size}{/cps}"
    window hide
    scene bg_sink
    with fade
    n "{cps=30}材質が違うのか、あるいはレンダリングの失敗か。{/cps}"
    n "{cps=30}目の前の蛇口は、脳内のアセットライブラリにある姿とは異なっている。{/cps}"
    n "{cps=30}鏡面反射するはずの蛇口の表面に、自分の顔を映し出すことはできなかった。 {/cps}"
    n "{cps=30}なんという非常識だ！{/cps}"
    nvl clear
    n "{cps=30}「蛇口は二つ。一つは水が出ない。ならもう一方は……{/cps}"
    extend "{cps=30}ニマイナスイチイコール一……」{/cps}"
    extend "{cps=30}頭はまだ算数の問題を処理している最中だというのに、体はすでに横へずれて隣の蛇口の前に立っていた。{/cps}"
    stop music fadeout 1.0
    n "{cps=30}迷いなくハンドルを回す。{/cps}"
    play audio "kaze.wav"
    n"{cps=30}昼食の汚れを鮮やかに、そしていさぎよく洗い流した。{/cps}"

    nvl clear
    
    window hide
    scene bg_exit
    with fade
    n "{cps=30}大沢ぴいは満足げに踵を返し、洗面台を後にした。{/cps}"

    window hide
    scene black
    with fade

    play music "Industrual Street.wav"
    centered "{cps=30}{size=30}また、{/size}{/cps}{nw=0.8}"
    extend "{cps=10}{size=30}日常の軌道に{/size}{/cps}{nw=0.8}"
    extend "{cps=30}{size=30}戻ったと感じている。{/size}{/cps}"
    centered "{cps=5}{size=30}One NICHIJOU after another.{/size}{/cps}"
    stop music fadeout 2.0

    window hide
    scene black
    with fade
    pause 0.5
    python:
        renpy.quit()