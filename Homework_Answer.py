import json

import requests

from Get_All_Course import get_all_course
from Get_Homework_List import get_homework_list


def main(stuid):
    info = get_all_course(stuid)
    homrwork_list = get_homework_list(stuid, info['openClassId'], info['courseOpenId'])
    homeworkId = homrwork_list['homeworkId']
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/previewHomework'
    data = {
        'homeWorkId': homeworkId
    }
    html = requests.post(url=url, data=data).json()['data']
    title = html['title']
    with open(f'{title}.txt', 'w', encoding='utf8') as f:
        for i in html['questions']:
            f.write(f'{int(i["sortOrder"]) + 1},{i["title"]}\n')
            try:
                for j in json.loads(i['dataJson']):
                    f.write(f'{j["SortOrder"]},{j["Content"]}\n')
                f.write(f'Answer:{i["answer"]}\n')
            except:
                pass
        input("作业答案已生成在软件目录下。请回车退出")


if __name__ == '__main__':
    main('')