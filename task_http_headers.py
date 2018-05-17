import json
def http_headers_to_json(headers, res):
    with open(headers) as f:

        readed = f.read()
        slin = readed.count('\n')
        slin = slin - 1
        f.seek(0)
        readed_data = f.readlines()
        f.seek(0)
        readed_line = f.readline()
        h = {}
        oh = readed_line.split(' ')

        if oh[0] == 'GET':
            method = oh[0]
            h.update({'method':method})
            uri = oh[1]
            h.update({'uri':uri})
            protocol = oh[2]
            protocol = str(protocol)
            protocol = protocol.replace("'", '')
            protocol = protocol.replace(",", '')
            protocol = protocol.replace("]", '')
            protocol = protocol.replace("[", '')
            protocol = protocol.replace("\\n", '')
            protocol = protocol.replace("\n", '')
            h.update({'protocol':protocol})

        else:
            if oh[0] != 'HTTP/2':
                protocol = oh[0]
                h.update({'protocol':protocol})
                status_code = oh[1]
                h.update({'status_code':status_code})
                status_message = oh[2:]
                status_message = str(status_message)
                status_message = status_message.replace("'", '')
                status_message = status_message.replace(",", '')
                status_message = status_message.replace("]", '')
                status_message = status_message.replace("[", '')
                status_message = status_message.replace("\\n", '')
                h.update({'status_message':status_message})
            else:
                protocol = oh[0]
                h.update({'protocol':protocol})
                status_code = oh[1]
                h.update({'status_code':status_code})


        for i in range(1, slin):
            x = readed_data[i].split(': ')
            y = str(x[1]).replace('\n', '')
            y = str(y)
            h.update({x[0]:y})

        with open(res, 'w') as l:
            json.dump(h, l, indent=4)
