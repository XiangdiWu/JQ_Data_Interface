import jqdatasdk as jq
from Config.config import JQ_USERNAME, JQ_PASSWORD

jq.auth(JQ_USERNAME, JQ_PASSWORD)

def get_auth_info():
    #查询当日剩余可调用数据条数
    count = jq.get_query_count()
    print(count)

    #查询账号信息
    infos = jq.get_account_info()
    print(infos)

if __name__ == "__main__":
    get_auth_info()