import asyncio

from CharmCord.CharmErrorHandling import CharmCord_Errors


async def waitReaction(args, context):
    """
    Ex. $waitMessage[ChannelID;User;emoji;timeout;timeoutErrMsg]
    """
    from CharmCord.Classes.CharmCord import bots

    split = args.split(";")
    if len(split) < 3:
        raise SyntaxError("ID, User, or timeout not provided to $waitMessage")
    try:
        channel_id = split[0]
        users = split[1]
        emoji = split[2]
        timeout = int(split[3])

        def check(reaction, user):
            if int(channel_id) == context.channel.id:
                if users == "everyone":
                    if str(reaction.emoji.name) == emoji:
                        return True
                elif int(users) == user.id:
                    if str(reaction.emoji.name) == emoji:
                        return True

        error = None
        if len(split[4]) > 1:
            error = split[4]
        if error is None:
            reaction, user = await bots.wait_for(
                "reaction_add", timeout=timeout, check=check
            )
            try:
                return reaction.emoji.name
            except AttributeError:
                return reaction.emoji
        else:
            try:
                reaction, user = await bots.wait_for(
                    "reaction_add", timeout=timeout, check=check
                )
                try:
                    return reaction.emoji.name
                except AttributeError:
                    return reaction.emoji
            except asyncio.TimeoutError:
                await context.channel.send(error)
    except ValueError:
        CharmCord_Errors(f"ID Error in {context.command.name}")
        return
