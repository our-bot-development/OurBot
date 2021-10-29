import os, sqlite3
def get_prefix(client, message):
    os.system(""""cd C:\\Users\\moon\\OneDrive\\Coding\\Python\\dis-bot\\db""")
    conn = sqlite3.connect("./db/guildPrefixes.db")
    c = conn.cursor()
    raw_prefix = c.execute(f"SELECT * FROM guild_prefixes WHERE guild_id={int(message.guild.id)}")
    raw_prefix = raw_prefix.fetchall()
    raw_prefix = raw_prefix[0]
    raw_prefix = raw_prefix[1]
    print(raw_prefix[0])
    return raw_prefix[0]
    conn.commit()
    conn.close()

