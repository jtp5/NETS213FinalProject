############################################################
# NETS 213: Project - Glam Guru
############################################################
import pandas as pd

#Reading File

sample_input = pd.read_csv("sample_input.csv", encoding= 'unicode_escape', header=0)

# Quality Control and Aggregation Module - Majority vote
# Majority Vote Worker Function
# This function takes input of a resulting dataset from our project specific HITs and result from Majority Vote function. 
# It calculates workers quality by comparing their inputs to the majority vote result for each image. It calculates workers' quality in identifying
# Fashionable/Not Fashionable, Formal/Casual, and overall quality as defined by ability to identify both Fashionable/Not Fashionable & Formal/Casual.
# Input Parameter: mturk_res - a dataset containing HIT results & votes - a list of tuples in the format (image, "Fashionable"/"Trashy", "Formal"/"Casual")
# Returns a list of tuples in the format (worker, fashion quality, casual quality, overall quality)
# where the second, third, and fourth elements of the tuples are determined based on majority vote results, and rounded off to 3 decimal places.

def majority_vote_workers(mturk_res, votes):
    tuples = []
    worker_answers = dict()
    for i in range(len(mturk_res)):
        worker_id = mturk_res['ï»¿Worker'][i]
        if worker_id not in worker_answers:
            worker_answers[worker_id] = []
            
        for j in range(1, 5):
            image = mturk_res['Image%sFile' % j][i]
            if mturk_res['Image%sTrashy/Fashionable' % j][i] == 'Fashionable':
                ans = 1
            elif mturk_res['Image%sTrashy/Fashionable' % j][i] == 'Trashy':
                ans = 0
            else:
                ans = -1

            if mturk_res['Image%sCasual/Formal' % j][i] == 'Casual':
                ans2 = 1
            elif mturk_res['Image%sCasual/Formal' % j][i] == 'Formal':
                ans2 = 0
            else:
                ans2 = -1

            worker_answers[worker_id].append((image, ans, ans2))
            
    votes_dict = dict()
    for tup in votes:
        votes_dict[tup[0]] = (tup[1], tup[2])
   
   
    qual = dict()
    for worker_id in worker_answers:
        num_pairs = len(worker_answers[worker_id])
        sum_correct_f = 0
        sum_correct_c = 0
        sum_correct_t = 0
        for tup in worker_answers[worker_id]:
            image = tup[0]
            worker_ans_f = tup[1]
            worker_ans_c = tup[2]
            maj_opn_f = int(votes_dict[image][0])
            maj_opn_c = int(votes_dict[image][1])
            sum_correct_f += int(worker_ans_f == maj_opn_f)
            sum_correct_c += int(worker_ans_c == maj_opn_c)
            sum_correct_t += int((worker_ans_f == maj_opn_f) & (worker_ans_c == maj_opn_c))

            
        fashion_qual = sum_correct_f / num_pairs
        casual_qual = sum_correct_c / num_pairs
        overall = sum_correct_t / num_pairs
        qual[worker_id] = (fashion_qual, casual_qual, overall)


    qual_lst = [(worker_id, "{:.3f}".format(qual[worker_id][0]), "{:.3f}".format(qual[worker_id][1]), "{:.3f}".format(qual[worker_id][2])) for worker_id in qual]
    return sorted(qual_lst, key=lambda tup: tup[0])

# Call to majority votes function on sample data
votes = majority_vote(sample_input)
df1 = pd.DataFrame(votes, columns=['image', 'fashionable', 'casual'])
df1.to_csv('sample_output.csv')

# Call to majority votes worker function on sample data and result of majority votes on sample data
qual_lst = majority_vote_workers(sample_input, votes)
df2 = pd.DataFrame(qual_lst, columns=['worker_id', 'fashion_qual', 'casual_qual', 'overall_qual'])
df2.to_csv('worker_qual.csv')
