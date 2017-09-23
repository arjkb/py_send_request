import argparse
import requests
import concurrent.futures
import time


def read_urls(url_file):
    urls = list()
    with open(url_file, 'r') as f:
        for url in f:
            urls.append(url.strip())
    return urls

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
        time.sleep(1)
    print(" blocked: {}, worked: {}, weird_1: {}, weird_2: {}, URL: {}"
                                        .format(blocked_count,
                                                worked_count,
                                                weird_count_1,
                                                weird_count_2,
                                                url_to_check))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("iter_count", help="number of iterations", type=int)
    parser.add_argument("url_file", help="file that contains urls to test", type=str)
    args = parser.parse_args()

    urls = read_urls(args.url_file)
    print(urls)

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        for url in urls:
            executor.submit(check_url, url, args.iter_count)

if __name__ == '__main__':
    main()
