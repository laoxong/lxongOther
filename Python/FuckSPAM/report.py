import json
import time
import os

import httpx
from dotenv import load_dotenv


def getReport(Host, I):
    resp = httpx.post(f"https://{Host}/api/admin/abuse-user-reports",
                      json={"state": "unresolved", "reporterOrigin": "combined", "targetUserOrigin": "combined",
                            "limit": 10, "allowPartial": True, "i": I}
                      )
    return resp.json()


def resolveReport(Host, I, reportId, forward=True):
    httpx.post(f"https://{Host}/api/admin/resolve-abuse-user-report",
                     json={"forward": forward, "reportId": reportId, "i": I})


def delUser(Host, I, userId):
    httpx.post(f"https://{Host}/api/admin/delete-account", json={"userId": userId, "i": I})


def main(autoDelete=False):
    load_dotenv()
    InstanceHost = os.getenv("InstanceHost")
    misskeyI = os.getenv('misskeyI')
    while True:
        res = getReport(InstanceHost, misskeyI)
        if res:
            for report in res:
                print("User:", report["targetUser"]["username"] + "@" + report["targetUser"]["host"])
                print("Comment:", report["comment"])
                if not autoDelete:
                    in_content = input("R/转发报告,Y/删除用户,N标记为已完成 ")
                    if in_content == "R" or in_content == "r":
                        resolveReport(InstanceHost, misskeyI, report["id"])
                    if in_content == "Y" or in_content == "y":
                        resolveReport(InstanceHost, misskeyI, report["id"])
                        delUser(InstanceHost, misskeyI, report["targetUserId"])
                    if in_content == "N" or in_content == "N":
                        resolveReport(InstanceHost, misskeyI, report["id"], forward=False)
                else:
                    time.sleep(0.5)
                    resolveReport(InstanceHost, misskeyI, report["id"])
                    delUser(InstanceHost, misskeyI, report["targetUserId"])
                    print("已删除：", report["targetUser"]["username"] + "@" + report["targetUser"]["host"])
        else:
            break


if __name__ == "__main__":
    main()
