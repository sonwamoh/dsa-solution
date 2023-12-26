class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        Use Hashsets to mantian unique emails
        Return the size of hashset
        split the the string into local & domain
        first clean the local name
        skip '.', ignore everything after '+'
        put the clean string in hashset
        """
        unique_email = set()
        for em in emails:
            split_arr = em.split("@")
            local_name = split_arr[0]
            domain_name = split_arr[1]
            new_local_name = ""
            for ch in local_name:
                if ch == '+':
                    break
                if ch != '.':
                    new_local_name += ch
            unique_email.add(new_local_name + '@'+ domain_name)   
        return len(unique_email)     