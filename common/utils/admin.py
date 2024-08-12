def append_fields(fieldsets, section_name, new_fields):
    fieldsets_dict = dict(fieldsets)
    if section_name in fieldsets_dict:
        fieldsets_dict[section_name]['fields'] += tuple(new_fields)
    else:
        fieldsets_dict[section_name] = {'fields': tuple(new_fields)}

    return list(fieldsets_dict.items())


def move_fields(fieldsets, section_name, before_field=None, fields_to_move=None):
    if not fields_to_move:
        return fieldsets
    
    fieldsets_dict = dict(fieldsets)
    if section_name in fieldsets_dict:
        fields = list(fieldsets_dict[section_name]['fields'])
        if before_field:
            index = fields.index(before_field)
            fields = fields[:index] + list(fields_to_move) + fields[index:]
        else:
            fields.extend(fields_to_move)
        fieldsets_dict[section_name]['fields'] = tuple(fields)
    else:
        fieldsets_dict[section_name] = {'fields': tuple(fields_to_move)}

    return list(fieldsets_dict.items())



def remove_fields(fieldsets, section_name, fields_to_remove=None):
    if not fields_to_remove:
        return fieldsets
    
    fieldsets_dict = dict(fieldsets)
    if section_name in fieldsets_dict:
        fields = list(fieldsets_dict[section_name]['fields'])
        for field in fields_to_remove:
            if field in fields:
                fields.remove(field)
        fieldsets_dict[section_name]['fields'] = tuple(fields)

    return list(fieldsets_dict.items())