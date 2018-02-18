from collections import namedtuple

fieldnames = [
    'record_type',
    'date',
    'requester_cnpj',
    'file_identifier',
    'records_number',
    'merchant_cnpj',
    'affiliation_code',
    'legal_name',
    'trade_name',
    'name',
    'email',
    'area_code',
    'telephone',
    'operation_result_code',
    'validation_result_code',
    'product_code',
    'operation_type',
    'other'
]

Fields = namedtuple('Fields', fieldnames)

offsets = {}

offsets['SH'] = Fields(
    record_type = (0,2),
    date = (2,8),
    requester_cnpj = (10, 14),
    file_identifier = (24, 9),
    records_number = (33, 5),
    merchant_cnpj = None,
    affiliation_code = None,
    legal_name = None,
    trade_name = None,
    name = None,
    email = None,
    area_code = None,
    telephone = None,
    operation_result_code = None,
    validation_result_code = None,
    product_code = None,
    operation_type = None,
    other = (38, 361))

offsets['S1'] = Fields(
    record_type = (0,2),
    merchant_cnpj = (2, 14),
    affiliation_code = (16,15),
    legal_name = (31,32),
    trade_name = (63,32),
    name = (95,32),
    email = (127, 60),
    area_code = (187,3),
    telephone = (190,9),
    operation_result_code = (199,2),
    validation_result_code = (201,2),
    other = (203, 196),
    date = None,
    requester_cnpj = None,
    file_identifier = None,
    records_number = None,
    operation_type = None,
    product_code = None)

offsets['S2'] = Fields(
    record_type = (0,2),
    affiliation_code = (2,15),
    merchant_cnpj = (17, 14),
    product_code = (31,2),
    operation_type = (33,1),
    operation_result_code = (34,2),
    validation_result_code = (36,2),
    other = (38, 361),
    legal_name = None,
    trade_name = None,
    name = None,
    email = None,
    area_code = None,
    telephone = None,
    date = None,
    requester_cnpj = None,
    file_identifier = None,
    records_number = None)

offsets['ST'] = Fields(
    record_type = (0,2),
    date = (2,8),
    requester_cnpj = (10, 14),
    file_identifier = (24, 9),
    records_number = (33, 5),
    merchant_cnpj = None,
    affiliation_code = None,
    legal_name = None,
    trade_name = None,
    name = None,
    email = None,
    area_code = None,
    telephone = None,
    operation_result_code = None,
    validation_result_code = None,
    product_code = None,
    operation_type = None,
    other = (38, 361))

with open("testfile.rem") as f:
    for row in f:
        print (row)
    #Get record type
        rt = row[:2]
    #Get field structure
        fields = offsets[rt]
        for name in fieldnames:
        #Get field offset data by field name
            t = getattr(fields, name)
            if t is not None:
                start, flen = t
                stop = start + flen
                data = row[start : stop]
                print ("%-32s ... %r" % (name, data))
