res_list = ["McDonalds", "Subway", "In N Out", "Canes", "Panda Express" ]

new_res = input("What restaurant would you like to add to the list?")

def rank_res(new_res, res_list):

    for i in range(len(res_list)):
        rank = input("Do you like A) " + new_res + " or B) " + res_list[i] + " more? A/B")

        if rank == "A":
            res_list.insert(i, new_res)
            return res_list

        elif rank == "B":
            continue

    else:
        res_list.append(new_res)
        return res_list

print("Your new ranking of restaurants is " + rank_res(new_res, res_list))

