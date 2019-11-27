#!/usr/bin/env python2
# -*- coding: utf-8 -*-
def count_score(a):
    score = 0
    flame = [10]
    flame_count = 0 
    throw_count = 0
    while flame_count < 10:
        if a[throw_count] == 10:
            score +=  a[throw_count] + a[throw_count + 1] + a[throw_count + 2]; "フレームの計算"
            flame[flame_count] = score
            flame_count += 1
            throw_count += 1
        elif a[throw_count] + a[throw_count + 1] == 10:
            score += a[throw_count] + a[throw_count + 1] + a[throw_count + 2]
            flame[flame_count] = score
            flame_count += 1
            throw_count += 2
        else:
            score += a[throw_count] + a[throw_count + 1]
            flame[flame_count] = score
            flame_count += 1 
            throw_count += 2
    print(score)
    print(flame)
def test(a):
    count_score([10,8,2,10,0,10,10,6,4,10,8,2,10,9,1,10])
    print("a")
