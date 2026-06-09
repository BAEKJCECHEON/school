학교 급식 메뉴 크롤러
전북 지역 학교(용소중학교, 영광고등학교)의 급식 메뉴를 자동으로 수집하여 JSON 파일로 저장하고, 웹에서 조회할 수 있는 프로젝트입니다.

데모
https://school-baekjc94.vercel.app

주요 기능
- 전북교육청 학교 홈페이지에서 월별 급식 메뉴 자동 크롤링
- 학교별 파서 분리 (용소중, 영광고)
- 크롤링 결과를 JSON 파일로 저장 (`학교명_년월.json`)
- 저장된 JSON 데이터를 웹 페이지에서 날짜별로 조회 가능

기술 스택
Python
requests, BeautifulSoup4
HTML / JavaScript
Vercel (배포)

사용 방법

1. 패키지 설치
```bash
pip install requests beautifulsoup4
```
2. 크롤러 실행
```bash
python crawler.py
```
3. 실행 후 각 학교별 월별 JSON 파일이 생성됩니다.

AI 협업
- Claude AI를 활용하여 학교별 HTML 구조에 맞는 CSS 선택자를 분석하고 파서를 구현
- 학교마다 상이한 HTML 구조를 파악하는 과정에서 AI와 협업하여 디버깅 시간을 단축

업데이트 이력
- 2026.03 초기 크롤러 개발 및 용소중 파서 구현
- 2026.04 영광고 파서 추가
- 2026.05 ~ 06 월별 데이터 지속 업데이트
