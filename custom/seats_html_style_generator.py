"""script used to generate cinema seats"""
letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

for l in letters_list:
    print(f'''<div class="box-description p{l.lower()}1">{l}</div>
                <div class="box-available p{l.lower()}2" id="available">{l}1</div>
                <div class="box-available p{l.lower()}3" id="available">{l}2</div>
                <div class="box-none p{l.lower()}4">None</div>
                <div class="box-available p{l.lower()}5" id="available">{l}3</div>
                <div class="box-available p{l.lower()}6" id="available">{l}4</div>
                <div class="box-available p{l.lower()}7" id="available">{l}5</div>
                <div class="box-available p{l.lower()}8" id="available">{l}6</div>
                <div class="box-available p{l.lower()}9" id="available">{l}7</div>
                <div class="box-available p{l.lower()}10" id="available">{l}8</div>
                <div class="box-available p{l.lower()}11" id="available">{l}9</div>
                <div class="box-available p{l.lower()}12" id="available">{l}10</div>
                <div class="box-none p{l.lower()}13">None</div>
                <div class="box-available p{l.lower()}14" id="available">{l}11</div>
                <div class="box-available p{l.lower()}15" id="available">{l}12</div>
                <div class="box-description p{l.lower()}16">{l}</div>''')

for idx, l in enumerate(letters_list):
    for i in range(1, 17):
        print(f'''.p{l.lower()}{i} |
        grid-column-start: {i};
        grid-column-end: {1 + i};
        grid-row-start: {idx + 1};
        grid-row-end: {idx + 2};
    *''')

print('LEN: ', len(letters_list))
