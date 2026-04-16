class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def add_list(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def delete_list(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                self.head = temp.next
            else:
                temp.next = temp.next.next
            print("data berhasil dihapus")
            break

        temp = temp.next
        print("data tidak ditemukan")
    
    def search_list(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                print("data ditemukan")
                break
            temp = temp.next
        print("data tidak ditemukan")


ll= linkedlist()
ll.add_list(30)
print("cetak linked list:")
ll.display()
ll.add_list(20)
ll.add_list(10)
print("\ncetak linked list:")
ll.display()
ll.delete_list(20)
print("\ncetak linked list:")
ll.display()
ll.search_list(20)
print("\ncetak linked list:")
ll.display()