# -*- coding: utf-8 -*-
import os

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('.result-body')
end_idx = content.find('.score-bar-row')

old_text = content[idx:end_idx]
print('Old text length:', len(old_text))
print('First 200:', repr(old_text[:200]))

new_text = '''.result-body{padding:32px 28px}
.result-section{margin-bottom:28px;animation:fadeSlideIn 0.6s ease-out forwards}
.result-section:last-child{margin-bottom:0}
.result-section-title{font-family:var(--font-calligraphy);font-size:17px;font-weight:400;color:var(--ink);margin-bottom:12px;padding-left:14px;border-left:3px solid var(--gold);letter-spacing:0.12em}
.result-section p{font-size:15px;line-height:2;color:var(--ink-light);text-indent:2em}
.result-section ul{list-style:none;padding-left:14px}
.result-section ul li{font-size:15px;line-height:2;color:var(--ink-light);position:relative;padding-left:20px}
.result-section ul li::before{content:'◆';position:absolute;left:0;font-size:6px;top:12px;color:var(--gold)}
.result-traits{display:flex;gap:10px;flex-wrap:wrap;margin-top:16px}
.trait-tag{padding:6px 16px;background:#f5efe0;border:1px solid #e0d8c8;border-radius:20px;font-size:13px;color:var(--ink-light)}
.trait-tag:first-child{border-color:var(--gold);color:var(--gold)}
.percent-chart{margin:16px 0 0}
.percent-row{display:flex;align-items:center;gap:12px;margin-bottom:10px}
.percent-label{width:42px;font-size:13px;color:var(--ink-light);text-align:right;flex-shrink:0}
.percent-bar-track{flex:1;height:10px;background:#e8dfcc;border-radius:5px;overflow:hidden}
.percent-bar-fill{height:100%;border-radius:5px;transition:width 1.2s cubic-bezier(0.25,0.46,0.45,0.94)}
.percent-value{width:38px;font-size:12px;color:var(--ink-light);text-align:right;flex-shrink:0}
.hexagon-section{margin:24px 0 0}
.hexagon-chart-wrap{position:relative;width:280px;height:260px;margin:0 auto}
.hexagon-chart-wrap svg{width:100%;height:100%}
.hex-label{font-family:var(--font-calligraphy);font-size:11px;fill:var(--ink-light);letter-spacing:0.05em;text-anchor:middle}
.compat-section{margin:24px 0 0}
.compat-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:16px}
.compat-card{border-radius:12px;padding:16px;position:relative;overflow:hidden}
.compat-best{background:linear-gradient(135deg,rgba(74,124,89,0.08),rgba(74,124,89,0.04));border:1px solid rgba(74,124,89,0.25)}
.compat-worst{background:linear-gradient(135deg,rgba(194,57,42,0.08),rgba(194,57,42,0.04));border:1px solid rgba(194,57,42,0.2)}
.compat-badge{font-size:11px;letter-spacing:0.1em;padding:3px 10px;border-radius:10px;display:inline-block;margin-bottom:10px}
.compat-best .compat-badge{background:rgba(74,124,89,0.15);color:#4a7c59}
.compat-worst .compat-badge{background:rgba(194,57,42,0.12);color:#c23a2b}
.compat-instrument{font-family:var(--font-calligraphy);font-size:22px;letter-spacing:0.1em;margin-bottom:8px}
.compat-reason{font-size:13px;line-height:1.8;color:var(--ink-light)}
'''

new_content = content[:idx] + new_text + content[end_idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Done. New size:', len(new_content))