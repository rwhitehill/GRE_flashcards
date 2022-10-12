#!/usr/bin/env python3

import os
import subprocess
import random


if __name__ == '__main__':

    cwd     = os.getcwd()

    correct_count = 0
    total_count   = 0
   
    for _ in [2]:
        storage = cwd + '/storage'+str(_)
        
        cards = os.listdir(storage)
        random.shuffle(cards)

        for card in cards:
            if card == 'temp_card':
                continue
            print(card)
            path = storage+'/'+card
            os.chdir(path)
            if not os.path.isfile('question.pdf'):
                res = subprocess.run('pdflatex %s'%('question.tex'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                os.remove('question.aux')
                os.remove('question.log')

            res = subprocess.run('open %s'%('question.pdf'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

            input('Press Enter to show answer...')

            answer_path = path+'answer'
            if not os.path.isfile('answer.pdf'):
                res = subprocess.run('pdflatex %s'%('answer.tex'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                os.remove('answer.aux')
                os.remove('answer.log')

            res = subprocess.run('open %s'%('answer.pdf'),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            
            total_count += 1
            while True:
                user_input = input('Card %d: Correct? Enter yes or no \n\t'%total_count)
                if user_input == 'yes':
                    if _ != 3:
                        os.rename(path,cwd+'/storage'+str(_+1)+'/'+card)
                    correct_count += 1
                    break
                elif user_input == 'no':
                    if _ != 1:
                        os.rename(path,cwd+'/storage'+str(_-1)+'/'+card)
                    break
                elif user_input == 'pass':
                    break

    print('\n%d/%d =  %.2f%%'%(correct_count,total_count,100*correct_count/total_count))
            
        

