
"|""""
"|"π~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~π
"|"            from |=== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_-====|
"|"           For any support ask me in here @vrtxmusic
"|"π~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~π
"|"
"|"πRemastered Version of Riyuk_Singer_Vrtxπ
"|"""
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"|"
"|"
"|"
import asyncio
import os
from datetime import datetime, timedelta
from pyrogram import Client, filters, emoji
from pyrogram.methods.messages.download_media import DEFAULT_DOWNLOAD_DIR
from pyrogram.types import Message
from VOIP.filters import main_filter, self_or_contact_filter
from VOIP.voice import ded
from NoteBook.notes import *
from Misa_Amane.life_death import *
#from Misa_Amane.red_eye import current_vc
from pytgcalls import GroupCall
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"|"
"|"
"|"
async def current_vc_filter(_, __, m: Message):
    group_call = ded.group_call
    if not group_call.is_connected:
        return False
    chat_id = int("-100" + str(group_call.full_chat.id))
    if m.chat.id == chat_id:
        return True
    return False

current_vc = filters.create(current_vc_filter)
"|"
"|"
"|"                                                                                                                                                  
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"******************************************** βππππππ€ π₯π¦π£ππππ π π π₯ππ π¦π€ππ£ππ π₯ ***********************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & filters.regex("^!on$"))
async def join_group_call(client, m: Message):
    group_call = ded.group_call
    group_call.client = client
    if group_call.is_connected:
        await m.reply_text(
            f"                         .δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
            "[π¦](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[π¦]\n"
            "                          .**Already joined**\n"
            "\n"
            "-/===============\-\n"
            "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
            "+\===============/+\n"
            )   
        return
    await group_call.start(m.chat.id)
    await m.delete()
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"*************************************** βππππππ€ π₯ππ π€ππ π¨πππ π π β¨Εα»Ε΄_Ζ€ΔΉΓΠΔ?ΕΔβ¨ ********************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & current_vc
                   & filters.regex("^.now$"))
async def show_current_playing_time(_, m: Message):
    start_time = ded.start_time
    playlist = ded.playlist
    if not start_time:
        reply = await m.reply_text(
            f"                         .δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
            "[π¦](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[π¦]"
            "                          .**Unknown**\n"
            "\n"
            "-/===============\-\n"
            "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
            "+\===============/+\n"
            )   
        await _delay_delete_messages((reply, m), Kill_Time)
        return
    utcnow = datetime.utcnow().replace(microsecond=0)
    if ded.msg.get('current') is not None:
        await ded.msg['current'].delete()
    ded.msg['current'] = await playlist[0].reply_text(
        f"{emoji.PLAY_BUTTON}  {utcnow - start_time} / "
        f"{timedelta(seconds=playlist[0].audio.duration)}",
        disable_notification=True
    )
    await m.delete()
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"**************************************** βππππππ€ π₯ππ π€ππ π¨πππ ππ¦ππ ππ ππππππ€ πππ€π₯ ******************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & (self_or_contact_filter | current_vc)
                   & filters.regex("^.cmd$"))
async def show_help(_, m: Message):
    if ded.msg.get('cmd') is not None:
        await ded.msg['cmd'].delete()
    ded.msg['cmd'] = await m.reply_text(FULL_PLAYING_HELP, quote=False)
    await m.delete()
"|"
"|"
"|"
# "+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
# "**************************************** βππππππ€ π₯ππ π€ππ π¨πππ π π ππππππ£ ππ ππππππ€ *****************************"
"|"
"|"
"|"
# @Client.on_message(main_filter
#                    & (self_or_contact_filter | current_vc)
#                    & filters.regex("^.cmd$"))
# async def show_help(_, m: Message):
#     if ded.msg.get('cmd') is not None:
#         await ded.msg['cmd'].delete()
#     ded.msg['cmd'] = await m.reply_text(MEMBERS_PLAYING_HELP, quote=False)
#     await m.delete()

