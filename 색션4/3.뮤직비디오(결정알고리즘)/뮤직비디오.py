"""
뮤직비디오(결정알고리즘)

DVD에는 총 N개의 곡이 들어간다.
DVD에 녹화할때에는 라이브에서의 순서가 그대로 유지되어야 한다.
M개의 DVD


9 3
1 2 3 4 5 6 7 8 9

9개의 곡 3개의 DVD
분 단위의 곡들.

3개의 DVD에 노래를 넣기 위한 최소한의 DVD 용량은?
"""

import sys
sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
songs = list(map(int, input().split()))


