
def mergesort(in_list):
        if len(in_list) <= 1:
                return in_list

        mid = int(len(in_list)/2)

        top_list = mergesort(in_list[:mid])
        bot_list = mergesort(in_list[mid:])

        out_list = []
        mergelist(top_list, bot_list, out_list)
        return out_list


def mergelist(top_list, bot_list, out_list):
        if len(top_list) == 0:
                while len(bot_list) != 0:
                        out_list.append(bot_list.pop(0))
                return
        elif len(bot_list) == 0:
                while len(top_list) != 0:
                        out_list.append(top_list.pop(0))
                return
        else:
                if top_list[0] <= bot_list[0]:
                        out_list.append(top_list[0])
                        mergelist(top_list[1:], bot_list, out_list)
                else:
                        out_list.append(bot_list[0])
                        mergelist(top_list, bot_list[1:], out_list)

        return
