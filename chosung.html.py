< !DOCTYPE
html >
< html
lang = "ko" >
< head >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > 초성
퀴즈 < / title >
< link
rel = "preconnect"
href = "https://fonts.googleapis.com" >
< link
href = "https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&family=Playfair+Display:wght@700&display=swap"
rel = "stylesheet" >
< style >
:root
{
    --bg:  # 0f1117;
        --surface:  # 1a1d27;
--surface2:  # 22263a;
--border:  # 2e3350;
--accent:  # 5c7cfa;
--accent2:  # f06595;
--green:  # 51cf66;
--red:  # ff6b6b;
--text:  # e8ecf4;
--text - muted:  # 7880a0;
--shadow: 0
8
px
40
px
rgba(0, 0, 0, 0.5);
--radius: 18
px;
--font: 'Noto Sans KR', sans - serif;
}
*{box - sizing: border - box;
margin: 0;
padding: 0;}

body
{
    font - family: var(--font);
background: var(--bg);
color: var(--text);
min - height: 100
vh;
display: flex;
flex - direction: column;
align - items: center;
padding: 28
px
16
px
80
px;
overflow - x: hidden;
}

.nav - bar
{
    display: flex;
gap: 8
px;
margin - bottom: 36
px;
animation: fadeDown
.6
s
ease
both;
flex - wrap: wrap;
justify - content: center;
}
.nav - btn
{
    font - family: var(--font);
font - size: 12
px;
font - weight: 500;
text - decoration: none;
padding: 8
px
18
px;
border - radius: 100
px;
border: 1
px
solid
var(--border);
background: var(--surface);
color: var(--text - muted);
transition: color
.2
s, border - color
.2
s, background
.2
s;
}
.nav - btn: hover
{color: var(--accent);
border - color: var(--accent);
background: rgba(92, 124, 250, .08);}
.nav - btn.active
{color: var(--accent);
border - color: var(--accent);
background: rgba(92, 124, 250, .12);}

header
{
    text - align: center;
margin - bottom: 28
px;
animation: fadeDown
.6
s
ease
both;
}
header.label
{
    font - size: 11px;
letter - spacing: 4
px;
text - transform: uppercase;
color: var(--accent);
margin - bottom: 10
px;
}
header
h1
{
    font - family: 'Playfair Display', serif;
font - size: clamp(2
rem, 6
vw, 3
rem);
font - weight: 700;
color:  # fff;
line - height: 1.1;
}

/ *날짜
배지 * /
.date - badge
{
    display: flex;
align - items: center;
gap: 8
px;
background: var(--surface);
border: 1
px
solid
var(--border);
border - radius: 100
px;
padding: 8
px
20
px;
margin - bottom: 24
px;
font - size: 13
px;
color: var(--text - muted);
animation: fadeDown
.6
s
.1
s
ease
both;
}
.date - badge
span
{color: var(--accent);
font - weight: 500;}

/ *메인
카드 * /
.quiz - card
{
    width: 100 %;
max - width: 480
px;
background: var(--surface);
border: 1
px
solid
var(--border);
border - radius: var(--radius);
padding: 32
px
28
px;
box - shadow: var(--shadow);
animation: fadeUp
.6
s
.2
s
ease
both;
display: flex;
flex - direction: column;
gap: 24
px;
}

/ *카테고리
뱃지 * /
.category - badge
{
    display: inline - flex;
align - items: center;
gap: 6
px;
background: rgba(92, 124, 250, .15);
border: 1
px
solid
rgba(92, 124, 250, .3);
color: var(--accent);
font - size: 12
px;
font - weight: 500;
padding: 5
px
14
px;
border - radius: 100
px;
align - self: flex - start;
}

/ *초성
표시 * /
.chosung - wrap
{
    display: flex;
justify - content: center;
gap: 10
px;
flex - wrap: wrap;
padding: 8
px
0;
}
.chosung - char
{
    width: 52px;
height: 60
px;
background: var(--surface2);
border: 1.5
px
solid
var(--border);
border - radius: 12
px;
display: flex;
align - items: center;
justify - content: center;
font - size: 24
px;
font - weight: 700;
color: var(--accent);
letter - spacing: 0;
}
.chosung - char.space
{
    background: transparent;
border - color: transparent;
color: var(--text - muted);
font - size: 14
px;
}

