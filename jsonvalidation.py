# -*- coding: utf-8 -*-

import os
import argparse
import json
import jsonschema

KEY_DATA = 'data'
KEY_SCHM = 'event'
DEFAULT_JSON_DIR = 'task_folder\event'
DEFAULT_SCHM_DIR = 'task_folder\schema'
DEFAULT_OUT_FILE = 'report.log'

def validateJson(instance, schema):
    result = []    
    try:
        vcls = jsonschema.validators.validator_for(schema)
        vcls.check_schema(schema)
        validator_json = vcls(schema)
        errors = sorted(validator_json.iter_errors(instance), key=lambda e: e.path)
        for err in errors:
            result.append(err)
    except jsonschema.exceptions.SchemaError as err:
        result.append(err)        
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validating JSON')
    parser.add_argument('-j', dest='j', help='JSON directory')
    parser.add_argument('-s', dest='s', help='Schema directory')
    parser.add_argument('-o', dest='o', help='output file')
    
    args = parser.parse_args()
    json_dir = args.j if args.j else DEFAULT_JSON_DIR
    schm_dir = args.s if args.s else DEFAULT_SCHM_DIR
    out_file = args.o if args.o else DEFAULT_OUT_FILE
    
    validation_errors = {}

    json_list = [item for item in os.listdir(json_dir) if item.endswith(".json")]
    
    for file in json_list:
        error_list = []
        try:
            with open(json_dir + '/' + file, 'r') as jf:
                json_data = False
                json_schm = False                
                try:
                    json_data = json.loads(jf.read())
 
                    if not json_data:
                        error_list.append("JSON file contains nothing")
                    elif not json_data[KEY_SCHM]:
                        error_list.append("Schema \'" + json_data[KEY_SCHM] +
                                          "\' not defined")
                    else:
                        try:
                            with open(schm_dir + '/' + json_data[KEY_SCHM] + '.schema', 'r') as sf:
                                try:
                                    json_schm = json.loads(sf.read())
                                    if not json_schm:
                                        error_list.append("JSON Schema \'" +
                                                          json_data[KEY_SCHM] +
                                                          "\' contains nothing")
                                    else:
                                        errors = validateJson(json_data[KEY_DATA],
                                                              json_schm)
                                        for item in errors:
                                            error_list.append(item)
                                except ValueError:
                                    error_list.append("Decoding Schema \'" + 
                                                      json_data[KEY_SCHM] + 
                                                      "\' has failed")
                        except Exception:
                            error_list.append("Unable to find or load defined Schema\n" +
                                              ' '*6 + "In file\t->\tdefined Schema:   \'{}\'"
                                              .format(json_data[KEY_SCHM]))
                except ValueError:
                    error_list.append("Decoding JSON has failed")
        except ValueError:
            error_list.append("Unable to read JSON file")
        validation_errors[file] = error_list
    
    with open(out_file, 'w') as f:
        for json_file_name, json_errors in validation_errors.items():
            if len(json_errors):
                print(json_file_name, file=f)
                for i in range(len(json_errors)):
                    path_schm = KEY_DATA
                    path_inst = KEY_DATA
                    print(' '*3 + "ERROR # {}:  ".format(i+1), end='', file=f)
                    
                    if type(json_errors[i]) is jsonschema.exceptions.ValidationError:
                        for item in list(json_errors[i].schema_path)[1:-1]:
                            path_schm = path_schm + "[" + str(item) + "]"
                        for item in list(json_errors[i].path):
                            path_inst = path_inst + "[" + str(item) + "]"
                        
                        print("{}".format(str(json_errors[i].message)), file=f)
    
                        if json_errors[i].validator == 'required':
                            print(' '*6 + "In schema\t->\trequired properties of {}:   {}"
                                  .format(path_schm, json_errors[i].validator_value), file=f)
                        elif json_errors[i].validator == 'type':
                            print(' '*6 + "In schema\t->\ttype of {} must be:   {}"
                                  .format(path_schm, json_errors[i].validator_value), file=f)
                        
                        if json_errors[i].validator == 'required':
                            cont_prop = [item for item in json_errors[i].instance.keys()]
                            print(' '*6 + "In file\t->\tproperties of {}:   {}"
                                  .format(path_inst, cont_prop), file=f)
                        elif json_errors[i].validator == 'type':
                            print(' '*6 + "In file\t->\tvalue of {}:   {}"
                                  .format(path_inst, json_errors[i].instance), file=f)
                        else:
                            print("{}".format(json_errors[i]), file=f)
    
                    else:
                        print("{}".format(json_errors[i]), file=f)
                    print(file=f)
                print(file=f)
