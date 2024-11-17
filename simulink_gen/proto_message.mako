% for message in messages:
message ${message['name']} {
% for field in message['fields']:
  ${field['type']} ${field['name']} = ${field['number']};
% endfor
}
% endfor
