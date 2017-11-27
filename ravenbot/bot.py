from Slack.slack import SlackBot, slackcommand


class Bot(SlackBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @slackcommand()
    def ping(ctx):
        """Pong!"""
        ctx.send("Pong!")

    @slackcommand()
    def help(ctx, command=None):
        """Get a list of commands or extra information"""
        if command in slackcommand.commands:  # If command specified exists
            cmd = ctx.bot.get_command(command)  # Get the command
            help_info = "*Description:* " + cmd.get("callback").__doc__  # Description is docstring
            help_info += "\n*Usage:* `" + ctx.bot.get_usage(cmd) + "`"  # Get usage
        else:
            help_info = "*--------------------- Help Commands ---------------------*"
            for cmd in slackcommand.commands:
                help_info += "\n• `" + cmd + "`"  # List commands
            help_info += "\n\n Type `help <command>` for more info on that command"
        ctx.send(help_info)

token = open("token.txt").read().strip()
ravenkls = Bot(token)
