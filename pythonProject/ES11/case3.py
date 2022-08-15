import cantools

dbc_path = r'D:\DBC\ES11-A-001-020MM01 C_Matrix for SC_CANFD_V2.8确认版.dbc'
db = cantools.db.load_file(filename=dbc_path, database_format=None,
                           encoding="UTF-8",
                           frame_id_mask=None, strict=False, cache_dir=None)

select_message = db.get_message_by_frame_id(int('295',16))
print(select_message)