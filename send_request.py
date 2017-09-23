import argparse
import requests

def check_url(url_to_check):
    blocked_count = 0
    worked_count = 0
    for i in range(10):
        try:
            r = requests.get(url_to_check)
            worked_count += 1
        except Exception as e:
            blocked_count += 1
    print(" URL: {} Blocked: {} Worked: {}".format(url_to_check,
                                                blocked_count,
                                                worked_count))

def main():

    urls = ["http://www.whsw.edu.cn/q=freedom",
            "http://www.whsw.edu.cn/q=freenet",
            "http://www.nx.gov.cn/q=freedom",
            "http://www.nx.gov.cn/q=freenet",
            ]

    for url in urls:
        check_url(url)


if __name__ == '__main__':
    main()
