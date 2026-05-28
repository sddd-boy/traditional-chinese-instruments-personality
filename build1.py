# Build script for index.html - Part 1 of 4
# Writes the HTML/CSS/JS to index.html
import os

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

# ===== INSTRUMENT DATA =====
instruments_data = {
    'erhu': {'id':'erhu','img':'inst-erhu.png','name':'二胡','persona':'幽弦者','color':'#2c3e6b','colorLight':'#3d5a8a','traits':['敏感细腻','情深不寿','内敛深沉','善于倾听'],'description':'表面沉静如水，内心波涛汹涌。外人看你低调内敛，走近才发现你的情感世界丰富到令人心疼。你是深夜听歌会流泪的人，也是朋友最可靠的倾听者。你的力量不在张扬，而在那份不动声色的深情——如同二胡的两根弦，简简单单，却能奏出天地间最绵长的悲欢。','poetry_text':'白居易《琵琶行》虽写琵琶，但"弦弦掩抑声声思，似诉平生不得志"用在二胡上也极贴切。阿炳《二泉映月》——瞎子阿炳一生坎坷，将人世悲欢尽付两根琴弦，一曲之中有天地苍凉，也有不屈的风骨。','poetry_source':'','pieces':['《二泉映月》','《江河水》','《赛马》'],'figures':['李清照 — 深情婉约，晚景凄凉却风骨犹存','杜甫 — 心怀苍生，沉郁顿挫']},
    'pipa': {'id':'pipa','img':'inst-pipa.png','name':'琵琶','persona':'烈弦者','color':'#b5343a','colorLight':'#c94a50','traits':['敢爱敢恨','情绪饱满','热烈奔放','不藏不掖'],'description':'你像一杯烈酒，入口惊艳，让人难忘。你的人生大起大落都写在脸上，对朋友掏心掏肺，对生活全力以赴。敢爱敢恨是你的底色，永不平庸是你的宿命。如同琵琶自西域传入中原，你身上有一种文化交融的多元气质——热烈、丰富、永远出人意料。','poetry_text':'白居易《琵琶行》"大弦嘈嘈如急雨，小弦切切如私语。嘈嘈切切错杂弹，大珠小珠落玉盘。"——千古名篇，将琵琶的丰富表现力写到了极致。','poetry_source':'——白居易《琵琶行》','pieces':['《十面埋伏》','《霸王卸甲》','《春江花月夜》'],'figures':['李白 — 豪放不羁，诗酒趁年华','苏轼 — 大起大落，永远热爱生活']},
    'guqin': {'id':'guqin','img':'inst-guqin.png','name':'古琴','persona':'素弦者','color':'#576574','colorLight':'#6b7d8e','traits':['清雅通透','内心笃定','享受孤独','独立思考'],'description':'你是人群中的隐士，不争不抢，但所有人都尊重你的判断。你享受孤独，甚至需要孤独来充电。你的力量不在表面的热烈，而在内心的笃定——你知道自己要什么，也知道什么不值得。如同古琴七弦，素朴无华，却是君子修身养性之物，是士人精神的至高象征。','poetry_text':'伯牙子期《高山流水》——琴为知音而弹，知音既去，摔琴绝弦。古琴文化中最动人的就是这种"士为知己者死"的精神。《诗经》"窈窕淑女，琴瑟友之"，琴也是君子修养的象征。','poetry_source':'','pieces':['《高山流水》','《广陵散》','《平沙落雁》'],'figures':['陶渊明 — 归隐田园，不为五斗米折腰','嵇康 — 刑场上弹完《广陵散》，从容赴死']},
    'dizi': {'id':'dizi','img':'inst-dizi.png','name':'笛子','persona':'清风者','color':'#4a7c59','colorLight':'#5d9670','traits':['自由洒脱','浪漫气质','不喜束缚','随性而行'],'description':'你像一阵穿堂风，所到之处都是清爽。你不喜欢被束缚，无论是人际关系还是生活方式，你都需要足够的空间。你有一种天然的浪漫气质，别人眼里的"不靠谱"其实是你对世界的独特感知方式。如同笛声入春风，吹遍一座城——你的感染力不需要声嘶力竭，只需轻轻一吹。','poetry_text':'李白《春夜洛城闻笛》"谁家玉笛暗飞声，散入春风满洛城。此夜曲中闻折柳，何人不起故园情。"笛声入春风，吹遍一座城——这就是笛子的穿透力和感染力。','poetry_source':'——李白《春夜洛城闻笛》','pieces':['《姑苏行》','《鹧鸪飞》','《扬鞭催马运粮忙》'],'figures':['李白 — 一生好入名山游，千金散尽还复来','唐伯虎 — 别人笑我太疯癫，我笑他人看不穿']},
    'guzheng': {'id':'guzheng','img':'inst-guzheng.png','name':'古筝','persona':'玉弦者','color':'#8b8682','colorLight':'#a09b96','traits':['温润如玉','处世得体','外柔内刚','追求和谐'],'description':'你是那种"明明可以靠颜值，偏偏要靠实力"的人。你追求平衡与和谐，不喜欢极端和冲突。表面温柔好说话，其实内心有自己的底线和坚持。你是朋友圈里最让人舒服的存在，处世得体，润物无声。如同筝音清越悠远，如月照秋水，不争不抢却自有一种光芒。','poetry_text':'李端《听筝》"鸣筝金粟柱，素手玉房前。欲得周郎顾，时时误拂弦。"——用筝声引心上人注意，含蓄又狡黠，这种温柔的心机正是古筝人格的精髓。筝音清越悠远，如月照秋水，不争不抢却自有一种光芒。','poetry_source':'——李端《听筝》','pieces':['《渔舟唱晚》','《高山流水》','《战台风》'],'figures':['王昭君 — 柔中有刚，以一身系两国和平','上官婉儿 — 才冠巾帼，政坛风云']},
    'suona': {'id':'suona','img':'inst-suona.png','name':'唢呐','persona':'金声者','color':'#c4932a','colorLight':'#d4a840','traits':['热血热肠','不拘小节','感染力强','天生的聚光灯'],'description':'你天生就是人群的中心，聚会没有你就会少了很多乐趣。你的热情像唢呐的声音一样，穿透云霄，传到千里之外。你不记仇、不算计，对朋友永远热忱。你相信没有一顿烧烤解决不了的问题，如果有，就两顿。唢呐能高能低，能悲能喜——你就是那个永远在现场制造高潮的人。','poetry_text':'《宋史·五行志》记载"唢呐"来自波斯、龟兹一带，原是军乐之用，后传入民间。每一场乡村民间婚礼上，唢呐都是绝对主角——它是唯一一个能让全场人情不自禁起舞的中国乐器。','poetry_source':'','pieces':['《百鸟朝凤》','《抬花轿》','《喜庆》'],'figures':['鲁智深 — 倒拔垂杨柳，花和尚大闹野猪林','张飞 — 粗中有细，百万军中取上将首级']},
}

