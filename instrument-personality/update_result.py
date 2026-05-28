# -*- coding: utf-8 -*-
import codecs

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

with codecs.open(filepath, 'r', 'utf-8') as f:
    c = f.read()

# 1. Replace old showResult with new enhanced version
sr_start = c.find("function showResult(){var maxScore=0,winner='erhu'")
sr_end = c.find("function getDescription(")
old_showresult = c[sr_start:sr_end]

new_showresult = """function showResult(){var maxScore=0,winner='erhu';Object.keys(scores).forEach(function(inst){if(scores[inst]>maxScore){maxScore=scores[inst];winner=inst}});var inst=instruments[winner];var total=Object.values(scores).reduce(function(a,b){return a+b},0);var html='<div class="result-container"><div class="result-card"><div class="result-header" data-inst="'+inst.id+'"><div class="result-instrument-icon"><img src="'+inst.img+'" alt="'+inst.name+'"></div><div class="result-instrument-name">'+inst.name+'</div><div class="result-persona-title">'+inst.persona+'</div></div><div class="result-body"><div class="result-section"><div class="result-section-title">'+getDetailTitle(winner)+'</div><p>'+getDetailContent(winner)+'</p></div><div class="result-section"><div class="result-section-title">古韵诗词</div><p>'+getPoetry(winner)+'</p></div><div class="result-section"><div class="result-section-title">代表曲目</div><ul>'+getPieces(winner)+'</ul></div><div class="result-section"><div class="result-section-title">性格雷达</div>'+getHexChart(winner)+'<div style="margin-top:16px">'+getPercentBars(winner)+'</div></div><div class="result-section"><div class="result-section-title">知音古人</div><ul>'+getFigures(winner)+'</ul></div><div class="result-section"><div class="result-section-title">性格标签</div><div class="result-traits">'+getTraits(winner)+'</div></div>'+getCompatSection(winner)+'<div class="result-actions"><button class="btn-retry" onclick="retry()">重新测试</button><button class="btn-share" onclick="share()">分享结果</button></div></div></div></div>';document.getElementById('resultArea').innerHTML=html;document.body.classList.remove('on-home');showPage('result')}

"""

c = c[:sr_start] + new_showresult + c[sr_end:]
print('showResult replaced')

# 2. Replace getDescription with new detailed functions
gd_start = c.find("function getDescription(")
# Find the old function's end - it returns d[id]
gd_end = gd_start
while True:
    idx = c.find("return d[id]", gd_end)
    if idx == -1:
        gd_end = c.find("function getPoetry(")
        break
    gd_end = idx + len("return d[id]")
    break

# Actually let me find getPoetry directly
gp = c.find("function getPoetry(")
print('getDescription:', gd_start, '->', gp, '(old len:', gp - gd_start, ')')

