# Copyright 2018 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Utility functions for manipulating DNA sequences."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Error(Exception):
  pass


def _add_lowercase(d):
  """Returns a dictionary with the lowercase keys and values entered."""
  retval = d.copy()
  retval.update({k.lower(): v.lower() for k, v in d.items()})
  return retval


STRICT_DNA_COMPLEMENT_UPPER = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
DNA_COMPLEMENT_UPPER = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
IUPAC_DNA_COMPLEMENT_UPPER = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C',
    'R': 'Y',  # R is A/G
    'Y': 'R',  # Y is C/T
    'S': 'S',  # S is C/G
    'W': 'W',  # W is A/T
    'K': 'M',  # K is G/T
    'M': 'K',  # M is A/C
    'B': 'V',  # B is C/G/T
    'V': 'B',  # V is A/C/G
    'D': 'H',  # D is A/G/T
    'H': 'D',  # H is A/C/T
    'N': 'N',  # N is any base
}

STRICT_DNA_COMPLEMENT = _add_lowercase(STRICT_DNA_COMPLEMENT_UPPER)
DNA_COMPLEMENT = _add_lowercase(DNA_COMPLEMENT_UPPER)
IUPAC_DNA_COMPLEMENT = _add_lowercase(IUPAC_DNA_COMPLEMENT_UPPER)


STRICT_DNA_BASES_UPPER = frozenset(['A', 'C', 'G', 'T'])
STRICT_DNA_BASES = frozenset(['a', 'c', 'g', 't', 'A', 'C', 'G', 'T'])
DNA_BASES_UPPER = frozenset(['A', 'C', 'G', 'T', 'N'])
DNA_BASES = frozenset(['a', 'c', 'g', 't', 'n', 'A', 'C', 'G', 'T', 'N'])


def reverse_complement(sequence, complement_dict=None):
  """Returns the reverse complement of a DNA sequence.

  By default this will successfully reverse complement sequences comprised
  solely of A, C, G, and T letters. Other complement dictionaries can be
  passed in for more permissive matching.

  Args:
    sequence: The input sequence to reverse complement.
    complement_dict: The lookup dictionary holding the complement base pairs.

  Returns:
    The reverse complement DNA sequence.

  Raises:
    Error: The sequence contains letters not present in complement_dict.
  """
  if complement_dict is None:
    complement_dict = STRICT_DNA_COMPLEMENT_UPPER

  try:
    return ''.join(complement_dict[nt] for nt in reversed(sequence))
  except KeyError:
    raise Error('Unknown base in %s, cannot reverse complement using %s' %
                (sequence, str(complement_dict)))