/ *힌트 * /
.hint - box
{
    background: var(--surface2);
border - radius: 12
px;
padding: 14
px
16
px;
font - size: 13
px;
color: var(--text - muted);
line - height: 1.7;
display: flex;
gap: 8
px;
align - items: flex - start;
}
.hint - icon
{flex - shrink: 0;
font - size: 16
px;
margin - top: 1
px;}

/ *입력 * /
.input - row
{
    display: flex;
flex - direction: column;
gap: 10
px;
}
.input - row
input
{
    width: 100 %;
background: var(--surface2);
border: 1.5
px
solid
var(--border);
border - radius: 12
px;
padding: 14
px
16
px;
font - family: var(--font);
font - size: 16
px;
color: var(--text);
outline: none;
transition: border - color
.2
s;
text - align: center;
}
.input - row
input::placeholder
{color: var(--text - muted);}
.input - row
input: focus
{border - color: var(--accent);}
.input - row
input.correct
{border - color: var(--green);
background: rgba(81, 207, 102, .08);}
.input - row
input.wrong
{border - color: var(--red);
animation: shake
.3
s
ease;}

.btn - submit
{
    width: 100 %;
background: var(--accent);
border: none;
border - radius: 12
px;
padding: 14
px;
font - family: var(--font);
font - size: 15
px;
font - weight: 700;
color:  # fff;
cursor: pointer;
transition: opacity
.2
s, transform
.15
s;
-webkit - tap - highlight - color: transparent;
}
.btn - submit: hover
{opacity: .85;}
.btn - submit: active
{transform: scale(.97);}
.btn - submit: disabled
{opacity: .4;
cursor: not -allowed;
transform: none;}

/ *결과 * /
.result - box
{
    display: none;
flex - direction: column;
gap: 12
px;
padding: 20
px;
border - radius: 14
px;
text - align: center;
}
.result - box.correct - res
{
    display: flex;
background: rgba(81, 207, 102, .08);
border: 1
px
solid
rgba(81, 207, 102, .25);
}
.result - box.wrong - res
{
    display: flex;
background: rgba(255, 107, 107, .08);
border: 1
px
solid
rgba(255, 107, 107, .25);
}
.result - emoji
{font - size: 40px;
line - height: 1;}
.result - title
{font - size: 18px;
font - weight: 700;}
.result - title.ok
{color: var(--green);}
.result - title.no
{color: var(--red);}
.result - answer
{font - size: 22px;
font - weight: 700;
color: var(--text);}
.result - sub
{font - size: 13px;
color: var(--text - muted);}

/ *시도
횟수 * /
.tries - row
{
    display: flex;
align - items: center;
justify - content: space - between;
font - size: 12
px;
color: var(--text - muted);
}
.tries - dots
{display: flex;
gap: 5
px;}
.dot
{
    width: 8px;
height: 8
px;
border - radius: 50 %;
background: var(--border);
transition: background
.2
s;
}
.dot.used
{background: var(--red);}
.dot.correct
{background: var(--green);}

/ *내일
카드 * /
.tomorrow - card
{
    width: 100 %;
max - width: 480
px;
background: var(--surface);
border: 1
px
solid
var(--border);
border - radius: var(--radius);
padding: 20
px
24
px;
box - shadow: var(--shadow);
animation: fadeUp
.4
s
ease
both;
display: flex;
align - items: center;
justify - content: space - between;
gap: 12
px;
margin - top: 16
px;
}
.tomorrow - card
p
{font - size: 13px;
color: var(--text - muted);}
.tomorrow - card
strong
{color: var(--text);
font - weight: 500;}
.countdown
{font - size: 20px;
font - weight: 700;
color: var(--accent);
font - variant - numeric: tabular - nums;}

/ *로딩 * /
# loading {
color: var(--text - muted);
font - size: 14
px;
margin - top: 40
px;
animation: fadeUp
.4
s
ease
both;
}

footer
{
margin - top: 36
px;
font - size: 11
px;
color: var(--text - muted);
text - align: center;
opacity: .6;
animation: fadeUp
.6
s
.4
s
ease
both;
}

@keyframes


fadeDown
{
from

{opacity: 0;
transform: translateY(-18
px);} to
{opacity: 1;
transform: translateY(0);}}

@keyframes


fadeUp
{
from

{opacity: 0;
transform: translateY(18
px);} to
{opacity: 1;
transform: translateY(0);}}

@keyframes


