import argparse
import requests

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url to send request to", type=str)
    args = parser.parse_args()

    try:
        r = requests.get(args.url)
        print(" Response: {}".format(r.status_code))
    except Exception as e:
        print(e)
        print("Couldn't establish connection...")




if __name__ == '__main__':
    main()
