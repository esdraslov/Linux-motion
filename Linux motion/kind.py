import os

class _k:
    def __init__(self, MKind: tuple[int, str]):
        self.INK = MKind

class KIND:
    def __init__(self, _KIND: _k):
        self._KIND = _KIND.INK[1]

    def motion_WT(self, url: str):
        os.open(url, 0)

