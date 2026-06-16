class Hindex:

    def hindex(self, citations):
        citations.sort(reverse = True)

        h = 0

        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = i + 1

            else:
                break

        print("Papers contributing:", citations[:h])
        return h 
        
        
    
H1 = Hindex()

nums = list(map(int, input("Enter citations: ").split()))

print("H-Index =", H1.hindex(nums))



