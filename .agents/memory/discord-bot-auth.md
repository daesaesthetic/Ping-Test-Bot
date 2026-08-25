---
name: Discord bot authentication
description: The distinction between Replit’s Discord user connection and a Discord application bot token.
---

Use a separate project secret for a Discord application’s bot token when building a message-handling bot. The Replit Discord connector provides a user OAuth token with identity/server scopes and is not valid for bot gateway authentication or channel message operations.

**Why:** Discord separates user OAuth access from bot authentication, and the connector’s token type cannot operate a message-handling bot.

**How to apply:** Keep the bot token out of source and chat; read it from a Replit secret such as `DISCORD_BOT_TOKEN`. Use the connector only for user-scoped Discord API actions.