import requests
import argparse
import time
import re
from pattern import pattern

def ArgsParse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--hosts", type=str, help="list of hosts")
    parser.add_argument("-C", "--count" , type=int, default=1, help="count of requests")
    parser.add_argument("-F", "--file", type=str, help="File contained hosts") 
    parser.add_argument("-O", "--output", type=str, help="the path to the file to save the output to")
    
    args = parser.parse_args()
    return args

def ReadHostsFromFile(file_path):
    try:
        with open(file_path, "r") as file:
            hosts = [line.strip() for line in file.readlines() if line.strip()]
        return hosts
    except Exception as ex:
        print("Error reading the file")
        return []

def ServChecker(hosts, count,output_file=None):
    success_cnt = 0
    failed_cnt = 0
    error_cnt = 0
    response_time = [] #массив для хранения времени выполнения
    result = [] #массив для хранения результатов тестирования хостов
    for _ in range(count):
        for host in hosts:
            if not HostValidate(host):
                print(f"incorrect URL: {host}")
                error_cnt += 1
                continue 
            try:
                start_time = time.time()
                response = requests.get(host, timeout=3)
                end_time = time.time()
                elapsed_time = end_time - start_time
                response_time.append(elapsed_time)
                if response.status_code == 200:
                    success_cnt+=1
                    result.append(f"{host}")
                else:
                    failed_cnt+=1
                    result.append(f"{host}")
            except requests.RequestException:
                error_cnt+=1
                result.append(f"{host}")

    if response_time:
        min_time = min(response_time)
        max_time = max(response_time)
        avg_time = sum(response_time) / len(response_time)
        result.append(f" Min time: {min_time:.3f} sec")
        result.append(f" Max time: {max_time:.3f} sec")
        result.append(f" Average time: {avg_time:.3f} sec")
    else:
        result.append("There are no successful requests for calculating the time")
    
    result.append(f"Successful requests: {success_cnt}")
    result.append(f"Failed requests: {failed_cnt}")
    result.append(f"Errors: {error_cnt}")

    if output_file:
        with open(output_file, "w") as file:
            file.write("\n".join(result))
        print("The results are saved to a file")
    else:
        print("\n".join(result))

def HostValidate(host):
    return bool(re.match(pattern, host))

def main():
    args = ArgsParse()
    if args.file:
        hosts = ReadHostsFromFile(args.file)
    elif args.hosts:
        hosts = args.hosts.split(",")
    else:
        print("no host sources are specified")
    count = args.count
    output_file = args.output
    ServChecker(hosts,count, output_file)


if __name__ == "__main__":
    main()