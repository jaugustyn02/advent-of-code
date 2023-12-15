# input = 'data/sample.txt'
input = 'data/puzzle.txt'

        
def main():
    with open(input) as f:
        line = f.readlines()[0].rstrip()
    strings = line.split(',')
    
    
    box_slots = [{} for _ in range(256)]
    box_next_slot_id = [0 for _ in range(256)]
    for s in strings:
        box_id = 0
        remove_lens = False
        if '-' in s:
            lens_label = s.split('-')[0]
            remove_lens = True
        else:
            lens_label = s.split('=')[0]
            
        for c in lens_label:
            box_id = (box_id + ord(c))*17%256
        
        if remove_lens:
            if lens_label in box_slots[box_id]:
                box_slots[box_id].pop(lens_label)
        else:
            focal_len = int(s.split('=')[1])
            if lens_label in box_slots[box_id]:
                slot_id = box_slots[box_id][lens_label][1]
            else:
                slot_id = box_next_slot_id[box_id]
                
            new_lens = (focal_len, slot_id)
            box_slots[box_id][lens_label] = new_lens
            box_next_slot_id[box_id] += 1
    
    result_sum = 0
    for box_id in range(256):
        if len(box_slots[box_id]) > 0:
            lenses = list(box_slots[box_id].values())
            lenses.sort(key=lambda x: x[1])
            for slot, lens in enumerate(lenses):
                focal_len, slot_id = lens
                result_sum += (box_id+1) * focal_len * (slot+1)
    print(result_sum)
if __name__ == "__main__":
    main()