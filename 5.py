uni_list = []

nlist = int(input("Enter number of elements : "))
print("Enter the elements")

for i in range(nlist):
        list = input()
        uni_list.append(list)
print("The list is : ")
print(uni_list)

def insertion_sort(list):
        for i in range(1, len(list)):
                key = list[i]
                j = i-1
                while j >=0 and key < list[j] :
                        list[j+1] = list[j]
                        j -= 1
                list[j+1] = key
        return list


def bubble_sort(list):
        for i in range(len(list)):
                for j in range(0, len(list) - i - 1):
                        if list[j] > list[j + 1]:
                                temp = list[j]
                                list[j] = list[j+1]
                                list[j+1] = temp                
                
        return list


def Shell_sort(list):
        n = len(list)
        interval = n // 2
        while interval > 0 :
                for i in range(interval , n):
                        temp  = list[i]
                        j = i 
                        while j >= interval and list[j - interval] > temp:
                                list[j - interval] 
                                j -= interval
                        list[j] = temp
                interval = interval // 2
        
        return list

def Selection_sort(list):
	n = len(list)
	for i in range(n):
		m = i
		for j in range(i + 1, n):
			if list[j] < list[m]:
				m = j
		(list[i], list[m]) = (list[m], list[i])
	
	return list	
      
                
def menu():
	print("--------MENU--------")
	print("1.Sorting using  Insertion Sort : ")
	print("2.Sorting using Bubble Sort : ")
	print("3.Sorting using Shell Sort : ")
	print("4.Sorting using Selection Sort : ")
	print("5.Exit")

	mchoice = int(input())

	while mchoice:
		if mchoice == 1:
			print("Sorting using  Insertion Sort : ", insertion_sort(uni_list))
			menu()
		elif mchoice == 2:
			print("Sorting using Bubble Sort : ", bubble_sort(uni_list))
			menu()
		elif mchoice == 3:
			print("Sorting using Shell Sort : ", Shell_sort(uni_list))
			menu()
		elif mchoice == 4:
			print("Sorting using Selection Sort",Selection_sort(uni_list))
			menu() 
		elif mchoice == 5:
			exit()
menu()

