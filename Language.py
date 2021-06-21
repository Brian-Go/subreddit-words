import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from WordInfo import WordInfo
import matplotlib.pyplot as plt


class Language:
    def __init__(self, subreddit):
        self.subreddit = subreddit
        self.words = {}
        self.filename = ""
        self.submissions = []
        self.commentTrees = []
        self.vectorizedComments = []
        self.total_words = 0
        self.post_count = 0

    def add_submission(self, post):
        self.post_count += 1
        self.submissions.append(post)
        self.commentTrees.append(post.comments)

    def tokenize(self, input_str):
        input_str = input_str.lower()
        #result = re.sub(r'\d+', '', input_str)
        #nltk.download('stopwords')
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(input_str)
        result_list = [i for i in tokens if (not i in stop_words) and (i.isalnum())]
        return result_list

    def add_commentTree(self, comment):
        self.commentTrees.append(comment)

    def to_graph(self):
        x = [x for x,_ in self.words]
        y = [y.count for _,y in self.words]
        plt.plot(x[:15], y[:15])
        plt.xlabel('Commonly Used Words') 
        plt.ylabel('Occurences') 
        plt.title('Word Freq') 
        plt.show() 

    def create_text_output(self,filename, depth=2):
        self.filename = filename
        file1 = open(self.filename,"w", encoding='utf-8')
        for submission in self.submissions:
            submission.comments.replace_more(limit=depth)
            for comment in submission.comments.list():
                file1.write(comment.body + "\n")
        file1.close()

    def add_word(self, word, submission, comment):
        if not word in self.words:
            curr = WordInfo(word)
            curr.add_instance(submission, comment)
            self.words[word] = curr
        else:
            self.words[word].add_instance(submission, comment)

    def add_words_from_tree(self):
        for submission in self.submissions:
            submission.comments.replace_more(limit=None)
            for comment in submission.comments.list():
                result_list = self.tokenize(comment.body)
                for word in result_list:
                    self.total_words += 1
                    self.add_word(word, submission, comment)
        self.words = sorted(self.words.items(), key=lambda x: x[1].value, reverse=True)

    # def add_comment_from_Tree(self):
    #     for submission in self.submissions:
    #         submission.comments.replace_more(limit=None)
    #         for comment in submission.comments.list():
    #             result_list = self.tokenize(comment.body)

    def get_top_ranks(self, num):
        x = [x for x,_ in self.words]
        return x[:num]
        
    # def add_words_from_text(self, filename):
    #     self.filename = filename
    #     file1 = open(self.filename, "rt", encoding='utf8')
    #     input_str = file1.read()
    #     result_list = self.tokenize(input_str)
    #     for word in result_list:
    #         self.add_word(word)
    #     self.words = sorted(self.words.items(), key=lambda x: x[1].count, reverse=True)
    #     file1.close()