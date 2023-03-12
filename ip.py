import requests
import pandas as pd
from tqdm import tqdm
def get_location(ip):
    url = f"https://api.live.bilibili.com/client/v1/Ip/getInfoNew?ip={ip}"
    response = requests.get(url)
    data = response.json()
    return data["data"]["country"] + " " + data["data"]["province"] + " " + data["data"]["city"] + " " + data["data"]["isp"]    
def get_ip_list():
    with open("ip.txt", "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]
def save_to_excel(ip_list, location_list):
    df = pd.DataFrame({"ip": ip_list, "location": location_list})
    df.to_excel("result.xlsx", index=False)
ip_list = get_ip_list() 
location_list = []
pbar = tqdm(total=len(ip_list), desc="Querying progress", unit="query", bar_format="{percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]")
for ip in ip_list: 
  location_list.append(get_location(ip)) 
  pbar.update(1)      
pbar.close()
save_to_excel(ip_list, location_list)