# "+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
# "**************************************** βππππππ€ π₯ππ π€ππ π¨πππ π π πππππ ππ ππππππ€ *****************************"
"|"
"|"
"|"
# @Client.on_message(main_filter
#                    & (self_or_contact_filter | current_vc)
#                    & filters.regex("^.cmd$"))
# async def show_help(_, m: Message):
#     if ded.msg.get('cmd') is not None:
#         await ded.msg['cmd'].delete()
#     ded.msg['cmd'] = await m.reply_text(ADMIN_PLAYING_HELP, quote=False)
#     await m.delete()
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"************************* βππππππ€ πΉπ π₯π ππππππ ππ¦π€ππ π₯π  π‘πππͺπππ€π₯ πππ π₯π  π€ππ π¨ π‘πππͺπππ€π₯ **************************"
"|"
"|"
"|"
@Client.on_message(
    filters.group
    & ~filters.edited
    & current_vc
    & (filters.regex("^.sing$") | filters.audio)
)
async def play_track(client, m: Message):
    group_call = ded.group_call
    playlist = ded.playlist
    # check audio
    if m.audio:
        if m.audio.duration > (Auto_Add2Play_TimeM * 60):
            reply = await m.reply_text(
                f"{emoji.ROBOT} audio which duration longer than "
                f"{str(Auto_Add2Play_TimeM)} min won't be automatically "
                "                          .**added to playlist**\n"
                "\n"
                "-/===============\-\n"
                "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
                "+\===============/+\n"
            )
            await _delay_delete_messages((reply,), Kill_Time)
            return
        m_audio = m
    elif m.reply_to_message and m.reply_to_message.audio:
        m_audio = m.reply_to_message
        if m_audio.audio.duration > (Kill_Hour * 60 * 60):
            reply = await m.reply_text(
                f"{emoji.ROBOT} audio which duration longer than "
                f"{str(Kill_Hour)} hours won't be added to playlist\n"
                "\n"
                "-/===============\-\n"
                "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
                "+\===============/+\n"
            )
            await _delay_delete_messages((reply,), Kill_Time)
            return
    else:
        await ded.send_playlist()
        await m.delete()
        return
    # check already added
    if playlist and playlist[-1].audio.file_unique_id \
            == m_audio.audio.file_unique_id:
        reply = await m.reply_text(f"                        .δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ\n"
                                   "                         .**Already added**")
        await _delay_delete_messages((reply, m), Kill_Time)
        return
    # add to playlist
    playlist.append(m_audio)
    if len(playlist) == 1:
        m_status = await m.reply_text(
            f"                         .δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
            "[π¦](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[π¦]"            
            "Λβ*Β°β’ Analyzing Audio & sending to server β’Β°*βΛ\n"
            "\n"
            "-/===============\-\n"
            "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
            "+\===============/+\n"
        )
        await ded.download_audio(playlist[0])
        group_call.input_filename = os.path.join(
            client.workdir,
            DEFAULT_DOWNLOAD_DIR,
            f"{playlist[0].audio.file_unique_id}.raw"
        )
        await ded.update_start_time()
        await m_status.delete()
        print(f"- PLAYING: {playlist[0].audio.title}")
    await ded.send_playlist()
    for track in playlist[:2]:
        await ded.download_audio(track)
    if not m.audio:
        await m.delete()
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"****************************************** βππππππ€ π€πππ‘π‘πππ π π π₯π£ππππ€ ***************************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.command("skip", prefixes="!"))
async def skip_track(_, m: Message):
    playlist = ded.playlist
    if len(m.command) == 1:
        await ded.skip_current_playing()
    else:
        try:
            items = list(dict.fromkeys(m.command[1:]))
            items = [int(x) for x in items if x.isdigit()]
            items.sort(reverse=True)
            text = []
            for i in items:
                if 2 <= i <= (len(playlist) - 1):
                    audio = f"[{playlist[i].audio.title}]({playlist[i].link})"
                    playlist.pop(i)
                    text.append(f"{emoji.WASTEBASKET} {i}. **{audio}**")
                else:
                    text.append(f"{emoji.CROSS_MARK} {i}")
            reply = await m.reply_text("\n".join(text))
            await ded.send_playlist()
        except (ValueError, TypeError):
            reply = await m.reply_text(
                f"                         .δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
                "[π¦](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[π¦]"
                "                          .**Invalid input**"
                "\n"
                "-/===============\-\n"
                "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
                "+\===============/+\n",    
                                disable_web_page_preview=True
                                )
        await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"******************************************** βππππππ€ π₯π¦π£ππππ π ππ π₯ππ π¦π€ππ£ππ π₯ ***********************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!off$"))
async def leave_voice_chat(_, m: Message):
    group_call = ded.group_call
    ded.playlist.clear()
    group_call.input_filename = ''
    await group_call.stop()
    await m.delete()
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"********************************* βππππππ€ πππππππ π¨ππππ ππ£π π¦π‘ π₯ππ π¦π€ππ£ππ π₯ ππ€ π‘πππͺπππ *************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & filters.regex("^!group$"))
async def list_voice_chat(client, m: Message):
    group_call = ded.group_call
    if group_call.is_connected:
        chat_id = int("-100" + str(group_call.full_chat.id))
        chat = await client.get_chat(chat_id)
        reply = await m.reply_text(
            f"                         .δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
            "[π¦](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[π¦]"
            "                          .**currently in the voice chat:**"
            "                          .**{chat.title}**\n"
            "\n"
            "-/===============\-\n"
            "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
            "+\===============/+\n"
            )   
    else:
        reply = await m.reply_text(emoji.NO_ENTRY
                                   + "didn't join any voice chat yet")
    await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"***************************************** βππππππ€ π₯ππππππ₯ππ π π π π‘πππͺπππ€π₯ ***************************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!end$"))
async def stop_playing(_, m: Message):
    group_call = ded.group_call
    group_call.stop_playout()
    reply = await m.reply_text(
            f"                         .δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
            "[π¦](https://telegra.ph/file/2e419eca28153982c5e54.jpg)[π¦]"
            "                          .**βΉStopped Singing**\n"
            "\n"
            "-/===============\-\n"
            "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
            "+\===============/+\n"
            )   
    await ded.update_start_time(reset=True)
    ded.playlist.clear()
    await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"******************************************** βππππππ€ π‘ππ¦π€πππ ππ πππππ *****************************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!pause"))
