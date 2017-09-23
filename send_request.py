import argparse
import requests
import concurrent.futures
import time

def check_url(url_to_check, iteration_count):
    blocked_count = 0
    worked_count = 0
    weird_count_1 = 0
    weird_count_2 = 0
    for i in range(iteration_count):
        try:
            r = requests.get(url_to_check)
            if r.status_code == requests.codes.ok:
                worked_count += 1
            else:
                weird_count_1 = 0
        except requests.exceptions.ConnectionError:
            blocked_count += 1
        except:
            weird_count_2 = 0
        time.sleep(2)
    print(" blocked: {}, worked: {}, weird_1: {}, weird_2: {}, URL: {}"
                                        .format(blocked_count,
                                                worked_count,
                                                weird_count_1,
                                                weird_count_2,
                                                url_to_check))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("iter_count", help="number of iterations", type=int)
    args = parser.parse_args()

    urls = ["http://www.whsw.edu.cn/",
            "http://www.whsw.edu.cn/q=freenet",
            "http://www.nx.gov.cn/q=freedom",
            "http://www.nx.gov.cn/q=freenet",
            ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        for url in urls:
            executor.submit(check_url, url, args.iter_count)

if __name__ == '__main__':
    main()