shake
{
0 %, 100 % {transform: translateX(0);}
20 % {transform: translateX(-6px);}
40 % {transform: translateX(6px);}
60 % {transform: translateX(-4px);}
80 % {transform: translateX(4px);}
}
< / style >
    < / head >
        < body >

        < nav


class ="nav-bar" >

< a
href = "index.html"


class ="nav-btn" > 🍱 급식 < / a >

< a
href = "fortune.html"


class ="nav-btn" > 🔮 운세 < / a >

< a
href = "apple.html"


class ="nav-btn" > 🍎 사과게임 < / a >

< a
href = "chosung.html"


class ="nav-btn active" > 🔤 초성퀴즈 < / a >

< / nav >

< header >
< p


class ="label" > Daily Chosung Quiz < / p >

< h1 > 초성
퀴즈 < / h1 >
< / header >

< div


class ="date-badge" id="date-badge" >

📅 오늘의
문제
로딩
중...
< / div >

< div
id = "loading" > 문제를
불러오는
중이에요... < / div >

< div


class ="quiz-card" id="quiz-card" style="display:none;" >

< div
style = "display:flex; align-items:center; justify-content:space-between;" >
< div


class ="category-badge" id="category-badge" > < / div >

< div


class ="tries-row" >

< div


class ="tries-dots" id="tries-dots" > < / div >

< / div >
< / div >

< div


class ="chosung-wrap" id="chosung-wrap" > < / div >

< div


class ="hint-box" >

< span


class ="hint-icon" > 💡 < / span >

< span
id = "hint-text" > < / span >
< / div >

< div


class ="result-box" id="result-box" > < / div >

< div


class ="input-row" id="input-area" >

< input
type = "text"
id = "answer-input"
placeholder = "정답을 입력하세요"
autocomplete = "off"
autocorrect = "off"
spellcheck = "false" / >
< button


class ="btn-submit" id="btn-submit" onclick="submitAnswer()" > 제출 < / button >

< / div >
< / div >

< div


class ="tomorrow-card" id="tomorrow-card" style="display:none;" >

< div >
< p > 다음
문제까지 < / p >
< strong > 내일
자정에
새
문제가
나와요! < / strong >
< / div >
< div


class ="countdown" id="countdown" > --:--: -- <

/ div >
< / div >

< footer > 하루
한
문제 • 모두
같은
문제 • 초성으로
맞춰보세요 < / footer >

< script >
const
MAX_TRIES = 5;
let
quiz = null;
let
tries = 0;
let
solved = false;
let
failed = false;

/ * ── KST
날짜 ── * /
function
kstNow()
{
return new
Date(Date.now() + 9 * 60 * 60 * 1000);
}
function
todayKey()
{
const
d = kstNow();
return `${d.getUTCFullYear()} -${String(d.getUTCMonth() + 1).padStart(2, '0')} -${
    String(d.getUTCDate()).padStart(2, '0')}
`;
}
function
todayLabel()
{
const
d = kstNow();
const
days = ['일', '월', '화', '수', '목', '금', '토'];
return `${d.getUTCFullYear()}
년 ${d.getUTCMonth() + 1}
월 ${d.getUTCDate()}
일 ${days[d.getUTCDay()]}
요일
`;
}

/ * ── 날짜
기반
문제
선택(모두
같은
문제) ── * /
function
pickQuiz(list)
{
const
d = kstNow();
const
seed = d.getUTCFullYear() * 10000 + (d.getUTCMonth() + 1) * 100 + d.getUTCDate();
return list[seed % list.length];
}

/ * ── 로컬
스토리지로
오늘
상태
저장 ── * /
function
saveState()
{
const
key = 'chosung_' + todayKey();
localStorage.setItem(key, JSON.stringify({tries, solved, failed}));
}
function
loadState()
{
const
key = 'chosung_' + todayKey();
const
raw = localStorage.getItem(key);
if (!raw) return null;
return JSON.parse(raw);
}

/ * ── 초성
렌더링 ── * /
function
renderChosung(chosung)
{
const
wrap = document.getElementById('chosung-wrap');
wrap.innerHTML = '';
[...chosung].forEach(ch= > {
    const
div = document.createElement('div');
if (ch === ' ')
{
    div.className = 'chosung-char space';
div.textContent = '띄어쓰기';
} else {
    div.className = 'chosung-char';
div.textContent = ch;
}
wrap.appendChild(div);
});
}

