
from bs4 import BeautifulSoup
from requests import get
def extract_wwr_jobs(keyword):
	base_url = "https://weworkremotely.com/remote-jobs/search?term="

	response = get(f'{base_url}{keyword}')

	if response.status_code != 200:
		print("Can't Read website")

	else:
		results = []
		soup = BeautifulSoup(response.text, "html.parser")
		jobs = soup.find_all('section', class_="jobs")
## if len(jobs)를 추가해서 결과가 없을때에도 오류가 안나게 변경. jobs를 일단 soup에서 가져온 다음에 판단. len으로 개수 체크하고 결과값이 0이면 결과가 없다고 반환해줌
		if len(jobs) == 0:
			print("no jobs found")
			return None
## 여기까지 if len(jobs) 변경점

		for job_section in jobs:
			job_post = job_section.find_all('li')
			job_post.pop(-1)
			for post in job_post:
				anchors = post.find_all('a')
				anchor = anchors[1]
				link = anchor['href']
				company, kind, location = anchor.find_all('span', class_='company')
				title = anchor.find('span', class_='title')
				job_data = {
					'title': title.string,
					'company': company.string,
					'kind': kind.string,
					'location': location.string
				}
				results.append(job_data)
		return results