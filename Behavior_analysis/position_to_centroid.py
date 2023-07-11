import sys
import os
import re

def CenterPrint(tmp_filenm,tmp_rep):
    os.chdir('distances')
    fly_list = []
    for file_nm in os.listdir('.'):
        if file_nm.startswith('fly-'):
            fly_list.append(file_nm)
    fly_list = sorted(fly_list)
    f_out_nm = '_'.join([tmp_filenm,str(tmp_rep),'centroid.txt'])
    #Path of saving centroid position files for further analysis
    f_out_name = os.path.join('/home/kujin/Documents/Project/Social_Drosophila.2022/Analysis_centroid/',f_out_nm)
    f_output = open(f_out_name,'w')
    f_output.write('time\tx\ty\n')
    time2centroid = dict()
    fly_no = 0
    for tmp_fly_file in fly_list:
        if tmp_fly_file.endswith('.csv'):
            f_input = open(tmp_fly_file,'r')
            f_input.readline()
            for line in f_input:
                tokens = line.strip().split(',')
                tmp_time = float(tokens[2])
                tmp_x = float(tokens[3])
                tmp_y = float(tokens[4])
                if tmp_time not in time2centroid:
                    time2centroid[tmp_time] = dict()
                    time2centroid[tmp_time]['x'] = []
                    time2centroid[tmp_time]['y'] = []
                time2centroid[tmp_time]['x'].append(tmp_x)
                time2centroid[tmp_time]['y'].append(tmp_y)
        fly_no += 1
    
    #Calculate centroid position by each frame
    for tmp_sec in sorted(time2centroid.keys()):
        cent_x = sum(time2centroid[tmp_sec]['x']) / fly_no
        cent_y = sum(time2centroid[tmp_sec]['y']) / fly_no
        f_output.write('%f\t%.2f\t%.2f\n'%(tmp_sec,cent_x,cent_y))

    f_output.close()
    os.chdir('..')

    return()

DGRP_folder_list = os.listdir('.')
for DGRP_folder in DGRP_folder_list:
    if os.path.isdir(DGRP_folder) == True:
        os.chdir(DGRP_folder)
        arena_folder_list = os.listdir('.')
        rep_num = 0
        for arena_folder in sorted(arena_folder_list):
            if os.path.isdir(arena_folder) == True:
                os.chdir(arena_folder)
                rep_num += 1
                CenterPrint(DGRP_folder, rep_num)                
                os.chdir('..')
        os.chdir('..')


