class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        . --> current directory
        .. --> directory one leve up
        // --> treated as /
        ... -> treated as directory
        canonical path
        start with '/'
        directories are seperated by '/'
        path does not end with trailing '/'
        path contains directories root -> target
        no periods or double period
        """
        """
        example 1
        /home/usermohit///.../java/./src/../main
        split string based on '/'
        will get an array 
        stack
        [home, usermohit, ..., java, main]
        result: /home/usermohit/.../java/main
        """
        """
        example 2
        path = "/home//foo/"
        split string based on '/'
        will get an array 
        stack
        [home, foo]
        result: /home/foo
        """
        stack = []
        path_arr = path.split('/')
        print(path_arr)
        for ch in path_arr:
            if ch == '':
                continue
            if ch == '.':
                continue
            if ch == '..':
                if stack:
                    stack.pop()
                    continue
                else:
                    continue
            stack.append(ch)
        return '/' + '/'.join(stack)

