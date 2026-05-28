# Complete HTML rewrite
import os

html_parts = []

# Part 1: HTML head and CSS
part1 = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>弦外之音 · 中华传统乐器人格测试</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700;900&family=ZCOOL+XiaoWei&display=swap" rel="stylesheet">
<style>
:root {
  --paper: #f7f3eb; --paper-dark: #ede6d8; --ink: #2c2416; --ink-light: #5c5240;
  --ink-faint: #8a8070; --red-seal: #c23a2b; --gold: #b8934a; --gold-light: #d4af6b;
  --border: #7a5a32; --token-bg: #f5edd8;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { font-family: 'Noto Serif SC', 'SimSun', 'STSong', serif; background: var(--paper); color: var(--ink); min-height: 100vh; overflow-x: hidden; line-height: 1.8; }
.ink-bg { position: fixed; inset: 0; z-index: -1; pointer-events: none; overflow: hidden; }
.home-bg { position: fixed; inset: 0; z-index: -2; background-image: url('bg-home.png'); background-size: cover; background-position: center; background-repeat: no-repeat; transition: opacity 0.5s; }
body:not(.on-home) .home-bg { opacity: 0; pointer-events: none; }
.ink-blob { position: absolute; border-radius: 50%; filter: blur(80px); opacity: 0.06; animation: inkDrift 20s ease-in-out infinite; }
.ink-blob:nth-child(1) { width: 600px; height: 400px; background: #2c2416; top: -10%; left: -10%; animation-delay: 0s; }
.ink-blob:nth-child(2) { width: 500px; height: 350px; background: #5c4a3a; bottom: -15%; right: -8%; animation-delay: -7s; }
.ink-blob:nth-child(3) { width: 400px; height: 500px; background: #3a2c1e; top: 40%; left: 50%; animation-delay: -14s; }
.ink-blob:nth-child(4) { width: 300px; height: 300px; background: #c23a2b; top: 20%; right: 20%; opacity: 0.03; animation-delay: -3s; }
.ink-blob:nth-child(5) { width: 450px; height: 300px; background: #4a7c59; bottom: 30%; left: 15%; opacity: 0.04; animation-delay: -10s; }
@keyframes inkDrift { 0%, 100% { transform: translate(0, 0) scale(1); } 25% { transform: translate(30px, -20px) scale(1.08); } 50% { transform: translate(-15px, 25px) scale(0.94); } 75% { transform: translate(20px, 10px) scale(1.05); } }
.paper-texture { position: fixed; inset: 0; z-index: -1; pointer-events: none; opacity: 0.4; background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(139,119,90,0.03) 2px, rgba(139,119,90,0.03) 4px), repeating-linear-gradient(90deg, transparent, transparent 3px, rgba(139,119,90,0.02) 3px, rgba(139,119,90,0.02) 6px); }
.app-container { max-width: 960px; margin: 0 auto; padding: 24px 20px 60px; min-height: 100vh; display: flex; flex-direction: column; }
.page { display: none; flex: 1; }
.page.active { display: block; animation: fadeSlideIn 0.6s ease-out; }
@keyframes fadeSlideIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
#page-home .hero { background: rgba(245,237,216,0.78); border-radius: 16px; padding: 40px 24px 20px; text-align: center; }
.hero-seal { display: inline-block; width: 64px; height: 64px; border: 3px solid var(--red-seal); color: var(--red-seal); font-family: 'ZCOOL XiaoWei', serif; font-size: 28px; line-height: 58px; transform: rotate(-5deg); margin-bottom: 28px; opacity: 0; animation: sealAppear 1s ease-out 0.2s forwards; }
@keyframes sealAppear { from { opacity: 0; transform: rotate(-5deg) scale(2); } to { opacity: 0.85; transform: rotate(-5deg) scale(1); } }
.hero-title { font-family: 'ZCOOL XiaoWei', serif; font-size: clamp(36px, 6vw, 56px); font-weight: 900; letter-spacing: 0.15em; color: var(--ink); margin-bottom: 12px; opacity: 0; animation: fadeSlideIn 0.8s ease-out 0.4s forwards; }
.hero-subtitle { font-size: 16px; color: var(--ink-light); letter-spacing: 0.08em; opacity: 0; animation: fadeSlideIn 0.8s ease-out 0.6s forwards; }
.pattern-divider { width: 100%; height: 24px; background: repeating-linear-gradient(90deg, transparent 0px, transparent 8px, var(--ink-faint) 8px, var(--ink-faint) 10px, transparent 10px, transparent 16px, var(--ink-faint) 16px, var(--ink-faint) 18px, transparent 18px, transparent 24px); opacity: 0.25; margin: 32px 0; background-color: rgba(247,243,235,0.6); }
.tokens-section { padding: 30px 0 20px; }
#page-home .tokens-section { background: rgba(245,237,216,0.65); padding: 30px 16px 20px; }
.tokens-grid { display: flex; justify-content: center; gap: clamp(10px, 2vw, 20px); flex-wrap: wrap; }
.token { width: clamp(130px, 18vw, 170px); height: clamp(200px, 28vw, 260px); perspective: 800px; cursor: pointer; display: block; opacity: 0; transform: translateY(30px); transition: opacity 0.5s, transform 0.5s; }
.token.visible { opacity: 1; transform: translateY(0); }
.token-card { width: 100%; height: 100%; position: relative; transform-style: preserve-3d; transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1); }
.token:hover .token-card { transform: rotateY(180deg); }
.token-front, .token-back { position: absolute; inset: 0; backface-visibility: hidden; -webkit-backface-visibility: hidden; border-radius: 12px; overflow: hidden; border: 2px solid var(--border); box-shadow: 0 4px 12px rgba(44,36,22,0.12); }
.token-front { background: var(--token-bg); display: flex; flex-direction: column; }
.token-front-img { flex: 1; overflow: hidden; display: flex; align-items: center; justify-content: center; padding: 8px; }
.token-front-img img { width: 100%; height: 100%; object-fit: contain; }
.token-front-label { padding: 10px 8px 8px; text-align: center; background: linear-gradient(to bottom, rgba(245,237,216,0), rgba(245,237,216,0.95)); }
.token-front-name { font-family: 'ZCOOL XiaoWei', serif; font-size: clamp(18px, 2.5vw, 22px); font-weight: 700; color: var(--ink); letter-spacing: 0.12em; }
.token-front-tag { font-size: 11px; color: var(--ink-faint); letter-spacing: 0.06em; margin-top: 2px; }
.token-back { background: var(--token-bg); transform: rotateY(180deg); display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 16px; }
.token-back-icon { width: clamp(56px, 7vw, 70px); height: clamp(56px, 7vw, 70px); margin-bottom: 16px; border-radius: 50%; border: 2px solid var(--border); overflow: hidden; display: flex; align-items: center; justify-content: center; }
.token-back-icon img { width: 100%; height: 100%; object-fit: cover; }
.token-back-name { font-family: 'ZCOOL XiaoWei', serif; font-size: clamp(24px, 3.5vw, 32px); font-weight: 700; color: var(--ink); letter-spacing: 0.15em; }
.token-back-persona { font-size: clamp(14px, 1.8vw, 16px); color: var(--ink-light); margin-top: 8px; letter-spacing: 0.08em; }
.token-back-hint { font-size: 11px; color: var(--ink-faint); margin-top: 20px; letter-spacing: 0.05em; }
#page-home .intro-quote { background: rgba(245,237,216,0.7); padding: 24px 20px; }
.intro-quote { text-align: center; padding: 24px 20px; font-size: 15px; color: var(--ink-light); letter-spacing: 0.05em; line-height: 2; position: relative; }
.intro-quote::before, .intro-quote::after { content: ''; display: block; width: 40px; height: 2px; background: var(--ink-faint); margin: 16px auto; opacity: 0.3; }
#page-home .btn-start-wrapper { background: rgba(245,237,216,0.6); padding: 10px 0 40px; }
.btn-start-wrapper { text-align: center; padding: 10px 0 40px; }
.btn-start { display: inline-block; padding: 16px 48px; font-family: 'ZCOOL XiaoWei', serif; font-size: 20px; font-weight: 700; letter-spacing: 0.1em; color: var(--paper); background: linear-gradient(135deg, #3d2e1e, #5a4232); border: none; border-radius: 40px; cursor: pointer; position: relative; overflow: hidden; transition: all 0.4s; box-shadow: 0 6px 20px rgba(44,36,22,0.25); }
.btn-start::before { content: ''; position: absolute; top: 50%; left: 50%; width: 0; height: 0; background: rgba(255,255,255,0.15); border-radius: 50%; transform: translate(-50%, -50%); transition: width 0.6s, height 0.6s; }
.btn-start:hover::before { width: 400px; height: 400px; }
.btn-start:hover { transform: translateY(-3px); box-shadow: 0 10px 30px rgba(44,36,22,0.35); }
.btn-start:active { transform: translateY(1px); box-shadow: 0 3px 10px rgba(44,36,22,0.3); }
.quiz-header { display: flex; align-items: center; justify-content: space-between; padding: 20px 0 10px; }
.quiz-counter { font-family: 'ZCOOL XiaoWei', serif; font-size: 18px; color: var(--ink-faint); letter-spacing: 0.06em; }
.quiz-counter span { color: var(--ink); font-size: 24px; font-weight: 700; }
.quiz-progress { flex: 1; height: 3px; background: #e0d8c8; border-radius: 2px; margin: 0 20px; overflow: hidden; }
.quiz-progress-fill { height: 100%; background: linear-gradient(90deg, var(--gold), var(--red-seal)); border-radius: 2px; transition: width 0.5s ease-out; }
.btn-back { font-family: 'ZCOOL XiaoWei', serif; font-size: 14px; color: var(--ink-faint); background: none; border: 1px solid #d4c5a0; border-radius: 20px; padding: 6px 16px; cursor: pointer; transition: all 0.3s; }
.btn-back:hover { color: var(--ink); border-color: var(--ink); }
.question-card { background: #fdfaf5; border: 1px solid #e0d8c8; border-radius: 16px; padding: 36px 28px; margin: 20px 0; box-shadow: 0 4px 20px rgba(44,36,22,0.06); position: relative; }
.question-card::before { content: ''; position: absolute; top: 0; left: 28px; right: 28px; height: 1px; background: linear-gradient(90deg, transparent, var(--gold), transparent); opacity: 0.5; }
.question-text { font-family: 'ZCOOL XiaoWei', serif; font-size: clamp(18px, 2.5vw, 22px); font-weight: 600; line-height: 1.6; color: var(--ink); margin-bottom: 32px; text-align: center; }
.options-list { display: flex; flex-direction: column; gap: 12px; }
.option-btn { display: flex; align-items: center; gap: 16px; width: 100%; padding: 16px 20px; background: #faf7ef; border: 1.5px solid #e5dcc8; border-radius: 12px; cursor: pointer; font-family: 'Noto Serif SC', serif; font-size: 15px; color: var(--ink); text-align: left; transition: all 0.3s; position: relative; overflow: hidden; }
.option-btn::after { content: ''; position: absolute; inset: 0; background: linear-gradient(135deg, transparent 60%, rgba(184,147,74,0.06)); opacity: 0; transition: opacity 0.3s; }
.option-btn:hover { border-color: var(--gold); background: #fdf9f0; transform: translateX(4px); }
.option-btn:hover::after { opacity: 1; }
.option-btn:active { transform: scale(0.985); }
.option-label { width: 32px; height: 32px; border-radius: 50%; border: 2px solid #d4c5a0; display: flex; align-items: center; justify-content: center; font-family: 'ZCOOL XiaoWei', serif; font-size: 14px; color: var(--ink-faint); flex-shrink: 0; transition: all 0.3s; }
.option-btn:hover .option-label { border-color: var(--gold); color: var(--gold); background: rgba(184,147,74,0.08); }
.audio-options { display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; }
.audio-card { display: flex; flex-direction: column; align-items: center; gap: 10px; padding: 16px 10px; background: #faf7ef; border: 1.5px solid #e5dcc8; border-radius: 12px; cursor: pointer; transition: all 0.3s; position: relative; }
.audio-card:hover { border-color: var(--gold); transform: translateY(-3px); box-shadow: 0 8px 20px rgba(44,36,22,0.1); }
.audio-card.playing { border-color: var(--gold); background: #fef9ed; }
.audio-icon-circle { width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; overflow: hidden; border: 1.5px solid #d4c5a0; transition: all 0.3s; }
.audio-card:hover .audio-icon-circle { border-color: var(--gold); background: rgba(184,147,74,0.08); }
.audio-icon-circle img { width: 100%; height: 100%; object-fit: cover; }
.audio-instrument-name { font-family: 'ZCOOL XiaoWei', serif; font-size: 16px; font-weight: 600; }
.audio-wave { display: flex; align-items: flex-end; gap: 2px; height: 28px; }
.audio-wave-bar { width: 3px; background: #d4c5a0; border-radius: 2px; transition: all 0.15s; }
.audio-card.playing .audio-wave-bar { background: var(--gold); }
.audio-play-btn { width: 36px; height: 36px; border-radius: 50%; border: 2px solid #d4c5a0; background: none; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: all 0.3s; font-size: 14px; }
.audio-card:hover .audio-play-btn { border-color: var(--gold); color: var(--gold); }
.audio-select-text { font-size: 12px; color: var(--ink-faint); }
.result-container { max-width: 680px; margin: 0 auto; width: 100%; }
.result-card { background: #fdfaf5; border: 1px solid #e0d8c8; border-radius: 20px; overflow: hidden; box-shadow: 0 8px 40px rgba(44,36,22,0.1); animation: fadeSlideIn 0.8s ease-out; }
.result-header { padding: 40px 28px 30px; text-align: center; position: relative; color: #f7f3eb; }
.result-header[data-inst="erhu"] { background: linear-gradient(160deg, #1a2848, #2c3e6b, #3d5a8a); }
.result-header[data-inst="pipa"] { background: linear-gradient(160deg, #6b1a1e, #b5343a, #c94a50); }
.result-header[data-inst="guqin"] { background: linear-gradient(160deg, #2d3540, #576574, #6b7d8e); }
.result-header[data-inst="dizi"] { background: linear-gradient(160deg, #1e3d2a, #4a7c59, #5d9670); }
.result-header[data-inst="guzheng"] { background: linear-gradient(160deg, #3d3a35, #8b8682, #a09b96); }
.result-header[data-inst="suona"] { background: linear-gradient(160deg, #5a3e14, #c4932a, #d4a840); }
.result-instrument-icon { width: 90px; height: 90px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 12px; background: rgba(255,255,255,0.15); border: 2px solid rgba(255,255,255,0.3); overflow: hidden; }
.result-instrument-icon img { width: 100%; height: 100%; object-fit: cover; border-radius: 50%; }
.result-instrument-name { font-family: 'ZCOOL XiaoWei', serif; font-size: 36px; font-weight: 900; letter-spacing: 0.12em; }
.result-persona-title { font-size: 16px; letter-spacing: 0.1em; opacity: 0.8; margin-top: 4px; }
.result-body { padding: 32px 28px; }
.result-section { margin-bottom: 28px; }
.result-section:last-child { margin-bottom: 0; }
.result-section-title { font-family: 'ZCOOL XiaoWei', serif; font-size: 17px; font-weight: 700; color: var(--ink); margin-bottom: 12px; padding-left: 14px; border-left: 3px solid var(--gold); letter-spacing: 0.06em; }
.result-section p { font-size: 15px; line-height: 2; color: var(--ink-light); text-indent: 2em; }
.result-section ul { list-style: none; padding-left: 14px; }
.result-section ul li { font-size: 15px; line-height: 2; color: var(--ink-light); position: relative; padding-left: 20px; }
.result-section ul li::before { content: '◆'; position: absolute; left: 0; font-size: 6px; top: 12px; color: var(--gold); }
.result-traits { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 16px; }
.trait-tag { padding: 6px 16px; background: #f5efe0; border: 1px solid #e0d8c8; border-radius: 20px; font-size: 13px; color: var(--ink-light); }
.score-chart { margin: 20px 0; }
.score-bar-row { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
.score-bar-label { width: 50px; font-size: 13px; color: var(--ink-light); text-align: right; flex-shrink: 0; }
.score-bar-track { flex: 1; height: 8px; background: #e8dfcc; border-radius: 4px; overflow: hidden; }
.score-bar-fill { height: 100%; border-radius: 4px; transition: width 1s ease-out; }
.result-actions { display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; padding: 0 28px 40px; }
.btn-retry, .btn-share { padding: 14px 32px; font-family: 'ZCOOL XiaoWei', serif; font-size: 16px; letter-spacing: 0.08em; border-radius: 30px; cursor: pointer; transition: all 0.3s; }
.btn-retry { background: var(--ink); color: var(--paper); border: none; box-shadow: 0 4px 12px rgba(44,36,22,0.2); }
.btn-retry:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(44,36,22,0.3); }
.btn-share { background: none; color: var(--ink-light); border: 1.5px solid #d4c5a0; }
.btn-share:hover { border-color: var(--ink); color: var(--ink); }
.score-overview { padding: 20px 28px; border-top: 1px solid #e8dfcc; cursor: pointer; text-align: center; font-size: 14px; color: var(--ink-faint); transition: color 0.3s; }
.score-overview:hover { color: var(--ink); }
.footer { text-align: center; padding: 30px 0; font-size: 12px; color: var(--ink-faint); opacity: 0.6; letter-spacing: 0.05em; }
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #d4c5a0; border-radius: 3px; }
@media (max-width: 640px) {
  .tokens-grid { gap: 8px; }
  .token { width: 110px; height: 170px; }
  .token-front-name { font-size: 15px; }
  .token-back-name { font-size: 22px; }
  .token-back-persona { font-size: 12px; }
  .token-back-hint { font-size: 10px; margin-top: 12px; }
  .token-back-icon { width: 48px; height: 48px; margin-bottom: 10px; }
  .question-card { padding: 24px 16px; }
  .option-btn { padding: 14px 16px; font-size: 14px; gap: 12px; }
  .audio-options { grid-template-columns: repeat(3, 1fr); }
  .result-header { padding: 28px 16px 22px; }
  .result-instrument-name { font-size: 28px; }
  .result-body { padding: 24px 16px; }
  .result-actions { gap: 12px; }
  .btn-retry, .btn-share { padding: 12px 24px; font-size: 14px; }
  .quiz-header { flex-wrap: wrap; justify-content: center; gap: 10px; }
}
</style>
</head>
<body>
<div class="ink-bg"><div class="ink-blob"></div><div class="ink-blob"></div><div class="ink-blob"></div><div class="ink-blob"></div><div class="ink-blob"></div></div>
<div class="home-bg"></div>
<div class="paper-texture"></div>
<div class="app-container">
  <div class="page active" id="page-home">
    <div class="hero">
      <div class="hero-seal">音</div>
      <h1 class="hero-title">弦 外 之 音</h1>
      <p class="hero-subtitle">六音寻心 · 中华传统乐器人格测试</p>
    </div>
    <div class="pattern-divider"></div>
    <div class="tokens-section">
      <div class="tokens-grid" id="tokensGrid">
        <div class="token" data-inst="erhu" style="transition-delay: 0.1s">
          <div class="token-card">
            <div class="token-front">
              <div class="token-front-img"><img src="inst-erhu.png" alt="二胡"></div>
              <div class="token-front-label"><div class="token-front-name">二 胡</div><div class="token-front-tag">幽弦者</div></div>
            </div>
            <div class="token-back">
              <div class="token-back-icon"><img src="inst-erhu.png" alt="二胡"></div>
              <div class="token-back-name">二 胡</div>
              <div class="token-back-persona">幽弦者</div>
              <div class="token-back-hint">移开鼠标查看正面</div>
            </div>
          </div>
        </div>
        <div class="token" data-inst="pipa" style="transition-delay: 0.2s">
          <div class="token-card">
            <div class="token-front">
              <div class="token-front-img"><img src="inst-pipa.png" alt="琵琶"></div>
              <div class="token-front-label"><div class="token-front-name">琵 琶</div><div class="token-front-tag">烈弦者</div></div>
            </div>
            <div class="token-back">
              <div class="token-back-icon"><img src="inst-pipa.png" alt="琵琶"></div>
              <div class="token-back-name">琵 琶</div>
              <div class="token-back-persona">烈弦者</div>
              <div class="token-back-hint">移开鼠标查看正面</div>
            </div>
          </div>
        </div>
        <div class="token" data-inst="guqin" style="transition-delay: 0.3s">
          <div class="token-card">
            <div class="token-front">
              <div class="token-front-img"><img src="inst-guqin.png" alt="古琴"></div>
              <div class="token-front-label"><div class="token-front-name">古 琴</div><div class="token-front-tag">素弦者</div></div>
            </div>
            <div class="token-back">
              <div class="token-back-icon"><img src="inst-guqin.png" alt="古琴"></div>
              <div class="token-back-name">古 琴</div>
              <div class="token-back-persona">素弦者</div>
              <div class="token-back-hint">移开鼠标查看正面</div>
            </div>
          </div>
        </div>
        <div class="token" data-inst="dizi" style="transition-delay: 0.4s">
          <div class="token-card">
            <div class="token-front">
              <div class="token-front-img"><img src="inst-dizi.png" alt="笛子"></div>
              <div class="token-front-label"><div class="token-front-name">笛 子</div><div class="token-front-tag">清风者</div></div>
            </div>
            <div class="token-back">
              <div class="token-back-icon"><img src="inst-dizi.png" alt="笛子"></div>
              <div class="token-back-name">笛 子</div>
              <div class="token-back-persona">清风者</div>
              <div class="token-back-hint">移开鼠标查看正面</div>
            </div>
          </div>
        </div>
        <div class="token" data-inst="guzheng" style="transition-delay: 0.5s">
          <div class="token-card">
            <div class="token-front">
              <div class="token-front-img"><img src="inst-guzheng.png" alt="古筝"></div>
              <div class="token-front-label"><div class="token-front-name">古 筝</div><div class="token-front-tag">玉弦者</div></div>
            </div>
            <div class="token-back">
              <div class="token-back-icon"><img src="inst-guzheng.png" alt="古筝"></div>
              <div class="token-back-name">古 筝</div>
              <div class="token-back-persona">玉弦者</div>
              <div class="token-back-hint">移开鼠标查看正面</div>
            </div>
          </div>
        </div>
        <div class="token" data-inst="suona" style="transition-delay: 0.6s">
          <div class="token-card">
            <div class="token-front">
              <div class="token-front-img"><img src="inst-suona.png" alt="唢呐"></div>
              <div class="token-front-label"><div class="token-front-name">唢 呐</div><div class="token-front-tag">金声者</div></div>
            </div>
            <div class="token-back">
              <div class="token-back-icon"><img src="inst-suona.png" alt="唢呐"></div>
              <div class="token-back-name">唢 呐</div>
              <div class="token-back-persona">金声者</div>
              <div class="token-back-hint">移开鼠标查看正面</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="pattern-divider"></div>
    <div class="intro-quote">世间万物皆有性情<br>六弦之中，藏着你的前世今生<br>十问寻心，觅得属于你的那份天籁</div>
    <div class="btn-start-wrapper"><button class="btn-start" onclick="startQuiz()">开始测试</button></div>
  </div>
  <div class="page" id="page-quiz">
    <div class="quiz-header">
      <div class="quiz-counter">第 <span id="qCurrent">1</span> / 10 题</div>
      <div class="quiz-progress"><div class="quiz-progress-fill" id="progressFill" style="width: 0%"></div></div>
      <button class="btn-back" onclick="goHome()">← 返回</button>
    </div>
    <div id="questionArea"></div>
  </div>
  <div class="page" id="page-result"><div id="resultArea"></div></div>
  <div class="footer">弦外之音 · 以器观心 · 以音问道</div>
</div>
'''

print(f"Part 1 length: {len(part1)} chars")