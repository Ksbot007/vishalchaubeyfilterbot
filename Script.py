import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://clicksfly.com/ref/LazyDeveloperr')
    START_TXT = environ.get("START_TXT", '''<b> ʜᴇʟʟᴏ , {}\n
ᴍʏ ɴᴀᴍᴇ ɪs <a href=t.me/PlusTechzBot>@ᴘʟᴜsᴛᴇᴄʜᴢ</a>
ɪ ᴀᴍ ʙᴏᴛ ᴡʜɪᴄʜ ʜᴀᴠᴇ ᴍᴀɴʏ  ғɪʟᴇs ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ . ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs ᴡʜɪᴄʜ ᴀʀᴇ sᴛᴏʀᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ...
━━━━━━━━━━━━━━━━━━━━ 
ᴍᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀs ᴀɴ ᴀᴅᴍɪɴ  🙂 ... ɢᴇᴛ ᴀɴʏ ᴍᴏᴠɪᴇs ᴏғ ᴛʜᴇ ᴡᴏʀʟᴅ ɪɴ ᴊᴜsᴛ ᴏɴᴇ sᴇᴄᴏɴᴅ ......
━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━
ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ sᴇᴇ ᴛʜᴇ ᴍᴀɢɪᴄ ᴏʀ ʀᴇᴀᴅ ᴍᴏʀᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇɴᴜ ʙᴇʟᴏᴡ 🙂 </b>''')
    OWNER_TXT = """<b> <a href=t.me/iTeamXD>iTeamXD</a></b> """
    SUPPORT_TXT = """<b> 🔰 Aʟʟ Cʜᴀɴɴᴇʟs | Lɪsᴛ 🔰
═══════════════════
⪼<a href=https://t.me/HDFlims4U/5> Mᴏᴠɪᴇs</a>
⪼<a href=https://t.me/HDFlims4U/7>  Wᴇʙ Sᴇʀɪᴇs</a>
⪼<a href=https://t.me/HDFlims4U/9> Aɴɪᴍᴀᴛɪᴏɴ</a>
⪼<a href=https://t.me/HDFlims4U/11>  K-ᴅʀᴀᴍᴀ</a>
⪼<a href=https://t.me/HDFlims4U/13> Aɴɪᴍᴇ</a>
⪼<a href=https://t.me/HDFlims4U/15> Mᴏᴅɪɴɢ</a>   </b>""""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>✮ ᴍʏ ɴᴀᴍᴇ : <a href=t.me/PlusTechzBot>ᴘʟᴜsᴛᴇᴄʜᴢ</a>
✮ ᴄʀᴇᴀᴛᴏʀ: <a href=t.me/Knual>ᴛᴇᴀᴍ | sʜᴀᴅᴏᴡ</a>
✮ ʟɪʙʀᴀʀʏ: ᴘᴜʀᴏɢʀᴀᴍ
✮ ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ 𝟹
✮ ᴅᴀᴛᴀʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ
✮ ʙᴏᴛ sᴇʀᴠᴇʀ: ʜᴇʀᴜᴋᴏ
✮ ʙᴜɪʟᴅ sᴛᴀᴛs: ᴠ1.0.43
✮ sᴜᴘᴘᴏʀᴛ: <a href=t.me/PlusFlimz>sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ</a>
✮ ᴜᴘᴅᴀᴛᴇs: <a href=t.me/PlusTechz>ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ</a></b>"""
    SOURCE_TXT = """<b>LazyPrincess is an open source project</b>

You can easily get its source code from github - <a href='https://github.com/LazyDeveloperr/LazyPrincessV2'>LazyDeveloperr</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/LazyDeveloper)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    FILTER_TXT = """Help: <b>Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
