activities = [["A", 0, 6],
             ["B",2,3],
             ["C",4,6],
             ["D",7,8],
             ["E",5,8],
             ["F",8,10]]
             
def activitySelect(actlist):
    selactlist = []
    actlist.sort(key=lambda x: x[2])
#   firstAct = actlist[0][0]
    endoffirst = actlist[0][2]
    selactlist.append(actlist[0])

    for j in range(1,len(actlist)):
        if endoffirst <= actlist[j][1]:
            selactlist.append(actlist[j])
            endoffirst=actlist[j][2]
    return selactlist
            
print("Available activities are:","".join(str(act[0]) + ":" + str(act[1]) + "-" + str(act[2]) + ","for act in activities))
print("Selected activities are :","".join(str(act[0]) + ":" + str(act[1]) + "-" + str(act[2]) + ","for act in activitySelect(activities)))
