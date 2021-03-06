#!/usr/bin/env python
# -*- coding: utf-8 -*-
#.--. .-. ... .... -. - ... .-.-.- .. -.

import unittest
from metarna.target_scan import scan, free_energy

class TestTargetScan(unittest.TestCase):
  gene_seq = (
    "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCC"
    "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC"
    "CTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"
  )
  mirna_seq = "UGGCGAUUUUGGAACUCAAUGGCA"

  def test_default(self):
    delta_g = free_energy(self.gene_seq, self.mirna_seq)
    self.assertEqual(delta_g, -13.08)

  def test_report(self):
    scan_res = scan(self.gene_seq, self.mirna_seq)
    pass