questions_data = [
    {'id':1,'text':'你最适合以下哪种生活状态？','type':'text','options':[
        {'label':'A','text':'在深夜的窗边听雨，独处，整理心情','scores':{'erhu':3,'guqin':2}},
        {'label':'B','text':'和朋友彻夜长谈，聊人生聊理想','scores':{'pipa':3,'suona':3}},
        {'label':'C','text':'独自一人背上行囊，去陌生的远方','scores':{'dizi':3,'guqin':2}},
        {'label':'D','text':'宅在家里，看书、做饭、逗猫，享受慢时光','scores':{'guzheng':3,'guqin':2}},
    ]},
    {'id':2,'text':'你在朋友眼里是一个什么样的人？','type':'text','options':[
        {'label':'A','text':'温柔体贴，总是能注意到别人的情绪','scores':{'guzheng':3,'erhu':2}},
        {'label':'B','text':'有趣有料，有你在就不会冷场','scores':{'suona':3,'pipa':2}},
        {'label':'C','text':'安静但有力量，关键时刻才显山露水','scores':{'erhu':3,'guqin':3}},
        {'label':'D','text':'洒脱不羁，永远活得自由而洒脱','scores':{'dizi':3,'pipa':2}},
    ]},
    {'id':3,'text':'你更喜欢什么样的音乐？','type':'text','options':[
        {'label':'A','text':'低回婉转的弦乐，能让人安静下来','scores':{'erhu':3,'guqin':3}},
        {'label':'B','text':'节奏感强，前奏一响就心动','scores':{'pipa':3,'suona':3}},
        {'label':'C','text':'空灵悠远的笛声，如同在山巅','scores':{'dizi':3,'guqin':2}},
        {'label':'D','text':'古朴淡雅的琴音，洗涤心灵','scores':{'guqin':3,'guzheng':2}},
    ]},
    {'id':4,'text':'以下哪种情境最让你心动？','type':'text','options':[
        {'label':'A','text':'夕阳下，一个人的散步，有琴声相伴','scores':{'guqin':3,'guzheng':2}},
        {'label':'B','text':'突然收到消息：今晚老朋友聚会，走起！','scores':{'suona':3,'pipa':2}},
        {'label':'C','text':'读到一句诗词，让自己沉默了半小时','scores':{'erhu':3,'guqin':2}},
        {'label':'D','text':'在博物馆看到一件古琴，驻足良久','scores':{'guqin':3,'dizi':2}},
    ]},
    {'id':5,'text':'你更向往什么样的情感？','type':'text','options':[
        {'label':'A','text':'细水长流，平平淡淡才是真','scores':{'guzheng':3,'erhu':2}},
        {'label':'B','text':'轰轰烈烈，哪怕遍体鳞伤也要爱过','scores':{'pipa':3,'suona':2}},
        {'label':'C','text':'心有灵犀，懂的人不言自明','scores':{'guqin':3,'erhu':2}},
        {'label':'D','text':'自由相处，爱时不黏，不爱时不欠','scores':{'dizi':3,'pipa':2}},
    ]},
    {'id':6,'text':'以下哪种描述最符合你？','type':'text','options':[
        {'label':'A','text':'不轻易求人，但帮起人来毫不含糊','scores':{'guqin':3,'dizi':2}},
        {'label':'B','text':'朋友圈发得不多，但每条都是精华','scores':{'erhu':3,'guzheng':2}},
        {'label':'C','text':'敢于表达，讨厌就是讨厌，喜欢就是喜欢','scores':{'pipa':3,'suona':2}},
        {'label':'D','text':'社交达人，认识不认识都能聊上十分钟','scores':{'suona':3,'dizi':2}},
    ]},
    {'id':7,'text':'面对压力时，你通常会？','type':'text','options':[
        {'label':'A','text':'写日记、听音乐，一个人消化','scores':{'erhu':3,'guqin':3}},
        {'label':'B','text':'找朋友出来聊天，喝点小酒','scores':{'pipa':3,'suona':3}},
        {'label':'C','text':'出去跑步或旅行，换个环境透口气','scores':{'dizi':3,'guqin':2}},
        {'label':'D','text':'做家务、做饭，用忙碌转移注意力','scores':{'guzheng':3,'erhu':2}},
    ]},
    {'id':8,'text':'以下哪种场合你最享受？','type':'text','options':[
        {'label':'A','text':'在窗边焚香弹琴，独自冥想','scores':{'guqin':3,'guzheng':2}},
        {'label':'B','text':'过年回老家，和亲戚们热热闹闹','scores':{'suona':3,'pipa':2}},
        {'label':'C','text':'在路边小馆独饮，看人间烟火','scores':{'erhu':3,'dizi':2}},
        {'label':'D','text':'和朋友咖啡馆闲聊，交换彼此的秘密','scores':{'pipa':3,'guzheng':2}},
    ]},
    {'id':9,'text':'听音乐时，你最在意的是什么？','type':'text','options':[
        {'label':'A','text':'旋律是否动听，能否触动内心','scores':{'erhu':3,'guqin':3}},
        {'label':'B','text':'节奏是否带感，能否跟着摇头','scores':{'pipa':3,'suona':3}},
        {'label':'C','text':'音色是否空灵，能否让人放空','scores':{'dizi':3,'guzheng':2}},
        {'label':'D','text':'意境是否深远，值得反复回味','scores':{'guqin':3,'guzheng':2}},
    ]},
    {'id':10,'text':'如果用一种乐器代表你，你会选？','type':'text','options':[
        {'label':'A','text':'二胡 —— 两根弦，演绎人间悲欢','scores':{'erhu':3}},
        {'label':'B','text':'琵琶 —— 文武双全，丰富多彩','scores':{'pipa':3}},
        {'label':'C','text':'古琴 —— 七弦之间，风雅无限','scores':{'guqin':3}},
        {'label':'D','text':'笛子 —— 悠扬自在，随性而为','scores':{'dizi':3}},
        {'label':'E','text':'古筝 —— 玉润清越，八方来人','scores':{'guzheng':3}},
        {'label':'F','text':'唢呐 —— 喜庆逼人，天地共鸣','scores':{'suona':3}},
    ]},
]

