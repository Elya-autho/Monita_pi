import psycopg2


def get_code(employee_id: int):
    conn = psycopg2.connect(
        host="c-c9q6nqgic3cd8dpunlii.rw.mdb.yandexcloud.net",
        port=6432,
        dbname="stage-kb-monita",
        user="filippova",
        password="w7TBAs3HCCw7wFmSFgtc",
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT sms_token FROM sms_token_log "
        "WHERE employee_id = %s "
        "ORDER BY dt DESC LIMIT 1",
        (10318,),
    )
    row = cur.fetchone()
    conn.close()
    return row[0] if row else None


print(get_code(10318))
