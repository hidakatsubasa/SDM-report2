#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # --- 1. 有効同値（正常系） ---
        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        # [追加] 境界値: 最小値 (1, 1)
        def test_valid_min (self):
                self.assertEqual (1, calc(1,1))

        # [追加] 境界値: 最大値 (999, 999)
        def test_valid_max (self):
                self.assertEqual (998001, calc(999,999))

        # [追加] 境界値: 最小と最大の組み合わせ
        def test_valid_mix (self):
                self.assertEqual (999, calc(1,999))
                self.assertEqual (999, calc(999,1))

        # --- 2. 無効同値（範囲外・境界値エラー） --- 
        # Aが下限未満 (0)       
        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        # [追加] Bが下限未満 (0)
        def test_invalid_b_zero (self):
                self.assertEqual (-1, calc(150,0))

        # [追加] Aが上限超え (1000)
        def test_invalid_a_max_over (self):
                self.assertEqual (-1, calc(1000,150))

        # [追加] Bが上限超え (1000)
        def test_invalid_b_max_over (self):
                self.assertEqual (-1, calc(150,1000))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))

