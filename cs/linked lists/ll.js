class LinkedList {
  constructor(head = null) {
    this.head = head;
    this.getLast = this.getLast.bind(this);
  }

  //   getLast() {
  //     let pointer = this.head;
  //     if (this.head) {
  //       while (pointer.next) {
  //         pointer = pointer.next;
  //       }
  //     }
  //     return pointer;
  //   }

  getLast(node = this.head) {
    // let self = this;
    if (!node) {
      return null;
    }
    if (!node.next) {
      return node;
    }
    return this.getLast(node.next);
  }

  addNew(node) {
    if (!this.head) {
      this.head = node;
      return;
    }
    let last = this.getLast(this.head);
    last.next = node;
    return last.next;
  }
}

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

let list = new LinkedList(new Node(1));
list.addNew(new Node(2));
list.addNew(new Node(3));
list.addNew(new Node(4));
list.addNew(new Node(5));
// console.log(list.getLast());
