# Tiny Discord Ping Bot

A throwaway Discord bot with one slash command:

```text
/ping → Pong!
```

## Run it on Replit

1. Create a Discord application and bot in the [Discord Developer Portal](https://discord.com/developers/applications).
2. Invite the bot to a server with the `bot` and `applications.commands` scopes.
3. Add the bot token as a Replit Secret named `DISCORD_BOT_TOKEN`.
4. Start the `Discord bot` workflow.

The slash command is synced globally when the bot starts, so Discord may take a little while to display it in a server.