async def pause_playing(_, m: Message):
    ded.group_call.pause_playout()
    await ded.update_start_time(reset=True)
    reply = await m.reply_text(
            f"                         .δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
            "[π¦](https://telegra.ph/file/53c1e3bb9d92f745d32bc.jpg)[π¦]"
            "                          .**βΈPaused**"
            "\n"
            "-/===============\-\n"
            "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
            "+\===============/+\n",
                            quote=False
                            )
    ded.msg['pause'] = reply
    await m.delete()
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"******************************************** βππππππ€ π£ππ‘πππͺπππ π π π₯ππ π‘πππͺπππ€π₯ **********************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!replay$"))
async def restart_playing(_, m: Message):
    group_call = ded.group_call
    if not ded.playlist:
        return
    group_call.restart_playout()
    await ded.update_start_time()
    reply = await m.reply_text(
            f"                         .δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
            "[π¦](https://telegra.ph/file/c20d0c751ae61a68f8330.jpg)[π¦]"
            "                          .πPlaying from the beginning"
            "-_-\n"
            "-/===============\-\n"
            "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
            "+\===============/+\n"
            )   
    await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"******************************************** βππππππ€ π£ππ€π¦ππππ ππ πππππ ***************************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!resume"))
async def resume_playing(_, m: Message):
    ded.group_call.resume_playout()
    reply = await m.reply_text(
            f"                         .δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
            "[π¦](https://telegra.ph/file/0f0a508854eebdf8cd693.jpg)[π¦]"
            "                          .**βΆοΈResumed**"
            "\n"
            "-/===============\-\n"
            "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
            "+\===============/+\n",
                                quote=False
                                )
    if ded.msg.get('pause') is not None:
        await ded.msg['pause'].delete()
    await m.delete()
    await _delay_delete_messages((reply,), Kill_Time)
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"****************************************** βππππππ€ π¦πππ¦π₯πππ π₯ππ π¦π€ππ£ππ π₯ ππ π§π *********************************"
"|"
"|"
"|"
# @Client.on_message(main_filter
#                    & self_or_contact_filter
#                    & current_vc
#                    & filters.regex("^!unmutevc$"))
# async def unmute(_, m: Message):
#     group_call = ded.group_call
#     group_call.set_is_mute(False)
#     reply = await m.reply_text(
#             f"δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
#             "[π¦](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[π¦]\n"
#             "                          .**πΆUnmuted**\n"
#             "\n"
#             "-/===============\-\n"
#             "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
#             "+\===============/+\n"
#             )   
#     await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"******************************************** βππππππ€ ππππππππ π π π₯πππ‘ πππππ€ ************************************"
"|"
"|"
"|"
@Client.on_message(main_filter
                   & self_or_contact_filter
                   & current_vc
                   & filters.regex("^!temp$"))
async def clean_raw_pcm(client, m: Message):
    download_dir = os.path.join(client.workdir, DEFAULT_DOWNLOAD_DIR)
    all_fn: list[str] = os.listdir(download_dir)
    for track in ded.playlist[:2]:
        track_fn = f"{track.audio.file_unique_id}.raw"
        if track_fn in all_fn:
            all_fn.remove(track_fn)
    count = 0
    if all_fn:
        for fn in all_fn:
            if fn.endswith(".raw"):
                count += 1
                os.remove(os.path.join(download_dir, fn))
    reply = await m.reply_text(
            f"                         .δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"
            "                          .**Cleaned** {count} files\n"
            "\n"
            "-/===============\-\n"
            "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
            "+\===============/+\n"
            )   
    await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"******************************************** βππππππ€ ππ¦π₯πππ π₯ππ π¦π€ππ£ππ π₯ ππ π§π *********************************"
"|"
"|"
"|"
# @Client.on_message(main_filter
#                    & self_or_contact_filter
#                    & current_vc
#                    & filters.regex("^!mutevc$"))
# async def mute(_, m: Message):
#     group_call = ded.group_call
#     group_call.set_is_mute(True)
#     reply = await m.reply_text(
#             f"δΈβγοΈ» **ΦΙ¦Ι¨ΥΌΙ¨Ι’ΗΚΙ¨_RΚΚΣ** οΈ»γβδΈ"       
#             "[π¦](https://telegra.ph/file/8bdbb1581cc0914586fe2.jpg)[π¦]"
#             "                          .**βοΈMuted**\n"
#             "-/===============\-\n"
#             "|**ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ**|\n"
#             "+\===============/+\n"
#             )   
#     await _delay_delete_messages((reply, m), Kill_Time)
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"*********************************************** πππ ππ ππππ **********************************************"

async def _delay_delete_messages(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()
"|"
"|"
"|"
"+|========================================== ΚΗΦΘΆΙΚΚΙ¨ΥΌΙ-ΚΚΘΆΣΌ -_- ==============================================+"
"*********************************************** πππ ππ ππππ **********************************************"

