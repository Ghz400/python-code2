class Node:
    """链表节点"""
    def __init__(self, val):
        self.val = val
        self.next = None


class CircularLinkedList:
    """循环单链表"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def append(self, val):
        """在链表尾部插入节点"""
        node = Node(val)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node
            node.next = self.head

    def prepend(self, val):
        """在链表头部插入节点"""
        node = Node(val)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            node.next = self.head
            self.head = node
            cur.next = self.head

    def insert_after(self, target_val, val):
        """在指定值后面插入节点"""
        if self.is_empty():
            return False
        cur = self.head
        while True:
            if cur.val == target_val:
                node = Node(val)
                node.next = cur.next
                cur.next = node
                return True
            cur = cur.next
            if cur == self.head:
                break
        return False

    def delete(self, val):
        """删除第一个值为 val 的节点"""
        if self.is_empty():
            return False

        cur = self.head
        prev = None

        while True:
            if cur.val == val:
                if prev is None:
                    # 删除的是头节点
                    if cur.next == self.head:
                        # 只有一个节点
                        self.head = None
                    else:
                        # 找到尾节点更新它的 next
                        tail = self.head
                        while tail.next != self.head:
                            tail = tail.next
                        self.head = cur.next
                        tail.next = self.head
                else:
                    prev.next = cur.next
                return True
            prev = cur
            cur = cur.next
            if cur == self.head:
                break
        return False

    def search(self, val):
        """查找节点，返回节点引用，找不到返回 None"""
        if self.is_empty():
            return None
        cur = self.head
        while True:
            if cur.val == val:
                return cur
            cur = cur.next
            if cur == self.head:
                break
        return None

    def traverse(self):
        """遍历链表，返回所有节点值的列表"""
        result = []
        if self.is_empty():
            return result
        cur = self.head
        while True:
            result.append(cur.val)
            cur = cur.next
            if cur == self.head:
                break
        return result

    def length(self):
        """返回链表长度"""
        if self.is_empty():
            return 0
        count = 0
        cur = self.head
        while True:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def reverse(self):
        """反转循环链表"""
        if self.is_empty() or self.head.next == self.head:
            return

        prev = None
        cur = self.head
        tail = self.head  # 原来的头将成为新尾

        while True:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            if cur == tail:
                break

        self.head = prev
        tail.next = self.head

    def __str__(self):
        """打印链表"""
        vals = self.traverse()
        if not vals:
            return "空链表"
        return " -> ".join(str(v) for v in vals) + " -> (回到头部)"


if __name__ == '__main__':
    cll = CircularLinkedList()
    print("=== 循环链表测试 ===")

    # 尾部插入
    print("\n1. 尾部追加 1, 2, 3, 4")
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.append(4)
    print("   链表:", cll)
    print("   长度:", cll.length())

    # 头部插入
    print("\n2. 头部插入 0")
    cll.prepend(0)
    print("   链表:", cll)

    # 指定位置后插入
    print("\n3. 在 2 后面插入 99")
    cll.insert_after(2, 99)
    print("   链表:", cll)

    # 查找
    print("\n4. 查找 99:", "找到" if cll.search(99) else "未找到")
    print("   查找 100:", "找到" if cll.search(100) else "未找到")

    # 删除
    print("\n5. 删除 99")
    cll.delete(99)
    print("   链表:", cll)

    # 删除头节点
    print("\n6. 删除头节点 0")
    cll.delete(0)
    print("   链表:", cll)

    # 反转
    print("\n7. 反转链表")
    cll.reverse()
    print("   链表:", cll)
