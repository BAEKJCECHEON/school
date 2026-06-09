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
