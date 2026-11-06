class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        emailList = {} # email : parent (index)
        visited = set()
        userList = {} # parent : [] (heap sorted.)
        for i in range(len(accounts)):
            emails = accounts[i][1:]

            #check if any email is in already emailList
            # if founded get existing user id, else create new.

            userAccount = -1
            for e in emails:
                if e in emailList:
                    userAccount = emailList[e]
                    break
            if userAccount == -1: # create new
                userAccount = i
                userList[userAccount] = []


            for e in emails:
                emailList[e] = userAccount
                if e not in visited:
                    heapq.heappush(userList[userAccount], e)
                    visited.add(e)
            

        res = []
        for u, v in userList.items():
            cur = []
            cur.append(accounts[u][0])

            for email in v:
                cur.append(email)

            res.append(cur)

        return res
            
                


            



            