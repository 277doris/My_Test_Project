#coding:utf-8
import unittest
class Student(object):
    #一定不要把init写成int
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if 80 <= self.score <= 100:
            return 'A'
        if 60 <=  self.score < 80:
            return 'B'
        elif 0 <= self.score < 60:
            return 'C'
        else:
            print('value error! 0<=score<=100,now s=%s' % self.score)
            raise ValueError('value error! 0<=score<=100,now s=%s' % self.score)

