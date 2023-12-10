from loader import database
from data import admins

async def send_message_to_all(sender_id, message: str, _dp):
    
    if sender_id not in admins:
        return await _dp.bot.send_message(sender_id, "You're not an admin!") 
    
    users = database.get_users()
    
    message_text = f"Message from an administator:\n{message}"
    
    for user in users:
        u_id = user['USER_ID']
        try:
            await _dp.bot.send_message(u_id, message_text) 
        except:
            pass
    await _dp.bot.send_message(sender_id, "Your message is sent!") 
        