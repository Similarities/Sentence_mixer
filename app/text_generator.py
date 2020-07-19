# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:00:11 2020

@author: similarities
"""

import random
import csv
from itertools import permutations


class TextGenerator:

    def __init__(self, input_file_name: str, output_file_name: str):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.sentences = self._sentences
        self.number_of_lines = len(self.sentences)
        self.sample = self._sample
        self.result_string = str

    def original_text(self):
        print('original / Input:')
        print(self.sentences[self.sample[0]])
        print(self.sentences[self.sample[1]])
        print(self.sentences[self.sample[2]])
        print('       ')

    def mix_machine(self):
        for variation in list(permutations(self.sample)):
            self._write_line(variation)

    @property
    def _sample(self):
        population = range(0, self.number_of_lines)
        return random.sample(population, 3)

    @property
    def _sentences(self) -> list:
        with open(self.input_file_name, 'r') as csv_file:
            reader = csv.reader(csv_file)
            return [row for row in reader]

    def _write_line(self, variation):
        result = self.sentences[variation[0]][0] + \
                 self.sentences[variation[1]][1] + \
                 self.sentences[variation[2]][2]
        self._write_to_file(result)

    def _write_to_file(self, result):
        with open(self.output_file_name, "a+") as text_file:
            print(result)
            text_file.writelines(list(result))


if __name__ == '__main__':
    mixture = TextGenerator('../data/raw_data2.txt', '../data/out1.txt')
    mixture.mix_machine()
