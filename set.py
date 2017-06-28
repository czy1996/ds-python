# 作业一：
# 写一个 set 的类, 无序且元素不重复，内部使用数组来存储元素，具有以下成员函数
# 1. remove ，删除元素
# 2. add， 增加元素
# 3. has，判断元素是否存在
# 形式如下：


class Set(object):
    def __init__(self, *args):
        self.table_size = 10007
        self.table = [0] * self.table_size
        for s in args:
            self.add(s)

    def remove(self, x):
        if self.has(x):
            index = self._index(x)
            l = self.table[index]
            for i, e in enumerate(l):
                if e == x:
                    l.pop(i)

    def add(self, x):
        if not self.has(x):
            index = self._index(x)
            l = self.table[index]
            if isinstance(l, list):
                l.append(x)
            else:
                self.table[index] = [x]

    def has(self, x):
        index = self._index(x)
        l = self.table[index]
        if isinstance(l, list):
            if x in l:
                return True
        return False

    def _index(self, item):
        return self._hash(item) % self.table_size

    def _hash(self, item):
        r = 1
        f = 1
        for s in item:
            r += ord(s) * f
            f *= 10
        return r

    def all(self):
        r = []
        for l in self.table:
            if isinstance(l, int) is not True:
                r.extend(l)
        return r

    def __repr__(self):
        return str(self.all())

    def __eq__(self, other):
        for e in self.all():
            if not other.has(e):
                return False
        for e in other.all():
            if not self.has(e):
                return False
        return True


def test_set():
    a = Set('1', '2', '2', '3', '4', '4')
    b = Set('1', '2', '2', '3', '4')
    c = Set('1', '3', '4', '2')
    d = Set('2', '3')
    print(a)
    # assert (str(a) == '{1, 2, 3, 4}')
    print(a, b, c, d)
    assert (a == b)
    assert (a == c)
    assert (a != d)
    assert (a.has('1') is True)
    a.remove('1')
    assert (a.has('1') is False)
    a.add('1')
    assert (a.has('1') is True)


if __name__ == '__main__':
    test_set()
