# -*- coding: utf-8 -*-
import codecs, os

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

with codecs.open(filepath, 'r', 'utf-8') as f:
    content = f.read()

idx = content.find('function getDescription(')
end_script = content.rfind('</script>')
print('Will replace chars', end_script - idx, 'from pos', idx, 'to', end_script)

new_js = '''function getDescription(id){var d={erhu:'表面沉静如水，内心波涛汹涌。外人看你低调内敛，走近才发现你的情感世界丰富到令人心疼。你是深夜听歌会流泪的人，也是朋友最可靠的倾听者。你的力量不在张扬，而在那份不动声色的深情——如同二胡的两根弦，简简单单，却能奏出天地间最绵长的悲欢。',pipa:'你像一杯烈酒，入口惊艳，让人难忘。你的人生大起大落都写在脸上，对朋友掏心掏肺，对生活全力以赴。敢爱敢恨是你的底色，永不平庸是你的宿命。如同琵琶自西域传入中原，你身上有一种文化交融的多元气质——热烈、丰富、永远出人意料。',guqin:'你是人群中的隐士，不争不抢，但所有人都尊重你的判断。你享受孤独，甚至需要孤独来充电。你的力量不在表面的热烈，而在内心的笃定——你知道自己要什么，也知道什么不值得。如同古琴七弦，素朴无华，却是君子修身养性之物，是士人精神的至高象征。',dizi:'你像一阵穿堂风，所到之处都是清爽。你不喜欢被束缚，无论是人际关系还是生活方式，你都需要足够的空间。你有一种天然的浪漫气质，别人眼里的不靠谱其实是你对世界的独特感知方式。如同笛声入春风，吹遍一座城——你的感染力不需要声嘶力竭，只需轻轻一吹。',guzheng:'你是那种明明可以靠颜值，偏偏要靠实力的人。你追求平衡与和谐，不喜欢极端和冲突。表面温柔好说话，其实内心有自己的底线和坚持。你是朋友圈里最让人舒服的存在，处世得体，润物无声。如同筝音清越悠远，如月照秋水，不争不抢却自有一种光芒。',suona:'你天生就是人群的中心，聚会没有你就会少了很多乐趣。你的热情像唢呐的声音一样，穿透云霄，传到千里之外。你不记仇、不算计，对朋友永远热忱。你相信没有一顿烧烤解决不了的问题，如果有，就两顿。唢呐能高能低，能悲能喜——你就是那个永远在现场制造高潮的人。'};return d[id]||''}

function getDetailTitle(id){var t={erhu:'幽弦者的真实画像',pipa:'烈弦者的真实画像',guqin:'素弦者的真实画像',dizi:'清风者的真实画像',guzheng:'玉弦者的真实画像',suona:'金声者的真实画像'};return t[id]||''}

function getDetailContent(id){var c={erhu:'你有一种天赋——能够感知常人感知不到的情绪波动。别人看见一杯水，你看见的是水面折射出的所有光线。这种敏感性是你的超能力，也是你偶尔的负担。你不喜欢解释自己，因为在你能用语言描述之前，情绪已经发生、流动、消退了。朋友找你倾诉不是因为你能给方案，而是因为你能「懂」。这种懂，有时候比任何解决方案都管用。你在深夜里和自己对话。那些独处的时间不是孤独，是必要的充电。你的内心戏足够拍一部电影，但你不打算让任何人买票进场。你有一种温柔的力量——不说教，不强迫，只是在那里。但需要你的时候，你会发现自己的肩膀意外地可靠。在情感上，你是慢热型，但一旦投入，是那种把整颗心都放进去的方式。代价是，伤害也会更深。所以你学会了给自己留一点点退路。不是不信任，是学会了如何不让自己碎掉。',pipa:'你的人生没有「中间档」。要么全情投入，要么冷眼旁观，没有第三种选择。这种极致让你活得很烈，也让周围的人时常感到被你的热情灼伤。你讨厌虚伪。哪怕是善意的谎言，你也需要时间消化。在一个充斥fake nice的世界里，你的直接有时候是缺点，但更多时候是魅力。你对朋友是那种「两肋插刀」的类型——朋友有难，你会比当事人还急。你的朋友圈不大，但每一个都是过命的交情。你谈恋爱也是轰轰烈烈的。宁可遍体鳞伤，也不愿意将就平淡。这种态度让你受过伤，但也让你体验到了更深层的情感深度。你不是没有柔软的时候。只是你的柔软只会留给真正懂你的人。在那之前，你的刺是用来保护自己的铠甲。',guqin:'你是那种让周围人感到安心的存在——不急不躁，不争不抢。你的笃定不是来自无知，而是来自看过很多之后的选择。你知道自己想要什么，也知道自己可以放弃什么。你的内心是一座孤岛，但不是与世隔绝的那种孤岛——是有桥但你决定不开的那种。你的独处不是为了逃避社交，而是你需要那个独处来维持内心的秩序感。在决策上，你是深思熟虑型。一旦决定，几乎不会改变。这种稳定性有时候被误解为固执，但只有你自己知道，这是经过多少内心的权衡才得出的结论。你对「知音」的定义比任何人都苛刻。泛泛之交一大批，能走进你世界的人寥寥无几。但是一旦被你认定为同类，那是一种不需要解释的默契。你有一种能力——在混乱的环境中保持核心不变。无论外面多么喧嚣，你内心始终有一块是自己的净土。这是你的力量，也是你与生俱来的使命。',dizi:'你是那种让人「相处起来很舒服」的存在——不压迫，不黏人，不计较。你的自由不是刻意追求的结果，而是你本性如此，就像水往低处流一样自然。你不喜欢被关系绑架，哪怕是你在乎的人。你需要独立呼吸的空间，这是你的底线也是你的边界。所以在别人眼里你可能有些「不靠谱」，但那是你的生存策略。你有一种独特的幽默感——不是那种精心计算的搞笑，而是那种不经意间说出的话，却戳中了所有的笑点。你的有趣是随性的，不是表演的。你对世界有自己的一套解读方式，常常与主流不同。别人觉得你特立独行，只有你自己知道这只是因为你不想活成别人期待的样子。你的浪漫是骨子里的，不是那种送花送礼物的方式，而是一种存在本身的调调。你在的地方，空气里似乎都有一点点不同。',guzheng:'你是那种让人「如沐春风」的存在——和你在一起久了，会忘记原来世界还有其他温度。你把不舒服咽下去，把舒服留给别人。这种能力是你的天赋，也是你隐藏的代价。你有一种圆润的智慧——不是那种锋芒毕露的聪明，而是那种让人挑不出毛病的周到。你知道什么话该说什么话不该说，你知道什么时候该进什么时候该退。在关系中，你是付出型。常常把别人的需求放在前面，但不要以为你没有自己的底线——你只是选择了不轻易展示。这份隐忍是你的美德，也可能是你的弱点。你追求和谐，但和谐不等于没有冲突——而是你懂得如何把冲突化解成更深的理解。你有一种把矛盾变成黏合剂的能力，这是一种被低估的天赋。你是有温度的，但没有温度焦虑。你不需要持续被认可才能感到安全，你有自己的节奏和韵律。这是让你能够在各种环境中都活得不错的基础。',suona:'你是那种一出现整个房间能量就改变的人。你的存在本身就是一种声明——「我在这里」，不需要任何人认证。你是天生的聚光灯，哪怕在角落里，你也能成为焦点。你对生活的态度是「活着就要尽兴」。烦恼是用来解决的，不是用来发酵的。问题来了你想办法，实在没办法就想下次怎么避免。你很少在同一个地方跌倒两次——不是因为谨慎，是因为你的生活节奏太快，没时间在坑里待着。你的友情是热烈的、真诚的、不计回报的。你对朋友的态度是「有事你说」，然后真的会倾尽所能去帮。这种义气是你身上最耀眼的光环，也是你吸引人的地方。你不是一个细腻的人，至少表面上不是。但不要被这个骗了——你的内心其实很敏感。只是你选择了用热烈来保护那份敏感，不让任何人看见你的软肋。你的魅力来自于你对结果的在乎——不是那种精致的在乎，而是那种「管它呢先玩了再说」的豁达。这种态度让你活得很洒脱，也让你的生活充满了故事。'};return c[id]||''}

function getPoetry(id){var p={erhu:'白居易《琵琶行》虽写琵琶，但"弦弦掩抑声声思，似诉平生不得志"用在二胡上也极贴切。阿炳《二泉映月》——瞎子阿炳一生坎坷，将人世悲欢尽付两根琴弦，一曲之中有天地苍凉，也有不屈的风骨。',pipa:'白居易《琵琶行》"大弦嘈嘈如急雨，小弦切切如私语。嘈嘈切切错杂弹，大珠小珠落玉盘。"——千古名篇，将琵琶的丰富表现力写到了极致。琵琶自西域传入中原，本身就是文化交融的象征，热烈而多元。',guqin:'伯牙子期《高山流水》——琴为知音而弹，知音既去，摔琴绝弦。古琴文化中最动人的就是这种"士为知己者死"的精神。《诗经》"窈窕淑女，琴瑟友之"，琴也是君子修养的象征。',dizi:'李白《春夜洛城闻笛》"谁家玉笛暗飞声，散入春风满洛城。此夜曲中闻折柳，何人不起故园情。"笛声入春风，吹遍一座城——这就是笛子的穿透力和感染力。',guzheng:'李端《听筝》"鸣筝金粟柱，素手玉房前。欲得周郎顾，时时误拂弦。"——用筝声引心上人注意，含蓄又狡黠，这种温柔的心机正是古筝人格的精髓。筝音清越悠远，如月照秋水，不争不抢却自有一种光芒。',suona:'《宋史·五行志》记载"唢呐"来自波斯、龟兹一带，原是军乐之用，后传入民间。每一场乡村民间婚礼上，唢呐都是绝对主角——它是唯一一个能让全场人情不自禁起舞的中国乐器。'};return p[id]||''}

function getPieces(id){var pcs={erhu:'<li>《二泉映月》</li><li>《江河水》</li><li>《赛马》</li>',pipa:'<li>《十面埋伏》</li><li>《霸王卸甲》</li><li>《春江花月夜》</li>',guqin:'<li>《高山流水》</li><li>《广陵散》</li><li>《平沙落雁》</li>',dizi:'<li>《姑苏行》</li><li>《鹧鸪飞》</li><li>《扬鞭催马运粮忙》</li>',guzheng:'<li>《渔舟唱晚》</li><li>《高山流水》</li><li>《战台风》</li>',suona:'<li>《百鸟朝凤》</li><li>《抬花轿》</li><li>《喜庆》</li>'};return pcs[id]||''}

function getFigures(id){var figs={erhu:'<li>李清照 — 深情婉约，晚景凄凉却风骨犹存</li><li>杜甫 — 心怀苍生，沉郁顿挫</li>',pipa:'<li>李白 — 豪放不羁，诗酒趁年华</li><li>苏轼 — 大起大落，永远热爱生活</li>',guqin:'<li>陶渊明 — 归隐田园，不为五斗米折腰</li><li>嵇康 — 刑场上弹完《广陵散》，从容赴死</li>',dizi:'<li>李白 — 一生好入名山游，千金散尽还复来</li><li>唐伯虎 — 别人笑我太疯癫，我笑他人看不穿</li>',guzheng:'<li>王昭君 — 柔中有刚，以一身系两国和平</li><li>上官婉儿 — 才冠巾帼，政坛风云</li>',suona:'<li>鲁智深 — 倒拔垂杨柳，花和尚大闹野猪林</li><li>张飞 — 粗中有细，百万军中取上将首级</li>'};return figs[id]||''}

function getTraits(id){var tr={erhu:'<span class="trait-tag">敏感细腻</span><span class="trait-tag">情深不寿</span><span class="trait-tag">内敛深沉</span><span class="trait-tag">善于倾听</span>',pipa:'<span class="trait-tag">敢爱敢恨</span><span class="trait-tag">情绪饱满</span><span class="trait-tag">热烈奔放</span><span class="trait-tag">不藏不掖</span>',guqin:'<span class="trait-tag">清雅通透</span><span class="trait-tag">内心笃定</span><span class="trait-tag">享受孤独</span><span class="trait-tag">独立思考</span>',dizi:'<span class="trait-tag">自由洒脱</span><span class="trait-tag">浪漫气质</span><span class="trait-tag">不喜束缚</span><span class="trait-tag">随性而行</span>',guzheng:'<span class="trait-tag">温润如玉</span><span class="trait-tag">处世得体</span><span class="trait-tag">外柔内刚</span><span class="trait-tag">追求和谐</span>',suona:'<span class="trait-tag">热血热肠</span><span class="trait-tag">不拘小节</span><span class="trait-tag">感染力强</span><span class="trait-tag">聚光灯</span>'};return tr[id]||''}

function getCompatibility(id){var compat={erhu:{best:'guqin',worst:'suona',bestName:'古琴',worstName:'唢呐',bestR:'古琴的知音意境与二胡的深情最是契合，一个懂沉默，一个善倾听，是最高级的陪伴。',worstR:'唢呐的热烈有时会让二胡感到喧闹，热闹是他们的，二胡只想一个人静静听风雨。'},pipa:{best:'suona',worst:'guqin',bestName:'唢呐',worstName:'古琴',bestR:'琵琶与唢呐都是热烈之人，聚会中彼此懂得制造高潮，互相成就全场最佳气氛。',worstR:'古琴太静了，琵琶的热情在古琴那里常常得到沉默回应，时间久了会觉得自己在独角戏。'},guqin:{best:'dizi',worst:'pipa',bestName:'笛子',worstName:'琵琶',bestR:'古琴与笛子都是隐士之音，山高水长，一个在山巅吹笛，一个在林间抚琴，精神上门当户对。',worstR:'琵琶需要被看见，古琴不需要被看见。两种截然不同的存在方式，相处久了会彼此消耗。'},dizi:{best:'guqin',worst:'guzheng',bestName:'古琴',worstName:'古筝',bestR:'笛子与古琴是精神贵族的组合，一个不羁，一个通透，彼此给予空间却不失默契。',worstR:'古筝的"好好相处"哲学有时会让追求自由的笛子感到窒息——太圆滑了，少了那股清风。'},guzheng:{best:'erhu',worst:'dizi',bestName:'二胡',worstName:'笛子',bestR:'古筝的温润与二胡的深情彼此欣赏，彼此给对方留余地，是最舒服的长久相处模式。',worstR:'笛子的自由散漫有时会让追求和谐的的古筝感到不安——他们需要可预期的关系节奏。'},suona:{best:'pipa',worst:'erhu',bestName:'琵琶',worstName:'二胡',bestR:'唢呐和琵琶都是不吝啬表达的人，热闹在一起时谁也不欠谁，是天生派对搭档。',worstR:'二胡需要安静和深度理解，唢呐需要观众和欢呼——需求错位，相处久了两边都委屈。'}};return compat[id]||{}}

var dimDefs=[{name:'内省深度',max:15,base:{erhu:10,guqin:8,guzheng:6,dizi:6,pipa:5,suona:3}},{name:'社交活跃',max:15,base:{suona:12,pipa:10,guzheng:7,dizi:5,erhu:4,guqin:3}},{name:'审美维度',max:15,base:{guqin:12,dizi:10,guzheng:8,erhu:6,pipa:5,suona:3}},{name:'情感浓度',max:15,base:{erhu:12,pipa:10,guzheng:7,suona:6,guqin:5,dizi:3}},{name:'自由倾向',max:15,base:{dizi:12,guqin:10,pipa:7,suona:6,guzheng:4,erhu:3}},{name:'笃定程度',max:15,base:{guqin:12,guzheng:10,erhu:8,pipa:6,suona:4,dizi:3}}];

function getPercentBars(winId){
  var bars='';
  dimDefs.forEach(function(d){
    var val=d.base[winId]||0;
    var pct=Math.round(val/d.max*100);
    bars+='<div class="percent-row"><div class="percent-label">'+d.name+'</div><div class="percent-bar-track"><div class="percent-bar-fill" style="width:'+pct+'%;background:'+instruments[winId].color+'"></div></div><div class="percent-value">'+pct+'%</div></div>';
  });
  return'<div class="percent-chart">'+bars+'</div>';
}

function getHexChart(winId){
  var n=dimDefs.length,R=90,cx=140,cy=130;
  var points=dimDefs.map(function(d,i){
    var val=d.base[winId]||0;
    var ratio=Math.min(val/d.max,1);
    var angle=Math.PI*2*i/n-Math.PI/2;
    return{cx:cx+R*ratio*Math.cos(angle),cy:cy+R*ratio*Math.sin(angle),label:d.name,val:val,max:d.max};
  });
  var axisLines=points.map(function(p,i){
    var angle=Math.PI*2*i/n-Math.PI/2;
    return'<line x1="'+cx+'" y1="'+cy+'" x2="'+(cx+95*Math.cos(angle))+'" y2="'+(cy+95*Math.sin(angle))+'" stroke="#d8d0c0" stroke-width="1"/>';
  }).join('');
  var gridRings=[0.33,0.67,1];
  var gridLines=gridRings.map(function(r){
    var pts=[];
    for(var i=0;i<n;i++){
      var angle=Math.PI*2*i/n-Math.PI/2;
      pts.push((cx+r*R*Math.cos(angle))+','+(cy+r*R*Math.sin(angle)));
    }
    return'<polygon points="'+pts.join(' ')+'" fill="none" stroke="#e0d8c8" stroke-width="0.5" opacity="0.6"/>';
  }).join('');
  var polyFillPts=points.map(function(p){return p.cx+','+p.cy}).join(' ');
  var polyFill='<polygon points="'+polyFillPts+'" fill="rgba(184,147,74,0.18)" stroke="#b8934a" stroke-width="1.5"/>';
  var labels=points.map(function(p,i){
    var angle=Math.PI*2*i/n-Math.PI/2;
    var lx=cx+(108)*Math.cos(angle),ly=cy+(108)*Math.sin(angle);
    var pct=Math.round(p.val/p.max*100);
    return'<text class="hex-label" x="'+lx+'" y="'+ly+'" dy="0.3em">'+p.label+'</text><text class="hex-score-label" x="'+lx+'" y="'+(ly+14)+'">'+pct+'%</text>';
  }).join('');
  return'<div class="hexagon-chart-wrap"><svg viewBox="0 0 280 260" style="overflow:visible">'+gridLines+axisLines+polyFill+labels+'</svg></div>';
}

function getCompatSection(winId){
  var c=getCompatibility(winId);
  return'<div class="compat-section"><div class="result-section-title">乐见知音</div><div class="compat-grid"><div class="compat-card compat-best"><div class="compat-badge">最合拍</div><div class="compat-instrument">'+c.bestName+'</div><div class="compat-reason">'+c.bestR+'</div></div><div class="compat-card compat-worst"><div class="compat-badge">需注意</div><div class="compat-instrument">'+c.worstName+'</div><div class="compat-reason">'+c.worstR+'</div></div></div></div>';
}

function showResult(){var maxScore=0,winner='erhu';Object.keys(scores).forEach(function(inst){if(scores[inst]>maxScore){maxScore=scores[inst];winner=inst}});var inst=instruments[winner];var total=Object.values(scores).reduce(function(a,b){return a+b},0);var html='<div class="result-container"><div class="result-card"><div class="result-header" data-inst="'+inst.id+'"><div class="result-instrument-icon"><img src="'+inst.img+'" alt="'+inst.name+'"></div><div class="result-instrument-name">'+inst.name+'</div><div class="result-persona-title">'+inst.persona+'</div></div><div class="result-body"><div class="result-section"><div class="result-section-title">'+getDetailTitle(winner)+'</div><p>'+getDetailContent(winner)+'</p></div><div class="result-section"><div class="result-section-title">古韵诗词</div><p>'+getPoetry(winner)+'</p></div><div class="result-section"><div class="result-section-title">代表曲目</div><ul>'+getPieces(winner)+'</ul></div><div class="result-section"><div class="result-section-title">性格雷达</div><div class="hexagon-section">'+getHexChart(winner)+'</div><div style="margin-top:16px">'+getPercentBars(winner)+'</div></div><div class="result-section"><div class="result-section-title">知音古人</div><ul>'+getFigures(winner)+'</ul></div><div class="result-section"><div class="result-section-title">性格标签</div><div class="result-traits">'+getTraits(winner)+'</div></div>'+getCompatSection(winner)+'<div class="result-actions"><button class="btn-retry" onclick="retry()">重新测试</button><button class="btn-share" onclick="share()">分享结果</button></div></div></div></div>';document.getElementById('resultArea').innerHTML=html;document.body.classList.remove('on-home');showPage('result')}

function retry(){scores={erhu:0,pipa:0,guqin:0,dizi:0,guzheng:0,suona:0};currentQ=0;showPage('home');document.body.classList.add('on-home')}
function share(){var winId=Object.keys(scores).reduce(function(a,b){return scores[a]>scores[b]?a:b});var instName=instruments[winId].name;var text='我在弦外之音测试中是【'+instName+'】，快来测测你是哪种乐器吧！';if(navigator.share){navigator.share({title:'弦外之音',text:text})}else{navigator.clipboard.writeText(text).then(function(){alert('结果已复制到剪贴板！')})}}
document.addEventListener('DOMContentLoaded',function(){document.body.classList.add('on-home');setTimeout(function(){document.querySelectorAll('.token').forEach(function(t){t.classList.add('visible')})},300)});
'''

new_content = content[:idx] + new_js

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(new_content)

print('Done. New size:', len(new_content))