import argparse
import requests

def main():
    ""
    test_url = "http://www.whsw.edu.cn/?q=freedom"
    test_url2 = "http://www.nx.gov.cn/q=freenet"

    urls = ["http://www.whsw.edu.cn/q=freedom",
            "http://www.whsw.edu.cn/q=freenet",
            "http://www.nx.gov.cn/q=freedom",
            "http://www.nx.gov.cn/q=freenet",
            ]

    for url in urls:
        exception_count = 0
        no_exception_count = 0
        for i in range(1000):
            try:
                r = requests.get(url)
                # print(" Response: {}".format(r.status_code))
                no_exception_count += 1
            except Exception as e:
                exception_count += 1
                # print(e)
                # print(" Couldn't establish connection...")
        print(" {} Blocked: {}, Not blocked: {}".format(url, exception_count, no_exception_count))


if __name__ == '__main__':
    main()
