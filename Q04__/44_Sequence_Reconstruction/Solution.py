class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # Two questions to answer:
        #  1. can be reconstructed?
        #  2. the one sequence?
        orgIndex = {k: v for v, k in enumerate(org)}
        orgFound = {k: 0 for k in org}
        orgLink  = {}
        for i in range(len(org)-1):
            orgLink[ (i, i+1) ] = 0
        output = True

        # reason #1: order match
        for seq in seqs:
            lastIndex = -1
            for num in seq:
                if num in orgIndex:
                    orgFound[ num ] += 1
                    if lastIndex == -1:
                        lastIndex = orgIndex[ num ]
                    else:
                        if lastIndex < orgIndex[ num ]:
                            pass
                        else:
                            output = False
                            break
                        if lastIndex + 1 == orgIndex[ num ]:
                            orgLink[ (lastIndex, orgIndex[ num ]) ] = 1

                        lastIndex = orgIndex[ num ]
                else:
                    output = False
                    break
            if not output:
                break

        if output:
            # reason #2: element exist
            for num in orgFound:
                if orgFound[ num ] == 0:
                    return False

            # reason #3: relative position inconsistent
            for sLink in orgLink:
                if orgLink[ sLink ] == 0:
                    return False

            return output
        else:
            return output


