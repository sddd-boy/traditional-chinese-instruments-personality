# -*- coding: utf-8 -*-
import codecs

filepath = r'C:\Users\32047\lobsterai\project\instrument-personality\index.html'

with codecs.open(filepath, 'r', 'utf-8') as f:
    c = f.read()

# 1. Replace getHexChart function
old_fn = '''function getHexChart(winId){
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
}'''

new_fn = '''function getHexChart(winId){
  var n=dimDefs.length,R=88,cx=140,cy=130;
  var pts=dimDefs.map(function(d,i){
    var val=d.base[winId]||0;
    var ratio=Math.min(val/d.max,1);
    var angle=Math.PI*2*i/n-Math.PI/2;
    return{cx:cx+R*ratio*Math.cos(angle),cy:cy+R*ratio*Math.sin(angle),label:d.name,val:val,max:d.max,angle:angle};
  });
  var axisLines=pts.map(function(p,i){
    return'<line x1="'+cx+'" y1="'+cy+'" x2="'+(cx+92*Math.cos(p.angle))+'" y2="'+(cy+92*Math.sin(p.angle))+'" stroke="#c8c0b0" stroke-width="0.8" stroke-dasharray="2,2"/>';
  }).join('');
  var gridRings=[0.33,0.66,1];
  var gridLines=gridRings.map(function(r){
    var pstr=pts.map(function(p){return(cx+r*R*Math.cos(p.angle))+','+(cy+r*R*Math.sin(p.angle))}).join(' ');
    return'<polygon points="'+pstr+'" fill="none" stroke="#d0c8b8" stroke-width="0.6"/>';
  }).join('');
  var polyFill=pts.map(function(p){return p.cx+','+p.cy}).join(' ');
  var poly='<polygon points="'+polyFill+'" fill="rgba(80,100,120,0.08)" stroke="rgba(80,100,120,0.35)" stroke-width="1.2"/>';
  var labels=pts.map(function(p,i){
    var lx=cx+(106)*Math.cos(p.angle),ly=cy+(106)*Math.sin(p.angle);
    var pct=Math.round(p.val/p.max*100);
    return'<text class="hex-label" x="'+lx+'" y="'+ly+'" dy="0.3em">'+p.label+'</text><circle cx="'+p.cx+'" cy="'+p.cy+'" r="2.5" fill="rgba(60,80,100,0.5)"/>';
  }).join('');
  return'<div class="hexagon-chart-wrap"><svg viewBox="0 0 280 260" style="overflow:visible">'+gridLines+axisLines+poly+labels+'</svg></div>';
}'''

if old_fn in c:
    c = c.replace(old_fn, new_fn)
    print('getHexChart replaced OK')
else:
    print('getHexChart not found exactly')
    idx = c.find('function getHexChart')
    print('Found at:', idx)

# 2. Update CSS - make hex-label lighter, remove gold accents
old_css1 = '.hex-label{font-family:var(--font-calligraphy);font-size:11px;fill:var(--ink-light);letter-spacing:0.05em;text-anchor:middle}'
new_css1 = '.hex-label{font-family:var(--font-calligraphy);font-size:11px;fill:var(--ink-faint);letter-spacing:0.05em;text-anchor:middle}'

if old_css1 in c:
    c = c.replace(old_css1, new_css1)
    print('hex-label CSS updated')
else:
    print('hex-label CSS not found')

# 3. Add .hex-dot for the circle markers
old_css2 = '.hexagon-chart-wrap svg{width:100%;height:100%}'
new_css2 = '.hexagon-chart-wrap svg{width:100%;height:100%}\n.hex-dot{opacity:0}'

if old_css2 in c:
    c = c.replace(old_css2, new_css2)
    print('hex-dot CSS added')
else:
    print('hexagon svg CSS not found')

# 4. Update .result-section border-left color to be more muted
old_css3 = '.result-section-title{font-family:var(--font-calligraphy);font-size:17px;font-weight:400;color:var(--ink);margin-bottom:12px;padding-left:14px;border-left:3px solid var(--gold);letter-spacing:0.12em}'
new_css3 = '.result-section-title{font-family:var(--font-calligraphy);font-size:17px;font-weight:400;color:var(--ink);margin-bottom:12px;padding-left:14px;border-left:3px solid rgba(120,100,80,0.3);letter-spacing:0.12em}'

if old_css3 in c:
    c = c.replace(old_css3, new_css3)
    print('result-section-title CSS updated')
else:
    print('result-section-title CSS not found')

with codecs.open(filepath, 'w', 'utf-8') as f:
    f.write(c)

print('Done. Size:', len(c))