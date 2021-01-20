import collections

def findLongestSubString(array):
    head=0
    ans=0
    dictionary = collections.defaultdict(int)

    for i in range(len(array)):
        tail = array[i]
        dictionary[tail]+=1

        while head<len(array) and len(dictionary)<2:
            dictionary[array[head]]-=1

            if dictionary[array[head]]==0:
                del dictionary[array[head]]

            head+=1

            ans=max(ans,i-head+1)

    print ans

def main():

    array = [2, 2, 3, 2, 3, 4, 4, 5, 5, 5, 5, 7, 1, 1, 0, 9, 2, 2, 3, 4, 0, 5, 5, 1]

    print(array)
    findLongestSubString(array)

main()

