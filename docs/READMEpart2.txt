############################################################
# NETS 213: Project - Glam Guru
############################################################
quality_control.py creates a csv ("sample_output.csv") as 
output based on majority vote from an input csv 
("sample_input.csv"). Additionally, it creates a worker
quality csv ("worker_qual.csv") based on how frequently a
worker agrees with the gold standard data. Data from a
worker will be discarded if the worker quality is no better
than guessing at random (<=50% accuracy). The output data
will be used to train an image classifier