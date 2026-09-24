public class ListNode {
    public int Val;
    public ListNode Next;

    public ListNode(int val, ListNode next = null) {
        Val = val;
        Next = next;
    }
}

public class MyHashSet {

    public const int BucketSize = 101;
    public readonly ListNode[] Buckets = new ListNode[BucketSize];

    public MyHashSet() {
        // fake head
        for (int i = 0; i < BucketSize; i++)
        {
            Buckets[i] = new ListNode(-1);
        }
    }

    private int DoHash(int key)
    {
        return key % BucketSize;
    }
    
    public void Add(int key) {
        var hashed_key = DoHash(key);

        var fake_head = Buckets[hashed_key];
        var cur = fake_head;
        while (cur != null)
        {
            if (cur.Val == key)
            {
                return;
            }
            cur = cur.Next;
        }

        var newNode = new ListNode(val: key, fake_head.Next);
        fake_head.Next = newNode;
    }
    
    public void Remove(int key) {
        var hashed_key = DoHash(key);

        ListNode prev = Buckets[hashed_key];
        ListNode cur = prev.Next;
        
        while (cur != null)
        {
            if (cur.Val == key)
            {
                prev.Next = cur.Next;
                return;
            }
            prev = cur;
            cur = cur.Next;
        }
    }
    
    public bool Contains(int key) {
        var hashed_key = DoHash(key);

        var cur = Buckets[hashed_key];
        while (cur != null)
        {
            if (cur.Val == key)
            {
                return true;
            }
            cur = cur.Next;
        }
        return false;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.Add(key);
 * obj.Remove(key);
 * bool param_3 = obj.Contains(key);
 */