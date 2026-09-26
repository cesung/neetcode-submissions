public class ListNode
{
    public int Key { get; set; }
    public int Value { get; set; }
    public ListNode Prev { get; set; }
    public ListNode Next { get; set; }

    public ListNode(int key, int value, ListNode prev = null, ListNode next = null)
    {
        Key = key;
        Value = value;
        Prev = prev;
        Next = next;
    }
}

public class LRUCache {

    private readonly int _capacity;
    private readonly Dictionary<int, ListNode> _rcd;
    private readonly ListNode _head;
    private readonly ListNode _tail;

    public LRUCache(int capacity) {
        _capacity = capacity;
        _rcd = new Dictionary<int, ListNode>();
        _head = new ListNode(-1, -1);
        _tail = new ListNode(-1, -1);

        _head.Next = _tail;
        _tail.Prev = _head;
    }

    public void Remove(ListNode node)
    {
        ListNode prev = node.Prev;
        ListNode next = node.Next;
        prev.Next = next;
        next.Prev = prev;
    }

    public void Insert(ListNode node)
    {
        ListNode first = _head.Next;
        node.Prev = _head;
        node.Next = first;
        first.Prev = node;
        _head.Next = node;
    }
    
    public int Get(int key) {
        if (_rcd.TryGetValue(key, out var node))
        {
            Remove(node);
            Insert(node);
            return node.Value;
        }
        return -1;
    }
    
    public void Put(int key, int value) {
        if (_rcd.TryGetValue(key, out var node))
        {
            node.Value = value;
            Remove(node);
            Insert(node);
            return;
        }

        var newNode = new ListNode(key, value);
        _rcd[key] = newNode;
        Insert(newNode);

        if (_rcd.Count > _capacity)
        {
            var last = _tail.Prev;
            Remove(last);
            _rcd.Remove(last.Key);
        }
    }
}
