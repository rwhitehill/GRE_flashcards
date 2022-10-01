#!/usr/bin/env python3

import os
import subprocess


if __name__ == '__main__':

    cwd     = os.getcwd()

    correct_count = 0
    total_count   = 0
   
    for _ in [3,2,1]:
        storage = cwd + '/storage'+str(_)
        
        cards = os.listdir(storage)

        for card in cards:
            path = storage+'/'+card
            os.chdir(path)
            if not os.path.isfile('question.pdf'):
                res = subprocess.run('pdflatex %s'%('question.tex'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                os.remove('question.aux')
                os.remove('question.log')

            res = subprocess.run('open %s'%('question.pdf'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

            answer_path = path+'answer'
            if not os.path.isfile('answer.pdf'):
                res = subprocess.run('pdflatex %s'%('answer.tex'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                os.remove('answer.aux')
                os.remove('answer.log')

            res = subprocess.run('open %s'%('answer.pdf'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            
            total_count += 1
            user_input = input('Card %d: Correct? Enter yes or no \n\t'%total_count)
            if user_input == 'yes':
                correct_count += 1
                if _ != 3:
                    os.rename(path,cwd+'/storage'+str(_+1)+'/'+card)

    print('\n%d/%d =  %.2f'%(correct_count,total_count,correct_count/total_count))
            
        

