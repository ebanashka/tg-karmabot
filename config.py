token = "916448783:AAHCjX-Siu0TMdc2tkESU611jNviCR25WVw"  # bot token
botName = "KDq3CVM43w_bot"  # bot username
chatId = -278344922  # id of chat where bot should work

# DB settings
database = "d5r90gpedannss"
host = "ec2-54-217-219-235.eu-west-1.compute.amazonaws.com"
user = "gkutectlapyvny"
password = "fedf24caea2072d0f7b9422b6b7b45f7dac025632c93c631a9cb5a3a19681acb"

admins = [923083745, 0, 0]  # users ids that can use /ban and /unban commands

helpText = """
чтобы *добавить реп*,ответь на респектовое сообщение фразой "rep" .
\n чтобы *убрать реп*, ответь с фразой "mrep" тому кого хочешь минуснуть.

\n/top20 - топ 20
\n/untop20 - топ20 в минусе
\n/help - это сообщение лол
"""

# text for new users
welcomeText = """
привет, @%s!
\nты хуесос
\nиди в хуй.
"""

# text for new users without username
welcomeUser = """
привет, %s!
\nты даже не хуесос
\nу тебя нет логина блядь чтоб я мог считать твой реп, иди настройки себе логин @... в настрйоках бомж
 
"""

# text for chat where bot don't work
dontWork = "Sorry, but I don't work in this chat."

# karma text for user without username
notUsername = "у педика нет логина, его карму не учесть :("

# text for message without reply
shouldReply = "@%s, ты должен ответить на сообщение что помогло тебе!"
shouldReply2 = "@%s, должено ответить на сообщение которое не понравилось!"

# text with thanks to bot
thxToBot = "@%s, семпай наполни меня!"

# text with reduce karma to bot
botMinus = "@%s, семпай, за что(!"

# text with karma to urself
masturbate = "@%s, хахахах вот и шлюха спалилась!"
unmasturbate = "@%s, любишь когда тебя унижают? :("

# text to karma add
karmaPlus = """
Добавил реп @%s
\n-------------------
@%s теперь имеет: %d  реп
"""

# text to reduce karma
karmaMinus = """
снизил реп @%s
\n-------------------
@%s теперь имеет: %d реп
"""

# text for a ban for a little karma
banForKarma = "@%s имеет -100 репа. Он заБАНен."

# text for ban if user doesn't exist in DB
cantBan = "нет пользака в бд."

# text for unban if user doesn't exist in DB
cantUnban = "нет пользака в бд."

# text for ban
banned = "забанен"

# text for unban
unbanned = "разбанен"