old_gd = c[gd_start:gp]
new_gd = """function getDetailTitle(id){var t={erhu:'幽弦者的真实画像',pipa:'烈弦者的真实画像',guqin:'素弦者的真实画像',dizi:'清风者的真实画像',guzheng:'玉弦者的真实画像',suona:'金声者的真实画像'};return t[id]||''}

function getDetailContent(id){var c={erhu:'你有一种天赋——能够感知常人感知不到的情绪波动。别人看见一杯水，你看见的是水面折射出的所有光线。这种敏感性是你的超能力，也是你偶尔的负担。你不喜欢解释自己，因为在你能用语言描述之前，情绪已经发生、流动、消退了。朋友找你倾诉不是因为你能给方案，而是因为你能「懂」。这种懂，有时候比任何解决方案都管用。你在深夜里和自己对话。那些独处的时间不是孤独，是必要的充电。你的内心戏足够拍一部电影，但你不打算让任何人买票进场。你有一种温柔的力量——不说教，不强迫，只是在那里。但需要你的时候，你会发现自己的肩膀意外地可靠。在情感上，你是慢热型，但一旦投入，是那种把整颗心都放进去的方式。代价是，伤害也会更深。所以你学会了给自己留一点点退路。不是不信任，是学会了如何不让自己碎掉。',pipa:'你的人生没有「中间档」。要么全情投入，要么冷眼旁观，没有第三种选择。这种极致让你活得很烈，也让周围的人时常感到被你的热情灼伤。你讨厌虚伪。哪怕是善意的谎言，你也需要时间消化。在一个充斥fake nice的世界里，你的直接有时候是缺点，但更多时候是魅力。你对朋友是那种「两肋插刀」的类型——朋友有难，你会比当事人还急。你的朋友圈不大，但每一个都是过命的交情。你谈恋爱也是轰轰烈烈的。宁可遍体鳞伤，也不愿意将就平淡。这种态度让你受过伤，但也让你体验到了更深层的情感深度。你不是没有柔软的时候。只是你的柔软只会留给真正懂你的人。在那之前，你的刺是用来保护自己的铠甲。',guqin:'你是那种让周围人感到安心的存在——不急不躁，不争不抢。你的笃定不是来自无知，而是来自看过很多之后的选择。你知道自己想要什么，也知道自己可以放弃什么。你的内心是一座孤岛，但不是与世隔绝的那种孤岛——是有桥但你决定不开的那种。你的独处不是为了逃避社交，而是你需要那个独处来维持内心的秩序感。在决策上，你是深思熟虑型。一旦决定，几乎不会改变。这种稳定性有时候被误解为固执，但只有你自己知道，这是经过多少内心的权衡才得出的结论。你对「知音」的定义比任何人都苛刻。泛泛之交一大批，能走进你世界的人寥寥无几。但是一旦被你认定为同类，那是一种不需要解释的默契。你有一种能力——在混乱的环境中保持核心不变。无论外面多么喧嚣，你内心始终有一块是自己的净土。这是你的力量，也是你与生俱来的使命。',dizi:'你是那种让人「相处起来很舒服」的存在——不压迫，不黏人，不计较。你的自由不是刻意追求的结果，而是你本性如此，就像水往低处流一样自然。你不喜欢被关系绑架，哪怕是你在乎的人。你需要独立呼吸的空间，这是你的底线也是你的边界。所以在别人眼里你可能有些「不靠谱」，但那是你的生存策略。你有一种独特的幽默感——不是那种精心计算的搞笑，而是那种不经意间说出的话，却戳中了所有的笑点。你的有趣是随性的，不是表演的。你对世界有自己的一套解读方式，常常与主流不同。别人觉得你特立独行，只有你自己知道这只是因为你不想活成别人期待的样子。你的浪漫是骨子里的，不是那种送花送礼物的方式，而是一种存在本身的调调。你在的地方，空气里似乎都有一点点不同。',guzheng:'你是那种让人「如沐春风」的存在——和你在一起久了，会忘记原来世界还有其他温度。你把不舒服咽下去，把舒服留给别人。这种能力是你的天赋，也是你隐藏的代价。你有一种圆润的智慧——不是那种锋芒毕露的聪明，而是那种让人挑不出毛病的周到。你知道什么话该说什么话不该说，你知道什么时候该进什么时候该退。在关系中，你是付出型。常常把别人的需求放在前面，但不要以为你没有自己的底线——你只是选择了不轻易展示。这份隐忍是你的美德，也可能是你的弱点。你追求和谐，但和谐不等于没有冲突——而是你懂得如何把冲突化解成更深的理解。你有一种把矛盾变成黏合剂的能力，这是一种被低估的天赋。你是有温度的，但没有温度焦虑。你不需要持续被认可才能感到安全，你有自己的节奏和韵律。这是让你能够在各种环境中都活得不错的基础。',suona:'你是那种一出现整个房间能量就改变的人。你的存在本身就是一种声明——「我在这里」，不需要任何人认证。你是天生的聚光灯，哪怕在角落里，你也能成为焦点。你对生活的态度是「活着就要尽兴」。烦恼是用来解决的，不是用来发酵的。问题来了你想办法，实在没办法就想下次怎么避免。你很少在同一个地方跌倒两次——不是因为谨慎，是因为你的生活节奏太快，没时间在坑里待着。你的友情是热烈的、真诚的、不计回报的。你对朋友的态度是「有事你说」，然后真的会倾尽所能去帮。这种义气是你身上最耀眼的光环，也是你吸引人的地方。你不是一个细腻的人，至少表面上不是。但不要被这个骗了——你的内心其实很敏感。只是你选择了用热烈来保护那份敏感，不让任何人看见你的软肋。你的魅力来自于你对结果的在乎——不是那种精致的在乎，而是那种「管它呢先玩了再说」的豁达。这种态度让你活得很洒脱，也让你的生活充满了故事。'};return c[id]||''}

"""

c = c[:gd_start] + new_gd + c[gp:]
print('getDescription replaced with getDetailTitle+getDetailContent')

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(c)

print('Done. Size:', len(c))
print('has showResult:', 'function showResult()' in c)
print('has getDetailTitle:', 'function getDetailTitle' in c)
print('has getDetailContent:', 'function getDetailContent' in c)
print('has getHexChart:', 'function getHexChart' in c)
print('has getCompatSection:', 'function getCompatSection' in c)
print('has getPercentBars:', 'function getPercentBars' in c)