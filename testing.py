import praw
from Language import Language
import csv


reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent="subreddit finder")
print(reddit.read_only)  # Output: True

subs = ["leagueoflegends", "nba", "wallstreetbets"]

commentTrees = []
l1 = Language(subs[0])
l2 = Language(subs[1])
l3 = Language(subs[2])

for submission in reddit.subreddit(subs[0]).hot(limit=3):
    l1.add_submission(submission)

for submission in reddit.subreddit(subs[1]).hot(limit=3):
    l2.add_submission(submission)

for submission in reddit.subreddit(subs[2]).hot(limit=3):
    l3.add_submission(submission)

l1.add_words_from_tree()
l1.to_graph()
l1.create_text_output("lolcomments.txt")

# l2.add_words_from_tree()
# l2.to_graph()
# l2.create_text_output("nbacomments.txt")


def create_file_output(lang, filename):
    file1 = open(filename,"w", encoding='utf-8')
    file1.write("total words: " + str(lang.total_words) + "\n")
    for word in lang.words:
        file1.write(str(word) + "\n")
    file1.close()

create_file_output(l1, "output/testoutputleague.txt")
create_file_output(l2, "testoutputnba.txt")
# create_file_output(l3, "testoutputwsb.txt")


def compare_two(lang1, lang2, num):
    l1 = lang1.get_top_ranks(num)
    l2 = lang2.get_top_ranks(num)
    common = 0
    error = 0
    for i in range(num):
        curr = l1[i]
        if curr in l2:
            common += 1
            error += (i - l2.index(curr))**2
    error /= num
    return [common, error]

# curr =l1 
# langs = [l2,l3]

# with open('lol.csv', 'w', newline='',encoding='utf-8') as csvfile:
#     fieldnames = ['text', 'contained']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     print("start")
#     for submission in curr.submissions:
#             submission.comments.replace_more(limit=1)
#             for comment in submission.comments.list():
#                 writer.writerow({'text': comment.body, 'contained': 1})
#     for i in langs:
#         for submission in i.submissions:
#             submission.comments.replace_more(limit=1)
#             for comment in submission.comments.list():
#                 writer.writerow({'text': comment.body, 'contained': 0})
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

print(compare_two(l1,l2,200))
# print(compare_two(l1,l3,200))
# print(compare_two(l2,l3,200))