/ * ── 시도
횟수
dots ── * /
function
renderDots()
{
const
wrap = document.getElementById('tries-dots');
wrap.innerHTML = '';
for (let i = 0; i < MAX_TRIES; i++) {
    const d = document.createElement('div');
d.className = 'dot' + (i < tries ? (solved & & i == = tries-1 ? ' correct': ' used'): '');
wrap.appendChild(d);
}
}

/ * ── 카테고리
이모지 ── * /
function
categoryEmoji(cat)
{
if (cat === '영화') return '🎬';
if (cat === '노래') return '🎵';
return '❓';
}

/ * ── 정답
비교(공백·대소문자
무시) ── * /
function
normalize(str)
{
return str.replace( /\s / g, '').toLowerCase();
}

/ * ── 결과
표시 ── * /
function
showResult(correct)
{
const
box = document.getElementById('result-box');
if (correct) {
box.className = 'result-box correct-res';
box.innerHTML = `
< div


class ="result-emoji" > 🎉 < / div >

< div


class ="result-title ok" > 정답이에요! < / div >

< div


class ="result-answer" > ${quiz.answer} < / div >

< div


class ="result-sub" > ${tries}번 만에 맞혔어요! < / div > `;

} else if (failed) {
box.className = 'result-box wrong-res';
box.innerHTML = `
< div


class ="result-emoji" > 😢 < / div >

< div


class ="result-title no" > 아쉽게 틀렸어요 < / div >

< div


class ="result-answer" > ${quiz.answer} < / div >

< div


class ="result-sub" > 내일 또 도전해보세요! < / div > `;

}
box.style.display = 'flex';
}

/ * ── 입력
비활성화 ── * /
function
lockInput()
{
    document.getElementById('answer-input').disabled = true;
document.getElementById('btn-submit').disabled = true;
document.getElementById('tomorrow-card').style.display = 'flex';
startCountdown();
}

/ * ── 제출 ── * /
function
submitAnswer()
{
if (solved | | failed)
return;
const
input = document.getElementById('answer-input');
const
val = input.value.trim();
if (!val) return;

tries + +;
const
correct = normalize(val) == = normalize(quiz.answer);

if (correct) {
solved = true;
input.classList.add('correct');
renderDots();
showResult(true);
lockInput();
} else {
input.classList.add('wrong');
setTimeout(() = > input.classList.remove('wrong'), 400);
input.value = '';

if (tries >= MAX_TRIES) {
failed = true;
renderDots();
showResult(false);
lockInput();
} else {
renderDots();
input.placeholder = `${MAX_TRIES - tries}번 남았어요...`;
}
}
saveState();
}

/ * ── 카운트다운 ── * /
function
startCountdown()
{
function
update()
{
    const
now = kstNow();
const
midnight = new
Date(Date.UTC(
    now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate() + 1
));
const
diff = midnight - now;
const
h = String(Math.floor(diff / 3600000)).padStart(2, '0');
const
m = String(Math.floor((diff % 3600000) / 60000)).padStart(2, '0');
const
s = String(Math.floor((diff % 60000) / 1000)).padStart(2, '0');
document.getElementById('countdown').textContent = `${h}:${m}:${s}
`;
}
update();
setInterval(update, 1000);
}

/ * ── 초기화 ── * /
async function
init()
{
document.getElementById('date-badge').innerHTML =
`📅 < span >${todayLabel()} < / span > 의
문제
`;

let
list;
try {
const res = await fetch('chosung.json?v=' + Date.now());
list = await res.json();
} catch {
document.getElementById('loading').textContent = '⚠️ 문제를 불러오지 못했어요.';
return;
}

quiz = pickQuiz(list);
document.getElementById('loading').style.display = 'none';
document.getElementById('quiz-card').style.display = 'flex';

document.getElementById('category-badge').textContent = \
categoryEmoji(quiz.category) + ' ' + quiz.category;
document.getElementById('hint-text').textContent = quiz.hint;
renderChosung(quiz.chosung);

/ *오늘
이미
풀었는지
확인 * /
const
saved = loadState();
if (saved)
{
tries = saved.tries;
solved = saved.solved;
failed = saved.failed;
renderDots();
if (solved | | failed) {
showResult(solved);
lockInput();
const input = document.getElementById('answer-input');
if (solved) input.classList.add('correct');
input.value = solved ? quiz.answer: '';
}
} else {
renderDots();
}

document.getElementById('answer-input').addEventListener('keydown', e= > {
if (e.key === 'Enter')
submitAnswer();
});
}

init();
< / script >
    < / body >
        < / html >
