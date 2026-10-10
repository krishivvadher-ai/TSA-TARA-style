
(function(){
  var KEY='tsa-ws-practice', root=document.documentElement, btn=document.getElementById('practice');
  if(!btn)return;
  function set(on){root.classList.toggle('practice',on);btn.setAttribute('aria-pressed',on?'true':'false');
    btn.textContent=on?'Practice mode: on (working hidden)':'Practice mode: off';try{localStorage.setItem(KEY,on?'1':'0')}catch(e){}}
  var saved=false;try{saved=localStorage.getItem(KEY)==='1'}catch(e){}
  set(saved);
  btn.addEventListener('click',function(){set(!root.classList.contains('practice'))});
  var wm=document.getElementById('wm-toggle'), WKEY='tsa-ws-methods';
  function setWm(on){root.classList.toggle('no-wm',!on);wm.setAttribute('aria-pressed',on?'true':'false');
    wm.textContent=on?'Written methods: shown':'Written methods: hidden';try{localStorage.setItem(WKEY,on?'1':'0')}catch(e){}}
  if(wm){var wsaved=true;try{wsaved=localStorage.getItem(WKEY)!=='0'}catch(e){}
    setWm(wsaved);wm.addEventListener('click',function(){setWm(root.classList.contains('no-wm'))});}
  document.querySelectorAll('.reveal').forEach(function(b){b.addEventListener('click',function(){
    var q=b.closest('.q'), on=!q.classList.contains('shown');
    q.classList.toggle('shown',on); b.textContent=on?'Hide working':'Show working';});});
})();

(function(){
  var app=document.getElementById('app'); if(!app)return;
  function load(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
  function save(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}

  /* side menu (a drawer on small screens) */
  var side=document.getElementById('side'), menuBtn=document.getElementById('menu-btn'), scrim=document.getElementById('scrim');
  function syncScrim(){if(scrim)scrim.hidden=!app.classList.contains('menu-open');}
  function menu(open){
    if(!side)return;
    app.classList.toggle('menu-open',open); syncScrim();
    if(menuBtn)menuBtn.setAttribute('aria-expanded',open?'true':'false');
    if(open){var f=side.querySelector('[aria-current="page"]')||side.querySelector('a');if(f)f.focus();}
    else if(menuBtn&&side.contains(document.activeElement))menuBtn.focus();
  }
  if(menuBtn)menuBtn.addEventListener('click',function(){menu(!app.classList.contains('menu-open'));});
  if(scrim)scrim.addEventListener('click',function(){menu(false);});
  document.querySelectorAll('[data-close-menu]').forEach(function(b){b.addEventListener('click',function(){menu(false);});});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')menu(false);});

  /* remember the last page for "Continue where you left off" */
  if(app.dataset.page!=='home'){
    save('tsa-last',{href:location.pathname.split('/').pop(),label:app.dataset.label});
  }else{
    var last=load('tsa-last'), c=document.getElementById('continue');
    if(c&&last&&last.href&&/^TSA_\w+\.html$/.test(last.href)){c.href=last.href;c.querySelector('b').textContent=last.label;c.hidden=false;}
  }

  /* question paper: zoom */
  var pages=document.getElementById('pages');
  document.querySelectorAll('.zoom button').forEach(function(b){b.addEventListener('click',function(){
    pages.dataset.z=b.dataset.z;
    document.querySelectorAll('.zoom button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false');});
  });});

  /* worked solutions: a button back to the question list once you have scrolled down */
  var toq=document.querySelector('.to-q');
  if(toq){var onScroll=function(){toq.classList.toggle('on',window.scrollY>700);};window.addEventListener('scroll',onScroll,{passive:true});onScroll();}
})();
