class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        a = len(version1)
        b = len(version2)
        l = 0
        if(a>b):
            l = a
        else:
            l = b
        i = 0
        while(i<l):
            try:
                if (int(version1[i])>int(version2[i])):
                    return 1
                elif (int(version1[i])<int(version2[i])):
                    return -1
            except:
                if (a<b):
                    version1.append(0)
                else:
                    version2.append(0)
                continue
            i = i + 1
        return 0
    
   