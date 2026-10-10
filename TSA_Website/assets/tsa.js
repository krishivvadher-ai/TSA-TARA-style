
(function(){
  var KEY='tsa-ws-practice', root=document.documentElement, btn=document.getElementById('practice');
  if(!btn)return;
  function set(on){root.classList.toggle('practice',on);btn.setAttribute('aria-pressed',on?'true':'false');
    btn.textContent=on?'Practice mode: on (working hidden)':'Practice mode: off';try{localStorage.setItem(KEY,on?'1':'0')}catch(e){}}
  var saved=false;try{saved=localStorage.getItem(KEY)==='1'}catch(e){}
  set(saved);
  btn.addEventListener('click',function(){set(!root.classList.contains('practice'))});
  document.querySelectorAll('.reveal').forEach(function(b){b.addEventListener('click',function(){
    var q=b.closest('.q'), on=!q.classList.contains('shown');
    q.classList.toggle('shown',on); b.textContent=on?'Hide working':'Show working';});});
})();

(function(){
  var picks=document.querySelectorAll('details.yearpick');
  document.addEventListener('click',function(e){picks.forEach(function(d){if(d.open&&!d.contains(e.target))d.open=false;});});
  document.addEventListener('keydown',function(e){if(e.key!=='Escape')return;
    picks.forEach(function(d){if(d.open){d.open=false;d.querySelector('summary').focus();}});});
  /* the bar slides away while you read down the page and comes back as soon as you scroll up */
  var bar=document.getElementById('sitebar'), toq=document.querySelector('.to-q'), last=window.scrollY;
  function onScroll(){
    var y=window.scrollY, d=y-last;
    if(bar){
      if(y<90||d<-6)bar.classList.remove('away');
      else if(d>6&&!bar.contains(document.activeElement)&&!bar.querySelector('details[open]'))bar.classList.add('away');
    }
    if(toq)toq.classList.toggle('on',y>700);
    last=y;
  }
  window.addEventListener('scroll',onScroll,{passive:true});
  if(bar)bar.addEventListener('focusin',function(){bar.classList.remove('away');});
  /* on a phone the page tabs scroll sideways: start with the current one in view */
  var tabs=document.querySelector('.tabs'), cur=tabs&&tabs.querySelector('[aria-current="page"]');
  if(tabs&&cur&&tabs.scrollWidth>tabs.clientWidth)tabs.scrollLeft=cur.offsetLeft-tabs.offsetLeft-tabs.clientWidth/2+cur.offsetWidth/2;
})();
