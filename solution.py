#!/usr/bin/env python3
import sys
import unittest

# Below values are not used in the table, but instead to unit test the prime seeking methods.
KNOWN_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

# 3 x 3 prime multiplication table (for testing).
PRIME_TABLE_SMALL = ''' 2 3 5
2 4 6 10
3 6 9 15
5 10 15 25'''


def is_prime(x):
  '''Determine whether a number is prime or not'''
  if x < 2:
    return False

  upper_bound = int(x / 2)
  for n in range(2, upper_bound + 1):
    if x % n == 0:
      return False
  return True


def find_primes(x):
  '''Find the first x prime numbers'''
  if x < 0:
    return

  primes = []
  num = 2
  while len(primes) < x:
    if is_prime(num):
      primes.append(num)

    num += 1

  return primes


def build_prime_table(primes):
  '''Build a list of lists representing a prime multiplication table'''
  header = primes.copy()
  header.insert(0, '')
  rows = [header] # row-multipliers (x-axis)

  for primeY in primes: # loop down y-axis
    cols = [primeY] # column-multipliers (y-axis)
    for primeX in primes:
      prod = primeY * primeX
      cols.append(prod)

    rows.append(cols)

  return rows


def format_prime_table(prime_table):
  '''Build a string representing a prime multiplication table'''
  lines = []
  for row in prime_table:
    cols = [str(col) for col in row]
    line = ' '.join(cols)
    lines.append(line)

  return '\n'.join(lines)


class TestPrimeMethods(unittest.TestCase):
  def test_is_prime(self):
    '''Test that we properly evaluate if entitites are prime or not'''
    for x in range(0, 200):
      if x in KNOWN_PRIMES:
        self.assertTrue(is_prime(x))
      else:
        self.assertFalse(is_prime(x))

  def test_find_primes(self):
    '''Test that primes can be found (up to the 30th)'''
    for x in range(0, 30):
      primes = find_primes(x)
      for prime in primes:
        self.assertIn(prime, KNOWN_PRIMES)

  def test_print_prime_table(self):
    '''Test building a prime table for a 3x3 case'''
    primes = find_primes(3)
    prime_table = build_prime_table(primes)
    prime_table_str = format_prime_table(prime_table)

    self.assertEqual(prime_table_str, PRIME_TABLE_SMALL)


def main():
  num = 1
  try:
    num = int(sys.argv[1]) # amount of primes to search for.
    if num < 1:
      raise ValueError
  except (IndexError, ValueError):
    print('Please provide a positive integer')
    return

  primes = find_primes(num)

  prime_table = build_prime_table(primes)
  prime_table_str = format_prime_table(prime_table)

  print(prime_table_str)


if __name__ == '__main__':
  main()