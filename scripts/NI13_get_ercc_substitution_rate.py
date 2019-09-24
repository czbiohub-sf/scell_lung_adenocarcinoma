""" get the ERCC substitution rate for a set of scRNA-seq alignment (.bam) files """

import pandas as pd
import os
import csv
import re
import numpy as np


def split_at_upper_case(text):
    """ splits a given string AFTER each upper case letter """
    result = ""
    for char in text:
        if char.isupper():
            result += char + " "
        else:
            result += char
    return result.split()



def generate_ercc_only_bams(ercc_l_):
    """ filters bams for ONLY the ERCC entries
        outputs a new set of filtered bams """
    print('generating ERCC only .bams...')

    cwd = os.getcwd()
    cell_names = os.listdir('TN_tumor/')

    for cell in cell_names:
        currCell = cwd + '/TN_tumor/' + cell
        bamFile = currCell + '/' + '*.bam'
        cell_ercc_out = cwd + '/TN_tumor_ercc_only/' + cell + '_ercc_only.txt'

        for ercc in ercc_l_:
            cmd = 'samtools view ' + bamFile + ' ' + str(ercc) + ' >> ' + cell_ercc_out
            #print(cmd)
            os.system(cmd)



def get_ercc_list():
    """ gets a list of the ERCCs in the hg38-plus reference"""
    ercc_list = []
    with open('hg38-plus.gtf') as hg_file:
        read_hg = csv.reader(hg_file, delimiter='\t')
        for row in read_hg:
            if 'ERCC' in row:
                ercc_list.append(row[0])

    return(ercc_list)



def get_substitution_rate(ercc_alignment_file):
    """ returns the base substitution rate in a given ERCC only alignement file """

    cwd = os.getcwd()
    currFile = cwd + '/TN_tumor_ercc_only/' + ercc_alignment_file
    numLines = 0
    subCount = 0 

    with open(currFile) as ercclines:
        ercclines_read = csv.reader(ercclines, delimiter='\t')
    
        for line in ercclines_read:
            numLines += 1
            cigarStr = line[5]
        
            if 'I' in cigarStr or 'D' in cigarStr or 'N' in cigarStr or 'X' in cigarStr:
                cigarStrSplit = split_at_upper_case(cigarStr)
            
                for item in cigarStrSplit:
                    if 'M' not in item and 'S' not in item and 'H' not in item and 'P' not in item:
                        rawNum = re.sub("\D", "", item)
                        subCount += int(rawNum)
                    
    numBases = numLines * 100
    subRate = subCount / numBases
    
    return(subRate)



""" main body here"""
ercc_l = get_ercc_list()
generate_ercc_only_bams(ercc_l)

cmd = 'find ./TN_tumor_ercc_only -size  0 -print0 |xargs -0 rm --' # remove empty files
os.system(cmd)

print('getting ERCC substitution rates...')

ercc_only_alignment_files = os.listdir('TN_tumor_ercc_only/')
sub_rates = []

for item in ercc_only_alignment_files:
    currRate = get_substitution_rate(item)
    sub_rates.append(currRate)

sub_rates_sr = pd.Series(sub_rates)
sub_rates_sr.to_csv('sub_rates_TN.csv', index=False)

sub_rate_mean = np.mean(sub_rates)
sub_rate_med = np.median(sub_rates)
sub_rate_min = np.amin(sub_rates)
sub_rate_max = np.amax(sub_rates)
sub_rate_q1 = np.quantile(sub_rates, 0.25)
sub_rate_q3 = np.quantile(sub_rates, 0.75)

print(' ')
print('min: %f' % sub_rate_min)
print('first quartile: %f' % sub_rate_q1)
print('median: %f' % sub_rate_med)
print('third quartile: %f' % sub_rate_q3)
print('max: %f' % sub_rate_max)
print(' ')


