import requests

print("\n已修正，可以正常运行！")
print("\n欢迎关注 Mingyu 的 GitHub 仓库 https://github.com/ymyuuu")
print("感谢大家支持！\n\n")


def list_dns_records(zone_id, api_key, e_mail):
    endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

    headers = {
        "Content-Type": "application/json",
        "X-Auth-Key": f"{api_key}",
        "X-Auth-Email": f"{e_mail}"
    }

    try:
        response = requests.get(endpoint, headers=headers)
        if response.status_code == 200:
            records = response.json()["result"]
            print("找到以下记录：")
            print("序号\t类型\t名称\t\t\t内容")
            for i, record in enumerate(records, start=1):
                # 使用ljust()方法填充列，保持相同的宽度
                print(f"{i}\t{record['type']}\t{record['name'].ljust(24)}{record['content']}")
            return records
        else:
            print("获取 DNS 记录失败。")
            return []
    except Exception as e:
        print(f"发生异常：{e}")
        return []

def delete_dns_record(records, zone_id, api_key, e_mail):
    while True:
        selected_input = input("请输入需要删除的记录的序号或类型 (多个序号或类型用空格分隔,直接回车则退出程序): ")

        if not selected_input.strip():  # 如果输入为空，则退出程序
            print("已退出,感谢支持")
            break

        headers = {
            "Content-Type": "application/json",
            "X-Auth-Key": f"{api_key}",
            "X-Auth-Email": f"{e_mail}"
        }

        selected_ids = selected_input.split()
        for index in selected_ids:
            try:
                index = int(index)
                record_id = records[index - 1]['id']
                delete_endpoint = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
                delete_response = requests.delete(delete_endpoint, headers=headers)
                if delete_response.status_code == 200:
                    # 获取要删除的记录的详细信息
                    record = records[index - 1]
                    print(f"记录 {record['type']} {record['name']} - {record['content']} 删除成功！")
                else:
                    print(f"记录 ID {record_id} 删除失败。")
            except (ValueError, IndexError):
                print(f"序号 {index} 无效，请输入有效的序号。")

# 用户输入 Zone ID 和 Cloudflare API Key
zone_id = input("请输入您的 Zone ID: ")
api_key = input("请输入您的 Cloudflare API Key: ")
email = input("请输入您的 Cloudflare Email: ")

# 列出 DNS 记录
records = list_dns_records(zone_id, api_key, email)

if records:
    # 删除 DNS 记录
    delete_dns_record(records, zone_id, api_key, email)



# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
