from channels.consumer import AsyncConsumer


class DiscordConsumer(AsyncConsumer):
    async def discord_ready(self, event):
        print(event)

    async def discord_guild_create(self, event):
        print(event)

    async def discord_guild_member_chunk(self, event):
        print(event)

    async def discord_presence_update(self, event):
        print(event)