print('Data prepared. Instruments:', len(instruments_data))
print('Questions:', len(questions_data))

# Token HTML generator
def make_token(inst_id, delay):
    inst = instruments_data[inst_id]
    name = inst['name']
    persona = inst['persona']
    img = inst['img']
    return f'''<div class="token" data-inst="{inst_id}" style="transition-delay:{delay}s">
  <div class="token-card">
    <div class="token-front">
      <div class="token-front-img"><img src="{img}" alt="{name}"></div>
      <div class="token-front-label">
        <div class="token-front-name">{name}</div>
        <div class="token-front-tag">{persona}</div>
      </div>
    </div>
    <div class="token-back">
      <div class="token-back-icon"><img src="{img}" alt="{name}"></div>
      <div class="token-back-name">{name}</div>
      <div class="token-back-persona">{persona}</div>
      <div class="token-back-hint">移开鼠标查看正面</div>
    </div>
  </div>
</div>'''

tokens_html = '\n'.join(make_token(inst_id, i*0.1) for i, inst_id in enumerate(['erhu','pipa','guqin','dizi','guzheng','suona']))

# Questions HTML generator
def make_question(q):
    qid = q['id']
    text = q['text']
    opts = q['options']
    html = f'<div class="question-card" id="q{qid}">'
    html += f'<div class="question-text">{text}</div>'
    html += '<div class="options-list">'
    for i, opt in enumerate(opts):
        label = opt['label']
        opt_text = opt['text']
        scores = opt['scores']
        scores_json = str(scores).replace("'","").replace('"','')
        html += f'''<button class="option-btn" onclick="selectOption({qid},{i},{scores_json})">
          <span class="option-label">{label}</span>
          <span class="option-text">{opt_text}</span>
        </button>'''
    html += '</div></div>'
    return html

print('Token HTML generated, question generators ready')
print('DONE_PART1')