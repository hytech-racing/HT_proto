import json
import os
from mako.template import Template

def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def extract_outports(model_json):
    outports = model_json.get("outports", {})

    messages = []
    for i, (name, value) in enumerate(outports.items()):
        if(type(value).__name__ == "int"):
            vartype = "float"
        else:
            vartype = type(value).__name__

        messages.append({
            "name": name,
            "type": vartype,
            "number": i + 1
        })
    return messages

def convert_outports_to_proto(outports, file_path):
    message_name = os.path.splitext(os.path.basename(file_path))[0] + "_outport"
    messages = [{
        "name": message_name,
        "fields":   [
            {"name": port["name"], "type": port["type"], "number": i + 1}
            for i, port in enumerate(outports)
        ]
    }]

    template = Template(filename="proto_message.mako")

    return message_name, template.render(messages=messages)


def append_proto_to_file(proto_content, proto_file_path):
    with open(proto_file_path, "a") as f:
        f.write(proto_content)

def pack_protos(proto_messages):
    packed_message = [{
    "name": "outports_proto",
    "fields": [
        {"name": f"{message}_msg", "type": message, "number": i + 1}
        for i, message in enumerate(proto_messages)
    ]}]

    template = Template(filename="proto_message.mako")
    return template.render(messages=packed_message)

def delete_after_string(file_path, search_string):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if search_string in line:
            lines = lines[:i]
            break

    with open(file_path, 'w') as file:
        file.writelines(lines)



if __name__ == "__main__":
    json_file_path = "test.json"
    proto_file_path = "../proto/hytech_msgs.proto"

    delete_after_string(proto_file_path, '_outport')

    proto_defs = []
    # for :
    # put all code in here when access to all the model jsons is available
    # add to proto defs

    model_json = load_json(json_file_path)
    outports = extract_outports(model_json)
    message_name, proto_content = convert_outports_to_proto(outports, json_file_path)
    proto_defs.append(message_name)
    append_proto_to_file(proto_content, proto_file_path)

    #code for final message
    proto_content = pack_protos(proto_defs)
    append_proto_to_file(proto_content, proto_file_path)