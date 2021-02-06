import json
import threading
from sseclient import SSEClient as EventSource


domain_data = {}
user_data = {}
domainReportInterval = 60
domain_data_in_5_min = {}
user_data_in_5_min = {}
bonusfunctionInterval = 300

url = "https://stream.wikimedia.org/v2/stream/revision-create"


def reports():
    global domain_data
    global user_data
    threading.Timer(domainReportInterval, reports).start()  # called every minute
    num_domains = len(domain_data.keys())

    print("--------------------------- Domains Report ---------------------------\n")
    print("Total number of Wikipedia Domains updated:", num_domains)
    for domain in domain_data:
        print(domain, " : ", domain_data[domain], " pages updated")
    print(
        "\n--------------------      *     *     *      --------------------------\n\n\n"
    )

    sorted_user_data = dict(
        sorted(user_data.items(), key=lambda item: item[1], reverse=True)
    )

    print("--------------------------- Users Report ---------------------------\n")
    print("Users who made changes to en.wikipedia.org\n")
    for user in sorted_user_data:
        print(user, " :   ", sorted_user_data[user])
    print(
        "\n--------------------      *     *     *      --------------------------\n\n\n"
    )

    domain_data = {}
    user_data = {}


def bonusfunctions():
    global domain_data_in_5_min
    global user_data_in_5_min
    threading.Timer(bonusfunctionInterval, bonusfunctions).start()  # called 5 minutes
    num_domains = len(domain_data_in_5_min.keys())

    print(
        "--------------------------- Bonus Domains Report ---------------------------\n"
    )
    print("Total number of Wikipedia Domains updated:", num_domains)
    for domain in domain_data_in_5_min:
        print(domain, " : ", domain_data_in_5_min[domain], " pages updated")
    print(
        "\n--------------------      *     *     *      --------------------------\n\n\n"
    )

    sorted_user_data = dict(
        sorted(user_data_in_5_min.items(), key=lambda item: item[1], reverse=True)
    )

    print(
        "--------------------------- Bonus Users Report ---------------------------\n"
    )
    print("Users who made changes to en.wikipedia.org\n")
    for user in sorted_user_data:
        print(user, " :   ", sorted_user_data[user])
    print(
        "\n--------------------      *     *     *      --------------------------\n\n\n"
    )
    domain_data_in_5_min = {}
    user_data_in_5_min = {}


def main():
    for event in EventSource(url):
        if event.event == "message":
            try:
                data = json.loads(event.data)
            except ValueError:
                pass
            else:
                domain = data["meta"]["domain"]

                if not domain in domain_data:
                    domain_data[domain] = 1
                else:
                    domain_data[domain] += 1

                try:
                    user_name = data["performer"]["user_text"]
                    user_edit_count = data["performer"]["user_edit_count"]
                    if domain == "en.wikipedia.org":
                        user_data[user_name] = user_edit_count
                except:
                    continue


reports()
bonusfunctions()
main()