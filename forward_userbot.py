from telethon import TelegramClient, events
import asyncio

# بيانات حسابك من https://my.telegram.org (API ID و API HASH)
api_id = 24420296         # استبدل هنا بالـ api_id الخاص بك
api_hash = '9e851fbf475c4f3b4bd7e4966fb7e57c'  # استبدل هنا بالـ api_hash الخاص بك

# اسم القناة المصدر (بدون @)
SOURCE_CHANNEL = 'Offsideahdaff'  # اسم القناة التي تريد نقل المنشورات منها

# اسم القناة الهدف (بدون @)
TARGET_CHANNEL = 'yallagoool'     # اسم قناتك الخاصة لنقل المنشورات إليها

# إنشاء عميل تيليجرام لحساب المستخدم
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def handler(event):
    try:
        # إعادة إرسال الرسالة إلى القناة الهدف
        await client.send_message(TARGET_CHANNEL, event.message)
        print(f"تم إرسال رسالة جديدة من {SOURCE_CHANNEL} إلى {TARGET_CHANNEL}")
    except Exception as e:
        print(f"خطأ أثناء الإرسال: {e}")

async def main():
    print("✅ البوت يعمل وينتظر منشورات جديدة...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
