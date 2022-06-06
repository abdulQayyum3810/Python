class superList(list):
    def __len__(self):
        return 1000

superList1=superList()
superList1.append(4)
print(superList1[0])
print(len(superList1))